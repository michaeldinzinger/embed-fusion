TASK_NAMES = [
    'SciFact',
    'FiQA2018',
    # 'TRECCOVID',
]

EMBEDDING_MODELS = [
    'BAAI/bge-small-en-v1.5',
    'BAAI/bge-large-en-v1.5',
    'Snowflake/snowflake-arctic-embed-m-v1.5',
    'dunzhang/stella_en_1.5B_v5',
    'Alibaba-NLP/gte-Qwen2-1.5B-instruct',
    'intfloat/e5-small-v2',
    'Salesforce/SFR-Embedding-Mistral',
]
    # 'BAAI/bge-multilingual-gemma2',
    # 'test',

REPO_NAMES = [
    'id_100_mid',
    'ood_100_mid',
    'id_500_mid',
    'ood_500_mid',
]

RESULTS_FOLDER = 'results'
RESULTS_CONCAT_FILE = 'results_concat.csv'