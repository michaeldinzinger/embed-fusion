import click
import json
from mteb import MTEB
from mteb.tasks.Retrieval.eng.SciFactRetrieval import SciFact
from ef.globals import *
from ef.utils import *


_dict = {}
_dict_ref = {
    'BAAI/bge-small-en-v1.5': 71.28,
    'TaylorAI/gte-tiny': 67.51,
    'mixedbread-ai/mxbai-embed-large-v1': 74.73,
    'Snowflake/snowflake-arctic-embed-m-v1.5': 71.59,
    'nthakur/contriever-base-msmarco': 65.51,
    'dunzhang/stella_en_1.5B_v5': 80.09,
    'Salesforce/SFR-Embedding-Mistral': 77.66,
    'Alibaba-NLP/gte-large-en-v1.5': 82.43,
    'Alibaba-NLP/gte-Qwen2-1.5B-instruct': 78.44,
    'Alibaba-NLP/gte-Qwen2-7B-instruct': 79.06,
    'nvidia/NV-Embed-v2': 80.13,
    'jinaai/jina-embeddings-v3': 72.31,
    'BAAI/bge-multilingual-gemma2': 72.05,
}


@click.command()
@click.argument("pretrained_model_name", type=click.Choice(EMBEDDING_MODELS + ['all']), default=EMBEDDING_MODELS[0])
def plausibility(pretrained_model_name: str):
    """
    Check plausibility with MTEB SciFact benchmark.
    """
    # Evaluate all pretrained models
    if pretrained_model_name == 'all':
        for pretrained_model_name in EMBEDDING_MODELS:
            _plausibility(pretrained_model_name)
    else:
        _plausibility(pretrained_model_name)


def _plausibility(pretrained_model_name: str):
    click.echo(f'Pretrained model: {pretrained_model_name}')

    model = RetrievalModel(pretrained_model_name, 'scifact')
    
    task = SciFact()

    task_output_path = os.path.join(RESULTS_FOLDER, 'temp', pretrained_model_name.replace('/', '_'))
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
        click.echo(f'NDCG@10 for model {pretrained_model_name} in task {type(task).__name__}: {ndcg_at_10}')

        _dict[pretrained_model_name] = ndcg_at_10
        for key, value in _dict.items():
            print(key, value, '(' + str(_dict_ref[key]) + ')')