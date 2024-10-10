## Set up:

We have two small embeddigns (33M) with 384 dim output:
* m1: `intfloat/e5-small-v2`  (33M)
    * ndcg@10 - NFCorpus: 0.31806
* m2: `BAAI/bge-small-en-v1.5`  (33M)
    * ndcg@10 - NFCorpus: 0.33708

* Naive concat: 0.35509

|           | Solo    | Up-train (1024) | Down-train (384) |
|-----------|---------|-----------------|------------------|
| e5-small  | 0.31806 |                 |                  |
| bge-small | 0.33708 |                 |                  |


* Down-train concatenation:
