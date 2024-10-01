Some numbers on e5 (output dim 1024), ndcg@10 on NFCorpus. The auto-encoders are trained  on 160k cleaned passages of wikipedia.  

|  dim      | ndcg@10 | loss(*)  |
|-----------|---------|----------|
| e5 (orig) |         |    -     |
| 1024      |         |          |
| 896       | 0.x     |          |
| 768       | 0.33509 | 0.000106 |
| 512       | 0.33013 | 0.000108 |
| 256       | 0.32846 | 0.000117 |

(*) The loss here represents the peak reconstruction loss that led to the score.

Some comments on training:

* The best val loss does not give the best model.
* Focusing on the dim  256:
    * Better success with batch size of 32.
    * hparam>  optim: adamw; lr: 4e-3; w_decay 1e-5

Make the same for Jina embeddings, and compare resutls of the MRL to auto-encoding approach:

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


### TODO:

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
