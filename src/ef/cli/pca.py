import click
import pickle
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from ef.utils import *


@click.command()
@click.argument("pretrained_model_name", type=click.Choice(EMBEDDING_MODELS), default=EMBEDDING_MODELS[0])
def pca(pretrained_model_name: str):
    """
    Run Principal Component Analysis.
    """
    click.echo('Running Principal Component Analysis')

    n_components = 20
    file_names = ['queries'] + REPO_NAMES

    # Path to explain variance ratios
    evr_path = os.path.join(RESULTS_FOLDER, 'pca', pretrained_model_name.replace("/", "_"), 'explained_variance_ratios.pkl')
    os.makedirs(os.path.dirname(evr_path), exist_ok=True)

    # Check if PCA results exist
    if os.path.exists(evr_path):
        click.echo('Loading PCA results...')
        with open(evr_path, 'rb') as f:
            explained_variance_ratios = pickle.load(f)

    else:
        click.echo('Computing PCA results...')

        # Explained variance ratios
        explained_variance_ratios = []

        # Embeddings path
        embeddings_path = os.path.join(RESULTS_FOLDER, 'embeddings', pretrained_model_name.replace("/", "_"))

        for file_name in file_names:
            click.echo(f'PCA for {file_name} corpus')

            # Load corpus embeddings for passages
            path = os.path.join(embeddings_path, f'{file_name}.jsonl')
            if not os.path.exists(path):
                raise ValueError(f'No corpus embeddings found for pretrained model {pretrained_model_name}')
            df = pd.read_json(path, orient='records', lines=True)
            if file_name == 'queries':
                df = df.set_index('query-id')
            else:
                df = df.set_index('corpus-id')
            dense_embeddings = np.array(df['embedding'].to_list())
            click.echo(f'Loaded {dense_embeddings.shape[0]} dense embeddings of shape {dense_embeddings.shape[1:]}')

            # Run PCA
            pca = PCA(n_components=n_components)
            dense_embeddings -= np.mean(dense_embeddings, axis=0)
            pca_result = pca.fit_transform(dense_embeddings)
            click.echo(f'PCA result shape: {pca_result.shape}')

            # Save the explained variance
            explained_variance_ratios.append(pca.explained_variance_ratio_)

        # Save the PCA results
        with open(evr_path, 'wb') as f:
            pickle.dump(explained_variance_ratios, f)

    # Visualize the explained variance
    plt.figure(figsize=(10, 6))
    plt.title('PCA: Explained Variance')

    for file_name, explained_variance_ratio in zip(file_names, explained_variance_ratios):
        cumulative_variance = np.cumsum(explained_variance_ratio)
        click.echo(f'{file_name}: Cumulative variance explained by {n_components} components: {cumulative_variance[-1]:.2f}')

        plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, marker='o', linestyle='--', label=file_name)

    plt.xlabel('Number of Components')
    plt.ylabel('Explained Variance')
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join(RESULTS_FOLDER, 'pca', pretrained_model_name.replace("/", "_"), 'ev.png'))

    plt.figure(figsize=(10, 6))
    plt.title('PCA: Cumulative Explained Variance')

    for file_name, explained_variance_ratio in zip(file_names, explained_variance_ratios):
        cumulative_variance = np.cumsum(explained_variance_ratio)
        click.echo(f'{file_name}: Cumulative variance explained by {n_components} components: {cumulative_variance[-1]:.2f}')

        plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--', label=file_name)

    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join(RESULTS_FOLDER, 'pca', pretrained_model_name.replace("/", "_"), 'cev.png'))