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

* Generate embeddings.
    * `python generate_single_model.py`

* Train auto-encoder:
    * Change `model.py` 
    * Change `config.py`

* Run eval:
    * `python embed_auto_enc.py dimension`
