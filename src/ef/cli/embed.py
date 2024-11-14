import click
import json
from datasets import load_dataset
from ef.globals import *
from ef.utils import *
from ef.config import *


CORPUS_CHUNK_SIZE = 50_000
LIMIT = 50_000


def embed_corpus(model: RetrievalModel, corpus: List[Dict[str, str]]):
    itr = range(0, len(corpus), CORPUS_CHUNK_SIZE)

    corpus_embeddings = []
    for _, corpus_start_idx in enumerate(itr):
        corpus_end_idx = min(corpus_start_idx + CORPUS_CHUNK_SIZE, len(corpus))

        # Encode chunk of corpus
        sub_corpus_embeddings = model.encode_corpus(corpus[corpus_start_idx:corpus_end_idx])
        corpus_embeddings.extend(sub_corpus_embeddings)

    return corpus_embeddings


@click.command()
@click.argument("pretrained_model_name", type=click.Choice(EMBEDDING_MODELS + ['all']), default=EMBEDDING_MODELS[0])
def embed(pretrained_model_name: str):
    """
    Embed all corpus documents using a pretrained model.
    """
    # Embed all pretrained models
    if pretrained_model_name == 'all':
        for pretrained_model_name in EMBEDDING_MODELS:
            _embed(pretrained_model_name)
    else:
        _embed(pretrained_model_name)


def _embed(pretrained_model_name: str):
    click.echo(f'Pretrained model: {pretrained_model_name}')

    # Load embedding model
    model = RetrievalModel(pretrained_model_name, 'msmarco')

    # Queries path
    path = os.path.join(RESULTS_FOLDER, 'embeddings', pretrained_model_name.replace('/', '_'), 'queries.jsonl')
    if os.path.exists(path):
        click.echo('Embedding of queries skipped...')
    else:
        click.echo('Embedding queries...')

        # Load queries dataset
        dataset_queries = load_dataset(f'michaeldinzinger/msmarco-chunkeval-base', 'queries')['queries']
        # print(dataset_queries)

        # Embed queries
        query_ids = []
        queries = []
        for d in dataset_queries:
            query_ids.append(d['_id'])
            queries.append(d['text'])

        queries_embeddings = model.encode_queries(queries)

        # Save queries
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as file:
            for query_id, query_embedding in zip(query_ids, queries_embeddings):
                file.write(json.dumps({'query-id': query_id, 'embedding': query_embedding.tolist()}) + '\n')

    # Loop over all repos of the customized MS-MARCO dataset
    for repo_name in REPO_NAMES:
        click.echo(f'Embedding {repo_name} corpus...')

        # Load corpus dataset
        dataset_corpus = load_dataset(f'michaeldinzinger/msmarco-chunkeval-{repo_name}', 'corpus')['corpus']
        # print(dataset_corpus)

        # Embed corpus
        corpus_ids = []
        corpus = []
        for d in dataset_corpus:
            corpus_ids.append(d['_id'])
            corpus.append({'title': d['title'], 'text': d['text']})

            if len(corpus) >= LIMIT:
                break

        # Embed corpus
        corpus_embeddings = embed_corpus(model, corpus)

        # Save corpus
        path = os.path.join(RESULTS_FOLDER, 'embeddings', pretrained_model_name.replace('/', '_'), f'{repo_name}.jsonl')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as file:
            for corpus_id, corpus_embedding in zip(corpus_ids, corpus_embeddings):
                file.write(json.dumps({'corpus-id': corpus_id, 'embedding': corpus_embedding.tolist()}) + '\n')