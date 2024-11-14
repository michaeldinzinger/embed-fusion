import click
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from ef.utils import *


@click.command()
@click.argument("pretrained_model_name", type=click.Choice(EMBEDDING_MODELS), default=EMBEDDING_MODELS[0])
def lda(pretrained_model_name: str):
    """
    Run Linear Discriminant Analysis.
    """
    click.echo('Running Linear Discriminant Analysis')

    # file_names = ['queries'] + REPO_NAMES
    # file_names = ['id_100_mid', 'ood_100_mid']
    # file_names = ['id_500_mid', 'ood_500_mid']
    # file_names = ['id_100_mid', 'id_500_mid']
    # file_names = ['queries', 'id_100_mid', 'id_500_mid']
    file_names = ['queries', 'id_100_mid', 'ood_100_mid', 'id_500_mid', 'ood_500_mid']

    # Embeddings path
    embeddings_path = os.path.join(RESULTS_FOLDER, 'embeddings', pretrained_model_name.replace("/", "_"))

    # List of dense embeddings
    embeddings_list = []
    labels = []
    
    for file_name in file_names:
        click.echo(f'Load corpus \'{file_name}\'')

        # Load corpus embeddings for passages
        path = os.path.join(embeddings_path, f'{file_name}.jsonl')
        if not os.path.exists(path):
            raise ValueError(f'No corpus embeddings found for pretrained model {pretrained_model_name}')
        df = pd.read_json(path, orient='records', lines=True)
        if file_name == 'queries':
            df = df.set_index('query-id')
        else:
            df = df.set_index('corpus-id')
        embeddings_list += df['embedding'].to_list()
        labels += [file_names.index(file_name)] * len(df)
        
    X = np.array(embeddings_list)
    y = np.array(labels)
    # y = np.random.randint(0, 2, len(df) * 2)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create the LDA model
    lda = LinearDiscriminantAnalysis(n_components=2)

    # Fit the model to the training data
    lda = lda.fit(X_train, y_train)

    # # Load coefficients
    # coefficients = lda.coef_[0]
    # click.echo(f'Coefficients: {coefficients.shape}')

    # # Sort the features by their importance
    # sorted_indices = np.argsort(np.abs(coefficients))[::-1]
    # sorted_coefficients = coefficients[sorted_indices]
    # important_dimensions = sorted_indices[:10]
    # importance = sorted_coefficients[:100]
    # print(important_dimensions)
    # print(importance)

    # Predict the labels for the test set
    y_pred = lda.predict(X_test)

    # Evaluate the model's performance
    accuracy = accuracy_score(y_test, y_pred)
    click.echo(f"Accuracy: {accuracy:.2f}")

    # Print predicted and true labels
    print("Predicted labels:", y_pred)
    print("True labels:", y_test)

    # Visualize the LDA results
    transformed = lda.transform(X_test)
    click.echo(f'LDA result: {transformed.shape}')

    plt.scatter(transformed[:, 0], transformed[:, 1], c=y_test, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlabel('LD1')
    plt.ylabel('LD2')
    plt.title('LDA of Iris dataset')
    plt.savefig('lda___1.png')

    plt.scatter(transformed[:, 0], transformed[:, 1], c=y_pred, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlabel('LD1')
    plt.ylabel('LD2')
    plt.title('LDA of Iris dataset')
    plt.savefig('lda___2.png')