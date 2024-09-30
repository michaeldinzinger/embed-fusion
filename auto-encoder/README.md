Some numbers on e5 (output dim 1024), ndcg@10 on NFCorpus. The auto-encoders are trained  on 160k cleaned passages of wikipedia.  

|   mension | ndcg@10 |
|-----------|---------|
| 1024      | 0.28966 |
| 900       | 0.29149 |
| 800       | 0.29719 |
| 700       | 0.2895  |
| 600       | 0.29119 |
| 500       | 0.27735 |



### TODO:

* Try better auto-encoders (better learning strategies, etc)
* Try sim. metrics on s Sparse auto-encoder 



### Play with:

* Generate embeddings.
    * `python generate_single_model.py`

* Train auto-encoder:
    * Change `model.py` 
    * Change `config.py`

* Run eval:
    * `python embed_auto_enc.py dimension`
