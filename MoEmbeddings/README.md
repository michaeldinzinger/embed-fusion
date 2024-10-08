## Idea:

Have 6 small embeddigs, and with every request merge two embeddigns (using a Router, itself an embeddign)

Target models: Small models of 30M parameters. 


Steps:

1. Pick the models and check if their encoding is right (using SentenceTransformer)

```python
models = {
"jina": "jinaai/jina-embeddings-v2-small-en" # should the base of the router


}
```
2. I think I might need a more serious dataset, with clear separation (english / french / code? )
    * See if the stronger in Fr model will be picked.




