Some numbers on e5 (output dim 1024), ndcg@10 on NFCorpus. The auto-encoders are trained  on 160k cleaned passages of wikipedia.  

|  dim      | ndcg@10 | loss(1)  |
|-----------|---------|----------|
| e5 (orig) | 0.35661 |    -     |
| 1024(2)   | 0.33514 | 0.000104 |
| 896       |         |          |
| 768       | 0.33509 | 0.000106 |
| 512       | 0.33013 | 0.000108 |
| 384       | 0.      | 0.       |
| 256       | 0.32846 | 0.000117 |


(1) The loss here represents the peak reconstruction loss that led to the score.

(2) Training sanity check (is fine-tuning on wiki hurting the embeddings) 

## e5 -- mxbai:

* Naive concat: 0.37744
* e5          : 0.35661
* mxbai       : 0.37716

|  dim      | ndcg@10 | loss(1)  |
|-----------|---------|----------|
| 2048 (*)  | 0.      | 0.       |
| 1024      | 0.36197 | 0.017030 |
| 768       | 0.53097 | 0.23     |
| 512       | 0.      | 0.       |
| 256       | 0.      | 0.       |

For the 1024 compression, see how the val loss (on wikipedia) affects the ndcg@10:

| ndcg@10 | val loss |
|---------|----------|
| 0.36197 | 0.017030 |
| 0.36382 | 0.017025 |

(*) No auto-encoder, naive concat.


Focusing on the 768 compression as it would be needed later on:




### Small models (<35M):

* Collect 2 models and check the mteb scores if ok.  [DONE]
    * m1: `intfloat/e5-small-v2`  (33M)
        * ndcg@10 - NFCorpus: 0.31806
    * m2: `BAAI/bge-small-en-v1.5`  (33M)
        * ndcg@10 - NFCorpus: 0.33708

* Naive concat (768):  0.35509

### Mini experiment: Can we improve naive concatenation of small models with compressed (using auto-encoders) concat of large models?

1. Using e5-large and mxbai:
    * Concat e5-large and mxbai > `e5-mxbai-2048`.
    * Learn a 786-dim (auto-enc) representation  `e5-mxbai-autoenc-768`.

2. Using bge-smal and e5-small:
    * Concat e5-large and mxbai > `bge-e5-768`.

3. Map the output of `bge-e5-768` to `e5-mxbai-autoenc-768`
    * Using a simple FFNN.
    * Maybe use residual links



Step 1: Using e5-large and mxbai                                         Step 2: Using bge-small and e5-small
--------------------------------                                         ------------------------------------

                  +----------------+                                       +----------------+ 
                  |   Input Text    |                                      |   Input Text   |
                  +--------+-------+                                       +--------+-------+
                           |                                                        |
            +--------------+--------------+                                +--------+-----------+
            |                             |                                |                    |
     +------+-----+                 +-----+------+                   +------+-----+      +------+-----+
     |  e5-large  |                 |   mxbai    |                   | bge-small  |      |  e5-small  |
     +------------+                 +------------+                   +------------+      +------------+
            |                             |                                  |                  |
   [Embedding A (1024)]          [Embedding B (1024)]           [Embedding C (384)]    [Embedding D (384)]
            |                             |                                  |                  |
            +--------------+--------------+                                  +------------------+
                           |                                                         |        
                      [Concatenate]                                             [Concatenate]
                           |                                                         |
                   [e5-mxbai-2048]                                              [bge-e5-768]
                           |                                                       
                     [Autoencoder]                                                 
                           |                                                       
                 [e5-mxbai-autoenc-768]                                        


Step 3: Mapping bge-e5-768 to e5-mxbai-autoenc-768
---------------------------------------------------

                          [bge-e5-768]
                                |
                         +------v------+
                         |    FFNN     |
                         +------+------+  
                                |
                      [e5-mxbai-autoenc-768]
                                |
                      (Optional Residual Links)


### Comparing MRL's implicit representation to Auto-encoder's learned representations:

Model: `jiaai/jina-embeddings-v3` [Link to abstract](https://arxiv.org/pdf/2409.10173)

| Dim   | MRL     | Auto-encoder |
|-------|---------|--------------|
| 32    | 0.23143 |              |
| 64    | 0.28707 |              |
| 128   | 0.31171 |              |
| 512   | 0.33101 |              |
| 768   | 0.33466 |              |
| 1024  | 0.33535 |      X       |



### Urgent TODO:

```python
configs = {
    "256" : {
        "lr" : 4e-3,
        "step-size" : 2, #(used to decay the lr)  
        "w_decay" : 4e-4,
        "batch_size" : 32,
    },
    "512" : {
        "lr" : 4e-3,
        "step-size" : 2, #(used to decay the lr)  
        "w_decay" : 1e-5,
        "batch_size" : 32,
    },

}
```



### Play with:

* Generate data and embeddings of each model: see `auto-encoder/generate_data/README.md`

* Train auto-encoder:
    * Change `config.py`
    * Change `model.py` (if needed)

* Run eval:
    * `python embed_autoencode.py dimension  path_to_checkpoint_of_autoencoder`
    * (if the architecture of the auto-encoder is changed, then it should be changed accord. again) 
