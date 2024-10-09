Steps:

1. Generate the wiki embeddigns and save them, along side the split of indices:
```bash
$ python generate_split.py
```

2. Generate embeddigns of each model, following the same index split:
```bash
$ python generate_embeddings model_name
```

Model names should be one of these keys:
```python
models = {
            "mxbai"     : "mixedbread-ai/mxbai-embed-large-v1",  
            "bge"       : "BAAI/bge-large-en-v1.5"                 ,
            "e5"        : "intfloat/e5-large-v2"              ,
            "snowflake-m" : "Snowflake/snowflake-arctic-embed-m",
            "snowflake-l" : "Snowflake/snowflake-arctic-embed-l",
            "gte-base"        : "thenlper/gte-base",
            "gte-large"       : "thenlper/gte-large",
            "gte-small"       : "thenlper/gte-small",
            "e5-small"        : "intfloat/e5-small-v2", # (33M)
            "bge-small"       : "BAAI/bge-small-en-v1.5" # (33M)
}
```

