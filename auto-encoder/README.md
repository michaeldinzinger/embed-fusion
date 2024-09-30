Some numbers on e5 (output dim 1024), ndcg@10 on NFCorpus. The auto-encoders are trained  on 160k cleaned passages of wikipedia.  

|  dim      | ndcg@10 |
|-----------|---------|
| 1024      | 0.28966 |
| 900       | 0.29149 |
| 800       | 0.29719 |
| 700       | 0.2895  |
| 600       | 0.29119 |
| 500       | 0.27735 |



| 256 | 0.23603 |  adam



### TODO:

* Try better auto-encoders (better learning strategies, etc)
* Train a on Sparse auto-encoder, and see if sim tests holds.





### Play with:

* Generate embeddings.
    * `python generate_single_model.py`

* Train auto-encoder:
    * Change `model.py` 
    * Change `config.py`

* Run eval:
    * `python embed_auto_enc.py dimension`
