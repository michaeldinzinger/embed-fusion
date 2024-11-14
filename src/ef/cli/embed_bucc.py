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
def embed_bucc(pretrained_model_name: str):
    """
    Embed all corpus documents using a pretrained model.
    """
    # Embed all pretrained models
    if pretrained_model_name == 'all':
        for pretrained_model_name in EMBEDDING_MODELS:
            _embed_bucc(pretrained_model_name)
    else:
        _embed_bucc(pretrained_model_name)


def _embed_bucc(pretrained_model_name: str):
    click.echo(f'Pretrained model: {pretrained_model_name}')

    # Load embedding model
    model = RetrievalModel(pretrained_model_name, 'msmarco')

    # Load BUCC dataset
    dataset = load_dataset('mteb/bucc-bitext-mining', 'de-en')['test']

    # Embed corpus
    corpus = []
    for i, d in enumerate(dataset):
        if i >= LIMIT:
            break
        
        corpus.append({'title': '', 'text': d['sentence1']})
        corpus.append({'title': '', 'text': d['sentence2']})

    # Embed corpus
    corpus_embeddings = embed_corpus(model, corpus)

    # Save corpus
    path = os.path.join(RESULTS_FOLDER, 'bucc', pretrained_model_name.replace('/', '_'), f'embeddings.jsonl')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        for i in range(0, len(corpus_embeddings), 2):
            file.write(json.dumps({'de': corpus_embeddings[i].tolist(), 'en': corpus_embeddings[i + 1].tolist()}) + '\n')