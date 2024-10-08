Some numbers on e5 (output dim 1024), ndcg@10 on NFCorpus. The auto-encoders are trained  on 160k cleaned passages of wikipedia.  

|  dim      | ndcg@10 | loss(1)  |
|-----------|---------|----------|
| e5 (orig) | 0.35661 |    -     |
| 1024(2)   | 0.33514 | 0.000104 |
| 896       |         |          |
| 768       | 0.33509 | 0.000106 |
| 512       | 0.33013 | 0.000108 |
| 256       | 0.32846 | 0.000117 |


(1) The loss here represents the peak reconstruction loss that led to the score.

(2) Training sanity check (is fine-tuning on wiki hurting the embeddings) 

## e5 -- mxbai:

* Naive concat: 0.37744
* e5          : 0.35661
* mxbai       : 0.37716

|  dim      | ndcg@10 | loss(1)  |
|-----------|---------|----------|
| 2048 (*)  | 0.      | 0. |
| 1024      | 0.36197 | 0.017030 |
| 512       | 0.      | 0. |
| 256       | 0.      | 0. |

For the 1024 compression, see how the val loss (on wikipedia) affects the ndcg@10:

| ndcg@10 | val loss |
|---------|----------|
| 0.36197 | 0.017030 |
| 0.36382 | 0.017025 |
| 0.      | 0.       |

(*) No auto-encoder, naive concat.

### mini experiment: Augment small models with compressed 384 dim e5 // 384 dim mxbai.

* Compress e5/ mxbai to 384.
* Train the FF (input: embeddings of e5-small // output: embeddings of e5-large)
* Test on mteb.

### Small models (<35M):

* Collect 2 models and check the mteb scores if ok.  [DONE]
    * m1: `intfloat/e5-small-v2`  (33M)
        * ndcg@10 - NFCorpus: 0.31806
    * m2: `BAAI/bge-small-en-v1.5`  (33M)
        * ndcg@10 - NFCorpus: 0.33708

* Generate wiki embeddings of each.

* Collect some data, naive concat?

### Urgent TODO:

* Make the same for Jina embeddings, and compare resutls of the MRL to auto-encoding approach.
* Re-run the concatenation code with the new hparams. 
* Concat weak models (up to 5), and subject it to a loss.

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


### Plan:

* Train a on Sparse auto-encoder, and see if sim tests holds.
* Train >> Combine two models.
* Combine two with loss.

### Play with:

* Generate data and embeddings of each model: see `auto-encoder/generate_data/README.md`

* Train auto-encoder:
    * Change `config.py`
    * Change `model.py` (if needed)

* Run eval:
    * `python embed_autoencode.py dimension  path_to_checkpoint_of_autoencoder`
    * (if the architecture of the auto-encoder is changed, then it should be changed accord. again) 
