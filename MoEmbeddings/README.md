## Set up:

We have two small embeddigns (33M) with 384 dim output:
* m1: `intfloat/e5-small-v2`  (33M)
    * ndcg@10 - NFCorpus: 0.31806
* m2: `BAAI/bge-small-en-v1.5`  (33M)
    * ndcg@10 - NFCorpus: 0.33708

* Naive concat:
    *

         |  Solo     |            |   up-train (1024) |  Down-train (384) | 
e5-small | 0.31806   |            |                   |                   |  
bge-small| 0.33708   |            |                   |                   |

* Down-train concatenation:



## Delete this


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



