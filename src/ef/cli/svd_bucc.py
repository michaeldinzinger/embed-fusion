import click
import pickle
import numpy as np
import matplotlib.pyplot as plt
from ef.utils import *


@click.command()
@click.argument("pretrained_model_name", type=click.Choice(EMBEDDING_MODELS), default=EMBEDDING_MODELS[0])
def svd_bucc(pretrained_model_name: str):
    """
    Run Singular Value Decomposition.
    """
    click.echo('Running Singular Value Decomposition')

    languages = ['de', 'en']

    # Path to orthogonal basis
    ob_path = os.path.join(RESULTS_FOLDER, 'svd_bucc', pretrained_model_name.replace("/", "_"), 'orthogonal_basis.pkl')
    os.makedirs(os.path.dirname(ob_path), exist_ok=True)

    # Orthogonal basises
    orthogonal_basises = {}

    # Load embeddings for BUCC dataset
    path = os.path.join(RESULTS_FOLDER, 'bucc', pretrained_model_name.replace("/", "_"), 'embeddings.jsonl')
    if not os.path.exists(path):
        raise ValueError(f'No embeddings found for pretrained model {pretrained_model_name}')
    df = pd.read_json(path, orient='records', lines=True)

    # Check if PCA results exist
    if os.path.exists(ob_path):
        click.echo('Loading SVD results...')
        with open(ob_path, 'rb') as f:
            orthogonal_basises = pickle.load(f)

    else:
        click.echo('Computing SVD results...')

        for language in languages:
            click.echo(f'SVD for language \'{language}\'')

            # Load embeddings for language
            dense_embeddings = np.array(df[language].to_list())
            click.echo(f'Loaded {dense_embeddings.shape[0]} dense embeddings of shape {dense_embeddings.shape[1:]}')

            # Run SVD
            mean = np.mean(dense_embeddings, axis=0)
            mean_centered = dense_embeddings - mean
            U, S, Vt = np.linalg.svd(mean_centered, full_matrices=False)
            click.echo(f'SVD result: U: {U.shape}; S: {S.shape}; Vt: {Vt.shape}')

            explained_variance = (S ** 2) / np.sum(S ** 2)
            cumulative_variance = np.cumsum(explained_variance)
            n_components = np.argmax(cumulative_variance >= 0.9) + 1
            click.echo(f'Cumulative variance explained by {n_components} components: {cumulative_variance[n_components - 1]:.2f}')

            # Save the explained variance
            Vt_subspace = Vt[:n_components, :]
            orthogonal_basises[language] = (Vt_subspace, mean)

        # Save the PCA results
        with open(ob_path, 'wb') as f:
            pickle.dump(orthogonal_basises, f)

    # Compute perplexity
    V_a = orthogonal_basises['de'][0].transpose()
    Vt_a = orthogonal_basises['de'][0]
    mean = orthogonal_basises['de'][1]
    
    dense_embeddings = np.array(df['de'].to_list())
    for x in dense_embeddings:
        proj_a = np.dot(np.dot(V_a, Vt_a), x - mean) + mean
        print(proj_a.shape)
        perplexity = np.exp(-np.sum(x * np.log(proj_a)))
        print(perplexity)
        break

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