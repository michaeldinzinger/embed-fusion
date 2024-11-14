import click
import pickle
import numpy as np
import matplotlib.pyplot as plt
from ef.utils import *


@click.command()
@click.argument("pretrained_model_name", type=click.Choice(EMBEDDING_MODELS), default=EMBEDDING_MODELS[0])
def svd(pretrained_model_name: str):
    """
    Run Singular Value Decomposition.
    """
    click.echo('Running Singular Value Decomposition')

    n_components = 20
    file_names = ['queries'] + REPO_NAMES

    # Path to orthogonal basis
    ob_path = os.path.join(RESULTS_FOLDER, 'svd', pretrained_model_name.replace("/", "_"), 'orthogonal_basis.pkl')
    os.makedirs(os.path.dirname(ob_path), exist_ok=True)

    # Check if PCA results exist
    if os.path.exists(ob_path):
        click.echo('Loading SVD results...')
        with open(ob_path, 'rb') as f:
            orthogonal_basises = pickle.load(f)

    else:
        click.echo('Computing SVD results...')

        # Embeddings path
        embeddings_path = os.path.join(RESULTS_FOLDER, 'embeddings', pretrained_model_name.replace("/", "_"))

        for file_name in file_names:
            click.echo(f'SVD for {file_name} corpus')

            # Orthogonal basises
            orthogonal_basises = []

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

            # Run SVD
            from sklearn.decomposition import PCA
            pca = PCA(n_components=4)
            pca_result = pca.fit_transform(dense_embeddings)
            print(pca_result.shape)
            print(pca_result)

            print(dense_embeddings.shape)
            print(dense_embeddings)
            print(np.mean(dense_embeddings, axis=0))
            mean_centered = dense_embeddings - np.mean(dense_embeddings, axis=0)
            print(mean_centered.shape)
            print(mean_centered)
            U, _, _ = np.linalg.svd(mean_centered, full_matrices=False)
            print(U)
            click.echo(f'SVD result shape: {U.shape}')

            # Save the explained variance
            orthogonal_basises.append(U)

            break

        # # Save the PCA results
        # with open(ob_path, 'wb') as f:
        #     pickle.dump(orthogonal_basises, f)

    # # Visualize the explained variance
    # plt.figure(figsize=(10, 6))
    # plt.title('SVD: Explained Variance')

    # for file_name, explained_variance_ratio in zip(file_names, orthogonal_basises):
    #     cumulative_variance = np.cumsum(explained_variance_ratio)
    #     click.echo(f'{file_name}: Cumulative variance explained by {n_components} components: {cumulative_variance[-1]:.2f}')

    #     plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, marker='o', linestyle='--', label=file_name)

    # plt.xlabel('Number of Components')
    # plt.ylabel('Explained Variance')
    # plt.grid()
    # plt.legend()
    # plt.savefig(os.path.join(RESULTS_FOLDER, 'svd', pretrained_model_name.replace("/", "_"), 'ev.png'))

    # plt.figure(figsize=(10, 6))
    # plt.title('PCA: Cumulative Explained Variance')

    # for file_name, explained_variance_ratio in zip(file_names, orthogonal_basises):
    #     cumulative_variance = np.cumsum(explained_variance_ratio)
    #     click.echo(f'{file_name}: Cumulative variance explained by {n_components} components: {cumulative_variance[-1]:.2f}')

    #     plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--', label=file_name)

    # plt.xlabel('Number of Components')
    # plt.ylabel('Cumulative Explained Variance')
    # plt.grid()
    # plt.legend()
    # plt.savefig(os.path.join(RESULTS_FOLDER, 'svd', pretrained_model_name.replace("/", "_"), 'cev.png'))