import click
import json
import torch
import torch.nn as nn
import torch.optim as optim
from mteb import MTEB
from mteb.tasks.Retrieval.eng.SciFactRetrieval import SciFact
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from ef.cli.plausibility import _dict, _dict_ref
from ef.config import *
from ef.globals import *
from ef.utils import *


class LinearTranslation(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearTranslation, self).__init__()
        
        # Linear layer
        self.layer = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        y = torch.sigmoid(self.layer(x))
        return y


class RetrievalModelWithTranslation(RetrievalModel):
    def __init__(self, pretrained_model_name: str, task: str, model, **kwargs):
        super().__init__(pretrained_model_name, task, **kwargs)
        self.translation_model = model

    def encode_queries(self, queries: List[str], **kwargs) -> np.ndarray:
        embeddings = super().encode_queries(queries, **kwargs)
        with torch.no_grad():
            return self.translation_model(torch.tensor(embeddings, dtype=torch.float32)).numpy()

    def encode_corpus(self, corpus: List[Dict[str, str]], **kwargs) -> np.ndarray:
        embeddings = super().encode_corpus(corpus, **kwargs)
        with torch.no_grad():
            return self.translation_model(torch.tensor(embeddings, dtype=torch.float32)).numpy()


def train(
        from_vectors: np.ndarray,
        to_vectors: np.ndarray,
        learning_rate=0.001,
        epochs=10,
        batch_size=128,
        validation_split=0.2
):
    input_dim = from_vectors.shape[1]
    output_dim = to_vectors.shape[1]
    
    # Convert numpy data to PyTorch tensors
    from_vectors = torch.tensor(from_vectors, dtype=torch.float32)
    to_vectors = torch.tensor(to_vectors, dtype=torch.float32)

    # Create dataset and dataloaders
    dataset = TensorDataset(from_vectors, to_vectors)
    train_size = int((1 - validation_split) * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    
    # Initialize model, loss function, and optimizer
    model = LinearTranslation(input_dim, output_dim)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    # Training loop
    for epoch in range(epochs):
        model.train()
        train_loss = 0
        for batch in train_loader:
            inputs, targets = batch
            
            # Forward pass
            outputs = model(inputs)
            
            # Compute loss (reconstruction loss + L1 regularization)
            loss = criterion(outputs, targets)
            
            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
        
        # Validation
        model.eval()
        val_loss = 0
        with torch.no_grad():
            for batch in val_loader:
                inputs, targets = batch
                outputs = model(inputs)
                loss = criterion(outputs, targets)
                val_loss += loss.item()
        
        click.echo(f"Epoch {epoch + 1}/{epochs}, Train Loss: {train_loss/len(train_loader)}, Val Loss: {val_loss/len(val_loader)}")
    
    return model


@click.command()
@click.argument("method", type=click.Choice(['train', 'evaluate']))
@click.argument("from_pretrained_model_name", type=click.Choice(EMBEDDING_MODELS), default=EMBEDDING_MODELS[0])
@click.argument("to_pretrained_model_name", type=click.Choice(EMBEDDING_MODELS), default=EMBEDDING_MODELS[-1])
def translate(method: str, from_pretrained_model_name: str, to_pretrained_model_name: str):
    """
    Run translation.
    """
    click.echo(f'Method: {method}')
    click.echo(f'From pretrained model name: {from_pretrained_model_name}')
    click.echo(f'To pretrained model name: {to_pretrained_model_name}')

    # Embeddings paths
    from_embeddings_path = os.path.join(RESULTS_FOLDER, 'embeddings', from_pretrained_model_name.replace("/", "_"))
    to_embeddings_path = os.path.join(RESULTS_FOLDER, 'embeddings', to_pretrained_model_name.replace("/", "_"))

    # Translation model path
    model_path = os.path.join(RESULTS_FOLDER, 'translation', f'{from_pretrained_model_name.replace("/", "_")}_to_{to_pretrained_model_name.replace("/", "_")}', 'model.pt')
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    # Load corpus embeddings for passages
    file_name = 'id_100_mid'
    path = os.path.join(from_embeddings_path, f'{file_name}.jsonl')
    if not os.path.exists(path):
        raise ValueError(f'No corpus embeddings found for pretrained model {from_pretrained_model_name}')
    df = pd.read_json(path, orient='records', lines=True)
    if file_name == 'queries':
        df = df.set_index('query-id')
    else:
        df = df.set_index('corpus-id')
    X = np.array(df['embedding'].to_list())

    path = os.path.join(to_embeddings_path, f'{file_name}.jsonl')
    if not os.path.exists(path):
        raise ValueError(f'No corpus embeddings found for pretrained model {to_pretrained_model_name}')
    df = pd.read_json(path, orient='records', lines=True)
    if file_name == 'queries':
        df = df.set_index('query-id')
    else:
        df = df.set_index('corpus-id')
    y = np.array(df['embedding'].to_list())

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if method == 'train':
        # Train translation model
        model = train(X_train, y_train)

        # Save translation model
        torch.save(model.state_dict(), model_path)

    else:
        # Load translation model
        translation_model = LinearTranslation(X.shape[1], y.shape[1])
        translation_model.load_state_dict(torch.load(model_path))

        # # Evaluate test set
        # model.eval()
        # with torch.no_grad():
        #     y_pred = model(torch.tensor(X_test, dtype=torch.float32)).numpy()

        # # Compute evaluation metrics
        # mse = np.mean((y_pred - y_test) ** 2)
        # click.echo(f'Mean Squared Error: {mse}')

        # Load RetrievalModel with translation
        model = RetrievalModelWithTranslation(from_pretrained_model_name, 'scifact', translation_model)
    
        task = SciFact()

        task_output_path = os.path.join(RESULTS_FOLDER, 'temp', f'{from_pretrained_model_name.replace("/", "_")}_to_{to_pretrained_model_name.replace("/", "_")}')
        results_file_path = os.path.join(task_output_path, 'no_model_name_available', 'no_revision_available', f'{type(task).__name__}.json')
        eval_split = 'dev' if 'msmarco' in type(task).__name__.lower() else 'test'
        evaluation = MTEB(tasks=[task])
        evaluation.run(model, eval_splits=[eval_split],
                output_folder=task_output_path,
                overwrite_results=True)
        
        # Read json file
        with open(results_file_path, 'r') as file:
            data = json.load(file)
            print(data)
            ndcg_at_10 = data['scores'][eval_split][0]['ndcg_at_10']
            click.echo(f'NDCG@10 for model {from_pretrained_model_name} to {to_pretrained_model_name} in task {type(task).__name__}: {ndcg_at_10}')

            _dict[from_pretrained_model_name] = ndcg_at_10
            for key, value in _dict.items():
                print(key, value, '(' + str(_dict_ref[key]) + ')')

            _dict[to_pretrained_model_name] = ndcg_at_10
            for key, value in _dict.items():
                print(key, value, '(' + str(_dict_ref[key]) + ')')