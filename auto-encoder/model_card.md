---
model-index:
- name: no_model_name_available
  results:
  - dataset:
      config: en-ext
      name: MTEB AmazonCounterfactualClassification (en-ext)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 75.58470764617691
    - type: ap
      value: 24.719701151617723
    - type: ap_weighted
      value: 24.719701151617723
    - type: f1
      value: 63.00164246074738
    - type: f1_weighted
      value: 80.03796552199202
    - type: main_score
      value: 75.58470764617691
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 74.34328358208955
    - type: ap
      value: 37.50929758783498
    - type: ap_weighted
      value: 37.50929758783498
    - type: f1
      value: 68.47468266207234
    - type: f1_weighted
      value: 76.71536156910686
    - type: main_score
      value: 74.34328358208955
    task:
      type: Classification
  - dataset:
      config: en-ext
      name: MTEB AmazonCounterfactualClassification (en-ext)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: validation
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 73.10810810810811
    - type: ap
      value: 21.095894998268182
    - type: ap_weighted
      value: 21.095894998268182
    - type: f1
      value: 59.88562259265849
    - type: f1_weighted
      value: 78.24218318628027
    - type: main_score
      value: 73.10810810810811
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: validation
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 73.76119402985076
    - type: ap
      value: 33.462242773250075
    - type: ap_weighted
      value: 33.462242773250075
    - type: f1
      value: 66.50228790953409
    - type: f1_weighted
      value: 76.66423272035549
    - type: main_score
      value: 73.76119402985076
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification (default)
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 92.99744999999999
    - type: ap
      value: 89.7770669227447
    - type: ap_weighted
      value: 89.7770669227447
    - type: f1
      value: 92.98870898689393
    - type: f1_weighted
      value: 92.98870898689394
    - type: main_score
      value: 92.99744999999999
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 49.364000000000004
    - type: f1
      value: 48.09686892529694
    - type: f1_weighted
      value: 48.09686892529693
    - type: main_score
      value: 49.364000000000004
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: validation
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 48.797999999999995
    - type: f1
      value: 47.572308082658886
    - type: f1_weighted
      value: 47.572308082658886
    - type: main_score
      value: 48.797999999999995
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna (default)
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: main_score
      value: 59.345000000000006
    - type: map_at_1
      value: 34.993
    - type: map_at_10
      value: 50.93299999999999
    - type: map_at_100
      value: 51.653999999999996
    - type: map_at_1000
      value: 51.659
    - type: map_at_20
      value: 51.503
    - type: map_at_3
      value: 46.539
    - type: map_at_5
      value: 49.078
    - type: mrr_at_1
      value: 35.34850640113798
    - type: mrr_at_10
      value: 51.08029081713292
    - type: mrr_at_100
      value: 51.79453395523629
    - type: mrr_at_1000
      value: 51.79922640990794
    - type: mrr_at_20
      value: 51.64015533841996
    - type: mrr_at_3
      value: 46.68089141773353
    - type: mrr_at_5
      value: 49.20578473210052
    - type: nauc_map_at_1000_diff1
      value: 10.777019519798255
    - type: nauc_map_at_1000_max
      value: -7.407917463470924
    - type: nauc_map_at_1000_std
      value: -7.563268405241759
    - type: nauc_map_at_100_diff1
      value: 10.779545140640199
    - type: nauc_map_at_100_max
      value: -7.401298063310178
    - type: nauc_map_at_100_std
      value: -7.556601235531485
    - type: nauc_map_at_10_diff1
      value: 10.721539302065686
    - type: nauc_map_at_10_max
      value: -7.166136768327753
    - type: nauc_map_at_10_std
      value: -7.293662115267615
    - type: nauc_map_at_1_diff1
      value: 14.156914156584854
    - type: nauc_map_at_1_max
      value: -9.498793111705812
    - type: nauc_map_at_1_std
      value: -9.726351399489474
    - type: nauc_map_at_20_diff1
      value: 10.761980363958246
    - type: nauc_map_at_20_max
      value: -7.3011716552322445
    - type: nauc_map_at_20_std
      value: -7.474633798851565
    - type: nauc_map_at_3_diff1
      value: 10.32402309373244
    - type: nauc_map_at_3_max
      value: -7.789968158157112
    - type: nauc_map_at_3_std
      value: -8.459911202243127
    - type: nauc_map_at_5_diff1
      value: 9.950359837131687
    - type: nauc_map_at_5_max
      value: -7.54700058691015
    - type: nauc_map_at_5_std
      value: -7.4852438758641515
    - type: nauc_mrr_at_1000_diff1
      value: 9.545661892556165
    - type: nauc_mrr_at_1000_max
      value: -8.17995767306064
    - type: nauc_mrr_at_1000_std
      value: -7.690544153747644
    - type: nauc_mrr_at_100_diff1
      value: 9.54837560401051
    - type: nauc_mrr_at_100_max
      value: -8.173227861584765
    - type: nauc_mrr_at_100_std
      value: -7.683867106566364
    - type: nauc_mrr_at_10_diff1
      value: 9.522795074409384
    - type: nauc_mrr_at_10_max
      value: -7.9063165040486645
    - type: nauc_mrr_at_10_std
      value: -7.431873185012491
    - type: nauc_mrr_at_1_diff1
      value: 13.130099478615803
    - type: nauc_mrr_at_1_max
      value: -9.992669947319378
    - type: nauc_mrr_at_1_std
      value: -10.051618087478493
    - type: nauc_mrr_at_20_diff1
      value: 9.541270804874118
    - type: nauc_mrr_at_20_max
      value: -8.058828250931276
    - type: nauc_mrr_at_20_std
      value: -7.598979599209439
    - type: nauc_mrr_at_3_diff1
      value: 9.116533214412966
    - type: nauc_mrr_at_3_max
      value: -8.540266568222016
    - type: nauc_mrr_at_3_std
      value: -8.693222832504544
    - type: nauc_mrr_at_5_diff1
      value: 8.694955232599785
    - type: nauc_mrr_at_5_max
      value: -8.34107055995193
    - type: nauc_mrr_at_5_std
      value: -7.6629161714950484
    - type: nauc_ndcg_at_1000_diff1
      value: 10.526533346595262
    - type: nauc_ndcg_at_1000_max
      value: -6.703732662610731
    - type: nauc_ndcg_at_1000_std
      value: -6.603623582089393
    - type: nauc_ndcg_at_100_diff1
      value: 10.561172146895252
    - type: nauc_ndcg_at_100_max
      value: -6.514791218416639
    - type: nauc_ndcg_at_100_std
      value: -6.354781956088969
    - type: nauc_ndcg_at_10_diff1
      value: 10.361381171866082
    - type: nauc_ndcg_at_10_max
      value: -5.2230158943462985
    - type: nauc_ndcg_at_10_std
      value: -5.007524284028199
    - type: nauc_ndcg_at_1_diff1
      value: 14.156914156584854
    - type: nauc_ndcg_at_1_max
      value: -9.498793111705812
    - type: nauc_ndcg_at_1_std
      value: -9.726351399489474
    - type: nauc_ndcg_at_20_diff1
      value: 10.517676064474847
    - type: nauc_ndcg_at_20_max
      value: -5.711765067868173
    - type: nauc_ndcg_at_20_std
      value: -5.605824861630572
    - type: nauc_ndcg_at_3_diff1
      value: 9.186600380601536
    - type: nauc_ndcg_at_3_max
      value: -7.056576818596352
    - type: nauc_ndcg_at_3_std
      value: -7.812761606548313
    - type: nauc_ndcg_at_5_diff1
      value: 8.432418101937406
    - type: nauc_ndcg_at_5_max
      value: -6.480411547015269
    - type: nauc_ndcg_at_5_std
      value: -5.777975379414998
    - type: nauc_precision_at_1000_diff1
      value: 13.955746514246906
    - type: nauc_precision_at_1000_max
      value: 28.8840202640091
    - type: nauc_precision_at_1000_std
      value: 65.36756825837523
    - type: nauc_precision_at_100_diff1
      value: 14.686199038527814
    - type: nauc_precision_at_100_max
      value: 31.31632878025447
    - type: nauc_precision_at_100_std
      value: 54.07113844512418
    - type: nauc_precision_at_10_diff1
      value: 9.662188427513989
    - type: nauc_precision_at_10_max
      value: 9.22345326975617
    - type: nauc_precision_at_10_std
      value: 11.831872077040245
    - type: nauc_precision_at_1_diff1
      value: 14.156914156584854
    - type: nauc_precision_at_1_max
      value: -9.498793111705812
    - type: nauc_precision_at_1_std
      value: -9.726351399489474
    - type: nauc_precision_at_20_diff1
      value: 11.432148213771988
    - type: nauc_precision_at_20_max
      value: 18.514764981962074
    - type: nauc_precision_at_20_std
      value: 22.78510644336147
    - type: nauc_precision_at_3_diff1
      value: 5.6317217760949685
    - type: nauc_precision_at_3_max
      value: -4.676598241685319
    - type: nauc_precision_at_3_std
      value: -5.684836764145716
    - type: nauc_precision_at_5_diff1
      value: 2.5659150784472753
    - type: nauc_precision_at_5_max
      value: -2.1551693896958524
    - type: nauc_precision_at_5_std
      value: 1.384881159297645
    - type: nauc_recall_at_1000_diff1
      value: 13.955746514247625
    - type: nauc_recall_at_1000_max
      value: 28.884020264002835
    - type: nauc_recall_at_1000_std
      value: 65.36756825836953
    - type: nauc_recall_at_100_diff1
      value: 14.686199038527365
    - type: nauc_recall_at_100_max
      value: 31.31632878025263
    - type: nauc_recall_at_100_std
      value: 54.071138445123225
    - type: nauc_recall_at_10_diff1
      value: 9.662188427513836
    - type: nauc_recall_at_10_max
      value: 9.22345326975619
    - type: nauc_recall_at_10_std
      value: 11.83187207704014
    - type: nauc_recall_at_1_diff1
      value: 14.156914156584854
    - type: nauc_recall_at_1_max
      value: -9.498793111705812
    - type: nauc_recall_at_1_std
      value: -9.726351399489474
    - type: nauc_recall_at_20_diff1
      value: 11.432148213772072
    - type: nauc_recall_at_20_max
      value: 18.514764981961978
    - type: nauc_recall_at_20_std
      value: 22.785106443361688
    - type: nauc_recall_at_3_diff1
      value: 5.63172177609501
    - type: nauc_recall_at_3_max
      value: -4.676598241685221
    - type: nauc_recall_at_3_std
      value: -5.684836764145642
    - type: nauc_recall_at_5_diff1
      value: 2.5659150784473406
    - type: nauc_recall_at_5_max
      value: -2.1551693896959048
    - type: nauc_recall_at_5_std
      value: 1.3848811592975896
    - type: ndcg_at_1
      value: 34.993
    - type: ndcg_at_10
      value: 59.345000000000006
    - type: ndcg_at_100
      value: 62.324999999999996
    - type: ndcg_at_1000
      value: 62.437
    - type: ndcg_at_20
      value: 61.36899999999999
    - type: ndcg_at_3
      value: 50.381
    - type: ndcg_at_5
      value: 54.923
    - type: precision_at_1
      value: 34.993
    - type: precision_at_10
      value: 8.599
    - type: precision_at_100
      value: 0.988
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.694
    - type: precision_at_3
      value: 20.507
    - type: precision_at_5
      value: 14.495
    - type: recall_at_1
      value: 34.993
    - type: recall_at_10
      value: 85.989
    - type: recall_at_100
      value: 98.791
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_20
      value: 93.88300000000001
    - type: recall_at_3
      value: 61.522
    - type: recall_at_5
      value: 72.475
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 47.552697319955676
    - type: v_measure
      value: 47.552697319955676
    - type: v_measure_std
      value: 13.808952106577216
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S (default)
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 40.03337707775063
    - type: v_measure
      value: 40.03337707775063
    - type: v_measure_std
      value: 14.249888078941146
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions (default)
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: main_score
      value: 61.8126291529566
    - type: map
      value: 61.8126291529566
    - type: mrr
      value: 74.36705799586686
    - type: nAUC_map_diff1
      value: 8.967467836084921
    - type: nAUC_map_max
      value: 26.579764001539115
    - type: nAUC_map_std
      value: 17.40600362828969
    - type: nAUC_mrr_diff1
      value: 17.598155509582792
    - type: nAUC_mrr_max
      value: 39.897111892695534
    - type: nAUC_mrr_std
      value: 22.494399933018467
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: cosine_pearson
      value: 86.08936662443202
    - type: cosine_spearman
      value: 84.89832000798314
    - type: euclidean_pearson
      value: 84.81392595158542
    - type: euclidean_spearman
      value: 84.89832000798314
    - type: main_score
      value: 84.89832000798314
    - type: manhattan_pearson
      value: 85.13291943945366
    - type: manhattan_spearman
      value: 85.16820567558344
    - type: pearson
      value: 86.08936662443202
    - type: spearman
      value: 84.89832000798314
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 82.18831168831169
    - type: f1
      value: 81.5323786025089
    - type: f1_weighted
      value: 81.5323786025089
    - type: main_score
      value: 82.18831168831169
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 38.67384534802573
    - type: v_measure
      value: 38.67384534802573
    - type: v_measure_std
      value: 0.7568897383721817
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S (default)
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 34.355519780975385
    - type: v_measure
      value: 34.355519780975385
    - type: v_measure_std
      value: 1.110838684148089
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: main_score
      value: 49.34
    - type: map_at_1
      value: 31.978
    - type: map_at_10
      value: 42.963
    - type: map_at_100
      value: 44.446999999999996
    - type: map_at_1000
      value: 44.584
    - type: map_at_20
      value: 43.804
    - type: map_at_3
      value: 39.422000000000004
    - type: map_at_5
      value: 41.504000000000005
    - type: mrr_at_1
      value: 39.77110157367668
    - type: mrr_at_10
      value: 49.26595817153757
    - type: mrr_at_100
      value: 49.978002791230615
    - type: mrr_at_1000
      value: 50.02634861972985
    - type: mrr_at_20
      value: 49.71356312876928
    - type: mrr_at_3
      value: 46.49499284692418
    - type: mrr_at_5
      value: 48.22603719599428
    - type: nauc_map_at_1000_diff1
      value: 47.79618096338393
    - type: nauc_map_at_1000_max
      value: 41.176156568022584
    - type: nauc_map_at_1000_std
      value: -2.896933596181026
    - type: nauc_map_at_100_diff1
      value: 47.809435131565934
    - type: nauc_map_at_100_max
      value: 41.16647280007524
    - type: nauc_map_at_100_std
      value: -2.8831579711166193
    - type: nauc_map_at_10_diff1
      value: 48.10973144108661
    - type: nauc_map_at_10_max
      value: 40.664863006508625
    - type: nauc_map_at_10_std
      value: -3.578886025167837
    - type: nauc_map_at_1_diff1
      value: 51.708891898356256
    - type: nauc_map_at_1_max
      value: 36.28682951162398
    - type: nauc_map_at_1_std
      value: -7.4668723971868065
    - type: nauc_map_at_20_diff1
      value: 47.9555643209195
    - type: nauc_map_at_20_max
      value: 40.916180069472304
    - type: nauc_map_at_20_std
      value: -3.0932267113062433
    - type: nauc_map_at_3_diff1
      value: 48.98794466901641
    - type: nauc_map_at_3_max
      value: 39.681057169237455
    - type: nauc_map_at_3_std
      value: -5.066827772334784
    - type: nauc_map_at_5_diff1
      value: 48.646328680462275
    - type: nauc_map_at_5_max
      value: 40.477824460870764
    - type: nauc_map_at_5_std
      value: -4.491443351489804
    - type: nauc_mrr_at_1000_diff1
      value: 45.616911771663744
    - type: nauc_mrr_at_1000_max
      value: 41.74404269617856
    - type: nauc_mrr_at_1000_std
      value: -4.559184319493835
    - type: nauc_mrr_at_100_diff1
      value: 45.59611866833938
    - type: nauc_mrr_at_100_max
      value: 41.72604055232334
    - type: nauc_mrr_at_100_std
      value: -4.558345700839123
    - type: nauc_mrr_at_10_diff1
      value: 45.55894061838237
    - type: nauc_mrr_at_10_max
      value: 41.77360038611892
    - type: nauc_mrr_at_10_std
      value: -4.618036976051173
    - type: nauc_mrr_at_1_diff1
      value: 48.15582854302911
    - type: nauc_mrr_at_1_max
      value: 39.82659893618731
    - type: nauc_mrr_at_1_std
      value: -8.183852381071691
    - type: nauc_mrr_at_20_diff1
      value: 45.57723701387737
    - type: nauc_mrr_at_20_max
      value: 41.6914875419549
    - type: nauc_mrr_at_20_std
      value: -4.4669938868552865
    - type: nauc_mrr_at_3_diff1
      value: 46.254550893686755
    - type: nauc_mrr_at_3_max
      value: 41.4719065274011
    - type: nauc_mrr_at_3_std
      value: -5.655174401673945
    - type: nauc_mrr_at_5_diff1
      value: 46.042457649709675
    - type: nauc_mrr_at_5_max
      value: 42.03643705756859
    - type: nauc_mrr_at_5_std
      value: -4.958139821587032
    - type: nauc_ndcg_at_1000_diff1
      value: 45.81204094950804
    - type: nauc_ndcg_at_1000_max
      value: 42.73689566776186
    - type: nauc_ndcg_at_1000_std
      value: -0.7066382518858306
    - type: nauc_ndcg_at_100_diff1
      value: 45.28640379554905
    - type: nauc_ndcg_at_100_max
      value: 42.681083144594815
    - type: nauc_ndcg_at_100_std
      value: -0.09688585685774474
    - type: nauc_ndcg_at_10_diff1
      value: 45.71414379972128
    - type: nauc_ndcg_at_10_max
      value: 41.53626843173395
    - type: nauc_ndcg_at_10_std
      value: -1.8507612518474037
    - type: nauc_ndcg_at_1_diff1
      value: 48.15582854302911
    - type: nauc_ndcg_at_1_max
      value: 39.82659893618731
    - type: nauc_ndcg_at_1_std
      value: -8.183852381071691
    - type: nauc_ndcg_at_20_diff1
      value: 45.39833040860289
    - type: nauc_ndcg_at_20_max
      value: 41.55849686342755
    - type: nauc_ndcg_at_20_std
      value: -1.0215221134520232
    - type: nauc_ndcg_at_3_diff1
      value: 46.87312912585575
    - type: nauc_ndcg_at_3_max
      value: 41.057497209218255
    - type: nauc_ndcg_at_3_std
      value: -3.9052157576939535
    - type: nauc_ndcg_at_5_diff1
      value: 46.52903875914039
    - type: nauc_ndcg_at_5_max
      value: 41.793701014010786
    - type: nauc_ndcg_at_5_std
      value: -2.9870402822330866
    - type: nauc_precision_at_1000_diff1
      value: -19.737292446155067
    - type: nauc_precision_at_1000_max
      value: -10.181883018676627
    - type: nauc_precision_at_1000_std
      value: -3.068587468550703
    - type: nauc_precision_at_100_diff1
      value: -11.377068363169922
    - type: nauc_precision_at_100_max
      value: 6.3871026306788705
    - type: nauc_precision_at_100_std
      value: 8.872198838850938
    - type: nauc_precision_at_10_diff1
      value: 9.599810544198046
    - type: nauc_precision_at_10_max
      value: 26.62316097540815
    - type: nauc_precision_at_10_std
      value: 8.686741005293698
    - type: nauc_precision_at_1_diff1
      value: 48.15582854302911
    - type: nauc_precision_at_1_max
      value: 39.82659893618731
    - type: nauc_precision_at_1_std
      value: -8.183852381071691
    - type: nauc_precision_at_20_diff1
      value: 0.25496998553714123
    - type: nauc_precision_at_20_max
      value: 18.471523812532052
    - type: nauc_precision_at_20_std
      value: 10.351704374808387
    - type: nauc_precision_at_3_diff1
      value: 30.617775870803055
    - type: nauc_precision_at_3_max
      value: 38.01125065426583
    - type: nauc_precision_at_3_std
      value: -0.7623574434648546
    - type: nauc_precision_at_5_diff1
      value: 20.450147138491545
    - type: nauc_precision_at_5_max
      value: 33.18114326263472
    - type: nauc_precision_at_5_std
      value: 2.998578407482621
    - type: nauc_recall_at_1000_diff1
      value: 22.91280255517604
    - type: nauc_recall_at_1000_max
      value: 64.0102572612793
    - type: nauc_recall_at_1000_std
      value: 51.549096370979406
    - type: nauc_recall_at_100_diff1
      value: 28.635647358302503
    - type: nauc_recall_at_100_max
      value: 44.00473186289832
    - type: nauc_recall_at_100_std
      value: 19.912314783541138
    - type: nauc_recall_at_10_diff1
      value: 37.808472531928786
    - type: nauc_recall_at_10_max
      value: 38.67030494361658
    - type: nauc_recall_at_10_std
      value: 4.063425477456253
    - type: nauc_recall_at_1_diff1
      value: 51.708891898356256
    - type: nauc_recall_at_1_max
      value: 36.28682951162398
    - type: nauc_recall_at_1_std
      value: -7.4668723971868065
    - type: nauc_recall_at_20_diff1
      value: 34.51072533447235
    - type: nauc_recall_at_20_max
      value: 37.73082104160229
    - type: nauc_recall_at_20_std
      value: 8.219053762621884
    - type: nauc_recall_at_3_diff1
      value: 44.99432786987943
    - type: nauc_recall_at_3_max
      value: 39.55995143135335
    - type: nauc_recall_at_3_std
      value: -2.4914190692599165
    - type: nauc_recall_at_5_diff1
      value: 42.547651108851106
    - type: nauc_recall_at_5_max
      value: 40.85551908930608
    - type: nauc_recall_at_5_std
      value: 0.4962059846390094
    - type: ndcg_at_1
      value: 39.771
    - type: ndcg_at_10
      value: 49.34
    - type: ndcg_at_100
      value: 54.595000000000006
    - type: ndcg_at_1000
      value: 56.666000000000004
    - type: ndcg_at_20
      value: 51.492000000000004
    - type: ndcg_at_3
      value: 44.308
    - type: ndcg_at_5
      value: 46.838
    - type: precision_at_1
      value: 39.771
    - type: precision_at_10
      value: 9.442
    - type: precision_at_100
      value: 1.5010000000000001
    - type: precision_at_1000
      value: 0.2
    - type: precision_at_20
      value: 5.651
    - type: precision_at_3
      value: 21.125
    - type: precision_at_5
      value: 15.479000000000001
    - type: recall_at_1
      value: 31.978
    - type: recall_at_10
      value: 61.129
    - type: recall_at_100
      value: 83.052
    - type: recall_at_1000
      value: 96.378
    - type: recall_at_20
      value: 68.72500000000001
    - type: recall_at_3
      value: 46.518
    - type: recall_at_5
      value: 53.59
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval (default)
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: mteb/cqadupstack-english
    metrics:
    - type: main_score
      value: 45.286
    - type: map_at_1
      value: 30.169
    - type: map_at_10
      value: 39.711999999999996
    - type: map_at_100
      value: 40.898
    - type: map_at_1000
      value: 41.038999999999994
    - type: map_at_20
      value: 40.357
    - type: map_at_3
      value: 36.949
    - type: map_at_5
      value: 38.473
    - type: mrr_at_1
      value: 37.57961783439491
    - type: mrr_at_10
      value: 46.031847133757964
    - type: mrr_at_100
      value: 46.65912851493955
    - type: mrr_at_1000
      value: 46.707042666709604
    - type: mrr_at_20
      value: 46.40068681036863
    - type: mrr_at_3
      value: 43.7791932059448
    - type: mrr_at_5
      value: 45.10084925690022
    - type: nauc_map_at_1000_diff1
      value: 50.85056542222115
    - type: nauc_map_at_1000_max
      value: 31.05651616405919
    - type: nauc_map_at_1000_std
      value: -2.2368126065205987
    - type: nauc_map_at_100_diff1
      value: 50.89417988965435
    - type: nauc_map_at_100_max
      value: 30.997137971767142
    - type: nauc_map_at_100_std
      value: -2.3409324916593492
    - type: nauc_map_at_10_diff1
      value: 51.142437175292955
    - type: nauc_map_at_10_max
      value: 30.227559741209287
    - type: nauc_map_at_10_std
      value: -3.7930421273349264
    - type: nauc_map_at_1_diff1
      value: 55.941637622487214
    - type: nauc_map_at_1_max
      value: 25.080533324385613
    - type: nauc_map_at_1_std
      value: -8.864138917095795
    - type: nauc_map_at_20_diff1
      value: 50.96714330539312
    - type: nauc_map_at_20_max
      value: 30.56073364246607
    - type: nauc_map_at_20_std
      value: -3.1109111786530703
    - type: nauc_map_at_3_diff1
      value: 51.56324965582417
    - type: nauc_map_at_3_max
      value: 28.83764240000901
    - type: nauc_map_at_3_std
      value: -5.496574943583724
    - type: nauc_map_at_5_diff1
      value: 51.2643900871776
    - type: nauc_map_at_5_max
      value: 29.42492887150313
    - type: nauc_map_at_5_std
      value: -4.7906573624880675
    - type: nauc_mrr_at_1000_diff1
      value: 49.81188202883573
    - type: nauc_mrr_at_1000_max
      value: 32.758906990991626
    - type: nauc_mrr_at_1000_std
      value: 1.5051321484514517
    - type: nauc_mrr_at_100_diff1
      value: 49.808094282032876
    - type: nauc_mrr_at_100_max
      value: 32.75870267430557
    - type: nauc_mrr_at_100_std
      value: 1.5117004894545576
    - type: nauc_mrr_at_10_diff1
      value: 49.86964428608597
    - type: nauc_mrr_at_10_max
      value: 32.75447791816241
    - type: nauc_mrr_at_10_std
      value: 1.0472130007711005
    - type: nauc_mrr_at_1_diff1
      value: 54.63093984058127
    - type: nauc_mrr_at_1_max
      value: 31.486608661031973
    - type: nauc_mrr_at_1_std
      value: -1.3741363436543739
    - type: nauc_mrr_at_20_diff1
      value: 49.790685542152005
    - type: nauc_mrr_at_20_max
      value: 32.75477912841072
    - type: nauc_mrr_at_20_std
      value: 1.338641256922409
    - type: nauc_mrr_at_3_diff1
      value: 50.17281274015403
    - type: nauc_mrr_at_3_max
      value: 32.55859057277966
    - type: nauc_mrr_at_3_std
      value: 0.6635403402684905
    - type: nauc_mrr_at_5_diff1
      value: 49.99493486356793
    - type: nauc_mrr_at_5_max
      value: 32.61428342888774
    - type: nauc_mrr_at_5_std
      value: 0.7430591391457354
    - type: nauc_ndcg_at_1000_diff1
      value: 48.22576941926604
    - type: nauc_ndcg_at_1000_max
      value: 32.93511771089829
    - type: nauc_ndcg_at_1000_std
      value: 3.129856319572661
    - type: nauc_ndcg_at_100_diff1
      value: 48.62921110376326
    - type: nauc_ndcg_at_100_max
      value: 32.991588269891764
    - type: nauc_ndcg_at_100_std
      value: 3.0722970856766
    - type: nauc_ndcg_at_10_diff1
      value: 49.18605872592804
    - type: nauc_ndcg_at_10_max
      value: 32.24106173386995
    - type: nauc_ndcg_at_10_std
      value: -0.2906781273981978
    - type: nauc_ndcg_at_1_diff1
      value: 54.63093984058127
    - type: nauc_ndcg_at_1_max
      value: 31.486608661031973
    - type: nauc_ndcg_at_1_std
      value: -1.3741363436543739
    - type: nauc_ndcg_at_20_diff1
      value: 48.67444292759105
    - type: nauc_ndcg_at_20_max
      value: 32.38356642801882
    - type: nauc_ndcg_at_20_std
      value: 1.0417910616522417
    - type: nauc_ndcg_at_3_diff1
      value: 49.64405616341687
    - type: nauc_ndcg_at_3_max
      value: 31.851912727510662
    - type: nauc_ndcg_at_3_std
      value: -1.3378234982644532
    - type: nauc_ndcg_at_5_diff1
      value: 49.41698121410308
    - type: nauc_ndcg_at_5_max
      value: 31.796598394828706
    - type: nauc_ndcg_at_5_std
      value: -1.356552455719212
    - type: nauc_precision_at_1000_diff1
      value: -16.185681544062707
    - type: nauc_precision_at_1000_max
      value: 15.06181269349989
    - type: nauc_precision_at_1000_std
      value: 29.16661769411087
    - type: nauc_precision_at_100_diff1
      value: -4.50092289449142
    - type: nauc_precision_at_100_max
      value: 26.889499343262663
    - type: nauc_precision_at_100_std
      value: 34.61625224772955
    - type: nauc_precision_at_10_diff1
      value: 16.845250924167054
    - type: nauc_precision_at_10_max
      value: 33.18165476286763
    - type: nauc_precision_at_10_std
      value: 20.01633509478702
    - type: nauc_precision_at_1_diff1
      value: 54.63093984058127
    - type: nauc_precision_at_1_max
      value: 31.486608661031973
    - type: nauc_precision_at_1_std
      value: -1.3741363436543739
    - type: nauc_precision_at_20_diff1
      value: 7.904987701430007
    - type: nauc_precision_at_20_max
      value: 31.66538848828912
    - type: nauc_precision_at_20_std
      value: 27.373203146189333
    - type: nauc_precision_at_3_diff1
      value: 32.98074210677402
    - type: nauc_precision_at_3_max
      value: 35.70551590699247
    - type: nauc_precision_at_3_std
      value: 9.64957518804935
    - type: nauc_precision_at_5_diff1
      value: 25.68789006898062
    - type: nauc_precision_at_5_max
      value: 34.528632431840606
    - type: nauc_precision_at_5_std
      value: 13.758348844848392
    - type: nauc_recall_at_1000_diff1
      value: 27.292499993748585
    - type: nauc_recall_at_1000_max
      value: 33.50856923877545
    - type: nauc_recall_at_1000_std
      value: 32.219345025751586
    - type: nauc_recall_at_100_diff1
      value: 37.33505162034011
    - type: nauc_recall_at_100_max
      value: 33.97748076845698
    - type: nauc_recall_at_100_std
      value: 21.716723075947385
    - type: nauc_recall_at_10_diff1
      value: 42.67650896437499
    - type: nauc_recall_at_10_max
      value: 30.930396085103517
    - type: nauc_recall_at_10_std
      value: 2.5045964341943163
    - type: nauc_recall_at_1_diff1
      value: 55.941637622487214
    - type: nauc_recall_at_1_max
      value: 25.080533324385613
    - type: nauc_recall_at_1_std
      value: -8.864138917095795
    - type: nauc_recall_at_20_diff1
      value: 39.97433575808996
    - type: nauc_recall_at_20_max
      value: 31.44609230387655
    - type: nauc_recall_at_20_std
      value: 7.736221159385454
    - type: nauc_recall_at_3_diff1
      value: 46.21571868804605
    - type: nauc_recall_at_3_max
      value: 28.893654020460204
    - type: nauc_recall_at_3_std
      value: -3.6376291909998493
    - type: nauc_recall_at_5_diff1
      value: 44.64111423499069
    - type: nauc_recall_at_5_max
      value: 29.065352256728865
    - type: nauc_recall_at_5_std
      value: -2.0155177145574905
    - type: ndcg_at_1
      value: 37.580000000000005
    - type: ndcg_at_10
      value: 45.286
    - type: ndcg_at_100
      value: 49.518
    - type: ndcg_at_1000
      value: 51.778999999999996
    - type: ndcg_at_20
      value: 46.921
    - type: ndcg_at_3
      value: 41.237
    - type: ndcg_at_5
      value: 43.085
    - type: precision_at_1
      value: 37.580000000000005
    - type: precision_at_10
      value: 8.452
    - type: precision_at_100
      value: 1.358
    - type: precision_at_1000
      value: 0.186
    - type: precision_at_20
      value: 4.987
    - type: precision_at_3
      value: 19.66
    - type: precision_at_5
      value: 13.936000000000002
    - type: recall_at_1
      value: 30.169
    - type: recall_at_10
      value: 54.657999999999994
    - type: recall_at_100
      value: 72.631
    - type: recall_at_1000
      value: 86.99799999999999
    - type: recall_at_20
      value: 60.549
    - type: recall_at_3
      value: 42.703
    - type: recall_at_5
      value: 47.871
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval (default)
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: mteb/cqadupstack-gaming
    metrics:
    - type: main_score
      value: 57.935
    - type: map_at_1
      value: 39.459
    - type: map_at_10
      value: 52.041000000000004
    - type: map_at_100
      value: 53.123
    - type: map_at_1000
      value: 53.174
    - type: map_at_20
      value: 52.715999999999994
    - type: map_at_3
      value: 48.652
    - type: map_at_5
      value: 50.526
    - type: mrr_at_1
      value: 45.141065830721004
    - type: mrr_at_10
      value: 55.4189680051749
    - type: mrr_at_100
      value: 56.12734090607992
    - type: mrr_at_1000
      value: 56.15035665102205
    - type: mrr_at_20
      value: 55.870980474719914
    - type: mrr_at_3
      value: 52.92580982236154
    - type: mrr_at_5
      value: 54.380355276907
    - type: nauc_map_at_1000_diff1
      value: 49.350343037507805
    - type: nauc_map_at_1000_max
      value: 39.98281162376331
    - type: nauc_map_at_1000_std
      value: -3.6565717425989255
    - type: nauc_map_at_100_diff1
      value: 49.342545452256
    - type: nauc_map_at_100_max
      value: 39.98916109913233
    - type: nauc_map_at_100_std
      value: -3.643010722158061
    - type: nauc_map_at_10_diff1
      value: 49.45960781144599
    - type: nauc_map_at_10_max
      value: 39.68189953288183
    - type: nauc_map_at_10_std
      value: -4.405767261039445
    - type: nauc_map_at_1_diff1
      value: 52.089101330688045
    - type: nauc_map_at_1_max
      value: 33.85881212484232
    - type: nauc_map_at_1_std
      value: -8.418190685614235
    - type: nauc_map_at_20_diff1
      value: 49.32978868149478
    - type: nauc_map_at_20_max
      value: 39.75645643846
    - type: nauc_map_at_20_std
      value: -3.9860531109091193
    - type: nauc_map_at_3_diff1
      value: 50.04151871930599
    - type: nauc_map_at_3_max
      value: 37.79961474082032
    - type: nauc_map_at_3_std
      value: -6.670028333711345
    - type: nauc_map_at_5_diff1
      value: 49.71975459031514
    - type: nauc_map_at_5_max
      value: 38.817567597269466
    - type: nauc_map_at_5_std
      value: -5.434776325022176
    - type: nauc_mrr_at_1000_diff1
      value: 48.947499409111096
    - type: nauc_mrr_at_1000_max
      value: 40.93741059921989
    - type: nauc_mrr_at_1000_std
      value: -3.1825006442699553
    - type: nauc_mrr_at_100_diff1
      value: 48.942343488274815
    - type: nauc_mrr_at_100_max
      value: 40.95031134407549
    - type: nauc_mrr_at_100_std
      value: -3.160377489400296
    - type: nauc_mrr_at_10_diff1
      value: 48.840125595383455
    - type: nauc_mrr_at_10_max
      value: 41.02170174858195
    - type: nauc_mrr_at_10_std
      value: -3.197031134091893
    - type: nauc_mrr_at_1_diff1
      value: 52.064927865645075
    - type: nauc_mrr_at_1_max
      value: 38.44984483881011
    - type: nauc_mrr_at_1_std
      value: -6.416298888465512
    - type: nauc_mrr_at_20_diff1
      value: 48.906114080185866
    - type: nauc_mrr_at_20_max
      value: 40.87883825337818
    - type: nauc_mrr_at_20_std
      value: -3.255032101669121
    - type: nauc_mrr_at_3_diff1
      value: 49.32815249648534
    - type: nauc_mrr_at_3_max
      value: 40.432904378326384
    - type: nauc_mrr_at_3_std
      value: -4.370615209045244
    - type: nauc_mrr_at_5_diff1
      value: 48.83993033552693
    - type: nauc_mrr_at_5_max
      value: 40.71824702891057
    - type: nauc_mrr_at_5_std
      value: -3.655659400980567
    - type: nauc_ndcg_at_1000_diff1
      value: 48.474352967441945
    - type: nauc_ndcg_at_1000_max
      value: 41.96481325646208
    - type: nauc_ndcg_at_1000_std
      value: -0.6346960977825105
    - type: nauc_ndcg_at_100_diff1
      value: 48.3009196475395
    - type: nauc_ndcg_at_100_max
      value: 42.349365306663664
    - type: nauc_ndcg_at_100_std
      value: 0.16696421606061568
    - type: nauc_ndcg_at_10_diff1
      value: 48.22259923512447
    - type: nauc_ndcg_at_10_max
      value: 41.81263561142292
    - type: nauc_ndcg_at_10_std
      value: -1.6113767450068854
    - type: nauc_ndcg_at_1_diff1
      value: 52.064927865645075
    - type: nauc_ndcg_at_1_max
      value: 38.44984483881011
    - type: nauc_ndcg_at_1_std
      value: -6.416298888465512
    - type: nauc_ndcg_at_20_diff1
      value: 48.07530674920143
    - type: nauc_ndcg_at_20_max
      value: 41.481398876880355
    - type: nauc_ndcg_at_20_std
      value: -1.1959186932073145
    - type: nauc_ndcg_at_3_diff1
      value: 48.97047357315626
    - type: nauc_ndcg_at_3_max
      value: 39.3764554710483
    - type: nauc_ndcg_at_3_std
      value: -4.737405650853368
    - type: nauc_ndcg_at_5_diff1
      value: 48.465073616087444
    - type: nauc_ndcg_at_5_max
      value: 40.48611129423828
    - type: nauc_ndcg_at_5_std
      value: -3.2733514958040946
    - type: nauc_precision_at_1000_diff1
      value: -9.539304087056678
    - type: nauc_precision_at_1000_max
      value: 15.041788011496934
    - type: nauc_precision_at_1000_std
      value: 22.84867087898786
    - type: nauc_precision_at_100_diff1
      value: -5.179075253413082
    - type: nauc_precision_at_100_max
      value: 22.968148583194907
    - type: nauc_precision_at_100_std
      value: 28.16118112550293
    - type: nauc_precision_at_10_diff1
      value: 12.68864903314593
    - type: nauc_precision_at_10_max
      value: 33.402306007402416
    - type: nauc_precision_at_10_std
      value: 15.954788657247748
    - type: nauc_precision_at_1_diff1
      value: 52.064927865645075
    - type: nauc_precision_at_1_max
      value: 38.44984483881011
    - type: nauc_precision_at_1_std
      value: -6.416298888465512
    - type: nauc_precision_at_20_diff1
      value: 4.086070276980883
    - type: nauc_precision_at_20_max
      value: 28.466186216262646
    - type: nauc_precision_at_20_std
      value: 21.548953975789946
    - type: nauc_precision_at_3_diff1
      value: 31.827793894919836
    - type: nauc_precision_at_3_max
      value: 38.13215690903121
    - type: nauc_precision_at_3_std
      value: 2.3490498723729787
    - type: nauc_precision_at_5_diff1
      value: 23.36248316835303
    - type: nauc_precision_at_5_max
      value: 36.6085689865106
    - type: nauc_precision_at_5_std
      value: 8.730583249465882
    - type: nauc_recall_at_1000_diff1
      value: 35.58748183758336
    - type: nauc_recall_at_1000_max
      value: 63.481971018253866
    - type: nauc_recall_at_1000_std
      value: 50.255552349121324
    - type: nauc_recall_at_100_diff1
      value: 38.30162180279426
    - type: nauc_recall_at_100_max
      value: 55.32704556841503
    - type: nauc_recall_at_100_std
      value: 33.05803540444057
    - type: nauc_recall_at_10_diff1
      value: 42.88255606095961
    - type: nauc_recall_at_10_max
      value: 45.08979716365479
    - type: nauc_recall_at_10_std
      value: 6.080592095781171
    - type: nauc_recall_at_1_diff1
      value: 52.089101330688045
    - type: nauc_recall_at_1_max
      value: 33.85881212484232
    - type: nauc_recall_at_1_std
      value: -8.418190685614235
    - type: nauc_recall_at_20_diff1
      value: 40.717620176248104
    - type: nauc_recall_at_20_max
      value: 43.889494702908635
    - type: nauc_recall_at_20_std
      value: 9.674760090258394
    - type: nauc_recall_at_3_diff1
      value: 46.97768558746882
    - type: nauc_recall_at_3_max
      value: 38.285091697616465
    - type: nauc_recall_at_3_std
      value: -4.852209401420014
    - type: nauc_recall_at_5_diff1
      value: 44.54361378218751
    - type: nauc_recall_at_5_max
      value: 40.49656738354392
    - type: nauc_recall_at_5_std
      value: -0.39210246739263926
    - type: ndcg_at_1
      value: 45.141
    - type: ndcg_at_10
      value: 57.935
    - type: ndcg_at_100
      value: 62.121
    - type: ndcg_at_1000
      value: 63.086
    - type: ndcg_at_20
      value: 59.907999999999994
    - type: ndcg_at_3
      value: 52.358000000000004
    - type: ndcg_at_5
      value: 55.027
    - type: precision_at_1
      value: 45.141
    - type: precision_at_10
      value: 9.347999999999999
    - type: precision_at_100
      value: 1.232
    - type: precision_at_1000
      value: 0.136
    - type: precision_at_20
      value: 5.251
    - type: precision_at_3
      value: 23.344
    - type: precision_at_5
      value: 16.05
    - type: recall_at_1
      value: 39.459
    - type: recall_at_10
      value: 71.968
    - type: recall_at_100
      value: 89.81
    - type: recall_at_1000
      value: 96.55
    - type: recall_at_20
      value: 79.33099999999999
    - type: recall_at_3
      value: 57.099999999999994
    - type: recall_at_5
      value: 63.637
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval (default)
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: mteb/cqadupstack-gis
    metrics:
    - type: main_score
      value: 39.839999999999996
    - type: map_at_1
      value: 26.821
    - type: map_at_10
      value: 34.993
    - type: map_at_100
      value: 36.009
    - type: map_at_1000
      value: 36.083
    - type: map_at_20
      value: 35.554
    - type: map_at_3
      value: 32.228
    - type: map_at_5
      value: 33.904
    - type: mrr_at_1
      value: 28.926553672316384
    - type: mrr_at_10
      value: 36.986368935521476
    - type: mrr_at_100
      value: 37.895698883680886
    - type: mrr_at_1000
      value: 37.95031449676498
    - type: mrr_at_20
      value: 37.48535917350526
    - type: mrr_at_3
      value: 34.293785310734464
    - type: mrr_at_5
      value: 35.983050847457626
    - type: nauc_map_at_1000_diff1
      value: 43.31690408477667
    - type: nauc_map_at_1000_max
      value: 30.862014860762795
    - type: nauc_map_at_1000_std
      value: -0.8551391908390162
    - type: nauc_map_at_100_diff1
      value: 43.312902470408524
    - type: nauc_map_at_100_max
      value: 30.862986571062383
    - type: nauc_map_at_100_std
      value: -0.8637722733314122
    - type: nauc_map_at_10_diff1
      value: 43.385672679389984
    - type: nauc_map_at_10_max
      value: 30.714784436737087
    - type: nauc_map_at_10_std
      value: -1.2522744939678505
    - type: nauc_map_at_1_diff1
      value: 47.86681025046955
    - type: nauc_map_at_1_max
      value: 29.132194162422586
    - type: nauc_map_at_1_std
      value: -5.002201483950293
    - type: nauc_map_at_20_diff1
      value: 43.37717003110337
    - type: nauc_map_at_20_max
      value: 30.78438235738698
    - type: nauc_map_at_20_std
      value: -0.8953950024164806
    - type: nauc_map_at_3_diff1
      value: 44.38299520601522
    - type: nauc_map_at_3_max
      value: 29.83366218086086
    - type: nauc_map_at_3_std
      value: -2.5693730585913297
    - type: nauc_map_at_5_diff1
      value: 43.51921405125155
    - type: nauc_map_at_5_max
      value: 30.22504627106614
    - type: nauc_map_at_5_std
      value: -1.5972020248683592
    - type: nauc_mrr_at_1000_diff1
      value: 42.49108453787739
    - type: nauc_mrr_at_1000_max
      value: 31.972602761246655
    - type: nauc_mrr_at_1000_std
      value: 1.0231286981944512
    - type: nauc_mrr_at_100_diff1
      value: 42.479172722773896
    - type: nauc_mrr_at_100_max
      value: 31.987222969415342
    - type: nauc_mrr_at_100_std
      value: 1.0274146182701183
    - type: nauc_mrr_at_10_diff1
      value: 42.526290626365196
    - type: nauc_mrr_at_10_max
      value: 32.01830237899739
    - type: nauc_mrr_at_10_std
      value: 0.9161077778836639
    - type: nauc_mrr_at_1_diff1
      value: 46.621348392565736
    - type: nauc_mrr_at_1_max
      value: 31.470289340095604
    - type: nauc_mrr_at_1_std
      value: -2.4591738933621867
    - type: nauc_mrr_at_20_diff1
      value: 42.534853876861575
    - type: nauc_mrr_at_20_max
      value: 31.996618075721905
    - type: nauc_mrr_at_20_std
      value: 1.1174044583485392
    - type: nauc_mrr_at_3_diff1
      value: 43.24815151493605
    - type: nauc_mrr_at_3_max
      value: 31.282640177477422
    - type: nauc_mrr_at_3_std
      value: -0.2891247404070639
    - type: nauc_mrr_at_5_diff1
      value: 42.730970720344594
    - type: nauc_mrr_at_5_max
      value: 31.60546178005326
    - type: nauc_mrr_at_5_std
      value: 0.5275202736677842
    - type: nauc_ndcg_at_1000_diff1
      value: 41.11037892060558
    - type: nauc_ndcg_at_1000_max
      value: 31.981322365939096
    - type: nauc_ndcg_at_1000_std
      value: 2.5104274168043115
    - type: nauc_ndcg_at_100_diff1
      value: 40.72420815298269
    - type: nauc_ndcg_at_100_max
      value: 32.12478900255941
    - type: nauc_ndcg_at_100_std
      value: 2.823745879247313
    - type: nauc_ndcg_at_10_diff1
      value: 41.248176699595774
    - type: nauc_ndcg_at_10_max
      value: 31.76223462957885
    - type: nauc_ndcg_at_10_std
      value: 1.325254903938574
    - type: nauc_ndcg_at_1_diff1
      value: 46.621348392565736
    - type: nauc_ndcg_at_1_max
      value: 31.470289340095604
    - type: nauc_ndcg_at_1_std
      value: -2.4591738933621867
    - type: nauc_ndcg_at_20_diff1
      value: 41.2264296695926
    - type: nauc_ndcg_at_20_max
      value: 31.880018569087127
    - type: nauc_ndcg_at_20_std
      value: 2.5771307591404953
    - type: nauc_ndcg_at_3_diff1
      value: 43.14220610066874
    - type: nauc_ndcg_at_3_max
      value: 30.506711094581906
    - type: nauc_ndcg_at_3_std
      value: -1.32756254984396
    - type: nauc_ndcg_at_5_diff1
      value: 41.766023996364815
    - type: nauc_ndcg_at_5_max
      value: 30.89844409312977
    - type: nauc_ndcg_at_5_std
      value: 0.3788803778583815
    - type: nauc_precision_at_1000_diff1
      value: -1.6666285719678695
    - type: nauc_precision_at_1000_max
      value: 16.874851634956954
    - type: nauc_precision_at_1000_std
      value: 13.467634314792958
    - type: nauc_precision_at_100_diff1
      value: 12.127904836990574
    - type: nauc_precision_at_100_max
      value: 29.832469022456742
    - type: nauc_precision_at_100_std
      value: 17.83171142960893
    - type: nauc_precision_at_10_diff1
      value: 28.629632098778924
    - type: nauc_precision_at_10_max
      value: 36.382552111288504
    - type: nauc_precision_at_10_std
      value: 10.527329328113375
    - type: nauc_precision_at_1_diff1
      value: 46.621348392565736
    - type: nauc_precision_at_1_max
      value: 31.470289340095604
    - type: nauc_precision_at_1_std
      value: -2.4591738933621867
    - type: nauc_precision_at_20_diff1
      value: 26.30904506190692
    - type: nauc_precision_at_20_max
      value: 35.806707688621934
    - type: nauc_precision_at_20_std
      value: 15.568878952628618
    - type: nauc_precision_at_3_diff1
      value: 37.18723505833023
    - type: nauc_precision_at_3_max
      value: 33.61785834920449
    - type: nauc_precision_at_3_std
      value: 2.9164041375719263
    - type: nauc_precision_at_5_diff1
      value: 32.815958974052634
    - type: nauc_precision_at_5_max
      value: 34.22763811245109
    - type: nauc_precision_at_5_std
      value: 6.903458965358602
    - type: nauc_recall_at_1000_diff1
      value: 19.113079964836775
    - type: nauc_recall_at_1000_max
      value: 34.179678630291214
    - type: nauc_recall_at_1000_std
      value: 32.767248399630766
    - type: nauc_recall_at_100_diff1
      value: 25.8811372897862
    - type: nauc_recall_at_100_max
      value: 34.080364921744646
    - type: nauc_recall_at_100_std
      value: 19.89467893613937
    - type: nauc_recall_at_10_diff1
      value: 33.89551559779046
    - type: nauc_recall_at_10_max
      value: 32.010002950841205
    - type: nauc_recall_at_10_std
      value: 6.940984864057547
    - type: nauc_recall_at_1_diff1
      value: 47.86681025046955
    - type: nauc_recall_at_1_max
      value: 29.132194162422586
    - type: nauc_recall_at_1_std
      value: -5.002201483950293
    - type: nauc_recall_at_20_diff1
      value: 33.23701340255753
    - type: nauc_recall_at_20_max
      value: 32.4122108288123
    - type: nauc_recall_at_20_std
      value: 12.716938752356722
    - type: nauc_recall_at_3_diff1
      value: 40.13928334370612
    - type: nauc_recall_at_3_max
      value: 29.763781596658056
    - type: nauc_recall_at_3_std
      value: 0.34341106017726875
    - type: nauc_recall_at_5_diff1
      value: 36.11418609771827
    - type: nauc_recall_at_5_max
      value: 30.444939213226345
    - type: nauc_recall_at_5_std
      value: 4.2497080620670244
    - type: ndcg_at_1
      value: 28.927000000000003
    - type: ndcg_at_10
      value: 39.839999999999996
    - type: ndcg_at_100
      value: 45.044000000000004
    - type: ndcg_at_1000
      value: 46.937
    - type: ndcg_at_20
      value: 41.821999999999996
    - type: ndcg_at_3
      value: 34.455000000000005
    - type: ndcg_at_5
      value: 37.37
    - type: precision_at_1
      value: 28.927000000000003
    - type: precision_at_10
      value: 6.045
    - type: precision_at_100
      value: 0.914
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_20
      value: 3.4799999999999995
    - type: precision_at_3
      value: 14.313
    - type: precision_at_5
      value: 10.26
    - type: recall_at_1
      value: 26.821
    - type: recall_at_10
      value: 52.917
    - type: recall_at_100
      value: 77.093
    - type: recall_at_1000
      value: 91.316
    - type: recall_at_20
      value: 60.56700000000001
    - type: recall_at_3
      value: 38.51
    - type: recall_at_5
      value: 45.536
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval (default)
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: mteb/cqadupstack-mathematica
    metrics:
    - type: main_score
      value: 29.98
    - type: map_at_1
      value: 16.006999999999998
    - type: map_at_10
      value: 24.477
    - type: map_at_100
      value: 25.668000000000003
    - type: map_at_1000
      value: 25.788
    - type: map_at_20
      value: 25.048
    - type: map_at_3
      value: 21.656
    - type: map_at_5
      value: 23.34
    - type: mrr_at_1
      value: 20.024875621890548
    - type: mrr_at_10
      value: 29.197020848140255
    - type: mrr_at_100
      value: 30.11227723049729
    - type: mrr_at_1000
      value: 30.18189915906596
    - type: mrr_at_20
      value: 29.656175097568173
    - type: mrr_at_3
      value: 26.409618573797676
    - type: mrr_at_5
      value: 28.094941956882252
    - type: nauc_map_at_1000_diff1
      value: 29.373123176645237
    - type: nauc_map_at_1000_max
      value: 21.445648024191712
    - type: nauc_map_at_1000_std
      value: 4.405281916537104
    - type: nauc_map_at_100_diff1
      value: 29.35310092597499
    - type: nauc_map_at_100_max
      value: 21.40489526072531
    - type: nauc_map_at_100_std
      value: 4.380387058523312
    - type: nauc_map_at_10_diff1
      value: 29.141697351596253
    - type: nauc_map_at_10_max
      value: 21.03434833947413
    - type: nauc_map_at_10_std
      value: 4.144922514001805
    - type: nauc_map_at_1_diff1
      value: 38.13496031071367
    - type: nauc_map_at_1_max
      value: 21.901814324794117
    - type: nauc_map_at_1_std
      value: 0.4814120186616989
    - type: nauc_map_at_20_diff1
      value: 29.32299833637584
    - type: nauc_map_at_20_max
      value: 21.306214454816754
    - type: nauc_map_at_20_std
      value: 4.300356249155504
    - type: nauc_map_at_3_diff1
      value: 29.06177418598614
    - type: nauc_map_at_3_max
      value: 20.811300750566513
    - type: nauc_map_at_3_std
      value: 3.4414335533909166
    - type: nauc_map_at_5_diff1
      value: 29.338077175083153
    - type: nauc_map_at_5_max
      value: 20.905802602838854
    - type: nauc_map_at_5_std
      value: 3.718624565651613
    - type: nauc_mrr_at_1000_diff1
      value: 30.008651430755055
    - type: nauc_mrr_at_1000_max
      value: 22.107612668457936
    - type: nauc_mrr_at_1000_std
      value: 2.722385123849279
    - type: nauc_mrr_at_100_diff1
      value: 29.99004753126145
    - type: nauc_mrr_at_100_max
      value: 22.094848691097166
    - type: nauc_mrr_at_100_std
      value: 2.732788863788039
    - type: nauc_mrr_at_10_diff1
      value: 29.88442282413889
    - type: nauc_mrr_at_10_max
      value: 22.02646483854745
    - type: nauc_mrr_at_10_std
      value: 2.6648957296233644
    - type: nauc_mrr_at_1_diff1
      value: 37.967956104647755
    - type: nauc_mrr_at_1_max
      value: 21.44460113476502
    - type: nauc_mrr_at_1_std
      value: -1.7530679840582375
    - type: nauc_mrr_at_20_diff1
      value: 29.927851260160853
    - type: nauc_mrr_at_20_max
      value: 22.01880502582662
    - type: nauc_mrr_at_20_std
      value: 2.708224642328409
    - type: nauc_mrr_at_3_diff1
      value: 30.266105364910807
    - type: nauc_mrr_at_3_max
      value: 21.89072561010228
    - type: nauc_mrr_at_3_std
      value: 2.1435490321496875
    - type: nauc_mrr_at_5_diff1
      value: 30.15575881656933
    - type: nauc_mrr_at_5_max
      value: 22.16515882306906
    - type: nauc_mrr_at_5_std
      value: 2.577739748796098
    - type: nauc_ndcg_at_1000_diff1
      value: 27.90510789867005
    - type: nauc_ndcg_at_1000_max
      value: 22.530968354985028
    - type: nauc_ndcg_at_1000_std
      value: 6.781805354595171
    - type: nauc_ndcg_at_100_diff1
      value: 27.380292435540532
    - type: nauc_ndcg_at_100_max
      value: 21.809545194883373
    - type: nauc_ndcg_at_100_std
      value: 6.466454400897538
    - type: nauc_ndcg_at_10_diff1
      value: 26.787786754146648
    - type: nauc_ndcg_at_10_max
      value: 21.1259284562756
    - type: nauc_ndcg_at_10_std
      value: 5.5137140693199065
    - type: nauc_ndcg_at_1_diff1
      value: 37.967956104647755
    - type: nauc_ndcg_at_1_max
      value: 21.44460113476502
    - type: nauc_ndcg_at_1_std
      value: -1.7530679840582375
    - type: nauc_ndcg_at_20_diff1
      value: 27.263083511878065
    - type: nauc_ndcg_at_20_max
      value: 21.679228236914504
    - type: nauc_ndcg_at_20_std
      value: 6.089674507905745
    - type: nauc_ndcg_at_3_diff1
      value: 27.146357683499524
    - type: nauc_ndcg_at_3_max
      value: 21.104681584239923
    - type: nauc_ndcg_at_3_std
      value: 3.7675309462600217
    - type: nauc_ndcg_at_5_diff1
      value: 27.331511358161997
    - type: nauc_ndcg_at_5_max
      value: 21.18337870362178
    - type: nauc_ndcg_at_5_std
      value: 4.57529049323361
    - type: nauc_precision_at_1000_diff1
      value: 3.239653820602742
    - type: nauc_precision_at_1000_max
      value: 7.26961590562058
    - type: nauc_precision_at_1000_std
      value: 2.2025825300071125
    - type: nauc_precision_at_100_diff1
      value: 10.44430363394719
    - type: nauc_precision_at_100_max
      value: 14.264783558128372
    - type: nauc_precision_at_100_std
      value: 7.062602811028171
    - type: nauc_precision_at_10_diff1
      value: 18.25356714400902
    - type: nauc_precision_at_10_max
      value: 19.640874340636955
    - type: nauc_precision_at_10_std
      value: 7.720476038645774
    - type: nauc_precision_at_1_diff1
      value: 37.967956104647755
    - type: nauc_precision_at_1_max
      value: 21.44460113476502
    - type: nauc_precision_at_1_std
      value: -1.7530679840582375
    - type: nauc_precision_at_20_diff1
      value: 18.054556815828192
    - type: nauc_precision_at_20_max
      value: 20.132496075135354
    - type: nauc_precision_at_20_std
      value: 8.992246975170467
    - type: nauc_precision_at_3_diff1
      value: 20.99569005515048
    - type: nauc_precision_at_3_max
      value: 20.986073606132656
    - type: nauc_precision_at_3_std
      value: 4.447517886269654
    - type: nauc_precision_at_5_diff1
      value: 20.501261498730983
    - type: nauc_precision_at_5_max
      value: 20.506697758500973
    - type: nauc_precision_at_5_std
      value: 6.836691174582398
    - type: nauc_recall_at_1000_diff1
      value: 17.117021891023526
    - type: nauc_recall_at_1000_max
      value: 28.098336442218425
    - type: nauc_recall_at_1000_std
      value: 32.03347662796732
    - type: nauc_recall_at_100_diff1
      value: 17.981711126081034
    - type: nauc_recall_at_100_max
      value: 18.60340216104814
    - type: nauc_recall_at_100_std
      value: 14.313017781949211
    - type: nauc_recall_at_10_diff1
      value: 18.464197753039507
    - type: nauc_recall_at_10_max
      value: 18.474261038624018
    - type: nauc_recall_at_10_std
      value: 9.090322373993915
    - type: nauc_recall_at_1_diff1
      value: 38.13496031071367
    - type: nauc_recall_at_1_max
      value: 21.901814324794117
    - type: nauc_recall_at_1_std
      value: 0.4814120186616989
    - type: nauc_recall_at_20_diff1
      value: 19.45317881386327
    - type: nauc_recall_at_20_max
      value: 19.791890415922335
    - type: nauc_recall_at_20_std
      value: 11.195653035396559
    - type: nauc_recall_at_3_diff1
      value: 19.58052222735834
    - type: nauc_recall_at_3_max
      value: 18.390514209031757
    - type: nauc_recall_at_3_std
      value: 6.285979231354349
    - type: nauc_recall_at_5_diff1
      value: 19.957569014017217
    - type: nauc_recall_at_5_max
      value: 18.605256807993243
    - type: nauc_recall_at_5_std
      value: 6.7220712737663755
    - type: ndcg_at_1
      value: 20.025000000000002
    - type: ndcg_at_10
      value: 29.98
    - type: ndcg_at_100
      value: 35.69
    - type: ndcg_at_1000
      value: 38.568000000000005
    - type: ndcg_at_20
      value: 31.820999999999998
    - type: ndcg_at_3
      value: 24.891
    - type: ndcg_at_5
      value: 27.46
    - type: precision_at_1
      value: 20.025000000000002
    - type: precision_at_10
      value: 5.759
    - type: precision_at_100
      value: 0.984
    - type: precision_at_1000
      value: 0.136
    - type: precision_at_20
      value: 3.3640000000000003
    - type: precision_at_3
      value: 12.106
    - type: precision_at_5
      value: 9.179
    - type: recall_at_1
      value: 16.006999999999998
    - type: recall_at_10
      value: 42.081
    - type: recall_at_100
      value: 67.305
    - type: recall_at_1000
      value: 87.957
    - type: recall_at_20
      value: 48.704
    - type: recall_at_3
      value: 28.354000000000003
    - type: recall_at_5
      value: 34.605000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval (default)
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: mteb/cqadupstack-physics
    metrics:
    - type: main_score
      value: 45.073
    - type: map_at_1
      value: 28.136
    - type: map_at_10
      value: 38.868
    - type: map_at_100
      value: 40.108
    - type: map_at_1000
      value: 40.221000000000004
    - type: map_at_20
      value: 39.564
    - type: map_at_3
      value: 35.449000000000005
    - type: map_at_5
      value: 37.385000000000005
    - type: mrr_at_1
      value: 34.93743984600577
    - type: mrr_at_10
      value: 44.622385688314466
    - type: mrr_at_100
      value: 45.34143739001397
    - type: mrr_at_1000
      value: 45.39414063155817
    - type: mrr_at_20
      value: 45.00770434975747
    - type: mrr_at_3
      value: 41.88322104587745
    - type: mrr_at_5
      value: 43.50016041065127
    - type: nauc_map_at_1000_diff1
      value: 52.26823337938297
    - type: nauc_map_at_1000_max
      value: 37.37245329468808
    - type: nauc_map_at_1000_std
      value: 4.72166664574236
    - type: nauc_map_at_100_diff1
      value: 52.24616463751152
    - type: nauc_map_at_100_max
      value: 37.33426712740629
    - type: nauc_map_at_100_std
      value: 4.681771946538098
    - type: nauc_map_at_10_diff1
      value: 52.161361569838085
    - type: nauc_map_at_10_max
      value: 36.73617207301781
    - type: nauc_map_at_10_std
      value: 3.8276263103624397
    - type: nauc_map_at_1_diff1
      value: 58.609107153987026
    - type: nauc_map_at_1_max
      value: 35.02757021351409
    - type: nauc_map_at_1_std
      value: -0.6936621804258922
    - type: nauc_map_at_20_diff1
      value: 52.20038315316372
    - type: nauc_map_at_20_max
      value: 37.24718279507634
    - type: nauc_map_at_20_std
      value: 4.433483954204022
    - type: nauc_map_at_3_diff1
      value: 52.98890960683455
    - type: nauc_map_at_3_max
      value: 36.627227662545636
    - type: nauc_map_at_3_std
      value: 2.1473003055776303
    - type: nauc_map_at_5_diff1
      value: 52.138722935493796
    - type: nauc_map_at_5_max
      value: 36.57267129483463
    - type: nauc_map_at_5_std
      value: 2.9487505674940846
    - type: nauc_mrr_at_1000_diff1
      value: 52.727499174808976
    - type: nauc_mrr_at_1000_max
      value: 39.660587784745125
    - type: nauc_mrr_at_1000_std
      value: 7.215620440931916
    - type: nauc_mrr_at_100_diff1
      value: 52.71227861389539
    - type: nauc_mrr_at_100_max
      value: 39.65944541613258
    - type: nauc_mrr_at_100_std
      value: 7.232920570021006
    - type: nauc_mrr_at_10_diff1
      value: 52.605293878188306
    - type: nauc_mrr_at_10_max
      value: 39.39789652621602
    - type: nauc_mrr_at_10_std
      value: 6.994445305721646
    - type: nauc_mrr_at_1_diff1
      value: 58.87987158821745
    - type: nauc_mrr_at_1_max
      value: 39.883000294981386
    - type: nauc_mrr_at_1_std
      value: 4.525740385718022
    - type: nauc_mrr_at_20_diff1
      value: 52.709991373902476
    - type: nauc_mrr_at_20_max
      value: 39.63900552236034
    - type: nauc_mrr_at_20_std
      value: 7.180374629477749
    - type: nauc_mrr_at_3_diff1
      value: 52.87253562158551
    - type: nauc_mrr_at_3_max
      value: 39.8526236943088
    - type: nauc_mrr_at_3_std
      value: 6.312802069469314
    - type: nauc_mrr_at_5_diff1
      value: 52.4218392724399
    - type: nauc_mrr_at_5_max
      value: 39.31643340619565
    - type: nauc_mrr_at_5_std
      value: 6.497151104380261
    - type: nauc_ndcg_at_1000_diff1
      value: 50.896715084702
    - type: nauc_ndcg_at_1000_max
      value: 39.03137903719933
    - type: nauc_ndcg_at_1000_std
      value: 9.120093464579284
    - type: nauc_ndcg_at_100_diff1
      value: 50.57128970408371
    - type: nauc_ndcg_at_100_max
      value: 38.57734282233673
    - type: nauc_ndcg_at_100_std
      value: 8.948100860484162
    - type: nauc_ndcg_at_10_diff1
      value: 50.10362861621041
    - type: nauc_ndcg_at_10_max
      value: 36.81788741482043
    - type: nauc_ndcg_at_10_std
      value: 6.248168006196132
    - type: nauc_ndcg_at_1_diff1
      value: 58.87987158821745
    - type: nauc_ndcg_at_1_max
      value: 39.883000294981386
    - type: nauc_ndcg_at_1_std
      value: 4.525740385718022
    - type: nauc_ndcg_at_20_diff1
      value: 50.226356261645435
    - type: nauc_ndcg_at_20_max
      value: 38.11050217929487
    - type: nauc_ndcg_at_20_std
      value: 7.486965774997671
    - type: nauc_ndcg_at_3_diff1
      value: 51.11099202906786
    - type: nauc_ndcg_at_3_max
      value: 37.9283909559886
    - type: nauc_ndcg_at_3_std
      value: 4.702254100554942
    - type: nauc_ndcg_at_5_diff1
      value: 50.09568890455949
    - type: nauc_ndcg_at_5_max
      value: 36.9698296373855
    - type: nauc_ndcg_at_5_std
      value: 5.188587998085958
    - type: nauc_precision_at_1000_diff1
      value: -5.397384708148253
    - type: nauc_precision_at_1000_max
      value: 7.658538116479907
    - type: nauc_precision_at_1000_std
      value: 19.419371334393016
    - type: nauc_precision_at_100_diff1
      value: 4.13777630264156
    - type: nauc_precision_at_100_max
      value: 18.076564064280507
    - type: nauc_precision_at_100_std
      value: 24.333555979164466
    - type: nauc_precision_at_10_diff1
      value: 20.55388046991252
    - type: nauc_precision_at_10_max
      value: 29.41800073419997
    - type: nauc_precision_at_10_std
      value: 18.580366767122076
    - type: nauc_precision_at_1_diff1
      value: 58.87987158821745
    - type: nauc_precision_at_1_max
      value: 39.883000294981386
    - type: nauc_precision_at_1_std
      value: 4.525740385718022
    - type: nauc_precision_at_20_diff1
      value: 14.242304182638074
    - type: nauc_precision_at_20_max
      value: 28.10797068496045
    - type: nauc_precision_at_20_std
      value: 21.90112335945266
    - type: nauc_precision_at_3_diff1
      value: 37.46947895260127
    - type: nauc_precision_at_3_max
      value: 38.006705277755955
    - type: nauc_precision_at_3_std
      value: 12.158729151102953
    - type: nauc_precision_at_5_diff1
      value: 28.328393033049203
    - type: nauc_precision_at_5_max
      value: 33.15639175834532
    - type: nauc_precision_at_5_std
      value: 14.406771010005597
    - type: nauc_recall_at_1000_diff1
      value: 34.31859222623266
    - type: nauc_recall_at_1000_max
      value: 45.13722035429492
    - type: nauc_recall_at_1000_std
      value: 53.791310222471886
    - type: nauc_recall_at_100_diff1
      value: 38.78662480990974
    - type: nauc_recall_at_100_max
      value: 36.173587813938305
    - type: nauc_recall_at_100_std
      value: 26.619442060940923
    - type: nauc_recall_at_10_diff1
      value: 40.329036336117454
    - type: nauc_recall_at_10_max
      value: 30.912126881840678
    - type: nauc_recall_at_10_std
      value: 9.814880445182029
    - type: nauc_recall_at_1_diff1
      value: 58.609107153987026
    - type: nauc_recall_at_1_max
      value: 35.02757021351409
    - type: nauc_recall_at_1_std
      value: -0.6936621804258922
    - type: nauc_recall_at_20_diff1
      value: 40.18277885997754
    - type: nauc_recall_at_20_max
      value: 34.8149234226211
    - type: nauc_recall_at_20_std
      value: 14.12527070299619
    - type: nauc_recall_at_3_diff1
      value: 45.40990517015726
    - type: nauc_recall_at_3_max
      value: 34.69882134310449
    - type: nauc_recall_at_3_std
      value: 3.732266451734092
    - type: nauc_recall_at_5_diff1
      value: 41.766916839112206
    - type: nauc_recall_at_5_max
      value: 32.129792239721716
    - type: nauc_recall_at_5_std
      value: 5.6211961779763415
    - type: ndcg_at_1
      value: 34.937000000000005
    - type: ndcg_at_10
      value: 45.073
    - type: ndcg_at_100
      value: 50.182
    - type: ndcg_at_1000
      value: 52.276
    - type: ndcg_at_20
      value: 47.010000000000005
    - type: ndcg_at_3
      value: 39.612
    - type: ndcg_at_5
      value: 42.266999999999996
    - type: precision_at_1
      value: 34.937000000000005
    - type: precision_at_10
      value: 8.286999999999999
    - type: precision_at_100
      value: 1.268
    - type: precision_at_1000
      value: 0.163
    - type: precision_at_20
      value: 4.832
    - type: precision_at_3
      value: 18.704
    - type: precision_at_5
      value: 13.474
    - type: recall_at_1
      value: 28.136
    - type: recall_at_10
      value: 57.791000000000004
    - type: recall_at_100
      value: 79.521
    - type: recall_at_1000
      value: 93.176
    - type: recall_at_20
      value: 64.48700000000001
    - type: recall_at_3
      value: 42.427
    - type: recall_at_5
      value: 49.39
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval (default)
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: mteb/cqadupstack-programmers
    metrics:
    - type: main_score
      value: 40.65
    - type: map_at_1
      value: 24.381
    - type: map_at_10
      value: 34.522000000000006
    - type: map_at_100
      value: 35.823
    - type: map_at_1000
      value: 35.939
    - type: map_at_20
      value: 35.153
    - type: map_at_3
      value: 31.079
    - type: map_at_5
      value: 33.167
    - type: mrr_at_1
      value: 30.47945205479452
    - type: mrr_at_10
      value: 40.03556026672465
    - type: mrr_at_100
      value: 40.859486284310805
    - type: mrr_at_1000
      value: 40.91385465888402
    - type: mrr_at_20
      value: 40.44289694965349
    - type: mrr_at_3
      value: 37.29071537290716
    - type: mrr_at_5
      value: 38.86605783866057
    - type: nauc_map_at_1000_diff1
      value: 45.08645907290653
    - type: nauc_map_at_1000_max
      value: 37.93984277049077
    - type: nauc_map_at_1000_std
      value: 4.348018171635654
    - type: nauc_map_at_100_diff1
      value: 45.103728679899895
    - type: nauc_map_at_100_max
      value: 37.99535887007234
    - type: nauc_map_at_100_std
      value: 4.357619716783864
    - type: nauc_map_at_10_diff1
      value: 45.00658982142447
    - type: nauc_map_at_10_max
      value: 37.31815420707169
    - type: nauc_map_at_10_std
      value: 3.3382278188396106
    - type: nauc_map_at_1_diff1
      value: 52.252891830215134
    - type: nauc_map_at_1_max
      value: 32.77061213394142
    - type: nauc_map_at_1_std
      value: -2.8010640035289143
    - type: nauc_map_at_20_diff1
      value: 45.091235458676685
    - type: nauc_map_at_20_max
      value: 37.61754711974
    - type: nauc_map_at_20_std
      value: 3.980483359486563
    - type: nauc_map_at_3_diff1
      value: 45.96759132853502
    - type: nauc_map_at_3_max
      value: 35.70107657784562
    - type: nauc_map_at_3_std
      value: 0.5893514980003082
    - type: nauc_map_at_5_diff1
      value: 44.76256760745472
    - type: nauc_map_at_5_max
      value: 36.837428148742184
    - type: nauc_map_at_5_std
      value: 2.739539166736263
    - type: nauc_mrr_at_1000_diff1
      value: 42.92232217227843
    - type: nauc_mrr_at_1000_max
      value: 40.17925571552386
    - type: nauc_mrr_at_1000_std
      value: 8.148960526298065
    - type: nauc_mrr_at_100_diff1
      value: 42.91455614925039
    - type: nauc_mrr_at_100_max
      value: 40.20045379839933
    - type: nauc_mrr_at_100_std
      value: 8.18118615824958
    - type: nauc_mrr_at_10_diff1
      value: 42.813559222481004
    - type: nauc_mrr_at_10_max
      value: 40.22809168556719
    - type: nauc_mrr_at_10_std
      value: 7.862450240887059
    - type: nauc_mrr_at_1_diff1
      value: 49.85954283512805
    - type: nauc_mrr_at_1_max
      value: 39.100124047592615
    - type: nauc_mrr_at_1_std
      value: 4.308285447853536
    - type: nauc_mrr_at_20_diff1
      value: 42.916739579172855
    - type: nauc_mrr_at_20_max
      value: 40.18884672645215
    - type: nauc_mrr_at_20_std
      value: 8.070953502233257
    - type: nauc_mrr_at_3_diff1
      value: 43.33588918249767
    - type: nauc_mrr_at_3_max
      value: 40.02185259938533
    - type: nauc_mrr_at_3_std
      value: 6.611771804932232
    - type: nauc_mrr_at_5_diff1
      value: 42.31798087627212
    - type: nauc_mrr_at_5_max
      value: 39.95836322628087
    - type: nauc_mrr_at_5_std
      value: 7.8252604777639565
    - type: nauc_ndcg_at_1000_diff1
      value: 42.58508571989192
    - type: nauc_ndcg_at_1000_max
      value: 39.911165427637954
    - type: nauc_ndcg_at_1000_std
      value: 9.035223072322985
    - type: nauc_ndcg_at_100_diff1
      value: 42.85331157305972
    - type: nauc_ndcg_at_100_max
      value: 40.901343091681056
    - type: nauc_ndcg_at_100_std
      value: 10.085512946952077
    - type: nauc_ndcg_at_10_diff1
      value: 42.40611041378945
    - type: nauc_ndcg_at_10_max
      value: 39.0395878685548
    - type: nauc_ndcg_at_10_std
      value: 6.603225480063732
    - type: nauc_ndcg_at_1_diff1
      value: 49.85954283512805
    - type: nauc_ndcg_at_1_max
      value: 39.100124047592615
    - type: nauc_ndcg_at_1_std
      value: 4.308285447853536
    - type: nauc_ndcg_at_20_diff1
      value: 42.77709403486501
    - type: nauc_ndcg_at_20_max
      value: 39.45047866326879
    - type: nauc_ndcg_at_20_std
      value: 8.324410425742744
    - type: nauc_ndcg_at_3_diff1
      value: 43.358589542818706
    - type: nauc_ndcg_at_3_max
      value: 37.91671645220353
    - type: nauc_ndcg_at_3_std
      value: 3.548176766967823
    - type: nauc_ndcg_at_5_diff1
      value: 41.56594514959379
    - type: nauc_ndcg_at_5_max
      value: 38.42086968355651
    - type: nauc_ndcg_at_5_std
      value: 6.066217005485217
    - type: nauc_precision_at_1000_diff1
      value: -4.792438397619244
    - type: nauc_precision_at_1000_max
      value: 2.7129923853733118
    - type: nauc_precision_at_1000_std
      value: 11.67095620060032
    - type: nauc_precision_at_100_diff1
      value: 4.188981090197261
    - type: nauc_precision_at_100_max
      value: 24.721360175955237
    - type: nauc_precision_at_100_std
      value: 25.081372551205
    - type: nauc_precision_at_10_diff1
      value: 18.811203609613973
    - type: nauc_precision_at_10_max
      value: 38.14203413304164
    - type: nauc_precision_at_10_std
      value: 21.933474701361284
    - type: nauc_precision_at_1_diff1
      value: 49.85954283512805
    - type: nauc_precision_at_1_max
      value: 39.100124047592615
    - type: nauc_precision_at_1_std
      value: 4.308285447853536
    - type: nauc_precision_at_20_diff1
      value: 14.825255525788132
    - type: nauc_precision_at_20_max
      value: 33.96942297730217
    - type: nauc_precision_at_20_std
      value: 24.843048642950983
    - type: nauc_precision_at_3_diff1
      value: 31.399689348786293
    - type: nauc_precision_at_3_max
      value: 42.36936733454805
    - type: nauc_precision_at_3_std
      value: 13.606543019531983
    - type: nauc_precision_at_5_diff1
      value: 22.95129561216099
    - type: nauc_precision_at_5_max
      value: 40.15375346390098
    - type: nauc_precision_at_5_std
      value: 19.844337655067264
    - type: nauc_recall_at_1000_diff1
      value: 18.250357722466067
    - type: nauc_recall_at_1000_max
      value: 46.49889896497268
    - type: nauc_recall_at_1000_std
      value: 49.015133298216114
    - type: nauc_recall_at_100_diff1
      value: 34.14073541913647
    - type: nauc_recall_at_100_max
      value: 47.880871182499654
    - type: nauc_recall_at_100_std
      value: 33.394450460167654
    - type: nauc_recall_at_10_diff1
      value: 34.10055202985094
    - type: nauc_recall_at_10_max
      value: 37.29000268460915
    - type: nauc_recall_at_10_std
      value: 10.719966977592444
    - type: nauc_recall_at_1_diff1
      value: 52.252891830215134
    - type: nauc_recall_at_1_max
      value: 32.77061213394142
    - type: nauc_recall_at_1_std
      value: -2.8010640035289143
    - type: nauc_recall_at_20_diff1
      value: 34.77711534255729
    - type: nauc_recall_at_20_max
      value: 37.8830564545796
    - type: nauc_recall_at_20_std
      value: 17.204302583685262
    - type: nauc_recall_at_3_diff1
      value: 37.38919386647721
    - type: nauc_recall_at_3_max
      value: 34.570111627131695
    - type: nauc_recall_at_3_std
      value: 2.2380100020283096
    - type: nauc_recall_at_5_diff1
      value: 32.187904365676324
    - type: nauc_recall_at_5_max
      value: 35.77757062335063
    - type: nauc_recall_at_5_std
      value: 8.796247583408153
    - type: ndcg_at_1
      value: 30.479
    - type: ndcg_at_10
      value: 40.65
    - type: ndcg_at_100
      value: 46.366
    - type: ndcg_at_1000
      value: 48.689
    - type: ndcg_at_20
      value: 42.576
    - type: ndcg_at_3
      value: 35.116
    - type: ndcg_at_5
      value: 37.909
    - type: precision_at_1
      value: 30.479
    - type: precision_at_10
      value: 7.603
    - type: precision_at_100
      value: 1.226
    - type: precision_at_1000
      value: 0.16
    - type: precision_at_20
      value: 4.458
    - type: precision_at_3
      value: 17.122999999999998
    - type: precision_at_5
      value: 12.58
    - type: recall_at_1
      value: 24.381
    - type: recall_at_10
      value: 53.591
    - type: recall_at_100
      value: 78.31
    - type: recall_at_1000
      value: 93.952
    - type: recall_at_20
      value: 60.465999999999994
    - type: recall_at_3
      value: 38.189
    - type: recall_at_5
      value: 45.425
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: CQADupstackRetrieval_is_a_combined_dataset
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: main_score
      value: 40.268750000000004
    - type: ndcg_at_10
      value: 40.268750000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval (default)
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: mteb/cqadupstack-stats
    metrics:
    - type: main_score
      value: 34.89
    - type: map_at_1
      value: 24.343
    - type: map_at_10
      value: 31.064999999999998
    - type: map_at_100
      value: 32.013000000000005
    - type: map_at_1000
      value: 32.11
    - type: map_at_20
      value: 31.584
    - type: map_at_3
      value: 29.287999999999997
    - type: map_at_5
      value: 30.262
    - type: mrr_at_1
      value: 27.453987730061353
    - type: mrr_at_10
      value: 33.89503603077223
    - type: mrr_at_100
      value: 34.76452500547403
    - type: mrr_at_1000
      value: 34.831641998976096
    - type: mrr_at_20
      value: 34.39433378717007
    - type: mrr_at_3
      value: 32.20858895705521
    - type: mrr_at_5
      value: 33.09049079754601
    - type: nauc_map_at_1000_diff1
      value: 52.16433709147209
    - type: nauc_map_at_1000_max
      value: 41.895031426126124
    - type: nauc_map_at_1000_std
      value: 7.981597857750285
    - type: nauc_map_at_100_diff1
      value: 52.151218712376554
    - type: nauc_map_at_100_max
      value: 41.845879262079926
    - type: nauc_map_at_100_std
      value: 7.961900934081761
    - type: nauc_map_at_10_diff1
      value: 52.402838490484406
    - type: nauc_map_at_10_max
      value: 41.77705031749437
    - type: nauc_map_at_10_std
      value: 7.46409351133074
    - type: nauc_map_at_1_diff1
      value: 58.5759193069631
    - type: nauc_map_at_1_max
      value: 40.228075475738066
    - type: nauc_map_at_1_std
      value: -0.331391740789906
    - type: nauc_map_at_20_diff1
      value: 52.24118427663996
    - type: nauc_map_at_20_max
      value: 41.717633721989124
    - type: nauc_map_at_20_std
      value: 7.713122213513287
    - type: nauc_map_at_3_diff1
      value: 53.00130785485122
    - type: nauc_map_at_3_max
      value: 41.257807025801554
    - type: nauc_map_at_3_std
      value: 5.77564250625532
    - type: nauc_map_at_5_diff1
      value: 52.765771056206034
    - type: nauc_map_at_5_max
      value: 41.17385278218844
    - type: nauc_map_at_5_std
      value: 6.267751055469911
    - type: nauc_mrr_at_1000_diff1
      value: 50.542579627409346
    - type: nauc_mrr_at_1000_max
      value: 43.84384933961597
    - type: nauc_mrr_at_1000_std
      value: 8.9290783799145
    - type: nauc_mrr_at_100_diff1
      value: 50.52367459214615
    - type: nauc_mrr_at_100_max
      value: 43.83317399067154
    - type: nauc_mrr_at_100_std
      value: 8.93848179915739
    - type: nauc_mrr_at_10_diff1
      value: 50.592180069200076
    - type: nauc_mrr_at_10_max
      value: 43.86512615662472
    - type: nauc_mrr_at_10_std
      value: 8.648594684024122
    - type: nauc_mrr_at_1_diff1
      value: 56.64925132242809
    - type: nauc_mrr_at_1_max
      value: 44.302509524664245
    - type: nauc_mrr_at_1_std
      value: 2.8736722205582566
    - type: nauc_mrr_at_20_diff1
      value: 50.621524856832025
    - type: nauc_mrr_at_20_max
      value: 43.85010163029952
    - type: nauc_mrr_at_20_std
      value: 8.767065605432117
    - type: nauc_mrr_at_3_diff1
      value: 51.38022486401255
    - type: nauc_mrr_at_3_max
      value: 43.690091517144886
    - type: nauc_mrr_at_3_std
      value: 7.583000007208131
    - type: nauc_mrr_at_5_diff1
      value: 51.026555577484345
    - type: nauc_mrr_at_5_max
      value: 43.40937882095473
    - type: nauc_mrr_at_5_std
      value: 7.870192951985875
    - type: nauc_ndcg_at_1000_diff1
      value: 48.946807624632214
    - type: nauc_ndcg_at_1000_max
      value: 43.63846016728263
    - type: nauc_ndcg_at_1000_std
      value: 13.07112902361304
    - type: nauc_ndcg_at_100_diff1
      value: 48.46009023670086
    - type: nauc_ndcg_at_100_max
      value: 42.84578351440459
    - type: nauc_ndcg_at_100_std
      value: 13.048673429979113
    - type: nauc_ndcg_at_10_diff1
      value: 49.80098562249132
    - type: nauc_ndcg_at_10_max
      value: 42.46231067480857
    - type: nauc_ndcg_at_10_std
      value: 10.5896193945906
    - type: nauc_ndcg_at_1_diff1
      value: 56.64925132242809
    - type: nauc_ndcg_at_1_max
      value: 44.302509524664245
    - type: nauc_ndcg_at_1_std
      value: 2.8736722205582566
    - type: nauc_ndcg_at_20_diff1
      value: 49.32237998567543
    - type: nauc_ndcg_at_20_max
      value: 42.23892720118917
    - type: nauc_ndcg_at_20_std
      value: 11.311668576433599
    - type: nauc_ndcg_at_3_diff1
      value: 51.01125725288161
    - type: nauc_ndcg_at_3_max
      value: 42.12827055031322
    - type: nauc_ndcg_at_3_std
      value: 7.952435809082195
    - type: nauc_ndcg_at_5_diff1
      value: 50.88410133484621
    - type: nauc_ndcg_at_5_max
      value: 41.565359240466975
    - type: nauc_ndcg_at_5_std
      value: 8.314306379070254
    - type: nauc_precision_at_1000_diff1
      value: 4.413508451597973
    - type: nauc_precision_at_1000_max
      value: 33.762398288256094
    - type: nauc_precision_at_1000_std
      value: 25.98231326304456
    - type: nauc_precision_at_100_diff1
      value: 17.203842054243655
    - type: nauc_precision_at_100_max
      value: 41.105989573268204
    - type: nauc_precision_at_100_std
      value: 31.631978351351798
    - type: nauc_precision_at_10_diff1
      value: 34.696132889148664
    - type: nauc_precision_at_10_max
      value: 45.80034445639316
    - type: nauc_precision_at_10_std
      value: 25.084569022460418
    - type: nauc_precision_at_1_diff1
      value: 56.64925132242809
    - type: nauc_precision_at_1_max
      value: 44.302509524664245
    - type: nauc_precision_at_1_std
      value: 2.8736722205582566
    - type: nauc_precision_at_20_diff1
      value: 29.865679363368436
    - type: nauc_precision_at_20_max
      value: 43.51573363065152
    - type: nauc_precision_at_20_std
      value: 26.69033832110468
    - type: nauc_precision_at_3_diff1
      value: 41.389196232922316
    - type: nauc_precision_at_3_max
      value: 46.28755529729629
    - type: nauc_precision_at_3_std
      value: 16.909849769292716
    - type: nauc_precision_at_5_diff1
      value: 39.087938584206306
    - type: nauc_precision_at_5_max
      value: 43.92003534457625
    - type: nauc_precision_at_5_std
      value: 18.560228476365946
    - type: nauc_recall_at_1000_diff1
      value: 26.669464596984678
    - type: nauc_recall_at_1000_max
      value: 46.54456322772547
    - type: nauc_recall_at_1000_std
      value: 44.24504504678441
    - type: nauc_recall_at_100_diff1
      value: 31.188372051167907
    - type: nauc_recall_at_100_max
      value: 39.33606079794924
    - type: nauc_recall_at_100_std
      value: 31.351107197440655
    - type: nauc_recall_at_10_diff1
      value: 42.00542257322957
    - type: nauc_recall_at_10_max
      value: 40.557783865813306
    - type: nauc_recall_at_10_std
      value: 17.578789968761935
    - type: nauc_recall_at_1_diff1
      value: 58.5759193069631
    - type: nauc_recall_at_1_max
      value: 40.228075475738066
    - type: nauc_recall_at_1_std
      value: -0.331391740789906
    - type: nauc_recall_at_20_diff1
      value: 39.65715933448972
    - type: nauc_recall_at_20_max
      value: 38.93829722046506
    - type: nauc_recall_at_20_std
      value: 20.20996021737043
    - type: nauc_recall_at_3_diff1
      value: 46.87588712984084
    - type: nauc_recall_at_3_max
      value: 39.797140704347825
    - type: nauc_recall_at_3_std
      value: 10.153636337649985
    - type: nauc_recall_at_5_diff1
      value: 46.08928170734386
    - type: nauc_recall_at_5_max
      value: 39.01544586906766
    - type: nauc_recall_at_5_std
      value: 11.453087165740614
    - type: ndcg_at_1
      value: 27.454
    - type: ndcg_at_10
      value: 34.89
    - type: ndcg_at_100
      value: 39.612
    - type: ndcg_at_1000
      value: 42.045
    - type: ndcg_at_20
      value: 36.738
    - type: ndcg_at_3
      value: 31.630000000000003
    - type: ndcg_at_5
      value: 33.056000000000004
    - type: precision_at_1
      value: 27.454
    - type: precision_at_10
      value: 5.383
    - type: precision_at_100
      value: 0.8330000000000001
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_20
      value: 3.152
    - type: precision_at_3
      value: 13.65
    - type: precision_at_5
      value: 9.232999999999999
    - type: recall_at_1
      value: 24.343
    - type: recall_at_10
      value: 43.836999999999996
    - type: recall_at_100
      value: 65.202
    - type: recall_at_1000
      value: 83.206
    - type: recall_at_20
      value: 50.829
    - type: recall_at_3
      value: 34.695
    - type: recall_at_5
      value: 38.33
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval (default)
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: mteb/cqadupstack-tex
    metrics:
    - type: main_score
      value: 28.595
    - type: map_at_1
      value: 17.134
    - type: map_at_10
      value: 24.104
    - type: map_at_100
      value: 25.238
    - type: map_at_1000
      value: 25.368000000000002
    - type: map_at_20
      value: 24.691
    - type: map_at_3
      value: 21.803
    - type: map_at_5
      value: 23.066
    - type: mrr_at_1
      value: 20.750172057811426
    - type: mrr_at_10
      value: 27.87088017129311
    - type: mrr_at_100
      value: 28.81791033306077
    - type: mrr_at_1000
      value: 28.899375497257516
    - type: mrr_at_20
      value: 28.378447148229803
    - type: mrr_at_3
      value: 25.699701766460198
    - type: mrr_at_5
      value: 26.892062399632945
    - type: nauc_map_at_1000_diff1
      value: 36.89782887137058
    - type: nauc_map_at_1000_max
      value: 33.08016929719372
    - type: nauc_map_at_1000_std
      value: 3.3099635444764735
    - type: nauc_map_at_100_diff1
      value: 36.8780819112453
    - type: nauc_map_at_100_max
      value: 33.050931677418774
    - type: nauc_map_at_100_std
      value: 3.2972109847369
    - type: nauc_map_at_10_diff1
      value: 37.08595684018923
    - type: nauc_map_at_10_max
      value: 32.816323824163476
    - type: nauc_map_at_10_std
      value: 2.552386021070936
    - type: nauc_map_at_1_diff1
      value: 43.51132829968084
    - type: nauc_map_at_1_max
      value: 32.3415757101499
    - type: nauc_map_at_1_std
      value: 1.1401002178840585
    - type: nauc_map_at_20_diff1
      value: 36.94143359488415
    - type: nauc_map_at_20_max
      value: 32.982623511734424
    - type: nauc_map_at_20_std
      value: 2.948810693672891
    - type: nauc_map_at_3_diff1
      value: 38.71612128344212
    - type: nauc_map_at_3_max
      value: 32.637048522654034
    - type: nauc_map_at_3_std
      value: 1.156009064619756
    - type: nauc_map_at_5_diff1
      value: 37.78942760585617
    - type: nauc_map_at_5_max
      value: 32.75604432178518
    - type: nauc_map_at_5_std
      value: 2.0173303861590925
    - type: nauc_mrr_at_1000_diff1
      value: 36.135612852709095
    - type: nauc_mrr_at_1000_max
      value: 34.12476601616417
    - type: nauc_mrr_at_1000_std
      value: 3.845954153422737
    - type: nauc_mrr_at_100_diff1
      value: 36.12068139187418
    - type: nauc_mrr_at_100_max
      value: 34.119358854394214
    - type: nauc_mrr_at_100_std
      value: 3.849886746617628
    - type: nauc_mrr_at_10_diff1
      value: 36.21596271906166
    - type: nauc_mrr_at_10_max
      value: 34.0449176526415
    - type: nauc_mrr_at_10_std
      value: 3.392757560646604
    - type: nauc_mrr_at_1_diff1
      value: 42.4688892662091
    - type: nauc_mrr_at_1_max
      value: 34.61638632573713
    - type: nauc_mrr_at_1_std
      value: 1.842575033698782
    - type: nauc_mrr_at_20_diff1
      value: 36.100856934569805
    - type: nauc_mrr_at_20_max
      value: 34.09556229697657
    - type: nauc_mrr_at_20_std
      value: 3.6620323814000684
    - type: nauc_mrr_at_3_diff1
      value: 37.47429125012118
    - type: nauc_mrr_at_3_max
      value: 34.16045576255616
    - type: nauc_mrr_at_3_std
      value: 2.2755120232411903
    - type: nauc_mrr_at_5_diff1
      value: 36.65972061354651
    - type: nauc_mrr_at_5_max
      value: 33.96708531025307
    - type: nauc_mrr_at_5_std
      value: 2.8464790894241885
    - type: nauc_ndcg_at_1000_diff1
      value: 33.78518836462285
    - type: nauc_ndcg_at_1000_max
      value: 33.63185976032734
    - type: nauc_ndcg_at_1000_std
      value: 6.989447169026228
    - type: nauc_ndcg_at_100_diff1
      value: 33.39381937519511
    - type: nauc_ndcg_at_100_max
      value: 33.27132063948536
    - type: nauc_ndcg_at_100_std
      value: 6.813560048322648
    - type: nauc_ndcg_at_10_diff1
      value: 34.231562121939554
    - type: nauc_ndcg_at_10_max
      value: 32.957787193957664
    - type: nauc_ndcg_at_10_std
      value: 3.9141441526477867
    - type: nauc_ndcg_at_1_diff1
      value: 42.4688892662091
    - type: nauc_ndcg_at_1_max
      value: 34.61638632573713
    - type: nauc_ndcg_at_1_std
      value: 1.842575033698782
    - type: nauc_ndcg_at_20_diff1
      value: 33.73777473522033
    - type: nauc_ndcg_at_20_max
      value: 33.210514059183375
    - type: nauc_ndcg_at_20_std
      value: 5.073301185091096
    - type: nauc_ndcg_at_3_diff1
      value: 36.878575344351624
    - type: nauc_ndcg_at_3_max
      value: 33.32312056613959
    - type: nauc_ndcg_at_3_std
      value: 1.4148329239930337
    - type: nauc_ndcg_at_5_diff1
      value: 35.53121227641059
    - type: nauc_ndcg_at_5_max
      value: 32.97583732206957
    - type: nauc_ndcg_at_5_std
      value: 2.7296938204105046
    - type: nauc_precision_at_1000_diff1
      value: 5.048094785844507
    - type: nauc_precision_at_1000_max
      value: 20.72305226491182
    - type: nauc_precision_at_1000_std
      value: 13.166659843282705
    - type: nauc_precision_at_100_diff1
      value: 11.403111213178537
    - type: nauc_precision_at_100_max
      value: 25.876626218425784
    - type: nauc_precision_at_100_std
      value: 15.750263914866009
    - type: nauc_precision_at_10_diff1
      value: 21.812128842605574
    - type: nauc_precision_at_10_max
      value: 32.36024330484034
    - type: nauc_precision_at_10_std
      value: 8.30153625256048
    - type: nauc_precision_at_1_diff1
      value: 42.4688892662091
    - type: nauc_precision_at_1_max
      value: 34.61638632573713
    - type: nauc_precision_at_1_std
      value: 1.842575033698782
    - type: nauc_precision_at_20_diff1
      value: 18.126781090521444
    - type: nauc_precision_at_20_max
      value: 30.879595883417306
    - type: nauc_precision_at_20_std
      value: 10.9632189477538
    - type: nauc_precision_at_3_diff1
      value: 30.857088332242842
    - type: nauc_precision_at_3_max
      value: 34.435211511210596
    - type: nauc_precision_at_3_std
      value: 2.1743174606141897
    - type: nauc_precision_at_5_diff1
      value: 26.70684474302077
    - type: nauc_precision_at_5_max
      value: 33.881041843033714
    - type: nauc_precision_at_5_std
      value: 4.964700828623661
    - type: nauc_recall_at_1000_diff1
      value: 15.179090310075448
    - type: nauc_recall_at_1000_max
      value: 31.177239498655414
    - type: nauc_recall_at_1000_std
      value: 32.817986166465225
    - type: nauc_recall_at_100_diff1
      value: 19.791440992074865
    - type: nauc_recall_at_100_max
      value: 29.00647998704242
    - type: nauc_recall_at_100_std
      value: 19.00290442690933
    - type: nauc_recall_at_10_diff1
      value: 25.400689588358937
    - type: nauc_recall_at_10_max
      value: 29.67225586682777
    - type: nauc_recall_at_10_std
      value: 6.326653531699302
    - type: nauc_recall_at_1_diff1
      value: 43.51132829968084
    - type: nauc_recall_at_1_max
      value: 32.3415757101499
    - type: nauc_recall_at_1_std
      value: 1.1401002178840585
    - type: nauc_recall_at_20_diff1
      value: 23.158667708575777
    - type: nauc_recall_at_20_max
      value: 29.65979097031932
    - type: nauc_recall_at_20_std
      value: 10.004891834963093
    - type: nauc_recall_at_3_diff1
      value: 32.631467317064406
    - type: nauc_recall_at_3_max
      value: 30.531285335243492
    - type: nauc_recall_at_3_std
      value: 0.9187457345239257
    - type: nauc_recall_at_5_diff1
      value: 29.18624452088816
    - type: nauc_recall_at_5_max
      value: 29.708509257799818
    - type: nauc_recall_at_5_std
      value: 3.6369154905030765
    - type: ndcg_at_1
      value: 20.75
    - type: ndcg_at_10
      value: 28.595
    - type: ndcg_at_100
      value: 34.047
    - type: ndcg_at_1000
      value: 37.039
    - type: ndcg_at_20
      value: 30.526999999999997
    - type: ndcg_at_3
      value: 24.46
    - type: ndcg_at_5
      value: 26.339000000000002
    - type: precision_at_1
      value: 20.75
    - type: precision_at_10
      value: 5.231
    - type: precision_at_100
      value: 0.9400000000000001
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_20
      value: 3.1919999999999997
    - type: precision_at_3
      value: 11.482000000000001
    - type: precision_at_5
      value: 8.369
    - type: recall_at_1
      value: 17.134
    - type: recall_at_10
      value: 38.316
    - type: recall_at_100
      value: 62.913
    - type: recall_at_1000
      value: 84.233
    - type: recall_at_20
      value: 45.465
    - type: recall_at_3
      value: 26.840000000000003
    - type: recall_at_5
      value: 31.616
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval (default)
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: mteb/cqadupstack-unix
    metrics:
    - type: main_score
      value: 39.89
    - type: map_at_1
      value: 25.712000000000003
    - type: map_at_10
      value: 34.615
    - type: map_at_100
      value: 35.846000000000004
    - type: map_at_1000
      value: 35.953
    - type: map_at_20
      value: 35.321999999999996
    - type: map_at_3
      value: 32.056000000000004
    - type: map_at_5
      value: 33.315
    - type: mrr_at_1
      value: 29.850746268656714
    - type: mrr_at_10
      value: 38.71860933428097
    - type: mrr_at_100
      value: 39.61660285528755
    - type: mrr_at_1000
      value: 39.676734545015016
    - type: mrr_at_20
      value: 39.20100616633673
    - type: mrr_at_3
      value: 36.53606965174129
    - type: mrr_at_5
      value: 37.604166666666664
    - type: nauc_map_at_1000_diff1
      value: 44.53604492112556
    - type: nauc_map_at_1000_max
      value: 39.23951280655509
    - type: nauc_map_at_1000_std
      value: -0.5395031277467611
    - type: nauc_map_at_100_diff1
      value: 44.51770266447437
    - type: nauc_map_at_100_max
      value: 39.24922673974566
    - type: nauc_map_at_100_std
      value: -0.5418148801230667
    - type: nauc_map_at_10_diff1
      value: 44.65794786125487
    - type: nauc_map_at_10_max
      value: 38.73649462647244
    - type: nauc_map_at_10_std
      value: -1.2439485316781116
    - type: nauc_map_at_1_diff1
      value: 51.3015448718258
    - type: nauc_map_at_1_max
      value: 37.68162132042243
    - type: nauc_map_at_1_std
      value: -4.942523398750195
    - type: nauc_map_at_20_diff1
      value: 44.56752919145453
    - type: nauc_map_at_20_max
      value: 39.15671461993185
    - type: nauc_map_at_20_std
      value: -0.69839546492355
    - type: nauc_map_at_3_diff1
      value: 45.85932349411764
    - type: nauc_map_at_3_max
      value: 38.36052842023208
    - type: nauc_map_at_3_std
      value: -2.2972931157260588
    - type: nauc_map_at_5_diff1
      value: 45.05340840012778
    - type: nauc_map_at_5_max
      value: 38.498629564114125
    - type: nauc_map_at_5_std
      value: -1.5490287999131676
    - type: nauc_mrr_at_1000_diff1
      value: 43.86315579499585
    - type: nauc_mrr_at_1000_max
      value: 41.22972681259589
    - type: nauc_mrr_at_1000_std
      value: 0.2312354368485346
    - type: nauc_mrr_at_100_diff1
      value: 43.82688559618802
    - type: nauc_mrr_at_100_max
      value: 41.228924353114486
    - type: nauc_mrr_at_100_std
      value: 0.23800385006789107
    - type: nauc_mrr_at_10_diff1
      value: 43.83189862351878
    - type: nauc_mrr_at_10_max
      value: 41.10756388047098
    - type: nauc_mrr_at_10_std
      value: -0.21685246034735925
    - type: nauc_mrr_at_1_diff1
      value: 51.230432406020476
    - type: nauc_mrr_at_1_max
      value: 41.48741446620127
    - type: nauc_mrr_at_1_std
      value: -2.7496538177528658
    - type: nauc_mrr_at_20_diff1
      value: 43.83356230557604
    - type: nauc_mrr_at_20_max
      value: 41.22449434055463
    - type: nauc_mrr_at_20_std
      value: 0.1017557136662017
    - type: nauc_mrr_at_3_diff1
      value: 44.642204252525374
    - type: nauc_mrr_at_3_max
      value: 41.394135395117
    - type: nauc_mrr_at_3_std
      value: -0.3102479679512395
    - type: nauc_mrr_at_5_diff1
      value: 44.03177178118225
    - type: nauc_mrr_at_5_max
      value: 41.14617895311199
    - type: nauc_mrr_at_5_std
      value: -0.15778767756702847
    - type: nauc_ndcg_at_1000_diff1
      value: 41.931781429588355
    - type: nauc_ndcg_at_1000_max
      value: 40.19130298587713
    - type: nauc_ndcg_at_1000_std
      value: 2.4213241669516314
    - type: nauc_ndcg_at_100_diff1
      value: 41.47736552910553
    - type: nauc_ndcg_at_100_max
      value: 40.35512795681438
    - type: nauc_ndcg_at_100_std
      value: 2.797704103101513
    - type: nauc_ndcg_at_10_diff1
      value: 41.89774080166355
    - type: nauc_ndcg_at_10_max
      value: 39.068973811839285
    - type: nauc_ndcg_at_10_std
      value: 0.1409703112345929
    - type: nauc_ndcg_at_1_diff1
      value: 51.230432406020476
    - type: nauc_ndcg_at_1_max
      value: 41.48741446620127
    - type: nauc_ndcg_at_1_std
      value: -2.7496538177528658
    - type: nauc_ndcg_at_20_diff1
      value: 41.654873436264864
    - type: nauc_ndcg_at_20_max
      value: 40.02385895251709
    - type: nauc_ndcg_at_20_std
      value: 1.6616675841903024
    - type: nauc_ndcg_at_3_diff1
      value: 43.677208022052135
    - type: nauc_ndcg_at_3_max
      value: 39.355842345181706
    - type: nauc_ndcg_at_3_std
      value: -0.9994914032687997
    - type: nauc_ndcg_at_5_diff1
      value: 42.63394828100176
    - type: nauc_ndcg_at_5_max
      value: 38.78287388555721
    - type: nauc_ndcg_at_5_std
      value: -0.40383353126040594
    - type: nauc_precision_at_1000_diff1
      value: -12.720363964831158
    - type: nauc_precision_at_1000_max
      value: 1.780615695736265
    - type: nauc_precision_at_1000_std
      value: 6.9259933939590015
    - type: nauc_precision_at_100_diff1
      value: 1.5494816839626728
    - type: nauc_precision_at_100_max
      value: 21.16486694935512
    - type: nauc_precision_at_100_std
      value: 13.63358160875128
    - type: nauc_precision_at_10_diff1
      value: 21.022460223564163
    - type: nauc_precision_at_10_max
      value: 33.517939417026845
    - type: nauc_precision_at_10_std
      value: 6.777527986277892
    - type: nauc_precision_at_1_diff1
      value: 51.230432406020476
    - type: nauc_precision_at_1_max
      value: 41.48741446620127
    - type: nauc_precision_at_1_std
      value: -2.7496538177528658
    - type: nauc_precision_at_20_diff1
      value: 14.686385148466163
    - type: nauc_precision_at_20_max
      value: 31.18430505462782
    - type: nauc_precision_at_20_std
      value: 12.077548081645366
    - type: nauc_precision_at_3_diff1
      value: 33.70051545579217
    - type: nauc_precision_at_3_max
      value: 39.60907345133216
    - type: nauc_precision_at_3_std
      value: 4.2539653363781476
    - type: nauc_precision_at_5_diff1
      value: 27.941480760698635
    - type: nauc_precision_at_5_max
      value: 37.31639952677206
    - type: nauc_precision_at_5_std
      value: 6.219978856190591
    - type: nauc_recall_at_1000_diff1
      value: 20.47974719909093
    - type: nauc_recall_at_1000_max
      value: 40.904077508578574
    - type: nauc_recall_at_1000_std
      value: 36.68929060623499
    - type: nauc_recall_at_100_diff1
      value: 26.82928665193226
    - type: nauc_recall_at_100_max
      value: 39.0725275666681
    - type: nauc_recall_at_100_std
      value: 18.856939694213875
    - type: nauc_recall_at_10_diff1
      value: 32.48097141976132
    - type: nauc_recall_at_10_max
      value: 34.921002737123445
    - type: nauc_recall_at_10_std
      value: 2.8847239359758596
    - type: nauc_recall_at_1_diff1
      value: 51.3015448718258
    - type: nauc_recall_at_1_max
      value: 37.68162132042243
    - type: nauc_recall_at_1_std
      value: -4.942523398750195
    - type: nauc_recall_at_20_diff1
      value: 31.155212544928517
    - type: nauc_recall_at_20_max
      value: 37.903451497060075
    - type: nauc_recall_at_20_std
      value: 8.052860930292049
    - type: nauc_recall_at_3_diff1
      value: 38.338624569740745
    - type: nauc_recall_at_3_max
      value: 36.16696793299773
    - type: nauc_recall_at_3_std
      value: -0.5499014670399716
    - type: nauc_recall_at_5_diff1
      value: 35.47491917247829
    - type: nauc_recall_at_5_max
      value: 34.98125952824827
    - type: nauc_recall_at_5_std
      value: 1.18095697584272
    - type: ndcg_at_1
      value: 29.851
    - type: ndcg_at_10
      value: 39.89
    - type: ndcg_at_100
      value: 45.327
    - type: ndcg_at_1000
      value: 47.772999999999996
    - type: ndcg_at_20
      value: 42.022999999999996
    - type: ndcg_at_3
      value: 35.284
    - type: ndcg_at_5
      value: 37.062
    - type: precision_at_1
      value: 29.851
    - type: precision_at_10
      value: 6.707000000000001
    - type: precision_at_100
      value: 1.054
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_20
      value: 3.9690000000000003
    - type: precision_at_3
      value: 16.107
    - type: precision_at_5
      value: 10.97
    - type: recall_at_1
      value: 25.712000000000003
    - type: recall_at_10
      value: 51.754
    - type: recall_at_100
      value: 75.229
    - type: recall_at_1000
      value: 92.352
    - type: recall_at_20
      value: 59.224
    - type: recall_at_3
      value: 38.942
    - type: recall_at_5
      value: 43.608000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: mteb/cqadupstack-webmasters
    metrics:
    - type: main_score
      value: 39.275
    - type: map_at_1
      value: 25.207
    - type: map_at_10
      value: 33.73
    - type: map_at_100
      value: 35.314
    - type: map_at_1000
      value: 35.539
    - type: map_at_20
      value: 34.485
    - type: map_at_3
      value: 30.751
    - type: map_at_5
      value: 32.458
    - type: mrr_at_1
      value: 30.237154150197625
    - type: mrr_at_10
      value: 38.160330008156095
    - type: mrr_at_100
      value: 39.19604519073853
    - type: mrr_at_1000
      value: 39.25828944824003
    - type: mrr_at_20
      value: 38.76011256052923
    - type: mrr_at_3
      value: 35.573122529644266
    - type: mrr_at_5
      value: 37.02569169960474
    - type: nauc_map_at_1000_diff1
      value: 43.30050536386893
    - type: nauc_map_at_1000_max
      value: 34.49322247549182
    - type: nauc_map_at_1000_std
      value: 11.480704685860331
    - type: nauc_map_at_100_diff1
      value: 43.23374152493401
    - type: nauc_map_at_100_max
      value: 34.63190473420833
    - type: nauc_map_at_100_std
      value: 11.327553372568829
    - type: nauc_map_at_10_diff1
      value: 43.30961094445623
    - type: nauc_map_at_10_max
      value: 34.03516491801115
    - type: nauc_map_at_10_std
      value: 9.930448779277498
    - type: nauc_map_at_1_diff1
      value: 48.52093859650541
    - type: nauc_map_at_1_max
      value: 31.75748436789384
    - type: nauc_map_at_1_std
      value: 6.295511700792233
    - type: nauc_map_at_20_diff1
      value: 43.20196516265475
    - type: nauc_map_at_20_max
      value: 34.40279536967664
    - type: nauc_map_at_20_std
      value: 10.502521746353215
    - type: nauc_map_at_3_diff1
      value: 44.95075655761481
    - type: nauc_map_at_3_max
      value: 34.26130085326597
    - type: nauc_map_at_3_std
      value: 8.112284718354838
    - type: nauc_map_at_5_diff1
      value: 44.07530466847515
    - type: nauc_map_at_5_max
      value: 34.29301885967441
    - type: nauc_map_at_5_std
      value: 9.578236763789624
    - type: nauc_mrr_at_1000_diff1
      value: 43.74672886274306
    - type: nauc_mrr_at_1000_max
      value: 34.91906226000147
    - type: nauc_mrr_at_1000_std
      value: 11.902601352714218
    - type: nauc_mrr_at_100_diff1
      value: 43.723509090577245
    - type: nauc_mrr_at_100_max
      value: 34.90821615383906
    - type: nauc_mrr_at_100_std
      value: 11.929277924338157
    - type: nauc_mrr_at_10_diff1
      value: 43.79863834518147
    - type: nauc_mrr_at_10_max
      value: 34.77481237076968
    - type: nauc_mrr_at_10_std
      value: 11.621191309978766
    - type: nauc_mrr_at_1_diff1
      value: 47.691221572943014
    - type: nauc_mrr_at_1_max
      value: 33.83642419108169
    - type: nauc_mrr_at_1_std
      value: 9.150897325122848
    - type: nauc_mrr_at_20_diff1
      value: 43.72762657840614
    - type: nauc_mrr_at_20_max
      value: 34.93505549897513
    - type: nauc_mrr_at_20_std
      value: 11.77349360531995
    - type: nauc_mrr_at_3_diff1
      value: 44.801537918309464
    - type: nauc_mrr_at_3_max
      value: 35.19185952684632
    - type: nauc_mrr_at_3_std
      value: 10.129116464250496
    - type: nauc_mrr_at_5_diff1
      value: 44.002923041903024
    - type: nauc_mrr_at_5_max
      value: 35.04910165721431
    - type: nauc_mrr_at_5_std
      value: 11.398743784126784
    - type: nauc_ndcg_at_1000_diff1
      value: 42.1442239971562
    - type: nauc_ndcg_at_1000_max
      value: 35.56548085015422
    - type: nauc_ndcg_at_1000_std
      value: 14.555455012386773
    - type: nauc_ndcg_at_100_diff1
      value: 41.050980420258334
    - type: nauc_ndcg_at_100_max
      value: 35.2027650239632
    - type: nauc_ndcg_at_100_std
      value: 15.344655139587024
    - type: nauc_ndcg_at_10_diff1
      value: 41.471409940051366
    - type: nauc_ndcg_at_10_max
      value: 34.09128642447279
    - type: nauc_ndcg_at_10_std
      value: 12.90078883047037
    - type: nauc_ndcg_at_1_diff1
      value: 47.691221572943014
    - type: nauc_ndcg_at_1_max
      value: 33.83642419108169
    - type: nauc_ndcg_at_1_std
      value: 9.150897325122848
    - type: nauc_ndcg_at_20_diff1
      value: 41.1905793713784
    - type: nauc_ndcg_at_20_max
      value: 34.647479344052016
    - type: nauc_ndcg_at_20_std
      value: 13.402886235852945
    - type: nauc_ndcg_at_3_diff1
      value: 44.297355376548786
    - type: nauc_ndcg_at_3_max
      value: 35.81339314801316
    - type: nauc_ndcg_at_3_std
      value: 10.823231337841902
    - type: nauc_ndcg_at_5_diff1
      value: 42.800976621550305
    - type: nauc_ndcg_at_5_max
      value: 35.31553747718296
    - type: nauc_ndcg_at_5_std
      value: 12.999770768672233
    - type: nauc_precision_at_1000_diff1
      value: 1.3287822595564707
    - type: nauc_precision_at_1000_max
      value: -7.831380419769612
    - type: nauc_precision_at_1000_std
      value: 22.16155818707822
    - type: nauc_precision_at_100_diff1
      value: 7.9573230301645275
    - type: nauc_precision_at_100_max
      value: 8.250711189680114
    - type: nauc_precision_at_100_std
      value: 27.281502698532794
    - type: nauc_precision_at_10_diff1
      value: 20.32301793773069
    - type: nauc_precision_at_10_max
      value: 26.292089297975213
    - type: nauc_precision_at_10_std
      value: 22.04086433136549
    - type: nauc_precision_at_1_diff1
      value: 47.691221572943014
    - type: nauc_precision_at_1_max
      value: 33.83642419108169
    - type: nauc_precision_at_1_std
      value: 9.150897325122848
    - type: nauc_precision_at_20_diff1
      value: 15.599818198246682
    - type: nauc_precision_at_20_max
      value: 22.892539838177527
    - type: nauc_precision_at_20_std
      value: 25.01036353128196
    - type: nauc_precision_at_3_diff1
      value: 34.886829985942896
    - type: nauc_precision_at_3_max
      value: 35.42710937207887
    - type: nauc_precision_at_3_std
      value: 15.365089091648043
    - type: nauc_precision_at_5_diff1
      value: 28.15586527983956
    - type: nauc_precision_at_5_max
      value: 32.56389381889207
    - type: nauc_precision_at_5_std
      value: 21.509648911296196
    - type: nauc_recall_at_1000_diff1
      value: 26.26755669559851
    - type: nauc_recall_at_1000_max
      value: 47.26359554231266
    - type: nauc_recall_at_1000_std
      value: 49.17271507988052
    - type: nauc_recall_at_100_diff1
      value: 24.907171416372044
    - type: nauc_recall_at_100_max
      value: 31.73666795365669
    - type: nauc_recall_at_100_std
      value: 34.72430395157542
    - type: nauc_recall_at_10_diff1
      value: 31.950390817058445
    - type: nauc_recall_at_10_max
      value: 30.2098918820224
    - type: nauc_recall_at_10_std
      value: 14.899223627845695
    - type: nauc_recall_at_1_diff1
      value: 48.52093859650541
    - type: nauc_recall_at_1_max
      value: 31.75748436789384
    - type: nauc_recall_at_1_std
      value: 6.295511700792233
    - type: nauc_recall_at_20_diff1
      value: 30.085789421997823
    - type: nauc_recall_at_20_max
      value: 31.331626697063587
    - type: nauc_recall_at_20_std
      value: 17.995054512768437
    - type: nauc_recall_at_3_diff1
      value: 40.13064450428089
    - type: nauc_recall_at_3_max
      value: 34.31621377237918
    - type: nauc_recall_at_3_std
      value: 8.678472209664326
    - type: nauc_recall_at_5_diff1
      value: 36.077286485853236
    - type: nauc_recall_at_5_max
      value: 33.299301282489374
    - type: nauc_recall_at_5_std
      value: 13.612662967959412
    - type: ndcg_at_1
      value: 30.237000000000002
    - type: ndcg_at_10
      value: 39.275
    - type: ndcg_at_100
      value: 45.333
    - type: ndcg_at_1000
      value: 48.037
    - type: ndcg_at_20
      value: 41.370000000000005
    - type: ndcg_at_3
      value: 34.64
    - type: ndcg_at_5
      value: 36.909
    - type: precision_at_1
      value: 30.237000000000002
    - type: precision_at_10
      value: 7.371999999999999
    - type: precision_at_100
      value: 1.528
    - type: precision_at_1000
      value: 0.241
    - type: precision_at_20
      value: 4.733
    - type: precision_at_3
      value: 16.073999999999998
    - type: precision_at_5
      value: 11.700000000000001
    - type: recall_at_1
      value: 25.207
    - type: recall_at_10
      value: 49.727
    - type: recall_at_100
      value: 76.936
    - type: recall_at_1000
      value: 94.299
    - type: recall_at_20
      value: 57.589
    - type: recall_at_3
      value: 35.994
    - type: recall_at_5
      value: 42.406
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval (default)
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack-wordpress
    metrics:
    - type: main_score
      value: 32.471
    - type: map_at_1
      value: 19.356
    - type: map_at_10
      value: 27.230999999999998
    - type: map_at_100
      value: 28.081
    - type: map_at_1000
      value: 28.181
    - type: map_at_20
      value: 27.559
    - type: map_at_3
      value: 24.171
    - type: map_at_5
      value: 26.057999999999996
    - type: mrr_at_1
      value: 21.072088724584106
    - type: mrr_at_10
      value: 29.30647243493824
    - type: mrr_at_100
      value: 30.00869418929891
    - type: mrr_at_1000
      value: 30.080405060029037
    - type: mrr_at_20
      value: 29.578807931610335
    - type: mrr_at_3
      value: 26.247689463955638
    - type: mrr_at_5
      value: 28.188539741219966
    - type: nauc_map_at_1000_diff1
      value: 36.02401315504141
    - type: nauc_map_at_1000_max
      value: 31.376220748052575
    - type: nauc_map_at_1000_std
      value: 0.1346247536534226
    - type: nauc_map_at_100_diff1
      value: 35.97288988366299
    - type: nauc_map_at_100_max
      value: 31.37343097714007
    - type: nauc_map_at_100_std
      value: 0.0958351635147478
    - type: nauc_map_at_10_diff1
      value: 36.15899620024802
    - type: nauc_map_at_10_max
      value: 31.361037177575795
    - type: nauc_map_at_10_std
      value: -0.4041283486899738
    - type: nauc_map_at_1_diff1
      value: 45.43410283777835
    - type: nauc_map_at_1_max
      value: 32.58678422458408
    - type: nauc_map_at_1_std
      value: -2.6851172017575133
    - type: nauc_map_at_20_diff1
      value: 35.934404619775286
    - type: nauc_map_at_20_max
      value: 31.31030383249301
    - type: nauc_map_at_20_std
      value: -0.14717896898491972
    - type: nauc_map_at_3_diff1
      value: 37.86423915954705
    - type: nauc_map_at_3_max
      value: 32.2809012047829
    - type: nauc_map_at_3_std
      value: -2.1708148155059592
    - type: nauc_map_at_5_diff1
      value: 36.84265522390141
    - type: nauc_map_at_5_max
      value: 31.37157808476922
    - type: nauc_map_at_5_std
      value: -0.29963826158644064
    - type: nauc_mrr_at_1000_diff1
      value: 36.20544738283434
    - type: nauc_mrr_at_1000_max
      value: 32.30208954588085
    - type: nauc_mrr_at_1000_std
      value: 1.2838715864936316
    - type: nauc_mrr_at_100_diff1
      value: 36.15904411259169
    - type: nauc_mrr_at_100_max
      value: 32.327938256466766
    - type: nauc_mrr_at_100_std
      value: 1.2657067250082925
    - type: nauc_mrr_at_10_diff1
      value: 36.2543779320316
    - type: nauc_mrr_at_10_max
      value: 32.24904810717847
    - type: nauc_mrr_at_10_std
      value: 0.9726935050696278
    - type: nauc_mrr_at_1_diff1
      value: 45.20429144833244
    - type: nauc_mrr_at_1_max
      value: 33.82767894871078
    - type: nauc_mrr_at_1_std
      value: -1.8704335003125725
    - type: nauc_mrr_at_20_diff1
      value: 36.113279457295576
    - type: nauc_mrr_at_20_max
      value: 32.21594845332526
    - type: nauc_mrr_at_20_std
      value: 1.2095516871175558
    - type: nauc_mrr_at_3_diff1
      value: 38.20188328518054
    - type: nauc_mrr_at_3_max
      value: 33.4670227017699
    - type: nauc_mrr_at_3_std
      value: -0.9236814295925724
    - type: nauc_mrr_at_5_diff1
      value: 36.931570063812494
    - type: nauc_mrr_at_5_max
      value: 32.13489737875822
    - type: nauc_mrr_at_5_std
      value: 1.2076368928061894
    - type: nauc_ndcg_at_1000_diff1
      value: 33.10609773784356
    - type: nauc_ndcg_at_1000_max
      value: 31.453190993700264
    - type: nauc_ndcg_at_1000_std
      value: 4.163506021728012
    - type: nauc_ndcg_at_100_diff1
      value: 32.17682816382762
    - type: nauc_ndcg_at_100_max
      value: 31.138666275698608
    - type: nauc_ndcg_at_100_std
      value: 3.479378119538843
    - type: nauc_ndcg_at_10_diff1
      value: 32.36757537451326
    - type: nauc_ndcg_at_10_max
      value: 30.337414154328656
    - type: nauc_ndcg_at_10_std
      value: 1.2414375322956122
    - type: nauc_ndcg_at_1_diff1
      value: 45.20429144833244
    - type: nauc_ndcg_at_1_max
      value: 33.82767894871078
    - type: nauc_ndcg_at_1_std
      value: -1.8704335003125725
    - type: nauc_ndcg_at_20_diff1
      value: 31.63077246604112
    - type: nauc_ndcg_at_20_max
      value: 30.145549351574726
    - type: nauc_ndcg_at_20_std
      value: 2.2258665508440916
    - type: nauc_ndcg_at_3_diff1
      value: 35.7601957137602
    - type: nauc_ndcg_at_3_max
      value: 32.14158639451499
    - type: nauc_ndcg_at_3_std
      value: -1.5690858449662577
    - type: nauc_ndcg_at_5_diff1
      value: 33.96138687625853
    - type: nauc_ndcg_at_5_max
      value: 30.334046334206526
    - type: nauc_ndcg_at_5_std
      value: 1.6084690034355629
    - type: nauc_precision_at_1000_diff1
      value: 0.9129162358156773
    - type: nauc_precision_at_1000_max
      value: 0.31132302385509963
    - type: nauc_precision_at_1000_std
      value: 13.514346244208935
    - type: nauc_precision_at_100_diff1
      value: 9.48976640458681
    - type: nauc_precision_at_100_max
      value: 20.18267841145738
    - type: nauc_precision_at_100_std
      value: 19.747863553039213
    - type: nauc_precision_at_10_diff1
      value: 20.33134020850462
    - type: nauc_precision_at_10_max
      value: 27.91758448136032
    - type: nauc_precision_at_10_std
      value: 8.727850582611723
    - type: nauc_precision_at_1_diff1
      value: 45.20429144833244
    - type: nauc_precision_at_1_max
      value: 33.82767894871078
    - type: nauc_precision_at_1_std
      value: -1.8704335003125725
    - type: nauc_precision_at_20_diff1
      value: 15.896166469695693
    - type: nauc_precision_at_20_max
      value: 25.364993587711677
    - type: nauc_precision_at_20_std
      value: 13.114218169676196
    - type: nauc_precision_at_3_diff1
      value: 29.003771079583746
    - type: nauc_precision_at_3_max
      value: 32.65304146225246
    - type: nauc_precision_at_3_std
      value: 1.1340423196142706
    - type: nauc_precision_at_5_diff1
      value: 25.57516378319094
    - type: nauc_precision_at_5_max
      value: 28.99827810579553
    - type: nauc_precision_at_5_std
      value: 7.945608340859795
    - type: nauc_recall_at_1000_diff1
      value: 17.592328574711598
    - type: nauc_recall_at_1000_max
      value: 36.04732369555508
    - type: nauc_recall_at_1000_std
      value: 37.39190072119301
    - type: nauc_recall_at_100_diff1
      value: 17.82377173461608
    - type: nauc_recall_at_100_max
      value: 28.7134171033536
    - type: nauc_recall_at_100_std
      value: 14.674088397323942
    - type: nauc_recall_at_10_diff1
      value: 20.986778993947823
    - type: nauc_recall_at_10_max
      value: 25.73837718906844
    - type: nauc_recall_at_10_std
      value: 4.164768619671828
    - type: nauc_recall_at_1_diff1
      value: 45.43410283777835
    - type: nauc_recall_at_1_max
      value: 32.58678422458408
    - type: nauc_recall_at_1_std
      value: -2.6851172017575133
    - type: nauc_recall_at_20_diff1
      value: 17.951879051749504
    - type: nauc_recall_at_20_max
      value: 24.485751903899704
    - type: nauc_recall_at_20_std
      value: 7.330820639157978
    - type: nauc_recall_at_3_diff1
      value: 29.347120526930233
    - type: nauc_recall_at_3_max
      value: 30.40588230331169
    - type: nauc_recall_at_3_std
      value: -0.8229385769060911
    - type: nauc_recall_at_5_diff1
      value: 25.655758092986265
    - type: nauc_recall_at_5_max
      value: 26.529657553507846
    - type: nauc_recall_at_5_std
      value: 5.6563620697950405
    - type: ndcg_at_1
      value: 21.072
    - type: ndcg_at_10
      value: 32.471
    - type: ndcg_at_100
      value: 37.183
    - type: ndcg_at_1000
      value: 39.644
    - type: ndcg_at_20
      value: 33.559
    - type: ndcg_at_3
      value: 26.52
    - type: ndcg_at_5
      value: 29.773
    - type: precision_at_1
      value: 21.072
    - type: precision_at_10
      value: 5.396999999999999
    - type: precision_at_100
      value: 0.856
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_20
      value: 2.976
    - type: precision_at_3
      value: 11.522
    - type: precision_at_5
      value: 8.799
    - type: recall_at_1
      value: 19.356
    - type: recall_at_10
      value: 46.636
    - type: recall_at_100
      value: 69.663
    - type: recall_at_1000
      value: 87.789
    - type: recall_at_20
      value: 50.819
    - type: recall_at_3
      value: 30.745
    - type: recall_at_5
      value: 38.558
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER (default)
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: main_score
      value: 28.83
    - type: map_at_1
      value: 11.912
    - type: map_at_10
      value: 20.47
    - type: map_at_100
      value: 22.519
    - type: map_at_1000
      value: 22.723
    - type: map_at_20
      value: 21.597
    - type: map_at_3
      value: 17.14
    - type: map_at_5
      value: 18.784
    - type: mrr_at_1
      value: 26.97068403908795
    - type: mrr_at_10
      value: 38.490486531203146
    - type: mrr_at_100
      value: 39.53396099832615
    - type: mrr_at_1000
      value: 39.57210684594996
    - type: mrr_at_20
      value: 39.15425856866292
    - type: mrr_at_3
      value: 35.11400651465798
    - type: mrr_at_5
      value: 37.045602605863195
    - type: nauc_map_at_1000_diff1
      value: 24.76538935736538
    - type: nauc_map_at_1000_max
      value: 33.971343734250524
    - type: nauc_map_at_1000_std
      value: 15.514286902461812
    - type: nauc_map_at_100_diff1
      value: 24.779729311279336
    - type: nauc_map_at_100_max
      value: 33.919396423104644
    - type: nauc_map_at_100_std
      value: 15.447044791174381
    - type: nauc_map_at_10_diff1
      value: 24.846700880282587
    - type: nauc_map_at_10_max
      value: 33.009555706514895
    - type: nauc_map_at_10_std
      value: 13.466161448314931
    - type: nauc_map_at_1_diff1
      value: 30.77619025618349
    - type: nauc_map_at_1_max
      value: 29.34711506798961
    - type: nauc_map_at_1_std
      value: 5.370506534257179
    - type: nauc_map_at_20_diff1
      value: 24.887170838281627
    - type: nauc_map_at_20_max
      value: 33.417660516280556
    - type: nauc_map_at_20_std
      value: 14.573987916991893
    - type: nauc_map_at_3_diff1
      value: 26.268565940718595
    - type: nauc_map_at_3_max
      value: 31.393759098190273
    - type: nauc_map_at_3_std
      value: 9.903530484775908
    - type: nauc_map_at_5_diff1
      value: 25.92807753940896
    - type: nauc_map_at_5_max
      value: 31.75547205926257
    - type: nauc_map_at_5_std
      value: 11.144523593563873
    - type: nauc_mrr_at_1000_diff1
      value: 21.169799923106503
    - type: nauc_mrr_at_1000_max
      value: 30.197960966240423
    - type: nauc_mrr_at_1000_std
      value: 14.9456013284975
    - type: nauc_mrr_at_100_diff1
      value: 21.163213044565072
    - type: nauc_mrr_at_100_max
      value: 30.203598251460463
    - type: nauc_mrr_at_100_std
      value: 14.965088745621394
    - type: nauc_mrr_at_10_diff1
      value: 21.288223958797573
    - type: nauc_mrr_at_10_max
      value: 30.216972741035725
    - type: nauc_mrr_at_10_std
      value: 14.843389003635199
    - type: nauc_mrr_at_1_diff1
      value: 23.727724539614726
    - type: nauc_mrr_at_1_max
      value: 25.48232837843042
    - type: nauc_mrr_at_1_std
      value: 7.3658686447303365
    - type: nauc_mrr_at_20_diff1
      value: 21.169422189267745
    - type: nauc_mrr_at_20_max
      value: 30.301266953756706
    - type: nauc_mrr_at_20_std
      value: 15.075334986433173
    - type: nauc_mrr_at_3_diff1
      value: 21.196573573020927
    - type: nauc_mrr_at_3_max
      value: 28.977465265081033
    - type: nauc_mrr_at_3_std
      value: 13.332883636713632
    - type: nauc_mrr_at_5_diff1
      value: 21.357024988142246
    - type: nauc_mrr_at_5_max
      value: 29.813915226240674
    - type: nauc_mrr_at_5_std
      value: 14.24321875462318
    - type: nauc_ndcg_at_1000_diff1
      value: 21.61770986869092
    - type: nauc_ndcg_at_1000_max
      value: 36.60187844333304
    - type: nauc_ndcg_at_1000_std
      value: 22.795099112621724
    - type: nauc_ndcg_at_100_diff1
      value: 21.776142474396803
    - type: nauc_ndcg_at_100_max
      value: 36.2414089305107
    - type: nauc_ndcg_at_100_std
      value: 22.4799584915147
    - type: nauc_ndcg_at_10_diff1
      value: 22.481037341715847
    - type: nauc_ndcg_at_10_max
      value: 34.06739169204709
    - type: nauc_ndcg_at_10_std
      value: 17.57021576387562
    - type: nauc_ndcg_at_1_diff1
      value: 23.727724539614726
    - type: nauc_ndcg_at_1_max
      value: 25.48232837843042
    - type: nauc_ndcg_at_1_std
      value: 7.3658686447303365
    - type: nauc_ndcg_at_20_diff1
      value: 22.498496087588748
    - type: nauc_ndcg_at_20_max
      value: 34.892054494351775
    - type: nauc_ndcg_at_20_std
      value: 19.86842474039087
    - type: nauc_ndcg_at_3_diff1
      value: 23.227651070229673
    - type: nauc_ndcg_at_3_max
      value: 30.75938173648469
    - type: nauc_ndcg_at_3_std
      value: 12.463565273811932
    - type: nauc_ndcg_at_5_diff1
      value: 23.799000279668764
    - type: nauc_ndcg_at_5_max
      value: 32.0660491516285
    - type: nauc_ndcg_at_5_std
      value: 13.990017306982494
    - type: nauc_precision_at_1000_diff1
      value: -6.21355360115824
    - type: nauc_precision_at_1000_max
      value: 14.235538664122721
    - type: nauc_precision_at_1000_std
      value: 25.265885010833472
    - type: nauc_precision_at_100_diff1
      value: 0.562403756165029
    - type: nauc_precision_at_100_max
      value: 23.924206050764756
    - type: nauc_precision_at_100_std
      value: 31.338663218741008
    - type: nauc_precision_at_10_diff1
      value: 10.354652757659355
    - type: nauc_precision_at_10_max
      value: 30.758798212425408
    - type: nauc_precision_at_10_std
      value: 26.7031344564241
    - type: nauc_precision_at_1_diff1
      value: 23.727724539614726
    - type: nauc_precision_at_1_max
      value: 25.48232837843042
    - type: nauc_precision_at_1_std
      value: 7.3658686447303365
    - type: nauc_precision_at_20_diff1
      value: 7.953520958455318
    - type: nauc_precision_at_20_max
      value: 27.65892195364336
    - type: nauc_precision_at_20_std
      value: 29.388872379134785
    - type: nauc_precision_at_3_diff1
      value: 16.808332567181218
    - type: nauc_precision_at_3_max
      value: 29.936324350885325
    - type: nauc_precision_at_3_std
      value: 17.73176704168099
    - type: nauc_precision_at_5_diff1
      value: 14.763444123101097
    - type: nauc_precision_at_5_max
      value: 29.010028453553105
    - type: nauc_precision_at_5_std
      value: 20.023906594546354
    - type: nauc_recall_at_1000_diff1
      value: 7.556266790051787
    - type: nauc_recall_at_1000_max
      value: 39.68519315547223
    - type: nauc_recall_at_1000_std
      value: 42.629307490289136
    - type: nauc_recall_at_100_diff1
      value: 11.82811136427535
    - type: nauc_recall_at_100_max
      value: 34.385603696492915
    - type: nauc_recall_at_100_std
      value: 32.712899819080086
    - type: nauc_recall_at_10_diff1
      value: 16.862688054209933
    - type: nauc_recall_at_10_max
      value: 32.3375156464964
    - type: nauc_recall_at_10_std
      value: 20.728901631388972
    - type: nauc_recall_at_1_diff1
      value: 30.77619025618349
    - type: nauc_recall_at_1_max
      value: 29.34711506798961
    - type: nauc_recall_at_1_std
      value: 5.370506534257179
    - type: nauc_recall_at_20_diff1
      value: 16.155103050272285
    - type: nauc_recall_at_20_max
      value: 32.5683721009582
    - type: nauc_recall_at_20_std
      value: 24.833541877340508
    - type: nauc_recall_at_3_diff1
      value: 21.31158530879841
    - type: nauc_recall_at_3_max
      value: 30.2555482302795
    - type: nauc_recall_at_3_std
      value: 12.723641578903559
    - type: nauc_recall_at_5_diff1
      value: 20.646276690604772
    - type: nauc_recall_at_5_max
      value: 30.46478603020548
    - type: nauc_recall_at_5_std
      value: 14.74543343019217
    - type: ndcg_at_1
      value: 26.971
    - type: ndcg_at_10
      value: 28.83
    - type: ndcg_at_100
      value: 36.742000000000004
    - type: ndcg_at_1000
      value: 40.228
    - type: ndcg_at_20
      value: 31.983
    - type: ndcg_at_3
      value: 23.546
    - type: ndcg_at_5
      value: 25.291999999999998
    - type: precision_at_1
      value: 26.971
    - type: precision_at_10
      value: 9.075
    - type: precision_at_100
      value: 1.7500000000000002
    - type: precision_at_1000
      value: 0.24
    - type: precision_at_20
      value: 5.912
    - type: precision_at_3
      value: 17.59
    - type: precision_at_5
      value: 13.485
    - type: recall_at_1
      value: 11.912
    - type: recall_at_10
      value: 34.746
    - type: recall_at_100
      value: 61.869
    - type: recall_at_1000
      value: 81.178
    - type: recall_at_20
      value: 43.575
    - type: recall_at_3
      value: 21.706
    - type: recall_at_5
      value: 26.826
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: dev
      type: mteb/dbpedia
    metrics:
    - type: main_score
      value: 46.941
    - type: map_at_1
      value: 11.128
    - type: map_at_10
      value: 21.468
    - type: map_at_100
      value: 31.257
    - type: map_at_1000
      value: 32.994
    - type: map_at_20
      value: 25.85
    - type: map_at_3
      value: 15.384999999999998
    - type: map_at_5
      value: 17.918
    - type: mrr_at_1
      value: 74.6268656716418
    - type: mrr_at_10
      value: 82.71736555318644
    - type: mrr_at_100
      value: 82.86968222071188
    - type: mrr_at_1000
      value: 82.87289889595635
    - type: mrr_at_20
      value: 82.81686804074863
    - type: mrr_at_3
      value: 82.33830845771143
    - type: mrr_at_5
      value: 82.33830845771143
    - type: nauc_map_at_1000_diff1
      value: 28.205873220137107
    - type: nauc_map_at_1000_max
      value: 32.58677206955515
    - type: nauc_map_at_1000_std
      value: 5.320112182691084
    - type: nauc_map_at_100_diff1
      value: 30.2072705535807
    - type: nauc_map_at_100_max
      value: 31.398441843394203
    - type: nauc_map_at_100_std
      value: 0.3721987672572358
    - type: nauc_map_at_10_diff1
      value: 43.658171592848966
    - type: nauc_map_at_10_max
      value: 20.163715859146205
    - type: nauc_map_at_10_std
      value: -27.377423723665643
    - type: nauc_map_at_1_diff1
      value: 53.67643301898103
    - type: nauc_map_at_1_max
      value: 9.619896030610045
    - type: nauc_map_at_1_std
      value: -39.90622904765458
    - type: nauc_map_at_20_diff1
      value: 37.89256707694639
    - type: nauc_map_at_20_max
      value: 23.572362119543783
    - type: nauc_map_at_20_std
      value: -17.725673906501697
    - type: nauc_map_at_3_diff1
      value: 44.79713521587412
    - type: nauc_map_at_3_max
      value: 11.458612145657254
    - type: nauc_map_at_3_std
      value: -38.4860514263039
    - type: nauc_map_at_5_diff1
      value: 44.27015282190561
    - type: nauc_map_at_5_max
      value: 16.420591916821895
    - type: nauc_map_at_5_std
      value: -32.85173443465263
    - type: nauc_mrr_at_1000_diff1
      value: 40.68406246743924
    - type: nauc_mrr_at_1000_max
      value: 54.557403984682374
    - type: nauc_mrr_at_1000_std
      value: 40.971924667245645
    - type: nauc_mrr_at_100_diff1
      value: 40.68710053046815
    - type: nauc_mrr_at_100_max
      value: 54.561036423251075
    - type: nauc_mrr_at_100_std
      value: 40.97834383095643
    - type: nauc_mrr_at_10_diff1
      value: 41.01499432410833
    - type: nauc_mrr_at_10_max
      value: 54.97000112752338
    - type: nauc_mrr_at_10_std
      value: 41.318724395876444
    - type: nauc_mrr_at_1_diff1
      value: 38.93343855503621
    - type: nauc_mrr_at_1_max
      value: 44.716366048532024
    - type: nauc_mrr_at_1_std
      value: 31.486396303111274
    - type: nauc_mrr_at_20_diff1
      value: 40.64197845924939
    - type: nauc_mrr_at_20_max
      value: 54.6852354691744
    - type: nauc_mrr_at_20_std
      value: 41.1230179065546
    - type: nauc_mrr_at_3_diff1
      value: 40.82958545456673
    - type: nauc_mrr_at_3_max
      value: 55.153817526702355
    - type: nauc_mrr_at_3_std
      value: 41.650161545663664
    - type: nauc_mrr_at_5_diff1
      value: 40.82958545456673
    - type: nauc_mrr_at_5_max
      value: 55.153817526702355
    - type: nauc_mrr_at_5_std
      value: 41.650161545663664
    - type: nauc_ndcg_at_1000_diff1
      value: 23.929983013223506
    - type: nauc_ndcg_at_1000_max
      value: 44.75276524735193
    - type: nauc_ndcg_at_1000_std
      value: 29.517675569258962
    - type: nauc_ndcg_at_100_diff1
      value: 29.624406725667374
    - type: nauc_ndcg_at_100_max
      value: 41.6779897397469
    - type: nauc_ndcg_at_100_std
      value: 13.705531184382655
    - type: nauc_ndcg_at_10_diff1
      value: 31.416257175446887
    - type: nauc_ndcg_at_10_max
      value: 38.589902876894975
    - type: nauc_ndcg_at_10_std
      value: 11.728256480525854
    - type: nauc_ndcg_at_1_diff1
      value: 28.46337552050302
    - type: nauc_ndcg_at_1_max
      value: 38.225886384997445
    - type: nauc_ndcg_at_1_std
      value: 21.338500059461598
    - type: nauc_ndcg_at_20_diff1
      value: 33.256723866450166
    - type: nauc_ndcg_at_20_max
      value: 33.537144781805374
    - type: nauc_ndcg_at_20_std
      value: -0.33743018664631347
    - type: nauc_ndcg_at_3_diff1
      value: 13.969404562448364
    - type: nauc_ndcg_at_3_max
      value: 30.565751196256763
    - type: nauc_ndcg_at_3_std
      value: 17.30174026819281
    - type: nauc_ndcg_at_5_diff1
      value: 18.872272865937877
    - type: nauc_ndcg_at_5_max
      value: 35.263519230922064
    - type: nauc_ndcg_at_5_std
      value: 19.33016308269416
    - type: nauc_precision_at_1000_diff1
      value: -33.04092483049479
    - type: nauc_precision_at_1000_max
      value: 11.49095198021317
    - type: nauc_precision_at_1000_std
      value: 60.12678457700677
    - type: nauc_precision_at_100_diff1
      value: -31.078345270653546
    - type: nauc_precision_at_100_max
      value: 24.725068437496166
    - type: nauc_precision_at_100_std
      value: 67.57419232501738
    - type: nauc_precision_at_10_diff1
      value: -22.292617190022344
    - type: nauc_precision_at_10_max
      value: 24.54113659577851
    - type: nauc_precision_at_10_std
      value: 50.62947534355667
    - type: nauc_precision_at_1_diff1
      value: 38.93343855503621
    - type: nauc_precision_at_1_max
      value: 44.716366048532024
    - type: nauc_precision_at_1_std
      value: 31.486396303111274
    - type: nauc_precision_at_20_diff1
      value: -25.92502457178481
    - type: nauc_precision_at_20_max
      value: 23.621039548137382
    - type: nauc_precision_at_20_std
      value: 52.21318384886264
    - type: nauc_precision_at_3_diff1
      value: -15.971548173967095
    - type: nauc_precision_at_3_max
      value: 24.699430304690164
    - type: nauc_precision_at_3_std
      value: 35.799215461434265
    - type: nauc_precision_at_5_diff1
      value: -19.615035551746058
    - type: nauc_precision_at_5_max
      value: 30.732478067399917
    - type: nauc_precision_at_5_std
      value: 49.57700533096512
    - type: nauc_recall_at_1000_diff1
      value: 2.3453680689225975
    - type: nauc_recall_at_1000_max
      value: 41.49529473708931
    - type: nauc_recall_at_1000_std
      value: 41.33189951068062
    - type: nauc_recall_at_100_diff1
      value: 20.244471165146653
    - type: nauc_recall_at_100_max
      value: 37.4543481569782
    - type: nauc_recall_at_100_std
      value: 7.801110449891264
    - type: nauc_recall_at_10_diff1
      value: 46.105545914294964
    - type: nauc_recall_at_10_max
      value: 21.930607285926236
    - type: nauc_recall_at_10_std
      value: -29.972280971809862
    - type: nauc_recall_at_1_diff1
      value: 53.67643301898103
    - type: nauc_recall_at_1_max
      value: 9.619896030610045
    - type: nauc_recall_at_1_std
      value: -39.90622904765458
    - type: nauc_recall_at_20_diff1
      value: 31.224305541777962
    - type: nauc_recall_at_20_max
      value: 18.835055220233627
    - type: nauc_recall_at_20_std
      value: -23.34247163762115
    - type: nauc_recall_at_3_diff1
      value: 42.73205224851371
    - type: nauc_recall_at_3_max
      value: 9.89768785740234
    - type: nauc_recall_at_3_std
      value: -40.04768970629589
    - type: nauc_recall_at_5_diff1
      value: 43.48392547485277
    - type: nauc_recall_at_5_max
      value: 16.208422216255546
    - type: nauc_recall_at_5_std
      value: -33.79681691846111
    - type: ndcg_at_1
      value: 64.925
    - type: ndcg_at_10
      value: 46.941
    - type: ndcg_at_100
      value: 53.242999999999995
    - type: ndcg_at_1000
      value: 60.87200000000001
    - type: ndcg_at_20
      value: 47.138999999999996
    - type: ndcg_at_3
      value: 54.533
    - type: ndcg_at_5
      value: 50.536
    - type: precision_at_1
      value: 74.627
    - type: precision_at_10
      value: 34.477999999999994
    - type: precision_at_100
      value: 10.776
    - type: precision_at_1000
      value: 1.737
    - type: precision_at_20
      value: 26.939999999999998
    - type: precision_at_3
      value: 53.234
    - type: precision_at_5
      value: 45.074999999999996
    - type: recall_at_1
      value: 11.128
    - type: recall_at_10
      value: 27.354
    - type: recall_at_100
      value: 60.211999999999996
    - type: recall_at_1000
      value: 84.485
    - type: recall_at_20
      value: 38.645
    - type: recall_at_3
      value: 16.72
    - type: recall_at_5
      value: 20.648
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: main_score
      value: 40.463
    - type: map_at_1
      value: 9.029
    - type: map_at_10
      value: 19.262999999999998
    - type: map_at_100
      value: 27.32
    - type: map_at_1000
      value: 28.898000000000003
    - type: map_at_20
      value: 22.285
    - type: map_at_3
      value: 13.741999999999999
    - type: map_at_5
      value: 16.184
    - type: mrr_at_1
      value: 66.5
    - type: mrr_at_10
      value: 74.58015873015873
    - type: mrr_at_100
      value: 74.90889577505533
    - type: mrr_at_1000
      value: 74.91723981152577
    - type: mrr_at_20
      value: 74.81400519415226
    - type: mrr_at_3
      value: 72.75
    - type: mrr_at_5
      value: 74.0125
    - type: nauc_map_at_1000_diff1
      value: 18.09558210846325
    - type: nauc_map_at_1000_max
      value: 23.2203289549629
    - type: nauc_map_at_1000_std
      value: 26.956962795986172
    - type: nauc_map_at_100_diff1
      value: 19.26318278180542
    - type: nauc_map_at_100_max
      value: 21.385042416697452
    - type: nauc_map_at_100_std
      value: 24.102985219136333
    - type: nauc_map_at_10_diff1
      value: 23.01034372544496
    - type: nauc_map_at_10_max
      value: 10.878304152216096
    - type: nauc_map_at_10_std
      value: 2.362436293740753
    - type: nauc_map_at_1_diff1
      value: 37.366256622356744
    - type: nauc_map_at_1_max
      value: 3.3385920525541053
    - type: nauc_map_at_1_std
      value: -13.380038032859368
    - type: nauc_map_at_20_diff1
      value: 21.282079555449165
    - type: nauc_map_at_20_max
      value: 14.770333252524978
    - type: nauc_map_at_20_std
      value: 10.07082791626879
    - type: nauc_map_at_3_diff1
      value: 27.510938193340262
    - type: nauc_map_at_3_max
      value: 4.965379678339785
    - type: nauc_map_at_3_std
      value: -8.210306316829763
    - type: nauc_map_at_5_diff1
      value: 25.261898710191527
    - type: nauc_map_at_5_max
      value: 6.767168819826101
    - type: nauc_map_at_5_std
      value: -4.755049267878645
    - type: nauc_mrr_at_1000_diff1
      value: 43.97215491866585
    - type: nauc_mrr_at_1000_max
      value: 57.2564604463254
    - type: nauc_mrr_at_1000_std
      value: 37.52158604598497
    - type: nauc_mrr_at_100_diff1
      value: 43.9520395412017
    - type: nauc_mrr_at_100_max
      value: 57.25472510851986
    - type: nauc_mrr_at_100_std
      value: 37.512313370242985
    - type: nauc_mrr_at_10_diff1
      value: 44.149055538533176
    - type: nauc_mrr_at_10_max
      value: 57.33498205903583
    - type: nauc_mrr_at_10_std
      value: 37.47474466090973
    - type: nauc_mrr_at_1_diff1
      value: 47.2190330933805
    - type: nauc_mrr_at_1_max
      value: 54.17417392251676
    - type: nauc_mrr_at_1_std
      value: 32.26038934374714
    - type: nauc_mrr_at_20_diff1
      value: 43.968230171527594
    - type: nauc_mrr_at_20_max
      value: 57.29041263736231
    - type: nauc_mrr_at_20_std
      value: 37.544977698244445
    - type: nauc_mrr_at_3_diff1
      value: 43.34027046577654
    - type: nauc_mrr_at_3_max
      value: 56.66557913521474
    - type: nauc_mrr_at_3_std
      value: 38.76901326294043
    - type: nauc_mrr_at_5_diff1
      value: 44.12604461577999
    - type: nauc_mrr_at_5_max
      value: 57.612606984606195
    - type: nauc_mrr_at_5_std
      value: 37.82836737434154
    - type: nauc_ndcg_at_1000_diff1
      value: 17.44988479317236
    - type: nauc_ndcg_at_1000_max
      value: 37.7482696046901
    - type: nauc_ndcg_at_1000_std
      value: 38.65638419071411
    - type: nauc_ndcg_at_100_diff1
      value: 19.507315827241328
    - type: nauc_ndcg_at_100_max
      value: 30.400138333090588
    - type: nauc_ndcg_at_100_std
      value: 31.113058945606742
    - type: nauc_ndcg_at_10_diff1
      value: 20.815636696375392
    - type: nauc_ndcg_at_10_max
      value: 33.68288613631258
    - type: nauc_ndcg_at_10_std
      value: 29.671362930314803
    - type: nauc_ndcg_at_1_diff1
      value: 38.11376341528132
    - type: nauc_ndcg_at_1_max
      value: 44.403414549347204
    - type: nauc_ndcg_at_1_std
      value: 25.52384786407678
    - type: nauc_ndcg_at_20_diff1
      value: 20.918758451069003
    - type: nauc_ndcg_at_20_max
      value: 30.06195313262468
    - type: nauc_ndcg_at_20_std
      value: 26.54741096206399
    - type: nauc_ndcg_at_3_diff1
      value: 24.372445814427298
    - type: nauc_ndcg_at_3_max
      value: 37.527105863035004
    - type: nauc_ndcg_at_3_std
      value: 29.627357113821652
    - type: nauc_ndcg_at_5_diff1
      value: 22.24317304883715
    - type: nauc_ndcg_at_5_max
      value: 36.01451546088971
    - type: nauc_ndcg_at_5_std
      value: 29.681491475278758
    - type: nauc_precision_at_1000_diff1
      value: -16.787088918126038
    - type: nauc_precision_at_1000_max
      value: 7.469815188782062
    - type: nauc_precision_at_1000_std
      value: 20.347279526863016
    - type: nauc_precision_at_100_diff1
      value: -7.767846738327802
    - type: nauc_precision_at_100_max
      value: 29.03244278470077
    - type: nauc_precision_at_100_std
      value: 46.382880462091606
    - type: nauc_precision_at_10_diff1
      value: -0.5232913303652262
    - type: nauc_precision_at_10_max
      value: 38.64476507974731
    - type: nauc_precision_at_10_std
      value: 47.74014794238241
    - type: nauc_precision_at_1_diff1
      value: 47.2190330933805
    - type: nauc_precision_at_1_max
      value: 54.17417392251676
    - type: nauc_precision_at_1_std
      value: 32.26038934374714
    - type: nauc_precision_at_20_diff1
      value: -2.1834578501338147
    - type: nauc_precision_at_20_max
      value: 35.998198621553904
    - type: nauc_precision_at_20_std
      value: 48.111771749288465
    - type: nauc_precision_at_3_diff1
      value: 10.263223401237676
    - type: nauc_precision_at_3_max
      value: 38.014854436938116
    - type: nauc_precision_at_3_std
      value: 38.4358555773606
    - type: nauc_precision_at_5_diff1
      value: 4.413009169159884
    - type: nauc_precision_at_5_max
      value: 39.10496606345797
    - type: nauc_precision_at_5_std
      value: 42.78105363038704
    - type: nauc_recall_at_1000_diff1
      value: 5.614459025569145
    - type: nauc_recall_at_1000_max
      value: 30.609110099594243
    - type: nauc_recall_at_1000_std
      value: 41.7665129006611
    - type: nauc_recall_at_100_diff1
      value: 11.30144179728448
    - type: nauc_recall_at_100_max
      value: 16.59742852717951
    - type: nauc_recall_at_100_std
      value: 24.50296358615415
    - type: nauc_recall_at_10_diff1
      value: 16.490149625173352
    - type: nauc_recall_at_10_max
      value: 3.832770249980029
    - type: nauc_recall_at_10_std
      value: -2.374496776149457
    - type: nauc_recall_at_1_diff1
      value: 37.366256622356744
    - type: nauc_recall_at_1_max
      value: 3.3385920525541053
    - type: nauc_recall_at_1_std
      value: -13.380038032859368
    - type: nauc_recall_at_20_diff1
      value: 15.292191881271883
    - type: nauc_recall_at_20_max
      value: 8.415679565455628
    - type: nauc_recall_at_20_std
      value: 5.074936206972553
    - type: nauc_recall_at_3_diff1
      value: 24.152242185735222
    - type: nauc_recall_at_3_max
      value: 1.506727274505061
    - type: nauc_recall_at_3_std
      value: -10.019411125629754
    - type: nauc_recall_at_5_diff1
      value: 21.7463835872855
    - type: nauc_recall_at_5_max
      value: 2.645640036075683
    - type: nauc_recall_at_5_std
      value: -7.864417712754525
    - type: ndcg_at_1
      value: 54.625
    - type: ndcg_at_10
      value: 40.463
    - type: ndcg_at_100
      value: 45.693
    - type: ndcg_at_1000
      value: 53.21900000000001
    - type: ndcg_at_20
      value: 39.948
    - type: ndcg_at_3
      value: 44.546
    - type: ndcg_at_5
      value: 42.370000000000005
    - type: precision_at_1
      value: 66.5
    - type: precision_at_10
      value: 31.724999999999998
    - type: precision_at_100
      value: 10.308
    - type: precision_at_1000
      value: 2.015
    - type: precision_at_20
      value: 24.013
    - type: precision_at_3
      value: 47.5
    - type: precision_at_5
      value: 40.8
    - type: recall_at_1
      value: 9.029
    - type: recall_at_10
      value: 25.064999999999998
    - type: recall_at_100
      value: 52.578
    - type: recall_at_1000
      value: 76.43100000000001
    - type: recall_at_20
      value: 32.012
    - type: recall_at_3
      value: 15.046000000000001
    - type: recall_at_5
      value: 19.012
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 50.815
    - type: f1
      value: 44.094634894021816
    - type: f1_weighted
      value: 52.60818465807737
    - type: main_score
      value: 50.815
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: validation
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 50.25999999999999
    - type: f1
      value: 44.29688695357058
    - type: f1_weighted
      value: 51.782894585455274
    - type: main_score
      value: 50.25999999999999
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FEVER (default)
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: dev
      type: mteb/fever
    metrics:
    - type: main_score
      value: 86.581
    - type: map_at_1
      value: 74.727
    - type: map_at_10
      value: 82.856
    - type: map_at_100
      value: 83.08
    - type: map_at_1000
      value: 83.095
    - type: map_at_20
      value: 82.98
    - type: map_at_3
      value: 81.874
    - type: map_at_5
      value: 82.528
    - type: mrr_at_1
      value: 81.11311131113112
    - type: mrr_at_10
      value: 88.08008777068184
    - type: mrr_at_100
      value: 88.15267896396102
    - type: mrr_at_1000
      value: 88.15440036957291
    - type: mrr_at_20
      value: 88.12826180824881
    - type: mrr_at_3
      value: 87.42624262426241
    - type: mrr_at_5
      value: 87.90179017901791
    - type: nauc_map_at_1000_diff1
      value: 50.36356059540196
    - type: nauc_map_at_1000_max
      value: 23.9992915254945
    - type: nauc_map_at_1000_std
      value: -5.351570096789122
    - type: nauc_map_at_100_diff1
      value: 50.32379212854651
    - type: nauc_map_at_100_max
      value: 23.98098961038551
    - type: nauc_map_at_100_std
      value: -5.348874939403815
    - type: nauc_map_at_10_diff1
      value: 49.99523888098324
    - type: nauc_map_at_10_max
      value: 23.709118817821636
    - type: nauc_map_at_10_std
      value: -5.655330318910658
    - type: nauc_map_at_1_diff1
      value: 54.8096391515275
    - type: nauc_map_at_1_max
      value: 20.61234382722085
    - type: nauc_map_at_1_std
      value: -7.831309271791796
    - type: nauc_map_at_20_diff1
      value: 50.19276270347539
    - type: nauc_map_at_20_max
      value: 23.8325417359291
    - type: nauc_map_at_20_std
      value: -5.4936298430989
    - type: nauc_map_at_3_diff1
      value: 50.28796474395995
    - type: nauc_map_at_3_max
      value: 23.45783355551859
    - type: nauc_map_at_3_std
      value: -6.885753631015993
    - type: nauc_map_at_5_diff1
      value: 49.96283216222825
    - type: nauc_map_at_5_max
      value: 23.555049015922823
    - type: nauc_map_at_5_std
      value: -6.090659860215219
    - type: nauc_mrr_at_1000_diff1
      value: 69.17421533744194
    - type: nauc_mrr_at_1000_max
      value: 33.02158730991583
    - type: nauc_mrr_at_1000_std
      value: -8.948358014186812
    - type: nauc_mrr_at_100_diff1
      value: 69.17553004498271
    - type: nauc_mrr_at_100_max
      value: 33.028331950038684
    - type: nauc_mrr_at_100_std
      value: -8.942802854470754
    - type: nauc_mrr_at_10_diff1
      value: 69.13328163893561
    - type: nauc_mrr_at_10_max
      value: 33.18335904223495
    - type: nauc_mrr_at_10_std
      value: -8.89478907359742
    - type: nauc_mrr_at_1_diff1
      value: 69.59435273515031
    - type: nauc_mrr_at_1_max
      value: 28.41439149035527
    - type: nauc_mrr_at_1_std
      value: -9.895055694379428
    - type: nauc_mrr_at_20_diff1
      value: 69.19362398254414
    - type: nauc_mrr_at_20_max
      value: 33.09302969870915
    - type: nauc_mrr_at_20_std
      value: -8.903618952902336
    - type: nauc_mrr_at_3_diff1
      value: 69.03641198083353
    - type: nauc_mrr_at_3_max
      value: 33.689976336215125
    - type: nauc_mrr_at_3_std
      value: -9.53929739319604
    - type: nauc_mrr_at_5_diff1
      value: 69.03744477223476
    - type: nauc_mrr_at_5_max
      value: 33.343224412356946
    - type: nauc_mrr_at_5_std
      value: -9.107354899986388
    - type: nauc_ndcg_at_1000_diff1
      value: 52.37043460910987
    - type: nauc_ndcg_at_1000_max
      value: 26.868515910590585
    - type: nauc_ndcg_at_1000_std
      value: -3.8173698040799926
    - type: nauc_ndcg_at_100_diff1
      value: 51.59304592952214
    - type: nauc_ndcg_at_100_max
      value: 26.582916315809957
    - type: nauc_ndcg_at_100_std
      value: -3.507246327999668
    - type: nauc_ndcg_at_10_diff1
      value: 50.56748641091843
    - type: nauc_ndcg_at_10_max
      value: 25.937839511946397
    - type: nauc_ndcg_at_10_std
      value: -4.317117533070399
    - type: nauc_ndcg_at_1_diff1
      value: 69.59435273515031
    - type: nauc_ndcg_at_1_max
      value: 28.41439149035527
    - type: nauc_ndcg_at_1_std
      value: -9.895055694379428
    - type: nauc_ndcg_at_20_diff1
      value: 51.07942544100161
    - type: nauc_ndcg_at_20_max
      value: 26.079691268086176
    - type: nauc_ndcg_at_20_std
      value: -3.9867583589809534
    - type: nauc_ndcg_at_3_diff1
      value: 52.08099666063276
    - type: nauc_ndcg_at_3_max
      value: 26.743415311234692
    - type: nauc_ndcg_at_3_std
      value: -6.45797306431994
    - type: nauc_ndcg_at_5_diff1
      value: 50.763723596631735
    - type: nauc_ndcg_at_5_max
      value: 26.016889338180306
    - type: nauc_ndcg_at_5_std
      value: -5.248574264404534
    - type: nauc_precision_at_1000_diff1
      value: -5.387965863532961
    - type: nauc_precision_at_1000_max
      value: 10.372523367921854
    - type: nauc_precision_at_1000_std
      value: 13.415209647969087
    - type: nauc_precision_at_100_diff1
      value: -5.685856344844705
    - type: nauc_precision_at_100_max
      value: 13.882370685075996
    - type: nauc_precision_at_100_std
      value: 17.947725196159116
    - type: nauc_precision_at_10_diff1
      value: 1.4713194150281539
    - type: nauc_precision_at_10_max
      value: 20.264317861307276
    - type: nauc_precision_at_10_std
      value: 12.524533346684677
    - type: nauc_precision_at_1_diff1
      value: 69.59435273515031
    - type: nauc_precision_at_1_max
      value: 28.41439149035527
    - type: nauc_precision_at_1_std
      value: -9.895055694379428
    - type: nauc_precision_at_20_diff1
      value: -1.040212171206397
    - type: nauc_precision_at_20_max
      value: 17.76967921210208
    - type: nauc_precision_at_20_std
      value: 15.86703101590195
    - type: nauc_precision_at_3_diff1
      value: 27.397567762305414
    - type: nauc_precision_at_3_max
      value: 29.983353547368306
    - type: nauc_precision_at_3_std
      value: -2.024560146034635
    - type: nauc_precision_at_5_diff1
      value: 11.978185255474472
    - type: nauc_precision_at_5_max
      value: 25.336475474417213
    - type: nauc_precision_at_5_std
      value: 6.079864267936165
    - type: nauc_recall_at_1000_diff1
      value: 5.978402010181869
    - type: nauc_recall_at_1000_max
      value: 26.578352090329005
    - type: nauc_recall_at_1000_std
      value: 31.804174323172713
    - type: nauc_recall_at_100_diff1
      value: 9.67678765671401
    - type: nauc_recall_at_100_max
      value: 21.918365367812797
    - type: nauc_recall_at_100_std
      value: 24.820139168438597
    - type: nauc_recall_at_10_diff1
      value: 21.60125165788751
    - type: nauc_recall_at_10_max
      value: 21.565110839293144
    - type: nauc_recall_at_10_std
      value: 8.449173954921543
    - type: nauc_recall_at_1_diff1
      value: 54.8096391515275
    - type: nauc_recall_at_1_max
      value: 20.61234382722085
    - type: nauc_recall_at_1_std
      value: -7.831309271791796
    - type: nauc_recall_at_20_diff1
      value: 19.681237121526223
    - type: nauc_recall_at_20_max
      value: 20.77874943741462
    - type: nauc_recall_at_20_std
      value: 12.46872212646974
    - type: nauc_recall_at_3_diff1
      value: 35.25648317456749
    - type: nauc_recall_at_3_max
      value: 24.513936377413255
    - type: nauc_recall_at_3_std
      value: -3.46424213085049
    - type: nauc_recall_at_5_diff1
      value: 27.636657051463775
    - type: nauc_recall_at_5_max
      value: 22.76892845457896
    - type: nauc_recall_at_5_std
      value: 1.819321132167595
    - type: ndcg_at_1
      value: 81.113
    - type: ndcg_at_10
      value: 86.581
    - type: ndcg_at_100
      value: 87.37700000000001
    - type: ndcg_at_1000
      value: 87.634
    - type: ndcg_at_20
      value: 86.90299999999999
    - type: ndcg_at_3
      value: 85.126
    - type: ndcg_at_5
      value: 85.992
    - type: precision_at_1
      value: 81.113
    - type: precision_at_10
      value: 10.35
    - type: precision_at_100
      value: 1.102
    - type: precision_at_1000
      value: 0.11399999999999999
    - type: precision_at_20
      value: 5.281000000000001
    - type: precision_at_3
      value: 32.543
    - type: precision_at_5
      value: 20.150000000000002
    - type: recall_at_1
      value: 74.727
    - type: recall_at_10
      value: 92.93
    - type: recall_at_100
      value: 96.122
    - type: recall_at_1000
      value: 97.722
    - type: recall_at_20
      value: 94.038
    - type: recall_at_3
      value: 88.785
    - type: recall_at_5
      value: 91.143
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FEVER (default)
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: main_score
      value: 85.319
    - type: map_at_1
      value: 72.161
    - type: map_at_10
      value: 81.238
    - type: map_at_100
      value: 81.46
    - type: map_at_1000
      value: 81.473
    - type: map_at_20
      value: 81.365
    - type: map_at_3
      value: 80.01599999999999
    - type: map_at_5
      value: 80.857
    - type: mrr_at_1
      value: 77.93279327932792
    - type: mrr_at_10
      value: 85.94110601536343
    - type: mrr_at_100
      value: 86.02247464267394
    - type: mrr_at_1000
      value: 86.02424083776694
    - type: mrr_at_20
      value: 85.99713844897458
    - type: mrr_at_3
      value: 85.10351035103511
    - type: mrr_at_5
      value: 85.74182418241824
    - type: nauc_map_at_1000_diff1
      value: 48.87942532850865
    - type: nauc_map_at_1000_max
      value: 19.207999873933872
    - type: nauc_map_at_1000_std
      value: -6.426739011393975
    - type: nauc_map_at_100_diff1
      value: 48.844165528106586
    - type: nauc_map_at_100_max
      value: 19.19923211737889
    - type: nauc_map_at_100_std
      value: -6.413953838280856
    - type: nauc_map_at_10_diff1
      value: 48.66909865150514
    - type: nauc_map_at_10_max
      value: 19.08422286721995
    - type: nauc_map_at_10_std
      value: -6.550612019706119
    - type: nauc_map_at_1_diff1
      value: 52.38347452384079
    - type: nauc_map_at_1_max
      value: 15.321152180069644
    - type: nauc_map_at_1_std
      value: -9.404483536334594
    - type: nauc_map_at_20_diff1
      value: 48.75447470976026
    - type: nauc_map_at_20_max
      value: 19.146566952856375
    - type: nauc_map_at_20_std
      value: -6.433993868501403
    - type: nauc_map_at_3_diff1
      value: 48.848389883387796
    - type: nauc_map_at_3_max
      value: 18.375903836766348
    - type: nauc_map_at_3_std
      value: -8.115547043380014
    - type: nauc_map_at_5_diff1
      value: 48.45908591701036
    - type: nauc_map_at_5_max
      value: 18.91547083095089
    - type: nauc_map_at_5_std
      value: -7.0216129648180345
    - type: nauc_mrr_at_1000_diff1
      value: 61.86764697591185
    - type: nauc_mrr_at_1000_max
      value: 23.37259724729802
    - type: nauc_mrr_at_1000_std
      value: -11.240785012446858
    - type: nauc_mrr_at_100_diff1
      value: 61.86299894038223
    - type: nauc_mrr_at_100_max
      value: 23.377993723874425
    - type: nauc_mrr_at_100_std
      value: -11.234547507145425
    - type: nauc_mrr_at_10_diff1
      value: 61.89745030747914
    - type: nauc_mrr_at_10_max
      value: 23.51179181879897
    - type: nauc_mrr_at_10_std
      value: -11.21542754410092
    - type: nauc_mrr_at_1_diff1
      value: 62.87718289404487
    - type: nauc_mrr_at_1_max
      value: 20.036585845650016
    - type: nauc_mrr_at_1_std
      value: -11.824468808796672
    - type: nauc_mrr_at_20_diff1
      value: 61.87965159241426
    - type: nauc_mrr_at_20_max
      value: 23.46555093254262
    - type: nauc_mrr_at_20_std
      value: -11.184929381359039
    - type: nauc_mrr_at_3_diff1
      value: 61.96154941592062
    - type: nauc_mrr_at_3_max
      value: 23.30622207138397
    - type: nauc_mrr_at_3_std
      value: -12.526039371134765
    - type: nauc_mrr_at_5_diff1
      value: 61.71707334295513
    - type: nauc_mrr_at_5_max
      value: 23.5270336630759
    - type: nauc_mrr_at_5_std
      value: -11.623135779913035
    - type: nauc_ndcg_at_1000_diff1
      value: 50.409731512636114
    - type: nauc_ndcg_at_1000_max
      value: 21.65102021635264
    - type: nauc_ndcg_at_1000_std
      value: -4.92217385213998
    - type: nauc_ndcg_at_100_diff1
      value: 49.61567352404278
    - type: nauc_ndcg_at_100_max
      value: 21.66920626618109
    - type: nauc_ndcg_at_100_std
      value: -4.449124212637381
    - type: nauc_ndcg_at_10_diff1
      value: 48.92696345322944
    - type: nauc_ndcg_at_10_max
      value: 21.43134916536533
    - type: nauc_ndcg_at_10_std
      value: -4.875245880370844
    - type: nauc_ndcg_at_1_diff1
      value: 62.87718289404487
    - type: nauc_ndcg_at_1_max
      value: 20.036585845650016
    - type: nauc_ndcg_at_1_std
      value: -11.824468808796672
    - type: nauc_ndcg_at_20_diff1
      value: 49.11732939114983
    - type: nauc_ndcg_at_20_max
      value: 21.599262409124997
    - type: nauc_ndcg_at_20_std
      value: -4.420171263096915
    - type: nauc_ndcg_at_3_diff1
      value: 50.45116917733788
    - type: nauc_ndcg_at_3_max
      value: 20.80003117781856
    - type: nauc_ndcg_at_3_std
      value: -8.452770588263899
    - type: nauc_ndcg_at_5_diff1
      value: 48.748106275538724
    - type: nauc_ndcg_at_5_max
      value: 21.211994383559222
    - type: nauc_ndcg_at_5_std
      value: -6.225634212256297
    - type: nauc_precision_at_1000_diff1
      value: -2.65994713494688
    - type: nauc_precision_at_1000_max
      value: 9.355224820997055
    - type: nauc_precision_at_1000_std
      value: 6.93245511496358
    - type: nauc_precision_at_100_diff1
      value: -4.855736259082823
    - type: nauc_precision_at_100_max
      value: 13.36331723677647
    - type: nauc_precision_at_100_std
      value: 11.902586270338599
    - type: nauc_precision_at_10_diff1
      value: 3.216750400462425
    - type: nauc_precision_at_10_max
      value: 21.25636976697531
    - type: nauc_precision_at_10_std
      value: 12.137963028905675
    - type: nauc_precision_at_1_diff1
      value: 62.87718289404487
    - type: nauc_precision_at_1_max
      value: 20.036585845650016
    - type: nauc_precision_at_1_std
      value: -11.824468808796672
    - type: nauc_precision_at_20_diff1
      value: -1.4118811423454232
    - type: nauc_precision_at_20_max
      value: 18.692537535200373
    - type: nauc_precision_at_20_std
      value: 14.30532206890571
    - type: nauc_precision_at_3_diff1
      value: 30.339371349812698
    - type: nauc_precision_at_3_max
      value: 26.408309865804767
    - type: nauc_precision_at_3_std
      value: -4.0916660664063365
    - type: nauc_precision_at_5_diff1
      value: 12.879323748381793
    - type: nauc_precision_at_5_max
      value: 25.69174163377847
    - type: nauc_precision_at_5_std
      value: 6.093421699798719
    - type: nauc_recall_at_1000_diff1
      value: 12.273439585549289
    - type: nauc_recall_at_1000_max
      value: 36.35356580077124
    - type: nauc_recall_at_1000_std
      value: 48.56058221377234
    - type: nauc_recall_at_100_diff1
      value: 11.024787894935523
    - type: nauc_recall_at_100_max
      value: 32.31032622508141
    - type: nauc_recall_at_100_std
      value: 37.7793363899341
    - type: nauc_recall_at_10_diff1
      value: 23.70968015354158
    - type: nauc_recall_at_10_max
      value: 26.928818056185793
    - type: nauc_recall_at_10_std
      value: 15.603934216247126
    - type: nauc_recall_at_1_diff1
      value: 52.38347452384079
    - type: nauc_recall_at_1_max
      value: 15.321152180069644
    - type: nauc_recall_at_1_std
      value: -9.404483536334594
    - type: nauc_recall_at_20_diff1
      value: 19.803465715185133
    - type: nauc_recall_at_20_max
      value: 29.156847915934563
    - type: nauc_recall_at_20_std
      value: 23.60980197996787
    - type: nauc_recall_at_3_diff1
      value: 36.64320565102789
    - type: nauc_recall_at_3_max
      value: 21.36937034204157
    - type: nauc_recall_at_3_std
      value: -4.728003775515406
    - type: nauc_recall_at_5_diff1
      value: 27.617739447790917
    - type: nauc_recall_at_5_max
      value: 24.241178855068966
    - type: nauc_recall_at_5_std
      value: 4.7483438956009385
    - type: ndcg_at_1
      value: 77.93299999999999
    - type: ndcg_at_10
      value: 85.319
    - type: ndcg_at_100
      value: 86.13300000000001
    - type: ndcg_at_1000
      value: 86.378
    - type: ndcg_at_20
      value: 85.668
    - type: ndcg_at_3
      value: 83.41
    - type: ndcg_at_5
      value: 84.61999999999999
    - type: precision_at_1
      value: 77.93299999999999
    - type: precision_at_10
      value: 10.318
    - type: precision_at_100
      value: 1.095
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_20
      value: 5.2620000000000005
    - type: precision_at_3
      value: 32.063
    - type: precision_at_5
      value: 20.009
    - type: recall_at_1
      value: 72.161
    - type: recall_at_10
      value: 93.195
    - type: recall_at_100
      value: 96.455
    - type: recall_at_1000
      value: 97.98400000000001
    - type: recall_at_20
      value: 94.405
    - type: recall_at_3
      value: 88.061
    - type: recall_at_5
      value: 91.149
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FEVER (default)
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: train
      type: mteb/fever
    metrics:
    - type: main_score
      value: 86.26899999999999
    - type: map_at_1
      value: 72.449
    - type: map_at_10
      value: 82.03
    - type: map_at_100
      value: 82.296
    - type: map_at_1000
      value: 82.314
    - type: map_at_20
      value: 82.186
    - type: map_at_3
      value: 80.83500000000001
    - type: map_at_5
      value: 81.623
    - type: mrr_at_1
      value: 80.61287678717785
    - type: mrr_at_10
      value: 88.20712760713671
    - type: mrr_at_100
      value: 88.2553288872469
    - type: mrr_at_1000
      value: 88.2557710463964
    - type: mrr_at_20
      value: 88.24322934725306
    - type: mrr_at_3
      value: 87.53498467049145
    - type: mrr_at_5
      value: 88.02728956075644
    - type: nauc_map_at_1000_diff1
      value: 39.95106411898475
    - type: nauc_map_at_1000_max
      value: 9.654728508229924
    - type: nauc_map_at_1000_std
      value: -12.151917182587324
    - type: nauc_map_at_100_diff1
      value: 39.90468852636486
    - type: nauc_map_at_100_max
      value: 9.63167786931566
    - type: nauc_map_at_100_std
      value: -12.13835017665434
    - type: nauc_map_at_10_diff1
      value: 39.46904405606303
    - type: nauc_map_at_10_max
      value: 9.325543240387914
    - type: nauc_map_at_10_std
      value: -12.262834163465582
    - type: nauc_map_at_1_diff1
      value: 45.26755146712848
    - type: nauc_map_at_1_max
      value: 7.630523437842046
    - type: nauc_map_at_1_std
      value: -13.605176488921838
    - type: nauc_map_at_20_diff1
      value: 39.66853756850951
    - type: nauc_map_at_20_max
      value: 9.466678245833826
    - type: nauc_map_at_20_std
      value: -12.1759657705622
    - type: nauc_map_at_3_diff1
      value: 39.50530889629205
    - type: nauc_map_at_3_max
      value: 8.935845976271647
    - type: nauc_map_at_3_std
      value: -13.490923397297127
    - type: nauc_map_at_5_diff1
      value: 39.30464767323601
    - type: nauc_map_at_5_max
      value: 9.171957030191257
    - type: nauc_map_at_5_std
      value: -12.606276076261402
    - type: nauc_mrr_at_1000_diff1
      value: 61.318394082054084
    - type: nauc_mrr_at_1000_max
      value: 13.942830061515366
    - type: nauc_mrr_at_1000_std
      value: -23.553800119123004
    - type: nauc_mrr_at_100_diff1
      value: 61.31872034357897
    - type: nauc_mrr_at_100_max
      value: 13.94419608612362
    - type: nauc_mrr_at_100_std
      value: -23.553055204470468
    - type: nauc_mrr_at_10_diff1
      value: 61.31278822068778
    - type: nauc_mrr_at_10_max
      value: 14.031207581756833
    - type: nauc_mrr_at_10_std
      value: -23.584266855456125
    - type: nauc_mrr_at_1_diff1
      value: 62.02492634987989
    - type: nauc_mrr_at_1_max
      value: 12.426103478237204
    - type: nauc_mrr_at_1_std
      value: -21.462128885638194
    - type: nauc_mrr_at_20_diff1
      value: 61.315947046589194
    - type: nauc_mrr_at_20_max
      value: 13.974382096839708
    - type: nauc_mrr_at_20_std
      value: -23.54265969965065
    - type: nauc_mrr_at_3_diff1
      value: 61.15068247478852
    - type: nauc_mrr_at_3_max
      value: 14.166286324555182
    - type: nauc_mrr_at_3_std
      value: -24.539638368220956
    - type: nauc_mrr_at_5_diff1
      value: 61.27021769164674
    - type: nauc_mrr_at_5_max
      value: 14.18154187157247
    - type: nauc_mrr_at_5_std
      value: -23.86452902597003
    - type: nauc_ndcg_at_1000_diff1
      value: 42.33233119047479
    - type: nauc_ndcg_at_1000_max
      value: 11.565331883315682
    - type: nauc_ndcg_at_1000_std
      value: -12.178748604304223
    - type: nauc_ndcg_at_100_diff1
      value: 41.37693942834703
    - type: nauc_ndcg_at_100_max
      value: 11.328077098906448
    - type: nauc_ndcg_at_100_std
      value: -11.65003452480089
    - type: nauc_ndcg_at_10_diff1
      value: 39.766907902897806
    - type: nauc_ndcg_at_10_max
      value: 10.419530131217563
    - type: nauc_ndcg_at_10_std
      value: -12.020911860422277
    - type: nauc_ndcg_at_1_diff1
      value: 62.02492634987989
    - type: nauc_ndcg_at_1_max
      value: 12.426103478237204
    - type: nauc_ndcg_at_1_std
      value: -21.462128885638194
    - type: nauc_ndcg_at_20_diff1
      value: 40.21705035603188
    - type: nauc_ndcg_at_20_max
      value: 10.683814012195125
    - type: nauc_ndcg_at_20_std
      value: -11.69979166757856
    - type: nauc_ndcg_at_3_diff1
      value: 41.841810239951
    - type: nauc_ndcg_at_3_max
      value: 11.064226884457492
    - type: nauc_ndcg_at_3_std
      value: -14.913305538472887
    - type: nauc_ndcg_at_5_diff1
      value: 40.04853934119725
    - type: nauc_ndcg_at_5_max
      value: 10.57426706775158
    - type: nauc_ndcg_at_5_std
      value: -13.00820458664088
    - type: nauc_precision_at_1000_diff1
      value: 0.3851195665415394
    - type: nauc_precision_at_1000_max
      value: 10.719664087222139
    - type: nauc_precision_at_1000_std
      value: 4.060546631755005
    - type: nauc_precision_at_100_diff1
      value: -1.1672675937708246
    - type: nauc_precision_at_100_max
      value: 11.76706994923555
    - type: nauc_precision_at_100_std
      value: 6.682502752333491
    - type: nauc_precision_at_10_diff1
      value: -2.442502050324997
    - type: nauc_precision_at_10_max
      value: 9.982032022937407
    - type: nauc_precision_at_10_std
      value: 2.253707666893988
    - type: nauc_precision_at_1_diff1
      value: 62.02492634987989
    - type: nauc_precision_at_1_max
      value: 12.426103478237204
    - type: nauc_precision_at_1_std
      value: -21.462128885638194
    - type: nauc_precision_at_20_diff1
      value: -2.8909153065947506
    - type: nauc_precision_at_20_max
      value: 10.381422532792685
    - type: nauc_precision_at_20_std
      value: 4.880699672256141
    - type: nauc_precision_at_3_diff1
      value: 13.983067176933947
    - type: nauc_precision_at_3_max
      value: 11.941084260114476
    - type: nauc_precision_at_3_std
      value: -12.615897998044437
    - type: nauc_precision_at_5_diff1
      value: 2.6828558906895688
    - type: nauc_precision_at_5_max
      value: 10.78931350518598
    - type: nauc_precision_at_5_std
      value: -3.6318676409745203
    - type: nauc_recall_at_1000_diff1
      value: -8.672439956073752
    - type: nauc_recall_at_1000_max
      value: 23.244662839438533
    - type: nauc_recall_at_1000_std
      value: 40.18478080701204
    - type: nauc_recall_at_100_diff1
      value: -4.465450402228265
    - type: nauc_recall_at_100_max
      value: 15.424894718754112
    - type: nauc_recall_at_100_std
      value: 28.33923562045188
    - type: nauc_recall_at_10_diff1
      value: 5.824940232374557
    - type: nauc_recall_at_10_max
      value: 9.55369331654998
    - type: nauc_recall_at_10_std
      value: 8.705857917052512
    - type: nauc_recall_at_1_diff1
      value: 45.26755146712848
    - type: nauc_recall_at_1_max
      value: 7.630523437842046
    - type: nauc_recall_at_1_std
      value: -13.605176488921838
    - type: nauc_recall_at_20_diff1
      value: 1.1759544592030455
    - type: nauc_recall_at_20_max
      value: 10.197822183591066
    - type: nauc_recall_at_20_std
      value: 15.269883968698228
    - type: nauc_recall_at_3_diff1
      value: 21.902162866702668
    - type: nauc_recall_at_3_max
      value: 9.183669197010431
    - type: nauc_recall_at_3_std
      value: -8.694680120818228
    - type: nauc_recall_at_5_diff1
      value: 13.653229973783526
    - type: nauc_recall_at_5_max
      value: 9.716681689699136
    - type: nauc_recall_at_5_std
      value: -0.2880989596678906
    - type: ndcg_at_1
      value: 80.613
    - type: ndcg_at_10
      value: 86.26899999999999
    - type: ndcg_at_100
      value: 87.12100000000001
    - type: ndcg_at_1000
      value: 87.40299999999999
    - type: ndcg_at_20
      value: 86.651
    - type: ndcg_at_3
      value: 84.64500000000001
    - type: ndcg_at_5
      value: 85.59
    - type: precision_at_1
      value: 80.613
    - type: precision_at_10
      value: 10.763
    - type: precision_at_100
      value: 1.16
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_20
      value: 5.525
    - type: precision_at_3
      value: 33.415
    - type: precision_at_5
      value: 20.808
    - type: recall_at_1
      value: 72.449
    - type: recall_at_10
      value: 93.29899999999999
    - type: recall_at_100
      value: 96.421
    - type: recall_at_1000
      value: 98.053
    - type: recall_at_20
      value: 94.53200000000001
    - type: recall_at_3
      value: 88.594
    - type: recall_at_5
      value: 91.268
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: dev
      type: mteb/fiqa
    metrics:
    - type: main_score
      value: 42.362
    - type: map_at_1
      value: 22.462
    - type: map_at_10
      value: 34.717999999999996
    - type: map_at_100
      value: 36.561
    - type: map_at_1000
      value: 36.716
    - type: map_at_20
      value: 35.716
    - type: map_at_3
      value: 30.692000000000004
    - type: map_at_5
      value: 32.553
    - type: mrr_at_1
      value: 40.400000000000006
    - type: mrr_at_10
      value: 49.666428571428575
    - type: mrr_at_100
      value: 50.487418944361295
    - type: mrr_at_1000
      value: 50.51970264235359
    - type: mrr_at_20
      value: 50.13681738969665
    - type: mrr_at_3
      value: 47.56666666666667
    - type: mrr_at_5
      value: 48.85666666666666
    - type: nauc_map_at_1000_diff1
      value: 48.907747941693266
    - type: nauc_map_at_1000_max
      value: 33.36065026293396
    - type: nauc_map_at_1000_std
      value: 3.721763378995018
    - type: nauc_map_at_100_diff1
      value: 48.84727756808333
    - type: nauc_map_at_100_max
      value: 33.24694910436772
    - type: nauc_map_at_100_std
      value: 3.697147651138032
    - type: nauc_map_at_10_diff1
      value: 49.12331607215452
    - type: nauc_map_at_10_max
      value: 32.834495636560405
    - type: nauc_map_at_10_std
      value: 1.842046947246096
    - type: nauc_map_at_1_diff1
      value: 55.677889443633454
    - type: nauc_map_at_1_max
      value: 29.14429236432774
    - type: nauc_map_at_1_std
      value: -6.340931692625591
    - type: nauc_map_at_20_diff1
      value: 48.94402984571876
    - type: nauc_map_at_20_max
      value: 32.97842670695263
    - type: nauc_map_at_20_std
      value: 2.719721699786715
    - type: nauc_map_at_3_diff1
      value: 50.345833937052284
    - type: nauc_map_at_3_max
      value: 30.884637973451046
    - type: nauc_map_at_3_std
      value: -1.7032612225578052
    - type: nauc_map_at_5_diff1
      value: 49.4967472092422
    - type: nauc_map_at_5_max
      value: 32.04823415779001
    - type: nauc_map_at_5_std
      value: 0.11348259159930259
    - type: nauc_mrr_at_1000_diff1
      value: 53.4664833188161
    - type: nauc_mrr_at_1000_max
      value: 43.94130528629785
    - type: nauc_mrr_at_1000_std
      value: 6.3073911252297625
    - type: nauc_mrr_at_100_diff1
      value: 53.45784380239337
    - type: nauc_mrr_at_100_max
      value: 43.93103386484263
    - type: nauc_mrr_at_100_std
      value: 6.326857176825003
    - type: nauc_mrr_at_10_diff1
      value: 53.16999005935199
    - type: nauc_mrr_at_10_max
      value: 43.96148608534777
    - type: nauc_mrr_at_10_std
      value: 6.060709004613991
    - type: nauc_mrr_at_1_diff1
      value: 60.454425921819976
    - type: nauc_mrr_at_1_max
      value: 44.854772426097114
    - type: nauc_mrr_at_1_std
      value: 1.7461856169787138
    - type: nauc_mrr_at_20_diff1
      value: 53.4253064364276
    - type: nauc_mrr_at_20_max
      value: 43.93067697716607
    - type: nauc_mrr_at_20_std
      value: 6.132078452692403
    - type: nauc_mrr_at_3_diff1
      value: 53.75537772130037
    - type: nauc_mrr_at_3_max
      value: 43.612665358637784
    - type: nauc_mrr_at_3_std
      value: 5.3924645903759165
    - type: nauc_mrr_at_5_diff1
      value: 53.23878310443892
    - type: nauc_mrr_at_5_max
      value: 44.154494509820275
    - type: nauc_mrr_at_5_std
      value: 6.128619405551008
    - type: nauc_ndcg_at_1000_diff1
      value: 48.74084938103878
    - type: nauc_ndcg_at_1000_max
      value: 38.28143671294916
    - type: nauc_ndcg_at_1000_std
      value: 9.48205302587039
    - type: nauc_ndcg_at_100_diff1
      value: 47.86688156492628
    - type: nauc_ndcg_at_100_max
      value: 36.73585329637074
    - type: nauc_ndcg_at_100_std
      value: 9.886842243260414
    - type: nauc_ndcg_at_10_diff1
      value: 47.874511239978354
    - type: nauc_ndcg_at_10_max
      value: 35.7706902177999
    - type: nauc_ndcg_at_10_std
      value: 5.509978475259395
    - type: nauc_ndcg_at_1_diff1
      value: 60.454425921819976
    - type: nauc_ndcg_at_1_max
      value: 44.854772426097114
    - type: nauc_ndcg_at_1_std
      value: 1.7461856169787138
    - type: nauc_ndcg_at_20_diff1
      value: 47.98814179482003
    - type: nauc_ndcg_at_20_max
      value: 35.80004813629657
    - type: nauc_ndcg_at_20_std
      value: 6.632931898598267
    - type: nauc_ndcg_at_3_diff1
      value: 48.153795894304174
    - type: nauc_ndcg_at_3_max
      value: 36.28196005109544
    - type: nauc_ndcg_at_3_std
      value: 2.793405120536969
    - type: nauc_ndcg_at_5_diff1
      value: 47.88157624782777
    - type: nauc_ndcg_at_5_max
      value: 35.8935279838606
    - type: nauc_ndcg_at_5_std
      value: 4.0533111045329955
    - type: nauc_precision_at_1000_diff1
      value: -2.8869159343467605
    - type: nauc_precision_at_1000_max
      value: 21.13113140923961
    - type: nauc_precision_at_1000_std
      value: 24.212722433897408
    - type: nauc_precision_at_100_diff1
      value: 1.1594774420038931
    - type: nauc_precision_at_100_max
      value: 22.26831206413967
    - type: nauc_precision_at_100_std
      value: 29.81314341287538
    - type: nauc_precision_at_10_diff1
      value: 16.05087694540557
    - type: nauc_precision_at_10_max
      value: 29.809963401808616
    - type: nauc_precision_at_10_std
      value: 19.84954878024915
    - type: nauc_precision_at_1_diff1
      value: 60.454425921819976
    - type: nauc_precision_at_1_max
      value: 44.854772426097114
    - type: nauc_precision_at_1_std
      value: 1.7461856169787138
    - type: nauc_precision_at_20_diff1
      value: 9.748587851192008
    - type: nauc_precision_at_20_max
      value: 26.594687094795994
    - type: nauc_precision_at_20_std
      value: 24.150090984390086
    - type: nauc_precision_at_3_diff1
      value: 32.12647129845763
    - type: nauc_precision_at_3_max
      value: 38.608852867058395
    - type: nauc_precision_at_3_std
      value: 10.859746017200495
    - type: nauc_precision_at_5_diff1
      value: 23.827901543995793
    - type: nauc_precision_at_5_max
      value: 35.67460349135147
    - type: nauc_precision_at_5_std
      value: 15.9392352657892
    - type: nauc_recall_at_1000_diff1
      value: 35.2270895294026
    - type: nauc_recall_at_1000_max
      value: 42.19353048661261
    - type: nauc_recall_at_1000_std
      value: 38.04743729975647
    - type: nauc_recall_at_100_diff1
      value: 30.40548686084564
    - type: nauc_recall_at_100_max
      value: 25.92198350281053
    - type: nauc_recall_at_100_std
      value: 26.42423804923528
    - type: nauc_recall_at_10_diff1
      value: 36.90410693124825
    - type: nauc_recall_at_10_max
      value: 28.372843635416388
    - type: nauc_recall_at_10_std
      value: 7.8175786831627905
    - type: nauc_recall_at_1_diff1
      value: 55.677889443633454
    - type: nauc_recall_at_1_max
      value: 29.14429236432774
    - type: nauc_recall_at_1_std
      value: -6.340931692625591
    - type: nauc_recall_at_20_diff1
      value: 35.99767274556454
    - type: nauc_recall_at_20_max
      value: 27.04852589764223
    - type: nauc_recall_at_20_std
      value: 11.072120738834073
    - type: nauc_recall_at_3_diff1
      value: 41.25393288041596
    - type: nauc_recall_at_3_max
      value: 26.97488751275594
    - type: nauc_recall_at_3_std
      value: 0.21950460796902102
    - type: nauc_recall_at_5_diff1
      value: 38.26235012673011
    - type: nauc_recall_at_5_max
      value: 28.830247312497054
    - type: nauc_recall_at_5_std
      value: 4.072132303371853
    - type: ndcg_at_1
      value: 40.400000000000006
    - type: ndcg_at_10
      value: 42.362
    - type: ndcg_at_100
      value: 48.982
    - type: ndcg_at_1000
      value: 51.581999999999994
    - type: ndcg_at_20
      value: 44.937
    - type: ndcg_at_3
      value: 38.922000000000004
    - type: ndcg_at_5
      value: 39.596
    - type: precision_at_1
      value: 40.400000000000006
    - type: precision_at_10
      value: 11.18
    - type: precision_at_100
      value: 1.796
    - type: precision_at_1000
      value: 0.22300000000000003
    - type: precision_at_20
      value: 6.710000000000001
    - type: precision_at_3
      value: 24.532999999999998
    - type: precision_at_5
      value: 17.52
    - type: recall_at_1
      value: 22.462
    - type: recall_at_10
      value: 49.382999999999996
    - type: recall_at_100
      value: 74.494
    - type: recall_at_1000
      value: 90.427
    - type: recall_at_20
      value: 57.524
    - type: recall_at_3
      value: 36.028999999999996
    - type: recall_at_5
      value: 41.089
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: main_score
      value: 40.558
    - type: map_at_1
      value: 20.451
    - type: map_at_10
      value: 33.041
    - type: map_at_100
      value: 34.945
    - type: map_at_1000
      value: 35.136
    - type: map_at_20
      value: 34.114
    - type: map_at_3
      value: 29.03
    - type: map_at_5
      value: 31.423000000000002
    - type: mrr_at_1
      value: 39.50617283950617
    - type: mrr_at_10
      value: 48.47491671565746
    - type: mrr_at_100
      value: 49.25528865170789
    - type: mrr_at_1000
      value: 49.30492546288068
    - type: mrr_at_20
      value: 48.90574296444466
    - type: mrr_at_3
      value: 46.16769547325103
    - type: mrr_at_5
      value: 47.47170781893004
    - type: nauc_map_at_1000_diff1
      value: 42.33223793532006
    - type: nauc_map_at_1000_max
      value: 28.178269647825054
    - type: nauc_map_at_1000_std
      value: 4.694684846288862
    - type: nauc_map_at_100_diff1
      value: 42.23585502790571
    - type: nauc_map_at_100_max
      value: 28.09325262656699
    - type: nauc_map_at_100_std
      value: 4.635779769876692
    - type: nauc_map_at_10_diff1
      value: 42.29892463032549
    - type: nauc_map_at_10_max
      value: 26.885463946159042
    - type: nauc_map_at_10_std
      value: 3.439834407388629
    - type: nauc_map_at_1_diff1
      value: 48.29160916418846
    - type: nauc_map_at_1_max
      value: 20.558365030918516
    - type: nauc_map_at_1_std
      value: -0.44854024391070973
    - type: nauc_map_at_20_diff1
      value: 42.1753422786911
    - type: nauc_map_at_20_max
      value: 27.631926253435857
    - type: nauc_map_at_20_std
      value: 4.002081405774815
    - type: nauc_map_at_3_diff1
      value: 44.56188133973965
    - type: nauc_map_at_3_max
      value: 25.936921564225862
    - type: nauc_map_at_3_std
      value: 2.3757170812866804
    - type: nauc_map_at_5_diff1
      value: 43.183022909231234
    - type: nauc_map_at_5_max
      value: 26.115662732325145
    - type: nauc_map_at_5_std
      value: 2.584799983984164
    - type: nauc_mrr_at_1000_diff1
      value: 49.90329578326087
    - type: nauc_mrr_at_1000_max
      value: 35.86029877981383
    - type: nauc_mrr_at_1000_std
      value: 6.305323054154965
    - type: nauc_mrr_at_100_diff1
      value: 49.86929948930004
    - type: nauc_mrr_at_100_max
      value: 35.850698951924386
    - type: nauc_mrr_at_100_std
      value: 6.3311346338729
    - type: nauc_mrr_at_10_diff1
      value: 49.943023388207195
    - type: nauc_mrr_at_10_max
      value: 35.98541218521815
    - type: nauc_mrr_at_10_std
      value: 6.0382083805515805
    - type: nauc_mrr_at_1_diff1
      value: 53.793790143858146
    - type: nauc_mrr_at_1_max
      value: 33.46215151905759
    - type: nauc_mrr_at_1_std
      value: 4.310648959342706
    - type: nauc_mrr_at_20_diff1
      value: 49.78255203343183
    - type: nauc_mrr_at_20_max
      value: 35.67982988010112
    - type: nauc_mrr_at_20_std
      value: 6.097005492945753
    - type: nauc_mrr_at_3_diff1
      value: 50.78094748778293
    - type: nauc_mrr_at_3_max
      value: 36.31047156376032
    - type: nauc_mrr_at_3_std
      value: 5.551964274549184
    - type: nauc_mrr_at_5_diff1
      value: 50.22070037219334
    - type: nauc_mrr_at_5_max
      value: 35.82391876186752
    - type: nauc_mrr_at_5_std
      value: 5.989440675787551
    - type: nauc_ndcg_at_1000_diff1
      value: 43.29067795693791
    - type: nauc_ndcg_at_1000_max
      value: 32.770853091465156
    - type: nauc_ndcg_at_1000_std
      value: 9.075882750305011
    - type: nauc_ndcg_at_100_diff1
      value: 41.92437892838288
    - type: nauc_ndcg_at_100_max
      value: 31.977508922932984
    - type: nauc_ndcg_at_100_std
      value: 9.345565382601217
    - type: nauc_ndcg_at_10_diff1
      value: 41.86314487224504
    - type: nauc_ndcg_at_10_max
      value: 29.565216296817827
    - type: nauc_ndcg_at_10_std
      value: 5.173875408923697
    - type: nauc_ndcg_at_1_diff1
      value: 53.793790143858146
    - type: nauc_ndcg_at_1_max
      value: 33.46215151905759
    - type: nauc_ndcg_at_1_std
      value: 4.310648959342706
    - type: nauc_ndcg_at_20_diff1
      value: 41.426074027410706
    - type: nauc_ndcg_at_20_max
      value: 30.01328944145506
    - type: nauc_ndcg_at_20_std
      value: 6.169601231532484
    - type: nauc_ndcg_at_3_diff1
      value: 44.27395561376024
    - type: nauc_ndcg_at_3_max
      value: 31.503088046380313
    - type: nauc_ndcg_at_3_std
      value: 5.208532778972112
    - type: nauc_ndcg_at_5_diff1
      value: 42.81322677405853
    - type: nauc_ndcg_at_5_max
      value: 29.407079874158846
    - type: nauc_ndcg_at_5_std
      value: 4.483826520898586
    - type: nauc_precision_at_1000_diff1
      value: 1.621703595454423
    - type: nauc_precision_at_1000_max
      value: 23.880102194550204
    - type: nauc_precision_at_1000_std
      value: 13.80100184324797
    - type: nauc_precision_at_100_diff1
      value: 6.575602396019008
    - type: nauc_precision_at_100_max
      value: 28.264948074327478
    - type: nauc_precision_at_100_std
      value: 17.684872532407283
    - type: nauc_precision_at_10_diff1
      value: 16.8328055869745
    - type: nauc_precision_at_10_max
      value: 30.24323560145753
    - type: nauc_precision_at_10_std
      value: 11.304688858560379
    - type: nauc_precision_at_1_diff1
      value: 53.793790143858146
    - type: nauc_precision_at_1_max
      value: 33.46215151905759
    - type: nauc_precision_at_1_std
      value: 4.310648959342706
    - type: nauc_precision_at_20_diff1
      value: 12.904056330326577
    - type: nauc_precision_at_20_max
      value: 28.969423687460438
    - type: nauc_precision_at_20_std
      value: 12.029389701897678
    - type: nauc_precision_at_3_diff1
      value: 31.1308248469768
    - type: nauc_precision_at_3_max
      value: 33.86869420849858
    - type: nauc_precision_at_3_std
      value: 8.474707630694647
    - type: nauc_precision_at_5_diff1
      value: 23.15042207925308
    - type: nauc_precision_at_5_max
      value: 29.597450076869325
    - type: nauc_precision_at_5_std
      value: 9.148285720232177
    - type: nauc_recall_at_1000_diff1
      value: 30.844750307544324
    - type: nauc_recall_at_1000_max
      value: 30.58773950265899
    - type: nauc_recall_at_1000_std
      value: 35.28925560349968
    - type: nauc_recall_at_100_diff1
      value: 24.148211328845242
    - type: nauc_recall_at_100_max
      value: 26.79994369269315
    - type: nauc_recall_at_100_std
      value: 24.218335174944343
    - type: nauc_recall_at_10_diff1
      value: 28.95261846685996
    - type: nauc_recall_at_10_max
      value: 22.666727959324515
    - type: nauc_recall_at_10_std
      value: 5.513769892416629
    - type: nauc_recall_at_1_diff1
      value: 48.29160916418846
    - type: nauc_recall_at_1_max
      value: 20.558365030918516
    - type: nauc_recall_at_1_std
      value: -0.44854024391070973
    - type: nauc_recall_at_20_diff1
      value: 26.837633000701228
    - type: nauc_recall_at_20_max
      value: 22.535529588484504
    - type: nauc_recall_at_20_std
      value: 8.42648285205937
    - type: nauc_recall_at_3_diff1
      value: 38.25026260610774
    - type: nauc_recall_at_3_max
      value: 25.050690202547578
    - type: nauc_recall_at_3_std
      value: 3.1080253121438766
    - type: nauc_recall_at_5_diff1
      value: 34.50423249642314
    - type: nauc_recall_at_5_max
      value: 22.85592363545583
    - type: nauc_recall_at_5_std
      value: 3.640758629683203
    - type: ndcg_at_1
      value: 39.506
    - type: ndcg_at_10
      value: 40.558
    - type: ndcg_at_100
      value: 47.247
    - type: ndcg_at_1000
      value: 50.437
    - type: ndcg_at_20
      value: 43.162
    - type: ndcg_at_3
      value: 37.261
    - type: ndcg_at_5
      value: 38.391999999999996
    - type: precision_at_1
      value: 39.506
    - type: precision_at_10
      value: 11.142000000000001
    - type: precision_at_100
      value: 1.813
    - type: precision_at_1000
      value: 0.23600000000000002
    - type: precision_at_20
      value: 6.7589999999999995
    - type: precision_at_3
      value: 25.051000000000002
    - type: precision_at_5
      value: 18.395
    - type: recall_at_1
      value: 20.451
    - type: recall_at_10
      value: 46.79
    - type: recall_at_100
      value: 71.353
    - type: recall_at_1000
      value: 90.536
    - type: recall_at_20
      value: 54.517
    - type: recall_at_3
      value: 33.672000000000004
    - type: recall_at_5
      value: 39.678999999999995
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: train
      type: mteb/fiqa
    metrics:
    - type: main_score
      value: 42.217
    - type: map_at_1
      value: 21.418
    - type: map_at_10
      value: 34.437
    - type: map_at_100
      value: 36.254999999999995
    - type: map_at_1000
      value: 36.424
    - type: map_at_20
      value: 35.449999999999996
    - type: map_at_3
      value: 30.122
    - type: map_at_5
      value: 32.46
    - type: mrr_at_1
      value: 40.21818181818182
    - type: mrr_at_10
      value: 49.078658008658
    - type: mrr_at_100
      value: 49.9159011457498
    - type: mrr_at_1000
      value: 49.956067513298244
    - type: mrr_at_20
      value: 49.59237755036657
    - type: mrr_at_3
      value: 46.62424242424243
    - type: mrr_at_5
      value: 48.02424242424242
    - type: nauc_map_at_1000_diff1
      value: 40.17457855495732
    - type: nauc_map_at_1000_max
      value: 25.311659240262102
    - type: nauc_map_at_1000_std
      value: 5.059430044056764
    - type: nauc_map_at_100_diff1
      value: 40.151268380342515
    - type: nauc_map_at_100_max
      value: 25.21648990114121
    - type: nauc_map_at_100_std
      value: 5.026493196551854
    - type: nauc_map_at_10_diff1
      value: 40.040465022431576
    - type: nauc_map_at_10_max
      value: 24.355474347016965
    - type: nauc_map_at_10_std
      value: 3.5640713532110886
    - type: nauc_map_at_1_diff1
      value: 44.23533684826564
    - type: nauc_map_at_1_max
      value: 16.26051705102941
    - type: nauc_map_at_1_std
      value: -0.9304514636140965
    - type: nauc_map_at_20_diff1
      value: 40.07253921544327
    - type: nauc_map_at_20_max
      value: 24.840445695825426
    - type: nauc_map_at_20_std
      value: 4.3692544013620225
    - type: nauc_map_at_3_diff1
      value: 40.802965930319765
    - type: nauc_map_at_3_max
      value: 21.578173190568766
    - type: nauc_map_at_3_std
      value: 0.6624363947378223
    - type: nauc_map_at_5_diff1
      value: 40.41105488775194
    - type: nauc_map_at_5_max
      value: 22.962784936768788
    - type: nauc_map_at_5_std
      value: 2.061146134529408
    - type: nauc_mrr_at_1000_diff1
      value: 45.39271593141525
    - type: nauc_mrr_at_1000_max
      value: 32.71504880799005
    - type: nauc_mrr_at_1000_std
      value: 7.416955987371169
    - type: nauc_mrr_at_100_diff1
      value: 45.37668004444169
    - type: nauc_mrr_at_100_max
      value: 32.71589234567116
    - type: nauc_mrr_at_100_std
      value: 7.429449409497287
    - type: nauc_mrr_at_10_diff1
      value: 45.296174959712616
    - type: nauc_mrr_at_10_max
      value: 32.717197303838624
    - type: nauc_mrr_at_10_std
      value: 7.283098786281713
    - type: nauc_mrr_at_1_diff1
      value: 49.480470078543185
    - type: nauc_mrr_at_1_max
      value: 31.68605495492876
    - type: nauc_mrr_at_1_std
      value: 4.5814903060120304
    - type: nauc_mrr_at_20_diff1
      value: 45.36317431590108
    - type: nauc_mrr_at_20_max
      value: 32.706079440239364
    - type: nauc_mrr_at_20_std
      value: 7.382450020586175
    - type: nauc_mrr_at_3_diff1
      value: 46.001809326251454
    - type: nauc_mrr_at_3_max
      value: 32.46816837141833
    - type: nauc_mrr_at_3_std
      value: 6.707194036403839
    - type: nauc_mrr_at_5_diff1
      value: 45.46057942438407
    - type: nauc_mrr_at_5_max
      value: 32.408646791629394
    - type: nauc_mrr_at_5_std
      value: 7.11971218876357
    - type: nauc_ndcg_at_1000_diff1
      value: 40.315538048774236
    - type: nauc_ndcg_at_1000_max
      value: 29.577764682607636
    - type: nauc_ndcg_at_1000_std
      value: 9.802905608930201
    - type: nauc_ndcg_at_100_diff1
      value: 39.69359815845272
    - type: nauc_ndcg_at_100_max
      value: 28.64875657558225
    - type: nauc_ndcg_at_100_std
      value: 10.074769927489001
    - type: nauc_ndcg_at_10_diff1
      value: 39.42499828447507
    - type: nauc_ndcg_at_10_max
      value: 27.18259534858955
    - type: nauc_ndcg_at_10_std
      value: 6.306777798983758
    - type: nauc_ndcg_at_1_diff1
      value: 49.480470078543185
    - type: nauc_ndcg_at_1_max
      value: 31.68605495492876
    - type: nauc_ndcg_at_1_std
      value: 4.5814903060120304
    - type: nauc_ndcg_at_20_diff1
      value: 39.51807220300204
    - type: nauc_ndcg_at_20_max
      value: 27.62717063554887
    - type: nauc_ndcg_at_20_std
      value: 7.612068802546053
    - type: nauc_ndcg_at_3_diff1
      value: 41.04629803524383
    - type: nauc_ndcg_at_3_max
      value: 27.84818206495344
    - type: nauc_ndcg_at_3_std
      value: 4.828135065879767
    - type: nauc_ndcg_at_5_diff1
      value: 40.01813972950631
    - type: nauc_ndcg_at_5_max
      value: 26.524741885273233
    - type: nauc_ndcg_at_5_std
      value: 5.068529272139508
    - type: nauc_precision_at_1000_diff1
      value: 0.5470497141171098
    - type: nauc_precision_at_1000_max
      value: 24.170306355297317
    - type: nauc_precision_at_1000_std
      value: 18.50896415433208
    - type: nauc_precision_at_100_diff1
      value: 7.241268035021293
    - type: nauc_precision_at_100_max
      value: 28.939185497818976
    - type: nauc_precision_at_100_std
      value: 24.22708062648789
    - type: nauc_precision_at_10_diff1
      value: 18.067403140646473
    - type: nauc_precision_at_10_max
      value: 33.44992314337708
    - type: nauc_precision_at_10_std
      value: 16.388600267880083
    - type: nauc_precision_at_1_diff1
      value: 49.480470078543185
    - type: nauc_precision_at_1_max
      value: 31.68605495492876
    - type: nauc_precision_at_1_std
      value: 4.5814903060120304
    - type: nauc_precision_at_20_diff1
      value: 14.651721506297456
    - type: nauc_precision_at_20_max
      value: 32.54709281419177
    - type: nauc_precision_at_20_std
      value: 20.017505605751566
    - type: nauc_precision_at_3_diff1
      value: 30.04485384205624
    - type: nauc_precision_at_3_max
      value: 34.145525798671464
    - type: nauc_precision_at_3_std
      value: 9.385558743613709
    - type: nauc_precision_at_5_diff1
      value: 24.483639848034873
    - type: nauc_precision_at_5_max
      value: 33.41057528286542
    - type: nauc_precision_at_5_std
      value: 12.384466658411828
    - type: nauc_recall_at_1000_diff1
      value: 21.123402730271586
    - type: nauc_recall_at_1000_max
      value: 26.29127489133915
    - type: nauc_recall_at_1000_std
      value: 41.48297645436926
    - type: nauc_recall_at_100_diff1
      value: 23.190745050134876
    - type: nauc_recall_at_100_max
      value: 20.96730541491135
    - type: nauc_recall_at_100_std
      value: 24.579783248787745
    - type: nauc_recall_at_10_diff1
      value: 28.523056048729163
    - type: nauc_recall_at_10_max
      value: 21.334211258862197
    - type: nauc_recall_at_10_std
      value: 7.805738098876508
    - type: nauc_recall_at_1_diff1
      value: 44.23533684826564
    - type: nauc_recall_at_1_max
      value: 16.26051705102941
    - type: nauc_recall_at_1_std
      value: -0.9304514636140965
    - type: nauc_recall_at_20_diff1
      value: 27.256571523147745
    - type: nauc_recall_at_20_max
      value: 21.103408026023196
    - type: nauc_recall_at_20_std
      value: 11.445449145769603
    - type: nauc_recall_at_3_diff1
      value: 34.31934638156186
    - type: nauc_recall_at_3_max
      value: 18.78403262209476
    - type: nauc_recall_at_3_std
      value: 1.4901630112302768
    - type: nauc_recall_at_5_diff1
      value: 31.63689568492167
    - type: nauc_recall_at_5_max
      value: 19.123482920636295
    - type: nauc_recall_at_5_std
      value: 3.880507575208801
    - type: ndcg_at_1
      value: 40.217999999999996
    - type: ndcg_at_10
      value: 42.217
    - type: ndcg_at_100
      value: 48.762
    - type: ndcg_at_1000
      value: 51.63100000000001
    - type: ndcg_at_20
      value: 44.767
    - type: ndcg_at_3
      value: 38.057
    - type: ndcg_at_5
      value: 39.427
    - type: precision_at_1
      value: 40.217999999999996
    - type: precision_at_10
      value: 11.376
    - type: precision_at_100
      value: 1.815
    - type: precision_at_1000
      value: 0.232
    - type: precision_at_20
      value: 6.775
    - type: precision_at_3
      value: 24.812
    - type: precision_at_5
      value: 18.185000000000002
    - type: recall_at_1
      value: 21.418
    - type: recall_at_10
      value: 49.854
    - type: recall_at_100
      value: 74.37700000000001
    - type: recall_at_1000
      value: 91.72200000000001
    - type: recall_at_20
      value: 57.857
    - type: recall_at_3
      value: 35.221999999999994
    - type: recall_at_5
      value: 41.404999999999994
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA (default)
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: dev
      type: mteb/hotpotqa
    metrics:
    - type: main_score
      value: 74.175
    - type: map_at_1
      value: 41.041
    - type: map_at_10
      value: 66.31099999999999
    - type: map_at_100
      value: 67.104
    - type: map_at_1000
      value: 67.161
    - type: map_at_20
      value: 66.782
    - type: map_at_3
      value: 62.925
    - type: map_at_5
      value: 65.134
    - type: mrr_at_1
      value: 82.08187993390858
    - type: mrr_at_10
      value: 87.22340242626639
    - type: mrr_at_100
      value: 87.36059128975714
    - type: mrr_at_1000
      value: 87.364851053774
    - type: mrr_at_20
      value: 87.31789909538858
    - type: mrr_at_3
      value: 86.40842053729882
    - type: mrr_at_5
      value: 86.97478734471574
    - type: nauc_map_at_1000_diff1
      value: 15.036034548647908
    - type: nauc_map_at_1000_max
      value: 25.75085303993812
    - type: nauc_map_at_1000_std
      value: 17.465887392707984
    - type: nauc_map_at_100_diff1
      value: 15.005143661829045
    - type: nauc_map_at_100_max
      value: 25.745125861339808
    - type: nauc_map_at_100_std
      value: 17.504053167240222
    - type: nauc_map_at_10_diff1
      value: 14.893496342739656
    - type: nauc_map_at_10_max
      value: 25.56792154122193
    - type: nauc_map_at_10_std
      value: 17.09812367943331
    - type: nauc_map_at_1_diff1
      value: 69.96236855623434
    - type: nauc_map_at_1_max
      value: 49.448851447506925
    - type: nauc_map_at_1_std
      value: 2.889004800052033
    - type: nauc_map_at_20_diff1
      value: 14.907169096850453
    - type: nauc_map_at_20_max
      value: 25.664564175861543
    - type: nauc_map_at_20_std
      value: 17.43387597817089
    - type: nauc_map_at_3_diff1
      value: 14.819429540966336
    - type: nauc_map_at_3_max
      value: 24.63784431578106
    - type: nauc_map_at_3_std
      value: 13.51698248320979
    - type: nauc_map_at_5_diff1
      value: 14.793999397375302
    - type: nauc_map_at_5_max
      value: 25.273543691930023
    - type: nauc_map_at_5_std
      value: 15.528475200820887
    - type: nauc_mrr_at_1000_diff1
      value: 69.09310778251964
    - type: nauc_mrr_at_1000_max
      value: 51.91323689768607
    - type: nauc_mrr_at_1000_std
      value: 5.0427302617514265
    - type: nauc_mrr_at_100_diff1
      value: 69.08774366986974
    - type: nauc_mrr_at_100_max
      value: 51.91649892721352
    - type: nauc_mrr_at_100_std
      value: 5.055693527150247
    - type: nauc_mrr_at_10_diff1
      value: 69.04162799026531
    - type: nauc_mrr_at_10_max
      value: 51.94707923303371
    - type: nauc_mrr_at_10_std
      value: 5.073028039967743
    - type: nauc_mrr_at_1_diff1
      value: 69.96236855623434
    - type: nauc_mrr_at_1_max
      value: 49.448851447506925
    - type: nauc_mrr_at_1_std
      value: 2.889004800052033
    - type: nauc_mrr_at_20_diff1
      value: 69.07119075448549
    - type: nauc_mrr_at_20_max
      value: 51.945891610724935
    - type: nauc_mrr_at_20_std
      value: 5.120139371969651
    - type: nauc_mrr_at_3_diff1
      value: 69.04728116249032
    - type: nauc_mrr_at_3_max
      value: 52.19716746949592
    - type: nauc_mrr_at_3_std
      value: 4.455467076969271
    - type: nauc_mrr_at_5_diff1
      value: 68.99508759550626
    - type: nauc_mrr_at_5_max
      value: 52.00068611382036
    - type: nauc_mrr_at_5_std
      value: 4.853875045723172
    - type: nauc_ndcg_at_1000_diff1
      value: 21.56019247861624
    - type: nauc_ndcg_at_1000_max
      value: 29.992075228189385
    - type: nauc_ndcg_at_1000_std
      value: 19.52149913625525
    - type: nauc_ndcg_at_100_diff1
      value: 20.57182767444212
    - type: nauc_ndcg_at_100_max
      value: 29.671296370713957
    - type: nauc_ndcg_at_100_std
      value: 20.459885577163732
    - type: nauc_ndcg_at_10_diff1
      value: 19.899707356785555
    - type: nauc_ndcg_at_10_max
      value: 28.92080969944076
    - type: nauc_ndcg_at_10_std
      value: 18.985520950121536
    - type: nauc_ndcg_at_1_diff1
      value: 69.96236855623434
    - type: nauc_ndcg_at_1_max
      value: 49.448851447506925
    - type: nauc_ndcg_at_1_std
      value: 2.889004800052033
    - type: nauc_ndcg_at_20_diff1
      value: 19.817147184816825
    - type: nauc_ndcg_at_20_max
      value: 29.10607440644831
    - type: nauc_ndcg_at_20_std
      value: 20.055386680932457
    - type: nauc_ndcg_at_3_diff1
      value: 20.563849560253576
    - type: nauc_ndcg_at_3_max
      value: 28.040961943107828
    - type: nauc_ndcg_at_3_std
      value: 13.092847825660659
    - type: nauc_ndcg_at_5_diff1
      value: 19.974303695690292
    - type: nauc_ndcg_at_5_max
      value: 28.543507472783176
    - type: nauc_ndcg_at_5_std
      value: 15.984138613333693
    - type: nauc_precision_at_1000_diff1
      value: -3.673616783114865
    - type: nauc_precision_at_1000_max
      value: 23.053922175840807
    - type: nauc_precision_at_1000_std
      value: 49.11991772792811
    - type: nauc_precision_at_100_diff1
      value: -1.216591429661993
    - type: nauc_precision_at_100_max
      value: 22.391264965682506
    - type: nauc_precision_at_100_std
      value: 42.72424514027106
    - type: nauc_precision_at_10_diff1
      value: 3.616065203597004
    - type: nauc_precision_at_10_max
      value: 21.983666160174664
    - type: nauc_precision_at_10_std
      value: 29.4059520720441
    - type: nauc_precision_at_1_diff1
      value: 69.96236855623434
    - type: nauc_precision_at_1_max
      value: 49.448851447506925
    - type: nauc_precision_at_1_std
      value: 2.889004800052033
    - type: nauc_precision_at_20_diff1
      value: 1.0139909003288345
    - type: nauc_precision_at_20_max
      value: 21.586196202262293
    - type: nauc_precision_at_20_std
      value: 34.67062542720318
    - type: nauc_precision_at_3_diff1
      value: 8.864530763513228
    - type: nauc_precision_at_3_max
      value: 22.75139236955371
    - type: nauc_precision_at_3_std
      value: 15.906499760044241
    - type: nauc_precision_at_5_diff1
      value: 6.115146064055562
    - type: nauc_precision_at_5_max
      value: 22.511552769119312
    - type: nauc_precision_at_5_std
      value: 21.404838493866283
    - type: nauc_recall_at_1000_diff1
      value: -3.673616783114743
    - type: nauc_recall_at_1000_max
      value: 23.053922175841222
    - type: nauc_recall_at_1000_std
      value: 49.11991772792807
    - type: nauc_recall_at_100_diff1
      value: -1.2165914296620488
    - type: nauc_recall_at_100_max
      value: 22.391264965682254
    - type: nauc_recall_at_100_std
      value: 42.72424514027085
    - type: nauc_recall_at_10_diff1
      value: 3.6160652035968592
    - type: nauc_recall_at_10_max
      value: 21.983666160174625
    - type: nauc_recall_at_10_std
      value: 29.405952072043952
    - type: nauc_recall_at_1_diff1
      value: 69.96236855623434
    - type: nauc_recall_at_1_max
      value: 49.448851447506925
    - type: nauc_recall_at_1_std
      value: 2.889004800052033
    - type: nauc_recall_at_20_diff1
      value: 1.0139909003285874
    - type: nauc_recall_at_20_max
      value: 21.586196202262176
    - type: nauc_recall_at_20_std
      value: 34.67062542720296
    - type: nauc_recall_at_3_diff1
      value: 8.864530763513235
    - type: nauc_recall_at_3_max
      value: 22.75139236955375
    - type: nauc_recall_at_3_std
      value: 15.906499760044227
    - type: nauc_recall_at_5_diff1
      value: 6.115146064055457
    - type: nauc_recall_at_5_max
      value: 22.51155276911919
    - type: nauc_recall_at_5_std
      value: 21.404838493866148
    - type: ndcg_at_1
      value: 82.082
    - type: ndcg_at_10
      value: 74.175
    - type: ndcg_at_100
      value: 76.818
    - type: ndcg_at_1000
      value: 77.86999999999999
    - type: ndcg_at_20
      value: 75.324
    - type: ndcg_at_3
      value: 69.505
    - type: ndcg_at_5
      value: 72.25399999999999
    - type: precision_at_1
      value: 82.082
    - type: precision_at_10
      value: 15.459999999999999
    - type: precision_at_100
      value: 1.7500000000000002
    - type: precision_at_1000
      value: 0.189
    - type: precision_at_20
      value: 8.099
    - type: precision_at_3
      value: 44.696999999999996
    - type: precision_at_5
      value: 28.992
    - type: recall_at_1
      value: 41.041
    - type: recall_at_10
      value: 77.29899999999999
    - type: recall_at_100
      value: 87.516
    - type: recall_at_1000
      value: 94.428
    - type: recall_at_20
      value: 80.99
    - type: recall_at_3
      value: 67.04599999999999
    - type: recall_at_5
      value: 72.48
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA (default)
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: main_score
      value: 72.099
    - type: map_at_1
      value: 39.993
    - type: map_at_10
      value: 63.906
    - type: map_at_100
      value: 64.768
    - type: map_at_1000
      value: 64.825
    - type: map_at_20
      value: 64.434
    - type: map_at_3
      value: 60.428000000000004
    - type: map_at_5
      value: 62.65500000000001
    - type: mrr_at_1
      value: 79.9864956110736
    - type: mrr_at_10
      value: 85.597317342422
    - type: mrr_at_100
      value: 85.75538451417644
    - type: mrr_at_1000
      value: 85.76054586395492
    - type: mrr_at_20
      value: 85.70043434608681
    - type: mrr_at_3
      value: 84.7085302723385
    - type: mrr_at_5
      value: 85.3006977267612
    - type: nauc_map_at_1000_diff1
      value: 14.879240191611792
    - type: nauc_map_at_1000_max
      value: 17.352504404367227
    - type: nauc_map_at_1000_std
      value: 12.058834112176255
    - type: nauc_map_at_100_diff1
      value: 14.849169805835471
    - type: nauc_map_at_100_max
      value: 17.33232999123778
    - type: nauc_map_at_100_std
      value: 12.077792740295559
    - type: nauc_map_at_10_diff1
      value: 14.739688896718311
    - type: nauc_map_at_10_max
      value: 17.22236218684584
    - type: nauc_map_at_10_std
      value: 11.601003434736638
    - type: nauc_map_at_1_diff1
      value: 65.4983976623848
    - type: nauc_map_at_1_max
      value: 42.1548067294384
    - type: nauc_map_at_1_std
      value: -0.664907685382726
    - type: nauc_map_at_20_diff1
      value: 14.775964716898365
    - type: nauc_map_at_20_max
      value: 17.28407185806239
    - type: nauc_map_at_20_std
      value: 11.938629322344202
    - type: nauc_map_at_3_diff1
      value: 15.187257332075571
    - type: nauc_map_at_3_max
      value: 16.50469797840979
    - type: nauc_map_at_3_std
      value: 8.427502806629832
    - type: nauc_map_at_5_diff1
      value: 14.734331855452067
    - type: nauc_map_at_5_max
      value: 16.996649506768556
    - type: nauc_map_at_5_std
      value: 10.675417416580272
    - type: nauc_mrr_at_1000_diff1
      value: 64.77314045859816
    - type: nauc_mrr_at_1000_max
      value: 45.07640869774897
    - type: nauc_mrr_at_1000_std
      value: 1.1223707370777345
    - type: nauc_mrr_at_100_diff1
      value: 64.7736064468281
    - type: nauc_mrr_at_100_max
      value: 45.081668625794045
    - type: nauc_mrr_at_100_std
      value: 1.1301861065543417
    - type: nauc_mrr_at_10_diff1
      value: 64.7436125478473
    - type: nauc_mrr_at_10_max
      value: 45.17530304621016
    - type: nauc_mrr_at_10_std
      value: 1.1574487279881827
    - type: nauc_mrr_at_1_diff1
      value: 65.4983976623848
    - type: nauc_mrr_at_1_max
      value: 42.1548067294384
    - type: nauc_mrr_at_1_std
      value: -0.664907685382726
    - type: nauc_mrr_at_20_diff1
      value: 64.74897914048353
    - type: nauc_mrr_at_20_max
      value: 45.10718259984782
    - type: nauc_mrr_at_20_std
      value: 1.1414090900637834
    - type: nauc_mrr_at_3_diff1
      value: 64.66047914937114
    - type: nauc_mrr_at_3_max
      value: 45.240654624502135
    - type: nauc_mrr_at_3_std
      value: 0.6018871726391307
    - type: nauc_mrr_at_5_diff1
      value: 64.62465365659278
    - type: nauc_mrr_at_5_max
      value: 45.26782758375944
    - type: nauc_mrr_at_5_std
      value: 0.9729934670795005
    - type: nauc_ndcg_at_1000_diff1
      value: 20.735117506723284
    - type: nauc_ndcg_at_1000_max
      value: 21.973730279574237
    - type: nauc_ndcg_at_1000_std
      value: 14.435511069333268
    - type: nauc_ndcg_at_100_diff1
      value: 19.92424972281059
    - type: nauc_ndcg_at_100_max
      value: 21.46124911457025
    - type: nauc_ndcg_at_100_std
      value: 14.997278102074985
    - type: nauc_ndcg_at_10_diff1
      value: 19.482173354148614
    - type: nauc_ndcg_at_10_max
      value: 21.057780839586314
    - type: nauc_ndcg_at_10_std
      value: 13.183889323902614
    - type: nauc_ndcg_at_1_diff1
      value: 65.4983976623848
    - type: nauc_ndcg_at_1_max
      value: 42.1548067294384
    - type: nauc_ndcg_at_1_std
      value: -0.664907685382726
    - type: nauc_ndcg_at_20_diff1
      value: 19.492746981314262
    - type: nauc_ndcg_at_20_max
      value: 21.17506677843973
    - type: nauc_ndcg_at_20_std
      value: 14.226350927505344
    - type: nauc_ndcg_at_3_diff1
      value: 20.783583144063783
    - type: nauc_ndcg_at_3_max
      value: 20.412720533103773
    - type: nauc_ndcg_at_3_std
      value: 8.1573992813502
    - type: nauc_ndcg_at_5_diff1
      value: 19.678652006506965
    - type: nauc_ndcg_at_5_max
      value: 20.797671396298504
    - type: nauc_ndcg_at_5_std
      value: 11.325414041574488
    - type: nauc_precision_at_1000_diff1
      value: -10.450656807230294
    - type: nauc_precision_at_1000_max
      value: 13.984468023954232
    - type: nauc_precision_at_1000_std
      value: 47.62472479785625
    - type: nauc_precision_at_100_diff1
      value: -4.196473742286918
    - type: nauc_precision_at_100_max
      value: 12.121665049576427
    - type: nauc_precision_at_100_std
      value: 37.19008451156229
    - type: nauc_precision_at_10_diff1
      value: 3.061787271972301
    - type: nauc_precision_at_10_max
      value: 14.242591133970839
    - type: nauc_precision_at_10_std
      value: 22.61377683902424
    - type: nauc_precision_at_1_diff1
      value: 65.4983976623848
    - type: nauc_precision_at_1_max
      value: 42.1548067294384
    - type: nauc_precision_at_1_std
      value: -0.664907685382726
    - type: nauc_precision_at_20_diff1
      value: 0.6113817731563579
    - type: nauc_precision_at_20_max
      value: 13.40678529536442
    - type: nauc_precision_at_20_std
      value: 27.36583188393757
    - type: nauc_precision_at_3_diff1
      value: 9.006850832399767
    - type: nauc_precision_at_3_max
      value: 14.709279058037167
    - type: nauc_precision_at_3_std
      value: 11.083943561368818
    - type: nauc_precision_at_5_diff1
      value: 5.4640694491525785
    - type: nauc_precision_at_5_max
      value: 14.534695725481427
    - type: nauc_precision_at_5_std
      value: 17.261328831180144
    - type: nauc_recall_at_1000_diff1
      value: -10.45065680723015
    - type: nauc_recall_at_1000_max
      value: 13.984468023954296
    - type: nauc_recall_at_1000_std
      value: 47.624724797856494
    - type: nauc_recall_at_100_diff1
      value: -4.1964737422872425
    - type: nauc_recall_at_100_max
      value: 12.121665049576311
    - type: nauc_recall_at_100_std
      value: 37.19008451156221
    - type: nauc_recall_at_10_diff1
      value: 3.061787271972265
    - type: nauc_recall_at_10_max
      value: 14.242591133970848
    - type: nauc_recall_at_10_std
      value: 22.613776839024126
    - type: nauc_recall_at_1_diff1
      value: 65.4983976623848
    - type: nauc_recall_at_1_max
      value: 42.1548067294384
    - type: nauc_recall_at_1_std
      value: -0.664907685382726
    - type: nauc_recall_at_20_diff1
      value: 0.6113817731563769
    - type: nauc_recall_at_20_max
      value: 13.406785295364488
    - type: nauc_recall_at_20_std
      value: 27.365831883937688
    - type: nauc_recall_at_3_diff1
      value: 9.006850832399833
    - type: nauc_recall_at_3_max
      value: 14.709279058037176
    - type: nauc_recall_at_3_std
      value: 11.083943561368827
    - type: nauc_recall_at_5_diff1
      value: 5.464069449152512
    - type: nauc_recall_at_5_max
      value: 14.534695725481386
    - type: nauc_recall_at_5_std
      value: 17.261328831180222
    - type: ndcg_at_1
      value: 79.986
    - type: ndcg_at_10
      value: 72.099
    - type: ndcg_at_100
      value: 75.01100000000001
    - type: ndcg_at_1000
      value: 76.062
    - type: ndcg_at_20
      value: 73.38799999999999
    - type: ndcg_at_3
      value: 67.252
    - type: ndcg_at_5
      value: 70.03399999999999
    - type: precision_at_1
      value: 79.986
    - type: precision_at_10
      value: 15.084
    - type: precision_at_100
      value: 1.735
    - type: precision_at_1000
      value: 0.187
    - type: precision_at_20
      value: 7.957
    - type: precision_at_3
      value: 43.165
    - type: precision_at_5
      value: 28.097
    - type: recall_at_1
      value: 39.993
    - type: recall_at_10
      value: 75.422
    - type: recall_at_100
      value: 86.739
    - type: recall_at_1000
      value: 93.633
    - type: recall_at_20
      value: 79.57499999999999
    - type: recall_at_3
      value: 64.747
    - type: recall_at_5
      value: 70.243
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA (default)
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: train
      type: mteb/hotpotqa
    metrics:
    - type: main_score
      value: 74.675
    - type: map_at_1
      value: 41.071999999999996
    - type: map_at_10
      value: 66.92
    - type: map_at_100
      value: 67.723
    - type: map_at_1000
      value: 67.774
    - type: map_at_20
      value: 67.408
    - type: map_at_3
      value: 63.55499999999999
    - type: map_at_5
      value: 65.704
    - type: mrr_at_1
      value: 82.14470588235294
    - type: mrr_at_10
      value: 87.27400186741363
    - type: mrr_at_100
      value: 87.4140081509131
    - type: mrr_at_1000
      value: 87.41798363724548
    - type: mrr_at_20
      value: 87.36842561587122
    - type: mrr_at_3
      value: 86.50941176470587
    - type: mrr_at_5
      value: 87.00347058823529
    - type: nauc_map_at_1000_diff1
      value: 15.173631052534247
    - type: nauc_map_at_1000_max
      value: 26.068735945434245
    - type: nauc_map_at_1000_std
      value: 16.679793876109372
    - type: nauc_map_at_100_diff1
      value: 15.145622681798832
    - type: nauc_map_at_100_max
      value: 26.05989713486766
    - type: nauc_map_at_100_std
      value: 16.707010441285338
    - type: nauc_map_at_10_diff1
      value: 14.914638256007287
    - type: nauc_map_at_10_max
      value: 25.882443097244483
    - type: nauc_map_at_10_std
      value: 16.268808050707122
    - type: nauc_map_at_1_diff1
      value: 68.99857028038306
    - type: nauc_map_at_1_max
      value: 49.44823319018734
    - type: nauc_map_at_1_std
      value: 3.95480041595882
    - type: nauc_map_at_20_diff1
      value: 15.024824474002042
    - type: nauc_map_at_20_max
      value: 25.979156549532394
    - type: nauc_map_at_20_std
      value: 16.58495990193771
    - type: nauc_map_at_3_diff1
      value: 14.82922429946727
    - type: nauc_map_at_3_max
      value: 24.94644740438124
    - type: nauc_map_at_3_std
      value: 13.163454771602703
    - type: nauc_map_at_5_diff1
      value: 14.786835699591697
    - type: nauc_map_at_5_max
      value: 25.4952477897668
    - type: nauc_map_at_5_std
      value: 15.132801238151277
    - type: nauc_mrr_at_1000_diff1
      value: 68.01504171335921
    - type: nauc_mrr_at_1000_max
      value: 51.87765517862451
    - type: nauc_mrr_at_1000_std
      value: 6.86223778975253
    - type: nauc_mrr_at_100_diff1
      value: 68.01399006752484
    - type: nauc_mrr_at_100_max
      value: 51.88280954265237
    - type: nauc_mrr_at_100_std
      value: 6.873608557329335
    - type: nauc_mrr_at_10_diff1
      value: 67.99091321438537
    - type: nauc_mrr_at_10_max
      value: 51.969521221681624
    - type: nauc_mrr_at_10_std
      value: 6.931166148442037
    - type: nauc_mrr_at_1_diff1
      value: 68.99857028038306
    - type: nauc_mrr_at_1_max
      value: 49.44823319018734
    - type: nauc_mrr_at_1_std
      value: 3.95480041595882
    - type: nauc_mrr_at_20_diff1
      value: 68.01259861100158
    - type: nauc_mrr_at_20_max
      value: 51.92347187092682
    - type: nauc_mrr_at_20_std
      value: 6.916000236458142
    - type: nauc_mrr_at_3_diff1
      value: 67.78455056859933
    - type: nauc_mrr_at_3_max
      value: 51.871123397467976
    - type: nauc_mrr_at_3_std
      value: 6.43509345435153
    - type: nauc_mrr_at_5_diff1
      value: 67.90240615066607
    - type: nauc_mrr_at_5_max
      value: 52.0124881495014
    - type: nauc_mrr_at_5_std
      value: 6.803350773425626
    - type: nauc_ndcg_at_1000_diff1
      value: 21.69891416034566
    - type: nauc_ndcg_at_1000_max
      value: 30.461957789834806
    - type: nauc_ndcg_at_1000_std
      value: 19.18877840309474
    - type: nauc_ndcg_at_100_diff1
      value: 20.7970186296764
    - type: nauc_ndcg_at_100_max
      value: 30.15224012992887
    - type: nauc_ndcg_at_100_std
      value: 19.943169128048474
    - type: nauc_ndcg_at_10_diff1
      value: 19.84268006275167
    - type: nauc_ndcg_at_10_max
      value: 29.484945625149916
    - type: nauc_ndcg_at_10_std
      value: 18.258410671819046
    - type: nauc_ndcg_at_1_diff1
      value: 68.99857028038306
    - type: nauc_ndcg_at_1_max
      value: 49.44823319018734
    - type: nauc_ndcg_at_1_std
      value: 3.95480041595882
    - type: nauc_ndcg_at_20_diff1
      value: 20.04561491289907
    - type: nauc_ndcg_at_20_max
      value: 29.693953898939768
    - type: nauc_ndcg_at_20_std
      value: 19.236240432268765
    - type: nauc_ndcg_at_3_diff1
      value: 20.257610313097572
    - type: nauc_ndcg_at_3_max
      value: 28.337695262101402
    - type: nauc_ndcg_at_3_std
      value: 13.27057009577805
    - type: nauc_ndcg_at_5_diff1
      value: 19.813917540582832
    - type: nauc_ndcg_at_5_max
      value: 28.898934488412642
    - type: nauc_ndcg_at_5_std
      value: 16.037376675812613
    - type: nauc_precision_at_1000_diff1
      value: -2.7630728745432833
    - type: nauc_precision_at_1000_max
      value: 24.273957339049858
    - type: nauc_precision_at_1000_std
      value: 51.174814670874234
    - type: nauc_precision_at_100_diff1
      value: -0.3693685702558231
    - type: nauc_precision_at_100_max
      value: 23.540054418358388
    - type: nauc_precision_at_100_std
      value: 42.86307596340895
    - type: nauc_precision_at_10_diff1
      value: 3.839420261166957
    - type: nauc_precision_at_10_max
      value: 23.33220436834566
    - type: nauc_precision_at_10_std
      value: 27.497642027822938
    - type: nauc_precision_at_1_diff1
      value: 68.99857028038306
    - type: nauc_precision_at_1_max
      value: 49.44823319018734
    - type: nauc_precision_at_1_std
      value: 3.95480041595882
    - type: nauc_precision_at_20_diff1
      value: 2.149278982050884
    - type: nauc_precision_at_20_max
      value: 23.225228919773492
    - type: nauc_precision_at_20_std
      value: 32.583030590092996
    - type: nauc_precision_at_3_diff1
      value: 8.414263763743502
    - type: nauc_precision_at_3_max
      value: 23.266556039522364
    - type: nauc_precision_at_3_std
      value: 16.166789635561578
    - type: nauc_precision_at_5_diff1
      value: 6.100362067031837
    - type: nauc_precision_at_5_max
      value: 23.317092657737902
    - type: nauc_precision_at_5_std
      value: 21.439743834724506
    - type: nauc_recall_at_1000_diff1
      value: -2.763072874542946
    - type: nauc_recall_at_1000_max
      value: 24.273957339050046
    - type: nauc_recall_at_1000_std
      value: 51.17481467087451
    - type: nauc_recall_at_100_diff1
      value: -0.36936857025585346
    - type: nauc_recall_at_100_max
      value: 23.54005441835819
    - type: nauc_recall_at_100_std
      value: 42.86307596340905
    - type: nauc_recall_at_10_diff1
      value: 3.8394202611669916
    - type: nauc_recall_at_10_max
      value: 23.332204368345536
    - type: nauc_recall_at_10_std
      value: 27.497642027822835
    - type: nauc_recall_at_1_diff1
      value: 68.99857028038306
    - type: nauc_recall_at_1_max
      value: 49.44823319018734
    - type: nauc_recall_at_1_std
      value: 3.95480041595882
    - type: nauc_recall_at_20_diff1
      value: 2.1492789820506943
    - type: nauc_recall_at_20_max
      value: 23.22522891977323
    - type: nauc_recall_at_20_std
      value: 32.58303059009287
    - type: nauc_recall_at_3_diff1
      value: 8.414263763743387
    - type: nauc_recall_at_3_max
      value: 23.266556039522314
    - type: nauc_recall_at_3_std
      value: 16.166789635561496
    - type: nauc_recall_at_5_diff1
      value: 6.100362067031725
    - type: nauc_recall_at_5_max
      value: 23.317092657737877
    - type: nauc_recall_at_5_std
      value: 21.43974383472456
    - type: ndcg_at_1
      value: 82.145
    - type: ndcg_at_10
      value: 74.675
    - type: ndcg_at_100
      value: 77.35499999999999
    - type: ndcg_at_1000
      value: 78.31099999999999
    - type: ndcg_at_20
      value: 75.859
    - type: ndcg_at_3
      value: 70.056
    - type: ndcg_at_5
      value: 72.68900000000001
    - type: precision_at_1
      value: 82.145
    - type: precision_at_10
      value: 15.594
    - type: precision_at_100
      value: 1.7670000000000001
    - type: precision_at_1000
      value: 0.189
    - type: precision_at_20
      value: 8.177
    - type: precision_at_3
      value: 45.207
    - type: precision_at_5
      value: 29.199
    - type: recall_at_1
      value: 41.071999999999996
    - type: recall_at_10
      value: 77.968
    - type: recall_at_100
      value: 88.342
    - type: recall_at_1000
      value: 94.636
    - type: recall_at_20
      value: 81.768
    - type: recall_at_3
      value: 67.81099999999999
    - type: recall_at_5
      value: 72.99799999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 91.6404
    - type: ap
      value: 88.06069266911989
    - type: ap_weighted
      value: 88.06069266911989
    - type: f1
      value: 91.63447508338969
    - type: f1_weighted
      value: 91.63447508338966
    - type: main_score
      value: 91.6404
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MSMARCO (default)
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: dev
      type: mteb/msmarco
    metrics:
    - type: main_score
      value: 41.881
    - type: map_at_1
      value: 22.467000000000002
    - type: map_at_10
      value: 34.910999999999994
    - type: map_at_100
      value: 36.061
    - type: map_at_1000
      value: 36.108000000000004
    - type: map_at_20
      value: 35.624
    - type: map_at_3
      value: 30.941999999999997
    - type: map_at_5
      value: 33.263999999999996
    - type: mrr_at_1
      value: 23.08022922636103
    - type: mrr_at_10
      value: 35.50051735116205
    - type: mrr_at_100
      value: 36.59446189817308
    - type: mrr_at_1000
      value: 36.635988914583265
    - type: mrr_at_20
      value: 36.18253329805409
    - type: mrr_at_3
      value: 31.609360076408787
    - type: mrr_at_5
      value: 33.90305635148042
    - type: nauc_map_at_1000_diff1
      value: 35.55451924480011
    - type: nauc_map_at_1000_max
      value: 3.3973484820380984
    - type: nauc_map_at_1000_std
      value: -15.313643259934148
    - type: nauc_map_at_100_diff1
      value: 35.550804246990495
    - type: nauc_map_at_100_max
      value: 3.399807661520924
    - type: nauc_map_at_100_std
      value: -15.275642266336313
    - type: nauc_map_at_10_diff1
      value: 35.5782836837628
    - type: nauc_map_at_10_max
      value: 3.2528940284048993
    - type: nauc_map_at_10_std
      value: -15.969363396756405
    - type: nauc_map_at_1_diff1
      value: 38.48673772459152
    - type: nauc_map_at_1_max
      value: 3.058447908569679
    - type: nauc_map_at_1_std
      value: -14.963393022102997
    - type: nauc_map_at_20_diff1
      value: 35.51677537885897
    - type: nauc_map_at_20_max
      value: 3.3515639340449725
    - type: nauc_map_at_20_std
      value: -15.515763931018828
    - type: nauc_map_at_3_diff1
      value: 35.92227750150707
    - type: nauc_map_at_3_max
      value: 2.8055574560079064
    - type: nauc_map_at_3_std
      value: -16.880504853072285
    - type: nauc_map_at_5_diff1
      value: 35.55198639506613
    - type: nauc_map_at_5_max
      value: 2.9586919269467526
    - type: nauc_map_at_5_std
      value: -16.54701954101431
    - type: nauc_mrr_at_1000_diff1
      value: 35.431696643964436
    - type: nauc_mrr_at_1000_max
      value: 3.413854144953113
    - type: nauc_mrr_at_1000_std
      value: -15.142803785812797
    - type: nauc_mrr_at_100_diff1
      value: 35.426786864620986
    - type: nauc_mrr_at_100_max
      value: 3.4171950444493935
    - type: nauc_mrr_at_100_std
      value: -15.103678118737987
    - type: nauc_mrr_at_10_diff1
      value: 35.420624727408644
    - type: nauc_mrr_at_10_max
      value: 3.322578167282073
    - type: nauc_mrr_at_10_std
      value: -15.720250181753793
    - type: nauc_mrr_at_1_diff1
      value: 38.282779286642096
    - type: nauc_mrr_at_1_max
      value: 2.9904752802636327
    - type: nauc_mrr_at_1_std
      value: -15.138960622677649
    - type: nauc_mrr_at_20_diff1
      value: 35.38506376339875
    - type: nauc_mrr_at_20_max
      value: 3.394154792664457
    - type: nauc_mrr_at_20_std
      value: -15.296898873665988
    - type: nauc_mrr_at_3_diff1
      value: 35.7803854971965
    - type: nauc_mrr_at_3_max
      value: 2.7546109667567733
    - type: nauc_mrr_at_3_std
      value: -16.7760243616548
    - type: nauc_mrr_at_5_diff1
      value: 35.40507525930076
    - type: nauc_mrr_at_5_max
      value: 2.968967051093017
    - type: nauc_mrr_at_5_std
      value: -16.322983362913682
    - type: nauc_ndcg_at_1000_diff1
      value: 34.61165703664126
    - type: nauc_ndcg_at_1000_max
      value: 4.2633988477939315
    - type: nauc_ndcg_at_1000_std
      value: -13.07846493573677
    - type: nauc_ndcg_at_100_diff1
      value: 34.496098679488654
    - type: nauc_ndcg_at_100_max
      value: 4.35416012374578
    - type: nauc_ndcg_at_100_std
      value: -11.701820911709307
    - type: nauc_ndcg_at_10_diff1
      value: 34.510499084561594
    - type: nauc_ndcg_at_10_max
      value: 3.7195988744787765
    - type: nauc_ndcg_at_10_std
      value: -15.20204882975027
    - type: nauc_ndcg_at_1_diff1
      value: 38.282779286642096
    - type: nauc_ndcg_at_1_max
      value: 2.9904752802636327
    - type: nauc_ndcg_at_1_std
      value: -15.138960622677649
    - type: nauc_ndcg_at_20_diff1
      value: 34.28895557191255
    - type: nauc_ndcg_at_20_max
      value: 4.078634149451336
    - type: nauc_ndcg_at_20_std
      value: -13.495634934731186
    - type: nauc_ndcg_at_3_diff1
      value: 35.1825890111415
    - type: nauc_ndcg_at_3_max
      value: 2.6899697916041787
    - type: nauc_ndcg_at_3_std
      value: -17.3200148795559
    - type: nauc_ndcg_at_5_diff1
      value: 34.50553625093832
    - type: nauc_ndcg_at_5_max
      value: 2.9886919040366453
    - type: nauc_ndcg_at_5_std
      value: -16.682910398462134
    - type: nauc_precision_at_1000_diff1
      value: -5.237411685181927
    - type: nauc_precision_at_1000_max
      value: 12.33197477512628
    - type: nauc_precision_at_1000_std
      value: 14.624993194631372
    - type: nauc_precision_at_100_diff1
      value: 12.929312931181103
    - type: nauc_precision_at_100_max
      value: 11.682654496612322
    - type: nauc_precision_at_100_std
      value: 22.44127157890021
    - type: nauc_precision_at_10_diff1
      value: 28.260532585949555
    - type: nauc_precision_at_10_max
      value: 5.053591117400416
    - type: nauc_precision_at_10_std
      value: -11.685872129702071
    - type: nauc_precision_at_1_diff1
      value: 38.282779286642096
    - type: nauc_precision_at_1_max
      value: 2.9904752802636327
    - type: nauc_precision_at_1_std
      value: -15.138960622677649
    - type: nauc_precision_at_20_diff1
      value: 24.082555406455477
    - type: nauc_precision_at_20_max
      value: 7.220785769786994
    - type: nauc_precision_at_20_std
      value: -2.3466420348408876
    - type: nauc_precision_at_3_diff1
      value: 32.2680340644695
    - type: nauc_precision_at_3_max
      value: 2.195269827644658
    - type: nauc_precision_at_3_std
      value: -18.77340802819126
    - type: nauc_precision_at_5_diff1
      value: 30.01850058048678
    - type: nauc_precision_at_5_max
      value: 3.0452445562886243
    - type: nauc_precision_at_5_std
      value: -16.787002738887892
    - type: nauc_recall_at_1000_diff1
      value: 7.940551548703448
    - type: nauc_recall_at_1000_max
      value: 40.70493639275526
    - type: nauc_recall_at_1000_std
      value: 66.21346351313893
    - type: nauc_recall_at_100_diff1
      value: 26.395513427993123
    - type: nauc_recall_at_100_max
      value: 13.850278277490382
    - type: nauc_recall_at_100_std
      value: 31.262749365543495
    - type: nauc_recall_at_10_diff1
      value: 30.810510902525202
    - type: nauc_recall_at_10_max
      value: 5.342768575463394
    - type: nauc_recall_at_10_std
      value: -12.041087579697969
    - type: nauc_recall_at_1_diff1
      value: 38.48673772459152
    - type: nauc_recall_at_1_max
      value: 3.058447908569679
    - type: nauc_recall_at_1_std
      value: -14.963393022102997
    - type: nauc_recall_at_20_diff1
      value: 28.97941173115346
    - type: nauc_recall_at_20_max
      value: 7.387302922786026
    - type: nauc_recall_at_20_std
      value: -2.9701154270124537
    - type: nauc_recall_at_3_diff1
      value: 33.11138786633106
    - type: nauc_recall_at_3_max
      value: 2.3972198714504103
    - type: nauc_recall_at_3_std
      value: -18.444370167091602
    - type: nauc_recall_at_5_diff1
      value: 31.354710954894315
    - type: nauc_recall_at_5_max
      value: 3.0409753924683227
    - type: nauc_recall_at_5_std
      value: -17.003889653830544
    - type: ndcg_at_1
      value: 23.080000000000002
    - type: ndcg_at_10
      value: 41.881
    - type: ndcg_at_100
      value: 47.384
    - type: ndcg_at_1000
      value: 48.563
    - type: ndcg_at_20
      value: 44.394
    - type: ndcg_at_3
      value: 33.819
    - type: ndcg_at_5
      value: 37.951
    - type: precision_at_1
      value: 23.080000000000002
    - type: precision_at_10
      value: 6.619
    - type: precision_at_100
      value: 0.9369999999999999
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_20
      value: 3.836
    - type: precision_at_3
      value: 14.350999999999999
    - type: precision_at_5
      value: 10.705
    - type: recall_at_1
      value: 22.467000000000002
    - type: recall_at_10
      value: 63.363
    - type: recall_at_100
      value: 88.73
    - type: recall_at_1000
      value: 97.726
    - type: recall_at_20
      value: 73.072
    - type: recall_at_3
      value: 41.464
    - type: recall_at_5
      value: 51.367
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MSMARCO (default)
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: test
      type: mteb/msmarco
    metrics:
    - type: main_score
      value: 69.895
    - type: map_at_1
      value: 2.386
    - type: map_at_10
      value: 15.517
    - type: map_at_100
      value: 40.755
    - type: map_at_1000
      value: 48.650999999999996
    - type: map_at_20
      value: 23.866
    - type: map_at_3
      value: 6.593999999999999
    - type: map_at_5
      value: 9.733
    - type: mrr_at_1
      value: 90.69767441860465
    - type: mrr_at_10
      value: 94.26356589147287
    - type: mrr_at_100
      value: 94.26356589147287
    - type: mrr_at_1000
      value: 94.26356589147287
    - type: mrr_at_20
      value: 94.26356589147287
    - type: mrr_at_3
      value: 93.7984496124031
    - type: mrr_at_5
      value: 94.26356589147287
    - type: nauc_map_at_1000_diff1
      value: -17.43619926664674
    - type: nauc_map_at_1000_max
      value: 33.6129902421304
    - type: nauc_map_at_1000_std
      value: 46.534866437148445
    - type: nauc_map_at_100_diff1
      value: -3.4235524401190065
    - type: nauc_map_at_100_max
      value: 20.249118581525174
    - type: nauc_map_at_100_std
      value: 21.211678002623337
    - type: nauc_map_at_10_diff1
      value: 19.868551667849278
    - type: nauc_map_at_10_max
      value: -7.049880879841646
    - type: nauc_map_at_10_std
      value: -15.401797310529073
    - type: nauc_map_at_1_diff1
      value: 33.37422645090001
    - type: nauc_map_at_1_max
      value: -26.28998419171722
    - type: nauc_map_at_1_std
      value: -28.696833028930623
    - type: nauc_map_at_20_diff1
      value: 16.721532586974828
    - type: nauc_map_at_20_max
      value: 5.488066416387458
    - type: nauc_map_at_20_std
      value: -4.928338561410316
    - type: nauc_map_at_3_diff1
      value: 26.596230178724362
    - type: nauc_map_at_3_max
      value: -21.091821185844502
    - type: nauc_map_at_3_std
      value: -27.931616241692335
    - type: nauc_map_at_5_diff1
      value: 26.503416309451893
    - type: nauc_map_at_5_max
      value: -14.966431698877205
    - type: nauc_map_at_5_std
      value: -24.92953418435822
    - type: nauc_mrr_at_1000_diff1
      value: 37.25735469680115
    - type: nauc_mrr_at_1000_max
      value: 58.86319796354405
    - type: nauc_mrr_at_1000_std
      value: 91.72535591220716
    - type: nauc_mrr_at_100_diff1
      value: 37.25735469680115
    - type: nauc_mrr_at_100_max
      value: 58.86319796354405
    - type: nauc_mrr_at_100_std
      value: 91.72535591220716
    - type: nauc_mrr_at_10_diff1
      value: 37.25735469680115
    - type: nauc_mrr_at_10_max
      value: 58.86319796354405
    - type: nauc_mrr_at_10_std
      value: 91.72535591220716
    - type: nauc_mrr_at_1_diff1
      value: 34.671850640708776
    - type: nauc_mrr_at_1_max
      value: 51.21031217917046
    - type: nauc_mrr_at_1_std
      value: 89.79460562505535
    - type: nauc_mrr_at_20_diff1
      value: 37.25735469680115
    - type: nauc_mrr_at_20_max
      value: 58.86319796354405
    - type: nauc_mrr_at_20_std
      value: 91.72535591220716
    - type: nauc_mrr_at_3_diff1
      value: 38.60957957843779
    - type: nauc_mrr_at_3_max
      value: 60.97560743754536
    - type: nauc_mrr_at_3_std
      value: 92.34595421879162
    - type: nauc_mrr_at_5_diff1
      value: 37.25735469680115
    - type: nauc_mrr_at_5_max
      value: 58.86319796354405
    - type: nauc_mrr_at_5_std
      value: 91.72535591220716
    - type: nauc_ndcg_at_1000_diff1
      value: -16.225938948928025
    - type: nauc_ndcg_at_1000_max
      value: 55.89533466517005
    - type: nauc_ndcg_at_1000_std
      value: 55.40479015862836
    - type: nauc_ndcg_at_100_diff1
      value: -4.2505692685100485
    - type: nauc_ndcg_at_100_max
      value: 41.08810853075458
    - type: nauc_ndcg_at_100_std
      value: 51.72941963551418
    - type: nauc_ndcg_at_10_diff1
      value: 0.747121732650285
    - type: nauc_ndcg_at_10_max
      value: 39.232823971742405
    - type: nauc_ndcg_at_10_std
      value: 30.231095222965937
    - type: nauc_ndcg_at_1_diff1
      value: 50.70351721984524
    - type: nauc_ndcg_at_1_max
      value: 22.223151480238055
    - type: nauc_ndcg_at_1_std
      value: -1.6981049298345798
    - type: nauc_ndcg_at_20_diff1
      value: -5.964227909058437
    - type: nauc_ndcg_at_20_max
      value: 41.04081240965169
    - type: nauc_ndcg_at_20_std
      value: 38.124111046791164
    - type: nauc_ndcg_at_3_diff1
      value: 22.642365636430505
    - type: nauc_ndcg_at_3_max
      value: 36.65277646275841
    - type: nauc_ndcg_at_3_std
      value: 13.807981639504055
    - type: nauc_ndcg_at_5_diff1
      value: 13.228770870517279
    - type: nauc_ndcg_at_5_max
      value: 39.26501372019075
    - type: nauc_ndcg_at_5_std
      value: 18.117117619727306
    - type: nauc_precision_at_1000_diff1
      value: -34.34396146066081
    - type: nauc_precision_at_1000_max
      value: 25.35157697994365
    - type: nauc_precision_at_1000_std
      value: 52.692463751897535
    - type: nauc_precision_at_100_diff1
      value: -34.59882373262441
    - type: nauc_precision_at_100_max
      value: 30.38585569564875
    - type: nauc_precision_at_100_std
      value: 55.39043613247343
    - type: nauc_precision_at_10_diff1
      value: -34.84065479839732
    - type: nauc_precision_at_10_max
      value: 52.453330287918234
    - type: nauc_precision_at_10_std
      value: 65.94589958566101
    - type: nauc_precision_at_1_diff1
      value: 34.671850640708776
    - type: nauc_precision_at_1_max
      value: 51.21031217917046
    - type: nauc_precision_at_1_std
      value: 89.79460562505535
    - type: nauc_precision_at_20_diff1
      value: -34.405502025386006
    - type: nauc_precision_at_20_max
      value: 47.22465715601537
    - type: nauc_precision_at_20_std
      value: 60.3767447367751
    - type: nauc_precision_at_3_diff1
      value: -7.395035257468793
    - type: nauc_precision_at_3_max
      value: 62.69785319929072
    - type: nauc_precision_at_3_std
      value: 67.15720558808125
    - type: nauc_precision_at_5_diff1
      value: -19.659532277774154
    - type: nauc_precision_at_5_max
      value: 65.88294876723467
    - type: nauc_precision_at_5_std
      value: 65.5071257264847
    - type: nauc_recall_at_1000_diff1
      value: -32.13151178260713
    - type: nauc_recall_at_1000_max
      value: 49.599798672364024
    - type: nauc_recall_at_1000_std
      value: 53.416414623207245
    - type: nauc_recall_at_100_diff1
      value: 2.2830012629669367
    - type: nauc_recall_at_100_max
      value: 20.72697656877468
    - type: nauc_recall_at_100_std
      value: 15.090940745210233
    - type: nauc_recall_at_10_diff1
      value: 19.967019350754683
    - type: nauc_recall_at_10_max
      value: -10.459789162236417
    - type: nauc_recall_at_10_std
      value: -18.89446359106782
    - type: nauc_recall_at_1_diff1
      value: 33.37422645090001
    - type: nauc_recall_at_1_max
      value: -26.28998419171722
    - type: nauc_recall_at_1_std
      value: -28.696833028930623
    - type: nauc_recall_at_20_diff1
      value: 17.31230551930378
    - type: nauc_recall_at_20_max
      value: 3.20695402833611
    - type: nauc_recall_at_20_std
      value: -8.361923242107272
    - type: nauc_recall_at_3_diff1
      value: 26.874491125503315
    - type: nauc_recall_at_3_max
      value: -22.372781558886633
    - type: nauc_recall_at_3_std
      value: -30.08475617025354
    - type: nauc_recall_at_5_diff1
      value: 26.425992230237465
    - type: nauc_recall_at_5_max
      value: -17.053828088435072
    - type: nauc_recall_at_5_std
      value: -27.797398066593537
    - type: ndcg_at_1
      value: 74.806
    - type: ndcg_at_10
      value: 69.895
    - type: ndcg_at_100
      value: 64.736
    - type: ndcg_at_1000
      value: 71.563
    - type: ndcg_at_20
      value: 67.916
    - type: ndcg_at_3
      value: 72.72800000000001
    - type: ndcg_at_5
      value: 72.298
    - type: precision_at_1
      value: 90.69800000000001
    - type: precision_at_10
      value: 78.605
    - type: precision_at_100
      value: 38.256
    - type: precision_at_1000
      value: 6.914
    - type: precision_at_20
      value: 70.814
    - type: precision_at_3
      value: 86.047
    - type: precision_at_5
      value: 84.651
    - type: recall_at_1
      value: 2.386
    - type: recall_at_10
      value: 16.739
    - type: recall_at_100
      value: 52.782
    - type: recall_at_1000
      value: 77.948
    - type: recall_at_20
      value: 26.564
    - type: recall_at_3
      value: 6.789000000000001
    - type: recall_at_5
      value: 10.192
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MSMARCO (default)
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: train
      type: mteb/msmarco
    metrics:
    - type: main_score
      value: 39.287
    - type: map_at_1
      value: 20.312
    - type: map_at_10
      value: 32.37
    - type: map_at_100
      value: 33.617999999999995
    - type: map_at_1000
      value: 33.667
    - type: map_at_20
      value: 33.141999999999996
    - type: map_at_3
      value: 28.419
    - type: map_at_5
      value: 30.677
    - type: mrr_at_1
      value: 20.88106112272065
    - type: mrr_at_10
      value: 32.88347561288713
    - type: mrr_at_100
      value: 34.079369127830056
    - type: mrr_at_1000
      value: 34.12286416716751
    - type: mrr_at_20
      value: 33.6284955497779
    - type: mrr_at_3
      value: 29.00577074622038
    - type: mrr_at_5
      value: 31.230424233024944
    - type: nauc_map_at_1000_diff1
      value: 34.02708673784959
    - type: nauc_map_at_1000_max
      value: -0.13774596315365284
    - type: nauc_map_at_1000_std
      value: -14.811669105922384
    - type: nauc_map_at_100_diff1
      value: 34.01930820880688
    - type: nauc_map_at_100_max
      value: -0.1347868034897845
    - type: nauc_map_at_100_std
      value: -14.772649407858864
    - type: nauc_map_at_10_diff1
      value: 33.96158417816836
    - type: nauc_map_at_10_max
      value: -0.3136135162999447
    - type: nauc_map_at_10_std
      value: -15.444045950700714
    - type: nauc_map_at_1_diff1
      value: 37.58205211162927
    - type: nauc_map_at_1_max
      value: -0.4822908400800713
    - type: nauc_map_at_1_std
      value: -15.470046110078922
    - type: nauc_map_at_20_diff1
      value: 33.98271018950918
    - type: nauc_map_at_20_max
      value: -0.21381571255200063
    - type: nauc_map_at_20_std
      value: -15.007378462657424
    - type: nauc_map_at_3_diff1
      value: 34.289832746358385
    - type: nauc_map_at_3_max
      value: -0.5002033864794293
    - type: nauc_map_at_3_std
      value: -16.202034438595152
    - type: nauc_map_at_5_diff1
      value: 34.00117071654728
    - type: nauc_map_at_5_max
      value: -0.45851793692290926
    - type: nauc_map_at_5_std
      value: -16.006184527594332
    - type: nauc_mrr_at_1000_diff1
      value: 33.984976772028844
    - type: nauc_mrr_at_1000_max
      value: -0.1529354207124242
    - type: nauc_mrr_at_1000_std
      value: -14.857766881343624
    - type: nauc_mrr_at_100_diff1
      value: 33.97715243824301
    - type: nauc_mrr_at_100_max
      value: -0.14868509934664242
    - type: nauc_mrr_at_100_std
      value: -14.819185948867908
    - type: nauc_mrr_at_10_diff1
      value: 33.9073996451901
    - type: nauc_mrr_at_10_max
      value: -0.3117834117567206
    - type: nauc_mrr_at_10_std
      value: -15.447133275926591
    - type: nauc_mrr_at_1_diff1
      value: 37.569117720003305
    - type: nauc_mrr_at_1_max
      value: -0.4402285765126485
    - type: nauc_mrr_at_1_std
      value: -15.610329778824116
    - type: nauc_mrr_at_20_diff1
      value: 33.93531912336384
    - type: nauc_mrr_at_20_max
      value: -0.21832751838659756
    - type: nauc_mrr_at_20_std
      value: -15.02826142229628
    - type: nauc_mrr_at_3_diff1
      value: 34.233342147328905
    - type: nauc_mrr_at_3_max
      value: -0.48966505992824105
    - type: nauc_mrr_at_3_std
      value: -16.24404416215297
    - type: nauc_mrr_at_5_diff1
      value: 33.936224279069286
    - type: nauc_mrr_at_5_max
      value: -0.4505343004388219
    - type: nauc_mrr_at_5_std
      value: -16.009358996271995
    - type: nauc_ndcg_at_1000_diff1
      value: 33.15636942116579
    - type: nauc_ndcg_at_1000_max
      value: 0.7421529032280344
    - type: nauc_ndcg_at_1000_std
      value: -12.573458200734184
    - type: nauc_ndcg_at_100_diff1
      value: 32.93005052778217
    - type: nauc_ndcg_at_100_max
      value: 0.9174493718835769
    - type: nauc_ndcg_at_100_std
      value: -11.171269358523292
    - type: nauc_ndcg_at_10_diff1
      value: 32.702296942276526
    - type: nauc_ndcg_at_10_max
      value: -0.09434815260748751
    - type: nauc_ndcg_at_10_std
      value: -14.584325513499733
    - type: nauc_ndcg_at_1_diff1
      value: 37.58713933791024
    - type: nauc_ndcg_at_1_max
      value: -0.4513949591167018
    - type: nauc_ndcg_at_1_std
      value: -15.609650942411912
    - type: nauc_ndcg_at_20_diff1
      value: 32.73010631865281
    - type: nauc_ndcg_at_20_max
      value: 0.28286295130856637
    - type: nauc_ndcg_at_20_std
      value: -12.91199724170651
    - type: nauc_ndcg_at_3_diff1
      value: 33.376023670753284
    - type: nauc_ndcg_at_3_max
      value: -0.5120382325774017
    - type: nauc_ndcg_at_3_std
      value: -16.37620688280034
    - type: nauc_ndcg_at_5_diff1
      value: 32.84453673758015
    - type: nauc_ndcg_at_5_max
      value: -0.4424535321329695
    - type: nauc_ndcg_at_5_std
      value: -15.986073718543075
    - type: nauc_precision_at_1000_diff1
      value: -2.05172207477867
    - type: nauc_precision_at_1000_max
      value: 11.420451556771813
    - type: nauc_precision_at_1000_std
      value: 13.013500055223338
    - type: nauc_precision_at_100_diff1
      value: 14.09591129638288
    - type: nauc_precision_at_100_max
      value: 10.301532890390265
    - type: nauc_precision_at_100_std
      value: 21.262673040909597
    - type: nauc_precision_at_10_diff1
      value: 26.861179153662277
    - type: nauc_precision_at_10_max
      value: 0.9328475133208457
    - type: nauc_precision_at_10_std
      value: -10.923443610237937
    - type: nauc_precision_at_1_diff1
      value: 37.58713933791024
    - type: nauc_precision_at_1_max
      value: -0.4513949591167018
    - type: nauc_precision_at_1_std
      value: -15.609650942411912
    - type: nauc_precision_at_20_diff1
      value: 24.328515569316732
    - type: nauc_precision_at_20_max
      value: 2.876122000952972
    - type: nauc_precision_at_20_std
      value: -2.33467622450143
    - type: nauc_precision_at_3_diff1
      value: 30.578927129819753
    - type: nauc_precision_at_3_max
      value: -0.42632757194706555
    - type: nauc_precision_at_3_std
      value: -16.788412743765186
    - type: nauc_precision_at_5_diff1
      value: 28.78020642240962
    - type: nauc_precision_at_5_max
      value: -0.2124025605546784
    - type: nauc_precision_at_5_std
      value: -15.67344805195943
    - type: nauc_recall_at_1000_diff1
      value: 14.944369342374936
    - type: nauc_recall_at_1000_max
      value: 46.83432685416887
    - type: nauc_recall_at_1000_std
      value: 69.28042589318784
    - type: nauc_recall_at_100_diff1
      value: 24.745870493773193
    - type: nauc_recall_at_100_max
      value: 13.558884583015281
    - type: nauc_recall_at_100_std
      value: 31.59926593228638
    - type: nauc_recall_at_10_diff1
      value: 28.564011002637212
    - type: nauc_recall_at_10_max
      value: 0.6794665651327308
    - type: nauc_recall_at_10_std
      value: -11.184026264546878
    - type: nauc_recall_at_1_diff1
      value: 37.58205211162927
    - type: nauc_recall_at_1_max
      value: -0.4822908400800713
    - type: nauc_recall_at_1_std
      value: -15.470046110078922
    - type: nauc_recall_at_20_diff1
      value: 27.72144102460605
    - type: nauc_recall_at_20_max
      value: 2.6132011820945884
    - type: nauc_recall_at_20_std
      value: -2.461755722295994
    - type: nauc_recall_at_3_diff1
      value: 30.958109485805675
    - type: nauc_recall_at_3_max
      value: -0.5576168684477084
    - type: nauc_recall_at_3_std
      value: -16.72079877980838
    - type: nauc_recall_at_5_diff1
      value: 29.588704776525393
    - type: nauc_recall_at_5_max
      value: -0.4055192968984154
    - type: nauc_recall_at_5_std
      value: -15.750524291373111
    - type: ndcg_at_1
      value: 20.877000000000002
    - type: ndcg_at_10
      value: 39.287
    - type: ndcg_at_100
      value: 45.316
    - type: ndcg_at_1000
      value: 46.52
    - type: ndcg_at_20
      value: 42.028999999999996
    - type: ndcg_at_3
      value: 31.233
    - type: ndcg_at_5
      value: 35.259
    - type: precision_at_1
      value: 20.877000000000002
    - type: precision_at_10
      value: 6.327000000000001
    - type: precision_at_100
      value: 0.9329999999999999
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_20
      value: 3.7310000000000003
    - type: precision_at_3
      value: 13.379
    - type: precision_at_5
      value: 10.065
    - type: recall_at_1
      value: 20.312
    - type: recall_at_10
      value: 60.748999999999995
    - type: recall_at_100
      value: 88.682
    - type: recall_at_1000
      value: 97.867
    - type: recall_at_20
      value: 71.411
    - type: recall_at_3
      value: 38.800000000000004
    - type: recall_at_5
      value: 48.483
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 93.18741450068397
    - type: f1
      value: 93.0238595381845
    - type: f1_weighted
      value: 93.17789324951269
    - type: main_score
      value: 93.18741450068397
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: validation
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 93.05145413870247
    - type: f1
      value: 92.99732266407732
    - type: f1_weighted
      value: 93.02588804838254
    - type: main_score
      value: 93.05145413870247
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 67.33470132238944
    - type: f1
      value: 48.97680766700152
    - type: f1_weighted
      value: 69.63742750869805
    - type: main_score
      value: 67.33470132238944
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: validation
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 67.76733780760627
    - type: f1
      value: 48.841507782489195
    - type: f1_weighted
      value: 70.48620980474442
    - type: main_score
      value: 67.76733780760627
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 72.4310692669805
    - type: f1
      value: 70.33600790276014
    - type: f1_weighted
      value: 71.41893477886055
    - type: main_score
      value: 72.4310692669805
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 73.4284308903099
    - type: f1
      value: 69.55956726857646
    - type: f1_weighted
      value: 72.15631882777167
    - type: main_score
      value: 73.4284308903099
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 76.78883658372561
    - type: f1
      value: 76.32136975183587
    - type: f1_weighted
      value: 76.595264995014
    - type: main_score
      value: 76.78883658372561
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 77.03885882931628
    - type: f1
      value: 76.31184523539754
    - type: f1_weighted
      value: 76.88960030513515
    - type: main_score
      value: 77.03885882931628
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P (default)
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 33.095522581541175
    - type: v_measure
      value: 33.095522581541175
    - type: v_measure_std
      value: 1.2733644358152183
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S (default)
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 31.06849440193581
    - type: v_measure
      value: 31.06849440193581
    - type: v_measure_std
      value: 1.6047314419984595
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking (default)
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
      split: test
      type: mteb/mind_small
    metrics:
    - type: main_score
      value: 31.29908728873086
    - type: map
      value: 31.29908728873086
    - type: mrr
      value: 32.39123019117521
    - type: nAUC_map_diff1
      value: 13.066848043751357
    - type: nAUC_map_max
      value: -21.421847351002597
    - type: nAUC_map_std
      value: -1.6918937775056007
    - type: nAUC_mrr_diff1
      value: 12.280185578076129
    - type: nAUC_mrr_max
      value: -16.139433517987133
    - type: nAUC_mrr_std
      value: -0.23907632474680363
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB NFCorpus (default)
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: main_score
      value: 35.509
    - type: map_at_1
      value: 5.508
    - type: map_at_10
      value: 13.014999999999999
    - type: map_at_100
      value: 16.342000000000002
    - type: map_at_1000
      value: 17.797
    - type: map_at_20
      value: 14.456
    - type: map_at_3
      value: 9.363000000000001
    - type: map_at_5
      value: 11.064
    - type: mrr_at_1
      value: 45.51083591331269
    - type: mrr_at_10
      value: 54.5795862204531
    - type: mrr_at_100
      value: 55.07630032637193
    - type: mrr_at_1000
      value: 55.127586714933805
    - type: mrr_at_20
      value: 54.90781971103837
    - type: mrr_at_3
      value: 52.32198142414861
    - type: mrr_at_5
      value: 53.74613003095975
    - type: nauc_map_at_1000_diff1
      value: 24.501330360153915
    - type: nauc_map_at_1000_max
      value: 33.06045409371139
    - type: nauc_map_at_1000_std
      value: 19.95230416435316
    - type: nauc_map_at_100_diff1
      value: 25.806053286220532
    - type: nauc_map_at_100_max
      value: 31.933709402264153
    - type: nauc_map_at_100_std
      value: 15.842452059972015
    - type: nauc_map_at_10_diff1
      value: 29.890503647724593
    - type: nauc_map_at_10_max
      value: 25.92830734236527
    - type: nauc_map_at_10_std
      value: 3.6250471128132804
    - type: nauc_map_at_1_diff1
      value: 50.389087879996865
    - type: nauc_map_at_1_max
      value: 20.95986174718729
    - type: nauc_map_at_1_std
      value: -5.41570803338871
    - type: nauc_map_at_20_diff1
      value: 27.444531905945162
    - type: nauc_map_at_20_max
      value: 28.660078098188745
    - type: nauc_map_at_20_std
      value: 8.44788718797198
    - type: nauc_map_at_3_diff1
      value: 37.92764614538618
    - type: nauc_map_at_3_max
      value: 20.65857273684232
    - type: nauc_map_at_3_std
      value: -6.143600629025448
    - type: nauc_map_at_5_diff1
      value: 34.81301402702416
    - type: nauc_map_at_5_max
      value: 23.1193138262864
    - type: nauc_map_at_5_std
      value: -1.7057107446005662
    - type: nauc_mrr_at_1000_diff1
      value: 28.19968199215303
    - type: nauc_mrr_at_1000_max
      value: 46.82195714140159
    - type: nauc_mrr_at_1000_std
      value: 31.68998255433254
    - type: nauc_mrr_at_100_diff1
      value: 28.23773638204092
    - type: nauc_mrr_at_100_max
      value: 46.867704940087
    - type: nauc_mrr_at_100_std
      value: 31.72723785491753
    - type: nauc_mrr_at_10_diff1
      value: 28.235449464678208
    - type: nauc_mrr_at_10_max
      value: 46.757000930146255
    - type: nauc_mrr_at_10_std
      value: 31.38607887979623
    - type: nauc_mrr_at_1_diff1
      value: 30.395863641073404
    - type: nauc_mrr_at_1_max
      value: 39.14603700466295
    - type: nauc_mrr_at_1_std
      value: 22.81299502437437
    - type: nauc_mrr_at_20_diff1
      value: 28.26836846663423
    - type: nauc_mrr_at_20_max
      value: 46.71036119122077
    - type: nauc_mrr_at_20_std
      value: 31.717717995472462
    - type: nauc_mrr_at_3_diff1
      value: 27.677977469638744
    - type: nauc_mrr_at_3_max
      value: 46.281885617180905
    - type: nauc_mrr_at_3_std
      value: 29.971954604398306
    - type: nauc_mrr_at_5_diff1
      value: 28.002295498470435
    - type: nauc_mrr_at_5_max
      value: 46.24599903705559
    - type: nauc_mrr_at_5_std
      value: 30.64406412426167
    - type: nauc_ndcg_at_1000_diff1
      value: 23.52189648298028
    - type: nauc_ndcg_at_1000_max
      value: 48.84815340128893
    - type: nauc_ndcg_at_1000_std
      value: 38.191275632053504
    - type: nauc_ndcg_at_100_diff1
      value: 24.241636067072005
    - type: nauc_ndcg_at_100_max
      value: 44.044030318408616
    - type: nauc_ndcg_at_100_std
      value: 33.08892120061157
    - type: nauc_ndcg_at_10_diff1
      value: 19.38875035508853
    - type: nauc_ndcg_at_10_max
      value: 39.741010776186656
    - type: nauc_ndcg_at_10_std
      value: 31.608748238315908
    - type: nauc_ndcg_at_1_diff1
      value: 31.62521740234213
    - type: nauc_ndcg_at_1_max
      value: 37.777292135533955
    - type: nauc_ndcg_at_1_std
      value: 23.13720120267271
    - type: nauc_ndcg_at_20_diff1
      value: 21.084936669355745
    - type: nauc_ndcg_at_20_max
      value: 40.54909713178013
    - type: nauc_ndcg_at_20_std
      value: 32.197062113529576
    - type: nauc_ndcg_at_3_diff1
      value: 24.011090519352297
    - type: nauc_ndcg_at_3_max
      value: 41.390403583726155
    - type: nauc_ndcg_at_3_std
      value: 25.970801370304663
    - type: nauc_ndcg_at_5_diff1
      value: 21.665450103655758
    - type: nauc_ndcg_at_5_max
      value: 41.31692759970914
    - type: nauc_ndcg_at_5_std
      value: 28.27222783671603
    - type: nauc_precision_at_1000_diff1
      value: -12.949662625593387
    - type: nauc_precision_at_1000_max
      value: 9.813067200754695
    - type: nauc_precision_at_1000_std
      value: 40.89419595054123
    - type: nauc_precision_at_100_diff1
      value: -8.788626197601692
    - type: nauc_precision_at_100_max
      value: 24.009165542236552
    - type: nauc_precision_at_100_std
      value: 52.03060008921234
    - type: nauc_precision_at_10_diff1
      value: -0.8821033318569177
    - type: nauc_precision_at_10_max
      value: 36.63377864059687
    - type: nauc_precision_at_10_std
      value: 41.728479740505605
    - type: nauc_precision_at_1_diff1
      value: 30.395863641073404
    - type: nauc_precision_at_1_max
      value: 39.14603700466295
    - type: nauc_precision_at_1_std
      value: 22.81299502437437
    - type: nauc_precision_at_20_diff1
      value: -4.247170694530449
    - type: nauc_precision_at_20_max
      value: 34.1717839314797
    - type: nauc_precision_at_20_std
      value: 46.95915867262384
    - type: nauc_precision_at_3_diff1
      value: 14.08549588334381
    - type: nauc_precision_at_3_max
      value: 41.78305711419503
    - type: nauc_precision_at_3_std
      value: 29.937750126808016
    - type: nauc_precision_at_5_diff1
      value: 6.795675986788425
    - type: nauc_precision_at_5_max
      value: 41.1649623002547
    - type: nauc_precision_at_5_std
      value: 35.10676757427974
    - type: nauc_recall_at_1000_diff1
      value: 9.323813197352594
    - type: nauc_recall_at_1000_max
      value: 26.561710670307797
    - type: nauc_recall_at_1000_std
      value: 27.567182664914775
    - type: nauc_recall_at_100_diff1
      value: 19.40746686768132
    - type: nauc_recall_at_100_max
      value: 31.43872311644064
    - type: nauc_recall_at_100_std
      value: 22.723757402094883
    - type: nauc_recall_at_10_diff1
      value: 25.54082922198322
    - type: nauc_recall_at_10_max
      value: 22.018853511961083
    - type: nauc_recall_at_10_std
      value: 4.299087738075515
    - type: nauc_recall_at_1_diff1
      value: 50.389087879996865
    - type: nauc_recall_at_1_max
      value: 20.95986174718729
    - type: nauc_recall_at_1_std
      value: -5.41570803338871
    - type: nauc_recall_at_20_diff1
      value: 23.338815663373357
    - type: nauc_recall_at_20_max
      value: 23.350885868547458
    - type: nauc_recall_at_20_std
      value: 8.049814823974602
    - type: nauc_recall_at_3_diff1
      value: 33.134066342544145
    - type: nauc_recall_at_3_max
      value: 18.539807748844968
    - type: nauc_recall_at_3_std
      value: -5.923909673276145
    - type: nauc_recall_at_5_diff1
      value: 29.55575014531457
    - type: nauc_recall_at_5_max
      value: 19.067988699284534
    - type: nauc_recall_at_5_std
      value: -0.8407775036491218
    - type: ndcg_at_1
      value: 43.808
    - type: ndcg_at_10
      value: 35.509
    - type: ndcg_at_100
      value: 31.676
    - type: ndcg_at_1000
      value: 40.543
    - type: ndcg_at_20
      value: 32.988
    - type: ndcg_at_3
      value: 40.376
    - type: ndcg_at_5
      value: 38.41
    - type: precision_at_1
      value: 45.511
    - type: precision_at_10
      value: 26.811
    - type: precision_at_100
      value: 8.056000000000001
    - type: precision_at_1000
      value: 2.098
    - type: precision_at_20
      value: 19.505
    - type: precision_at_3
      value: 38.080000000000005
    - type: precision_at_5
      value: 33.437
    - type: recall_at_1
      value: 5.508
    - type: recall_at_10
      value: 17.319000000000003
    - type: recall_at_100
      value: 31.294
    - type: recall_at_1000
      value: 63.275999999999996
    - type: recall_at_20
      value: 21.431
    - type: recall_at_3
      value: 10.473
    - type: recall_at_5
      value: 13.507
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ (default)
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: main_score
      value: 49.393
    - type: map_at_1
      value: 26.849
    - type: map_at_10
      value: 41.499
    - type: map_at_100
      value: 42.653
    - type: map_at_1000
      value: 42.684
    - type: map_at_20
      value: 42.243
    - type: map_at_3
      value: 36.882999999999996
    - type: map_at_5
      value: 39.555
    - type: mrr_at_1
      value: 30.446118192352262
    - type: mrr_at_10
      value: 44.00585581857308
    - type: mrr_at_100
      value: 44.90568334013942
    - type: mrr_at_1000
      value: 44.927318173677044
    - type: mrr_at_20
      value: 44.606647073916015
    - type: mrr_at_3
      value: 40.02510621861723
    - type: mrr_at_5
      value: 42.41067979915025
    - type: nauc_map_at_1000_diff1
      value: 31.651453391622358
    - type: nauc_map_at_1000_max
      value: 21.072274916232775
    - type: nauc_map_at_1000_std
      value: -4.166680453231419
    - type: nauc_map_at_100_diff1
      value: 31.64962254039646
    - type: nauc_map_at_100_max
      value: 21.098240383541132
    - type: nauc_map_at_100_std
      value: -4.131604331386804
    - type: nauc_map_at_10_diff1
      value: 31.766862600658698
    - type: nauc_map_at_10_max
      value: 21.010891364290753
    - type: nauc_map_at_10_std
      value: -4.708084775930258
    - type: nauc_map_at_1_diff1
      value: 33.32708116835102
    - type: nauc_map_at_1_max
      value: 16.533091238015647
    - type: nauc_map_at_1_std
      value: -5.473056333831887
    - type: nauc_map_at_20_diff1
      value: 31.651686475476943
    - type: nauc_map_at_20_max
      value: 21.118504172703588
    - type: nauc_map_at_20_std
      value: -4.266813330654076
    - type: nauc_map_at_3_diff1
      value: 31.00533525886582
    - type: nauc_map_at_3_max
      value: 19.147198618391343
    - type: nauc_map_at_3_std
      value: -5.813774751421132
    - type: nauc_map_at_5_diff1
      value: 31.35355732909234
    - type: nauc_map_at_5_max
      value: 20.164291644935563
    - type: nauc_map_at_5_std
      value: -5.484865685870952
    - type: nauc_mrr_at_1000_diff1
      value: 31.2911953834966
    - type: nauc_mrr_at_1000_max
      value: 20.98587622652489
    - type: nauc_mrr_at_1000_std
      value: -2.899993822246
    - type: nauc_mrr_at_100_diff1
      value: 31.291944529588978
    - type: nauc_mrr_at_100_max
      value: 21.005023374269047
    - type: nauc_mrr_at_100_std
      value: -2.873367683133069
    - type: nauc_mrr_at_10_diff1
      value: 31.34953406118716
    - type: nauc_mrr_at_10_max
      value: 21.090610712235293
    - type: nauc_mrr_at_10_std
      value: -3.0680385450871865
    - type: nauc_mrr_at_1_diff1
      value: 33.28395799775457
    - type: nauc_mrr_at_1_max
      value: 17.5779149107383
    - type: nauc_mrr_at_1_std
      value: -4.09778735624495
    - type: nauc_mrr_at_20_diff1
      value: 31.26673427403389
    - type: nauc_mrr_at_20_max
      value: 21.065827511367623
    - type: nauc_mrr_at_20_std
      value: -2.9368911795293955
    - type: nauc_mrr_at_3_diff1
      value: 30.940055172744103
    - type: nauc_mrr_at_3_max
      value: 19.798185385046573
    - type: nauc_mrr_at_3_std
      value: -4.064157829412906
    - type: nauc_mrr_at_5_diff1
      value: 31.02626997196326
    - type: nauc_mrr_at_5_max
      value: 20.619867130693375
    - type: nauc_mrr_at_5_std
      value: -3.621718540966316
    - type: nauc_ndcg_at_1000_diff1
      value: 31.215275891803834
    - type: nauc_ndcg_at_1000_max
      value: 23.038486093151146
    - type: nauc_ndcg_at_1000_std
      value: -1.703062891132552
    - type: nauc_ndcg_at_100_diff1
      value: 31.222739143287704
    - type: nauc_ndcg_at_100_max
      value: 23.73579897144862
    - type: nauc_ndcg_at_100_std
      value: -0.7280084629042225
    - type: nauc_ndcg_at_10_diff1
      value: 31.552059739538358
    - type: nauc_ndcg_at_10_max
      value: 23.663866950433963
    - type: nauc_ndcg_at_10_std
      value: -2.8203583845097455
    - type: nauc_ndcg_at_1_diff1
      value: 33.28395799775457
    - type: nauc_ndcg_at_1_max
      value: 17.5779149107383
    - type: nauc_ndcg_at_1_std
      value: -4.09778735624495
    - type: nauc_ndcg_at_20_diff1
      value: 31.115573156536808
    - type: nauc_ndcg_at_20_max
      value: 23.91556914404219
    - type: nauc_ndcg_at_20_std
      value: -1.5512740313611486
    - type: nauc_ndcg_at_3_diff1
      value: 30.182801126285153
    - type: nauc_ndcg_at_3_max
      value: 20.116992880379968
    - type: nauc_ndcg_at_3_std
      value: -5.270323067103204
    - type: nauc_ndcg_at_5_diff1
      value: 30.55855867246541
    - type: nauc_ndcg_at_5_max
      value: 21.854891798578514
    - type: nauc_ndcg_at_5_std
      value: -4.621054609051083
    - type: nauc_precision_at_1000_diff1
      value: -1.2677610563440622
    - type: nauc_precision_at_1000_max
      value: 10.306514334211938
    - type: nauc_precision_at_1000_std
      value: 13.52311200877095
    - type: nauc_precision_at_100_diff1
      value: 4.584881683104716
    - type: nauc_precision_at_100_max
      value: 19.05218376135677
    - type: nauc_precision_at_100_std
      value: 19.53317534358223
    - type: nauc_precision_at_10_diff1
      value: 20.668826405226238
    - type: nauc_precision_at_10_max
      value: 27.133486139333527
    - type: nauc_precision_at_10_std
      value: 6.507236892401218
    - type: nauc_precision_at_1_diff1
      value: 33.28395799775457
    - type: nauc_precision_at_1_max
      value: 17.5779149107383
    - type: nauc_precision_at_1_std
      value: -4.09778735624495
    - type: nauc_precision_at_20_diff1
      value: 14.220253768827485
    - type: nauc_precision_at_20_max
      value: 25.76903982782269
    - type: nauc_precision_at_20_std
      value: 13.332493634341546
    - type: nauc_precision_at_3_diff1
      value: 25.11865756124606
    - type: nauc_precision_at_3_max
      value: 22.659692088129788
    - type: nauc_precision_at_3_std
      value: -2.4562156265188646
    - type: nauc_precision_at_5_diff1
      value: 23.14757206487534
    - type: nauc_precision_at_5_max
      value: 24.626603388946382
    - type: nauc_precision_at_5_std
      value: -0.3684391495744226
    - type: nauc_recall_at_1000_diff1
      value: 18.253568539360202
    - type: nauc_recall_at_1000_max
      value: 69.97593556184775
    - type: nauc_recall_at_1000_std
      value: 67.03053194965779
    - type: nauc_recall_at_100_diff1
      value: 27.49214266284193
    - type: nauc_recall_at_100_max
      value: 52.8893274817214
    - type: nauc_recall_at_100_std
      value: 41.90088287480938
    - type: nauc_recall_at_10_diff1
      value: 30.033274268188283
    - type: nauc_recall_at_10_max
      value: 32.423763247028035
    - type: nauc_recall_at_10_std
      value: 2.83469868226926
    - type: nauc_recall_at_1_diff1
      value: 33.32708116835102
    - type: nauc_recall_at_1_max
      value: 16.533091238015647
    - type: nauc_recall_at_1_std
      value: -5.473056333831887
    - type: nauc_recall_at_20_diff1
      value: 27.482504671207547
    - type: nauc_recall_at_20_max
      value: 36.766903843277824
    - type: nauc_recall_at_20_std
      value: 11.285869127910257
    - type: nauc_recall_at_3_diff1
      value: 26.871897458882167
    - type: nauc_recall_at_3_max
      value: 21.40857537556137
    - type: nauc_recall_at_3_std
      value: -5.177974131117242
    - type: nauc_recall_at_5_diff1
      value: 27.05417164774647
    - type: nauc_recall_at_5_max
      value: 25.54051973421125
    - type: nauc_recall_at_5_std
      value: -3.6239708422249772
    - type: ndcg_at_1
      value: 30.446
    - type: ndcg_at_10
      value: 49.393
    - type: ndcg_at_100
      value: 54.32900000000001
    - type: ndcg_at_1000
      value: 55.074999999999996
    - type: ndcg_at_20
      value: 51.837
    - type: ndcg_at_3
      value: 40.598
    - type: ndcg_at_5
      value: 45.129999999999995
    - type: precision_at_1
      value: 30.446
    - type: precision_at_10
      value: 8.456
    - type: precision_at_100
      value: 1.122
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_20
      value: 4.807
    - type: precision_at_3
      value: 18.694
    - type: precision_at_5
      value: 13.83
    - type: recall_at_1
      value: 26.849
    - type: recall_at_10
      value: 71.08
    - type: recall_at_100
      value: 92.528
    - type: recall_at_1000
      value: 98.124
    - type: recall_at_20
      value: 80.164
    - type: recall_at_3
      value: 48.211
    - type: recall_at_5
      value: 58.669000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval (default)
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: dev
      type: mteb/quora
    metrics:
    - type: main_score
      value: 88.414
    - type: map_at_1
      value: 70.451
    - type: map_at_10
      value: 84.743
    - type: map_at_100
      value: 85.31800000000001
    - type: map_at_1000
      value: 85.334
    - type: map_at_20
      value: 85.139
    - type: map_at_3
      value: 81.852
    - type: map_at_5
      value: 83.692
    - type: mrr_at_1
      value: 81.10000000000001
    - type: mrr_at_10
      value: 87.573
    - type: mrr_at_100
      value: 87.6829088327801
    - type: mrr_at_1000
      value: 87.68388325928169
    - type: mrr_at_20
      value: 87.6581424881448
    - type: mrr_at_3
      value: 86.69333333333334
    - type: mrr_at_5
      value: 87.29333333333334
    - type: nauc_map_at_1000_diff1
      value: 75.72104615748786
    - type: nauc_map_at_1000_max
      value: 31.609188396862343
    - type: nauc_map_at_1000_std
      value: -46.52088683693813
    - type: nauc_map_at_100_diff1
      value: 75.72964444793845
    - type: nauc_map_at_100_max
      value: 31.591912730669613
    - type: nauc_map_at_100_std
      value: -46.60975557872442
    - type: nauc_map_at_10_diff1
      value: 75.94308571775802
    - type: nauc_map_at_10_max
      value: 31.253563385398657
    - type: nauc_map_at_10_std
      value: -48.181322538551086
    - type: nauc_map_at_1_diff1
      value: 79.79532882332838
    - type: nauc_map_at_1_max
      value: 21.771809872442184
    - type: nauc_map_at_1_std
      value: -42.77169105840692
    - type: nauc_map_at_20_diff1
      value: 75.81259077387881
    - type: nauc_map_at_20_max
      value: 31.416579812982732
    - type: nauc_map_at_20_std
      value: -47.20581632849992
    - type: nauc_map_at_3_diff1
      value: 76.20949767229638
    - type: nauc_map_at_3_max
      value: 28.979538243065196
    - type: nauc_map_at_3_std
      value: -49.54877638998648
    - type: nauc_map_at_5_diff1
      value: 76.00775678250743
    - type: nauc_map_at_5_max
      value: 30.52865409003373
    - type: nauc_map_at_5_std
      value: -49.12438963420192
    - type: nauc_mrr_at_1000_diff1
      value: 76.53323969103015
    - type: nauc_mrr_at_1000_max
      value: 35.012128118744265
    - type: nauc_mrr_at_1000_std
      value: -42.21934663675809
    - type: nauc_mrr_at_100_diff1
      value: 76.53433148138932
    - type: nauc_mrr_at_100_max
      value: 35.01523464314866
    - type: nauc_mrr_at_100_std
      value: -42.218206899281256
    - type: nauc_mrr_at_10_diff1
      value: 76.55659780959033
    - type: nauc_mrr_at_10_max
      value: 35.12026307368733
    - type: nauc_mrr_at_10_std
      value: -42.332025538861515
    - type: nauc_mrr_at_1_diff1
      value: 77.4819303112777
    - type: nauc_mrr_at_1_max
      value: 33.87083528550898
    - type: nauc_mrr_at_1_std
      value: -40.70273058923244
    - type: nauc_mrr_at_20_diff1
      value: 76.54181877814159
    - type: nauc_mrr_at_20_max
      value: 35.029167402913025
    - type: nauc_mrr_at_20_std
      value: -42.26416201560607
    - type: nauc_mrr_at_3_diff1
      value: 76.13878281984827
    - type: nauc_mrr_at_3_max
      value: 34.95491780423885
    - type: nauc_mrr_at_3_std
      value: -42.5669408971239
    - type: nauc_mrr_at_5_diff1
      value: 76.36492389659307
    - type: nauc_mrr_at_5_max
      value: 35.26107283009812
    - type: nauc_mrr_at_5_std
      value: -42.42173398101322
    - type: nauc_ndcg_at_1000_diff1
      value: 75.72692836343464
    - type: nauc_ndcg_at_1000_max
      value: 33.247134568215095
    - type: nauc_ndcg_at_1000_std
      value: -44.439309524493986
    - type: nauc_ndcg_at_100_diff1
      value: 75.76218437396709
    - type: nauc_ndcg_at_100_max
      value: 33.213029188852076
    - type: nauc_ndcg_at_100_std
      value: -44.86123377474948
    - type: nauc_ndcg_at_10_diff1
      value: 76.0418708659554
    - type: nauc_ndcg_at_10_max
      value: 33.03535169276814
    - type: nauc_ndcg_at_10_std
      value: -47.78769977393773
    - type: nauc_ndcg_at_1_diff1
      value: 77.5187067567312
    - type: nauc_ndcg_at_1_max
      value: 33.752101025952825
    - type: nauc_ndcg_at_1_std
      value: -40.74843856168861
    - type: nauc_ndcg_at_20_diff1
      value: 75.93559598948329
    - type: nauc_ndcg_at_20_max
      value: 32.78328286896399
    - type: nauc_ndcg_at_20_std
      value: -46.52407523302919
    - type: nauc_ndcg_at_3_diff1
      value: 74.79008589166301
    - type: nauc_ndcg_at_3_max
      value: 31.808036331631794
    - type: nauc_ndcg_at_3_std
      value: -47.52652861987724
    - type: nauc_ndcg_at_5_diff1
      value: 75.43287367533794
    - type: nauc_ndcg_at_5_max
      value: 32.833203744407065
    - type: nauc_ndcg_at_5_std
      value: -48.200904530310275
    - type: nauc_precision_at_1000_diff1
      value: -43.672762408765834
    - type: nauc_precision_at_1000_max
      value: -2.214136208188294
    - type: nauc_precision_at_1000_std
      value: 40.29144301611288
    - type: nauc_precision_at_100_diff1
      value: -43.12206249775465
    - type: nauc_precision_at_100_max
      value: -1.6653962082743625
    - type: nauc_precision_at_100_std
      value: 37.5746847458721
    - type: nauc_precision_at_10_diff1
      value: -37.22201537627446
    - type: nauc_precision_at_10_max
      value: 2.313038479878318
    - type: nauc_precision_at_10_std
      value: 24.85067899903987
    - type: nauc_precision_at_1_diff1
      value: 77.5187067567312
    - type: nauc_precision_at_1_max
      value: 33.752101025952825
    - type: nauc_precision_at_1_std
      value: -40.74843856168861
    - type: nauc_precision_at_20_diff1
      value: -40.88285707082065
    - type: nauc_precision_at_20_max
      value: -0.4200418417967951
    - type: nauc_precision_at_20_std
      value: 31.468438530634213
    - type: nauc_precision_at_3_diff1
      value: -19.411745749449427
    - type: nauc_precision_at_3_max
      value: 10.67761072881965
    - type: nauc_precision_at_3_std
      value: 6.696045978354165
    - type: nauc_precision_at_5_diff1
      value: -30.962882716609258
    - type: nauc_precision_at_5_max
      value: 6.418634812410295
    - type: nauc_precision_at_5_std
      value: 17.387821173608316
    - type: nauc_recall_at_1000_diff1
      value: 94.69386728069973
    - type: nauc_recall_at_1000_max
      value: 84.28469880099311
    - type: nauc_recall_at_1000_std
      value: 27.77863150403283
    - type: nauc_recall_at_100_diff1
      value: 75.67916531615204
    - type: nauc_recall_at_100_max
      value: 38.167545891813184
    - type: nauc_recall_at_100_std
      value: -64.10332561926879
    - type: nauc_recall_at_10_diff1
      value: 74.06200450248475
    - type: nauc_recall_at_10_max
      value: 32.11315273973532
    - type: nauc_recall_at_10_std
      value: -66.65395786324505
    - type: nauc_recall_at_1_diff1
      value: 79.79532882332838
    - type: nauc_recall_at_1_max
      value: 21.771809872442184
    - type: nauc_recall_at_1_std
      value: -42.77169105840692
    - type: nauc_recall_at_20_diff1
      value: 75.33902902721827
    - type: nauc_recall_at_20_max
      value: 29.429302358270228
    - type: nauc_recall_at_20_std
      value: -71.19429079945306
    - type: nauc_recall_at_3_diff1
      value: 71.53824579534546
    - type: nauc_recall_at_3_max
      value: 27.06969939574833
    - type: nauc_recall_at_3_std
      value: -56.11546620113172
    - type: nauc_recall_at_5_diff1
      value: 71.03056598232821
    - type: nauc_recall_at_5_max
      value: 29.8357436692765
    - type: nauc_recall_at_5_std
      value: -60.42704500308669
    - type: ndcg_at_1
      value: 81.08
    - type: ndcg_at_10
      value: 88.414
    - type: ndcg_at_100
      value: 89.586
    - type: ndcg_at_1000
      value: 89.68599999999999
    - type: ndcg_at_20
      value: 89.092
    - type: ndcg_at_3
      value: 85.697
    - type: ndcg_at_5
      value: 87.215
    - type: precision_at_1
      value: 81.08
    - type: precision_at_10
      value: 13.344000000000001
    - type: precision_at_100
      value: 1.489
    - type: precision_at_1000
      value: 0.152
    - type: precision_at_20
      value: 7.0440000000000005
    - type: precision_at_3
      value: 37.627
    - type: precision_at_5
      value: 24.668
    - type: recall_at_1
      value: 70.451
    - type: recall_at_10
      value: 95.588
    - type: recall_at_100
      value: 99.53
    - type: recall_at_1000
      value: 99.985
    - type: recall_at_20
      value: 97.723
    - type: recall_at_3
      value: 87.775
    - type: recall_at_5
      value: 92.134
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval (default)
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: main_score
      value: 88.78
    - type: map_at_1
      value: 71.18100000000001
    - type: map_at_10
      value: 85.07900000000001
    - type: map_at_100
      value: 85.685
    - type: map_at_1000
      value: 85.702
    - type: map_at_20
      value: 85.476
    - type: map_at_3
      value: 82.15400000000001
    - type: map_at_5
      value: 83.99600000000001
    - type: mrr_at_1
      value: 81.94
    - type: mrr_at_10
      value: 88.03901984126983
    - type: mrr_at_100
      value: 88.12521550900104
    - type: mrr_at_1000
      value: 88.12597480807705
    - type: mrr_at_20
      value: 88.10112262221783
    - type: mrr_at_3
      value: 87.14833333333334
    - type: mrr_at_5
      value: 87.75433333333332
    - type: nauc_map_at_1000_diff1
      value: 76.35234622746741
    - type: nauc_map_at_1000_max
      value: 34.98127835356811
    - type: nauc_map_at_1000_std
      value: -48.412573733834584
    - type: nauc_map_at_100_diff1
      value: 76.360780142656
    - type: nauc_map_at_100_max
      value: 34.95463862302956
    - type: nauc_map_at_100_std
      value: -48.465125662089584
    - type: nauc_map_at_10_diff1
      value: 76.52051460855479
    - type: nauc_map_at_10_max
      value: 34.52605693128301
    - type: nauc_map_at_10_std
      value: -50.187292245995415
    - type: nauc_map_at_1_diff1
      value: 79.82094021507255
    - type: nauc_map_at_1_max
      value: 26.775009943003003
    - type: nauc_map_at_1_std
      value: -43.61817396485825
    - type: nauc_map_at_20_diff1
      value: 76.43954832866126
    - type: nauc_map_at_20_max
      value: 34.90428946303489
    - type: nauc_map_at_20_std
      value: -49.12609036782338
    - type: nauc_map_at_3_diff1
      value: 76.94334321778128
    - type: nauc_map_at_3_max
      value: 32.622560188949166
    - type: nauc_map_at_3_std
      value: -52.188893755275046
    - type: nauc_map_at_5_diff1
      value: 76.82067204509046
    - type: nauc_map_at_5_max
      value: 33.69870062813589
    - type: nauc_map_at_5_std
      value: -51.82728889112768
    - type: nauc_mrr_at_1000_diff1
      value: 76.95820451520244
    - type: nauc_mrr_at_1000_max
      value: 37.55235025494403
    - type: nauc_mrr_at_1000_std
      value: -44.920257644843616
    - type: nauc_mrr_at_100_diff1
      value: 76.9582899978155
    - type: nauc_mrr_at_100_max
      value: 37.553463697088354
    - type: nauc_mrr_at_100_std
      value: -44.91865155369245
    - type: nauc_mrr_at_10_diff1
      value: 76.9448254715384
    - type: nauc_mrr_at_10_max
      value: 37.57592800822079
    - type: nauc_mrr_at_10_std
      value: -44.99589549975646
    - type: nauc_mrr_at_1_diff1
      value: 77.9564573352381
    - type: nauc_mrr_at_1_max
      value: 37.315703535659146
    - type: nauc_mrr_at_1_std
      value: -42.14814981557996
    - type: nauc_mrr_at_20_diff1
      value: 76.96048519906928
    - type: nauc_mrr_at_20_max
      value: 37.595921188645136
    - type: nauc_mrr_at_20_std
      value: -44.95453191997584
    - type: nauc_mrr_at_3_diff1
      value: 76.75010647148396
    - type: nauc_mrr_at_3_max
      value: 37.33157903176563
    - type: nauc_mrr_at_3_std
      value: -45.76965088590701
    - type: nauc_mrr_at_5_diff1
      value: 76.91724094778046
    - type: nauc_mrr_at_5_max
      value: 37.6961116255935
    - type: nauc_mrr_at_5_std
      value: -45.315111572131336
    - type: nauc_ndcg_at_1000_diff1
      value: 76.17915741213382
    - type: nauc_ndcg_at_1000_max
      value: 36.3994100974221
    - type: nauc_ndcg_at_1000_std
      value: -46.52196285482035
    - type: nauc_ndcg_at_100_diff1
      value: 76.20633890208957
    - type: nauc_ndcg_at_100_max
      value: 36.300160051636446
    - type: nauc_ndcg_at_100_std
      value: -46.64640352852657
    - type: nauc_ndcg_at_10_diff1
      value: 76.15630905915566
    - type: nauc_ndcg_at_10_max
      value: 35.60844948367385
    - type: nauc_ndcg_at_10_std
      value: -49.545760942997966
    - type: nauc_ndcg_at_1_diff1
      value: 77.9374936485659
    - type: nauc_ndcg_at_1_max
      value: 37.284222900318895
    - type: nauc_ndcg_at_1_std
      value: -42.11990958304383
    - type: nauc_ndcg_at_20_diff1
      value: 76.27986532220213
    - type: nauc_ndcg_at_20_max
      value: 36.21561434308417
    - type: nauc_ndcg_at_20_std
      value: -48.37507535345429
    - type: nauc_ndcg_at_3_diff1
      value: 75.75636270427239
    - type: nauc_ndcg_at_3_max
      value: 35.032989706721466
    - type: nauc_ndcg_at_3_std
      value: -50.238571322181016
    - type: nauc_ndcg_at_5_diff1
      value: 76.196363901235
    - type: nauc_ndcg_at_5_max
      value: 35.00688298015009
    - type: nauc_ndcg_at_5_std
      value: -50.80538017477186
    - type: nauc_precision_at_1000_diff1
      value: -43.87939421459698
    - type: nauc_precision_at_1000_max
      value: -6.616664050809342
    - type: nauc_precision_at_1000_std
      value: 40.21658774987439
    - type: nauc_precision_at_100_diff1
      value: -43.38845573529132
    - type: nauc_precision_at_100_max
      value: -6.459899067577796
    - type: nauc_precision_at_100_std
      value: 38.97937099541361
    - type: nauc_precision_at_10_diff1
      value: -38.512616169714
    - type: nauc_precision_at_10_max
      value: -2.0392553261530506
    - type: nauc_precision_at_10_std
      value: 27.846561415195296
    - type: nauc_precision_at_1_diff1
      value: 77.9374936485659
    - type: nauc_precision_at_1_max
      value: 37.284222900318895
    - type: nauc_precision_at_1_std
      value: -42.11990958304383
    - type: nauc_precision_at_20_diff1
      value: -41.20993785338744
    - type: nauc_precision_at_20_max
      value: -3.883205139317751
    - type: nauc_precision_at_20_std
      value: 33.746465008755195
    - type: nauc_precision_at_3_diff1
      value: -18.925243780820253
    - type: nauc_precision_at_3_max
      value: 7.636938829464144
    - type: nauc_precision_at_3_std
      value: 5.1931719934549125
    - type: nauc_precision_at_5_diff1
      value: -30.993143706159508
    - type: nauc_precision_at_5_max
      value: 1.6891759655648126
    - type: nauc_precision_at_5_std
      value: 17.209212799329844
    - type: nauc_recall_at_1000_diff1
      value: 47.456878747204605
    - type: nauc_recall_at_1000_max
      value: 23.807161723272337
    - type: nauc_recall_at_1000_std
      value: -32.766355457141614
    - type: nauc_recall_at_100_diff1
      value: 72.34674588264632
    - type: nauc_recall_at_100_max
      value: 33.99490510103659
    - type: nauc_recall_at_100_std
      value: -36.46420217881495
    - type: nauc_recall_at_10_diff1
      value: 71.56272183904842
    - type: nauc_recall_at_10_max
      value: 32.016038250938735
    - type: nauc_recall_at_10_std
      value: -66.96989454392227
    - type: nauc_recall_at_1_diff1
      value: 79.82094021507255
    - type: nauc_recall_at_1_max
      value: 26.775009943003003
    - type: nauc_recall_at_1_std
      value: -43.61817396485825
    - type: nauc_recall_at_20_diff1
      value: 73.24474644767976
    - type: nauc_recall_at_20_max
      value: 36.40934106083169
    - type: nauc_recall_at_20_std
      value: -65.70195006740305
    - type: nauc_recall_at_3_diff1
      value: 72.78023437495966
    - type: nauc_recall_at_3_max
      value: 29.643076465434625
    - type: nauc_recall_at_3_std
      value: -60.40805827565894
    - type: nauc_recall_at_5_diff1
      value: 72.04421253222534
    - type: nauc_recall_at_5_max
      value: 30.353847712973938
    - type: nauc_recall_at_5_std
      value: -64.58955239875104
    - type: ndcg_at_1
      value: 81.95
    - type: ndcg_at_10
      value: 88.78
    - type: ndcg_at_100
      value: 89.90899999999999
    - type: ndcg_at_1000
      value: 90.011
    - type: ndcg_at_20
      value: 89.376
    - type: ndcg_at_3
      value: 86.027
    - type: ndcg_at_5
      value: 87.551
    - type: precision_at_1
      value: 81.95
    - type: precision_at_10
      value: 13.453999999999999
    - type: precision_at_100
      value: 1.528
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_20
      value: 7.1209999999999996
    - type: precision_at_3
      value: 37.6
    - type: precision_at_5
      value: 24.712
    - type: recall_at_1
      value: 71.18100000000001
    - type: recall_at_10
      value: 95.75099999999999
    - type: recall_at_100
      value: 99.544
    - type: recall_at_1000
      value: 99.98899999999999
    - type: recall_at_20
      value: 97.629
    - type: recall_at_3
      value: 87.801
    - type: recall_at_5
      value: 92.14099999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering (default)
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: main_score
      value: 53.81557774708997
    - type: v_measure
      value: 53.81557774708997
    - type: v_measure_std
      value: 4.940724653585969
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P (default)
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: main_score
      value: 63.059340693644785
    - type: v_measure
      value: 63.059340693644785
    - type: v_measure_std
      value: 11.97353413900713
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS (default)
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: main_score
      value: 20.441000000000003
    - type: map_at_1
      value: 4.508
    - type: map_at_10
      value: 12.141
    - type: map_at_100
      value: 14.316
    - type: map_at_1000
      value: 14.658
    - type: map_at_20
      value: 13.242
    - type: map_at_3
      value: 8.624
    - type: map_at_5
      value: 10.333
    - type: mrr_at_1
      value: 22.3
    - type: mrr_at_10
      value: 34.01488095238095
    - type: mrr_at_100
      value: 35.12947200540852
    - type: mrr_at_1000
      value: 35.18258200333811
    - type: mrr_at_20
      value: 34.72472937494222
    - type: mrr_at_3
      value: 30.51666666666667
    - type: mrr_at_5
      value: 32.471666666666664
    - type: nauc_map_at_1000_diff1
      value: 19.5295210919884
    - type: nauc_map_at_1000_max
      value: 35.776154650551575
    - type: nauc_map_at_1000_std
      value: 22.598989298641175
    - type: nauc_map_at_100_diff1
      value: 19.5575568280981
    - type: nauc_map_at_100_max
      value: 35.764999407927924
    - type: nauc_map_at_100_std
      value: 22.388928333977983
    - type: nauc_map_at_10_diff1
      value: 20.301784773079817
    - type: nauc_map_at_10_max
      value: 33.90741195696659
    - type: nauc_map_at_10_std
      value: 17.948501033988475
    - type: nauc_map_at_1_diff1
      value: 27.63795852560605
    - type: nauc_map_at_1_max
      value: 28.677707624382226
    - type: nauc_map_at_1_std
      value: 11.313097574744265
    - type: nauc_map_at_20_diff1
      value: 19.82097532850719
    - type: nauc_map_at_20_max
      value: 35.10681865871605
    - type: nauc_map_at_20_std
      value: 20.393280333290768
    - type: nauc_map_at_3_diff1
      value: 23.465265104601574
    - type: nauc_map_at_3_max
      value: 31.90516362728403
    - type: nauc_map_at_3_std
      value: 11.082550126615867
    - type: nauc_map_at_5_diff1
      value: 21.191560324800694
    - type: nauc_map_at_5_max
      value: 32.349846169015365
    - type: nauc_map_at_5_std
      value: 14.08086983687101
    - type: nauc_mrr_at_1000_diff1
      value: 22.43032918913008
    - type: nauc_mrr_at_1000_max
      value: 30.264097065600065
    - type: nauc_mrr_at_1000_std
      value: 17.16645379954286
    - type: nauc_mrr_at_100_diff1
      value: 22.431918077326362
    - type: nauc_mrr_at_100_max
      value: 30.278656848582674
    - type: nauc_mrr_at_100_std
      value: 17.205287864081686
    - type: nauc_mrr_at_10_diff1
      value: 22.399800621436718
    - type: nauc_mrr_at_10_max
      value: 30.17231346566611
    - type: nauc_mrr_at_10_std
      value: 17.12117352552421
    - type: nauc_mrr_at_1_diff1
      value: 27.338483005001855
    - type: nauc_mrr_at_1_max
      value: 28.516706043782
    - type: nauc_mrr_at_1_std
      value: 11.568218727642739
    - type: nauc_mrr_at_20_diff1
      value: 22.34527846970131
    - type: nauc_mrr_at_20_max
      value: 30.293795035108754
    - type: nauc_mrr_at_20_std
      value: 17.24818382223587
    - type: nauc_mrr_at_3_diff1
      value: 21.41347530740495
    - type: nauc_mrr_at_3_max
      value: 29.49578215215621
    - type: nauc_mrr_at_3_std
      value: 15.565310294336843
    - type: nauc_mrr_at_5_diff1
      value: 21.876219757110178
    - type: nauc_mrr_at_5_max
      value: 29.579506797264944
    - type: nauc_mrr_at_5_std
      value: 16.105358881703282
    - type: nauc_ndcg_at_1000_diff1
      value: 18.678582790233204
    - type: nauc_ndcg_at_1000_max
      value: 36.955188341480266
    - type: nauc_ndcg_at_1000_std
      value: 29.649172816911378
    - type: nauc_ndcg_at_100_diff1
      value: 18.52482522871902
    - type: nauc_ndcg_at_100_max
      value: 37.130183155861445
    - type: nauc_ndcg_at_100_std
      value: 29.52961271427892
    - type: nauc_ndcg_at_10_diff1
      value: 19.94175154982902
    - type: nauc_ndcg_at_10_max
      value: 33.9452753797045
    - type: nauc_ndcg_at_10_std
      value: 20.946470709263238
    - type: nauc_ndcg_at_1_diff1
      value: 27.338483005001855
    - type: nauc_ndcg_at_1_max
      value: 28.516706043782
    - type: nauc_ndcg_at_1_std
      value: 11.568218727642739
    - type: nauc_ndcg_at_20_diff1
      value: 19.293919910420897
    - type: nauc_ndcg_at_20_max
      value: 35.76522367701567
    - type: nauc_ndcg_at_20_std
      value: 24.376420891239388
    - type: nauc_ndcg_at_3_diff1
      value: 21.270066084825956
    - type: nauc_ndcg_at_3_max
      value: 31.326650210409184
    - type: nauc_ndcg_at_3_std
      value: 13.58976920494935
    - type: nauc_ndcg_at_5_diff1
      value: 20.02407289631927
    - type: nauc_ndcg_at_5_max
      value: 31.684362011594843
    - type: nauc_ndcg_at_5_std
      value: 16.249511700219692
    - type: nauc_precision_at_1000_diff1
      value: 6.234005186132995
    - type: nauc_precision_at_1000_max
      value: 29.34471048327642
    - type: nauc_precision_at_1000_std
      value: 39.64669468760326
    - type: nauc_precision_at_100_diff1
      value: 9.855106179885876
    - type: nauc_precision_at_100_max
      value: 34.132120560020866
    - type: nauc_precision_at_100_std
      value: 39.72164007339206
    - type: nauc_precision_at_10_diff1
      value: 15.90102642361928
    - type: nauc_precision_at_10_max
      value: 33.65916770662614
    - type: nauc_precision_at_10_std
      value: 25.390897965743548
    - type: nauc_precision_at_1_diff1
      value: 27.338483005001855
    - type: nauc_precision_at_1_max
      value: 28.516706043782
    - type: nauc_precision_at_1_std
      value: 11.568218727642739
    - type: nauc_precision_at_20_diff1
      value: 13.612513188408462
    - type: nauc_precision_at_20_max
      value: 35.277982280608725
    - type: nauc_precision_at_20_std
      value: 30.71930871320442
    - type: nauc_precision_at_3_diff1
      value: 18.807118007742872
    - type: nauc_precision_at_3_max
      value: 31.816570276319002
    - type: nauc_precision_at_3_std
      value: 14.449767808472858
    - type: nauc_precision_at_5_diff1
      value: 16.209744159726867
    - type: nauc_precision_at_5_max
      value: 31.151946588732997
    - type: nauc_precision_at_5_std
      value: 18.381161071520488
    - type: nauc_recall_at_1000_diff1
      value: 6.273647441536759
    - type: nauc_recall_at_1000_max
      value: 29.1162229253121
    - type: nauc_recall_at_1000_std
      value: 41.52051532378572
    - type: nauc_recall_at_100_diff1
      value: 10.065781985677573
    - type: nauc_recall_at_100_max
      value: 33.83167291115486
    - type: nauc_recall_at_100_std
      value: 40.006650979954934
    - type: nauc_recall_at_10_diff1
      value: 16.15411588223024
    - type: nauc_recall_at_10_max
      value: 33.49396867499272
    - type: nauc_recall_at_10_std
      value: 25.292996350892167
    - type: nauc_recall_at_1_diff1
      value: 27.63795852560605
    - type: nauc_recall_at_1_max
      value: 28.677707624382226
    - type: nauc_recall_at_1_std
      value: 11.313097574744265
    - type: nauc_recall_at_20_diff1
      value: 13.925034360460256
    - type: nauc_recall_at_20_max
      value: 34.99803447287975
    - type: nauc_recall_at_20_std
      value: 30.666854032413088
    - type: nauc_recall_at_3_diff1
      value: 18.998052423925802
    - type: nauc_recall_at_3_max
      value: 31.62628665469099
    - type: nauc_recall_at_3_std
      value: 14.239340647611009
    - type: nauc_recall_at_5_diff1
      value: 16.398224006899152
    - type: nauc_recall_at_5_max
      value: 30.935454145918744
    - type: nauc_recall_at_5_std
      value: 18.143468400300172
    - type: ndcg_at_1
      value: 22.3
    - type: ndcg_at_10
      value: 20.441000000000003
    - type: ndcg_at_100
      value: 28.836000000000002
    - type: ndcg_at_1000
      value: 34.705000000000005
    - type: ndcg_at_20
      value: 23.426
    - type: ndcg_at_3
      value: 19.205
    - type: ndcg_at_5
      value: 16.739
    - type: precision_at_1
      value: 22.3
    - type: precision_at_10
      value: 10.79
    - type: precision_at_100
      value: 2.2960000000000003
    - type: precision_at_1000
      value: 0.371
    - type: precision_at_20
      value: 7.115
    - type: precision_at_3
      value: 18.2
    - type: precision_at_5
      value: 14.84
    - type: recall_at_1
      value: 4.508
    - type: recall_at_10
      value: 21.853
    - type: recall_at_100
      value: 46.589999999999996
    - type: recall_at_1000
      value: 75.25
    - type: recall_at_20
      value: 28.853
    - type: recall_at_3
      value: 11.068
    - type: recall_at_5
      value: 15.033
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R (default)
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: cosine_pearson
      value: 84.30788927270164
    - type: cosine_spearman
      value: 80.07976019050732
    - type: euclidean_pearson
      value: 81.27116301839057
    - type: euclidean_spearman
      value: 80.07976519070897
    - type: main_score
      value: 80.07976019050732
    - type: manhattan_pearson
      value: 81.39470840383359
    - type: manhattan_spearman
      value: 80.11309125271727
    - type: pearson
      value: 84.30788927270164
    - type: spearman
      value: 80.07976019050732
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12 (default)
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: cosine_pearson
      value: 85.6494246715977
    - type: cosine_spearman
      value: 77.21364859343417
    - type: euclidean_pearson
      value: 82.16686843138514
    - type: euclidean_spearman
      value: 77.2132269119475
    - type: main_score
      value: 77.21364859343417
    - type: manhattan_pearson
      value: 82.17288769644415
    - type: manhattan_spearman
      value: 77.05682937722813
    - type: pearson
      value: 85.6494246715977
    - type: spearman
      value: 77.21364859343417
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13 (default)
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: cosine_pearson
      value: 82.12583205748827
    - type: cosine_spearman
      value: 83.55306391445943
    - type: euclidean_pearson
      value: 82.81699442422787
    - type: euclidean_spearman
      value: 83.55306391445943
    - type: main_score
      value: 83.55306391445943
    - type: manhattan_pearson
      value: 82.70032676616033
    - type: manhattan_spearman
      value: 83.43696105973991
    - type: pearson
      value: 82.12583205748827
    - type: spearman
      value: 83.55306391445943
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14 (default)
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: cosine_pearson
      value: 82.8072878574002
    - type: cosine_spearman
      value: 82.39917863256566
    - type: euclidean_pearson
      value: 82.34142760248918
    - type: euclidean_spearman
      value: 82.39918313271785
    - type: main_score
      value: 82.39917863256566
    - type: manhattan_pearson
      value: 82.35430476764317
    - type: manhattan_spearman
      value: 82.38775090940842
    - type: pearson
      value: 82.8072878574002
    - type: spearman
      value: 82.39917863256566
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15 (default)
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: cosine_pearson
      value: 87.05873896779867
    - type: cosine_spearman
      value: 88.08920102010087
    - type: euclidean_pearson
      value: 87.43579028480816
    - type: euclidean_spearman
      value: 88.08920593843715
    - type: main_score
      value: 88.08920102010087
    - type: manhattan_pearson
      value: 87.50258824179726
    - type: manhattan_spearman
      value: 88.18943707030766
    - type: pearson
      value: 87.05873896779867
    - type: spearman
      value: 88.08920102010087
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16 (default)
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: cosine_pearson
      value: 83.18613820567626
    - type: cosine_spearman
      value: 85.02812271380569
    - type: euclidean_pearson
      value: 84.0552020752535
    - type: euclidean_spearman
      value: 85.0281225608977
    - type: main_score
      value: 85.02812271380569
    - type: manhattan_pearson
      value: 83.79067016461165
    - type: manhattan_spearman
      value: 84.75880971236536
    - type: pearson
      value: 83.18613820567626
    - type: spearman
      value: 85.02812271380569
    task:
      type: STS
  - dataset:
      config: fr-en
      name: MTEB STS17 (fr-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 39.5876015348183
    - type: cosine_spearman
      value: 38.2945838490163
    - type: euclidean_pearson
      value: 39.79784346190561
    - type: euclidean_spearman
      value: 38.2945838490163
    - type: main_score
      value: 38.2945838490163
    - type: manhattan_pearson
      value: 39.977833809923645
    - type: manhattan_spearman
      value: 39.388422674752235
    - type: pearson
      value: 39.5876015348183
    - type: spearman
      value: 38.2945838490163
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 88.51383096083804
    - type: cosine_spearman
      value: 88.52537252266963
    - type: euclidean_pearson
      value: 89.1117050087703
    - type: euclidean_spearman
      value: 88.52537252266963
    - type: main_score
      value: 88.52537252266963
    - type: manhattan_pearson
      value: 89.31585295977288
    - type: manhattan_spearman
      value: 88.78380232395662
    - type: pearson
      value: 88.51383096083804
    - type: spearman
      value: 88.52537252266963
    task:
      type: STS
  - dataset:
      config: nl-en
      name: MTEB STS17 (nl-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 35.50474589697871
    - type: cosine_spearman
      value: 30.812689378913603
    - type: euclidean_pearson
      value: 36.25909794770876
    - type: euclidean_spearman
      value: 30.812689378913603
    - type: main_score
      value: 30.812689378913603
    - type: manhattan_pearson
      value: 36.26828913763471
    - type: manhattan_spearman
      value: 31.528781713909197
    - type: pearson
      value: 35.50474589697871
    - type: spearman
      value: 30.812689378913603
    task:
      type: STS
  - dataset:
      config: en-de
      name: MTEB STS17 (en-de)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 32.652743251558654
    - type: cosine_spearman
      value: 29.105392097318806
    - type: euclidean_pearson
      value: 32.74903065824115
    - type: euclidean_spearman
      value: 29.105392097318806
    - type: main_score
      value: 29.105392097318806
    - type: manhattan_pearson
      value: 33.540625008403524
    - type: manhattan_spearman
      value: 29.355480493447494
    - type: pearson
      value: 32.652743251558654
    - type: spearman
      value: 29.105392097318806
    task:
      type: STS
  - dataset:
      config: en-tr
      name: MTEB STS17 (en-tr)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 12.36849882661743
    - type: cosine_spearman
      value: 7.611138217911713
    - type: euclidean_pearson
      value: 12.77603971192848
    - type: euclidean_spearman
      value: 7.611138217911713
    - type: main_score
      value: 7.611138217911713
    - type: manhattan_pearson
      value: 11.619163669702509
    - type: manhattan_spearman
      value: 6.184520778812523
    - type: pearson
      value: 12.36849882661743
    - type: spearman
      value: 7.611138217911713
    task:
      type: STS
  - dataset:
      config: en-ar
      name: MTEB STS17 (en-ar)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 6.59159885046766
    - type: cosine_spearman
      value: 4.622204785531158
    - type: euclidean_pearson
      value: 6.593149700947697
    - type: euclidean_spearman
      value: 4.622204785531158
    - type: main_score
      value: 4.622204785531158
    - type: manhattan_pearson
      value: 5.566016374381194
    - type: manhattan_spearman
      value: 3.8796229563749285
    - type: pearson
      value: 6.59159885046766
    - type: spearman
      value: 4.622204785531158
    task:
      type: STS
  - dataset:
      config: es-en
      name: MTEB STS17 (es-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 30.35179238078445
    - type: cosine_spearman
      value: 29.625068788447894
    - type: euclidean_pearson
      value: 30.233806247338414
    - type: euclidean_spearman
      value: 29.625068788447894
    - type: main_score
      value: 29.625068788447894
    - type: manhattan_pearson
      value: 29.936866734034933
    - type: manhattan_spearman
      value: 28.57299479927884
    - type: pearson
      value: 30.35179238078445
    - type: spearman
      value: 29.625068788447894
    task:
      type: STS
  - dataset:
      config: it-en
      name: MTEB STS17 (it-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 30.30232199857813
    - type: cosine_spearman
      value: 27.219119781543988
    - type: euclidean_pearson
      value: 30.225835856043272
    - type: euclidean_spearman
      value: 27.219119781543988
    - type: main_score
      value: 27.219119781543988
    - type: manhattan_pearson
      value: 29.142315782629925
    - type: manhattan_spearman
      value: 25.901216206187065
    - type: pearson
      value: 30.30232199857813
    - type: spearman
      value: 27.219119781543988
    task:
      type: STS
  - dataset:
      config: de-en
      name: MTEB STS22 (de-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 43.22978323210299
    - type: cosine_spearman
      value: 47.01518443724799
    - type: euclidean_pearson
      value: 45.930506019807574
    - type: euclidean_spearman
      value: 47.01518443724799
    - type: main_score
      value: 47.01518443724799
    - type: manhattan_pearson
      value: 47.44811320365125
    - type: manhattan_spearman
      value: 47.73671354326406
    - type: pearson
      value: 43.22978323210299
    - type: spearman
      value: 47.01518443724799
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 65.93329041695125
    - type: cosine_spearman
      value: 65.95494400411647
    - type: euclidean_pearson
      value: 67.77439530118112
    - type: euclidean_spearman
      value: 65.95494400411647
    - type: main_score
      value: 65.95494400411647
    - type: manhattan_pearson
      value: 68.21709531505775
    - type: manhattan_spearman
      value: 66.39646560258034
    - type: pearson
      value: 65.93329041695125
    - type: spearman
      value: 65.95494400411647
    task:
      type: STS
  - dataset:
      config: pl-en
      name: MTEB STS22 (pl-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 46.929818903916804
    - type: cosine_spearman
      value: 44.44075531175433
    - type: euclidean_pearson
      value: 47.059078863657675
    - type: euclidean_spearman
      value: 44.44075531175433
    - type: main_score
      value: 44.44075531175433
    - type: manhattan_pearson
      value: 46.04521740640152
    - type: manhattan_spearman
      value: 44.576197773142866
    - type: pearson
      value: 46.929818903916804
    - type: spearman
      value: 44.44075531175433
    task:
      type: STS
  - dataset:
      config: es-en
      name: MTEB STS22 (es-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 56.86304728923609
    - type: cosine_spearman
      value: 63.05184294758852
    - type: euclidean_pearson
      value: 58.177828253582206
    - type: euclidean_spearman
      value: 63.05184294758852
    - type: main_score
      value: 63.05184294758852
    - type: manhattan_pearson
      value: 58.958715164135825
    - type: manhattan_spearman
      value: 63.755348809781395
    - type: pearson
      value: 56.86304728923609
    - type: spearman
      value: 63.05184294758852
    task:
      type: STS
  - dataset:
      config: zh-en
      name: MTEB STS22 (zh-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 45.6965322701485
    - type: cosine_spearman
      value: 49.44860243126726
    - type: euclidean_pearson
      value: 45.71922769223791
    - type: euclidean_spearman
      value: 49.44860243126726
    - type: main_score
      value: 49.44860243126726
    - type: manhattan_pearson
      value: 45.78318374788422
    - type: manhattan_spearman
      value: 49.521422718994984
    - type: pearson
      value: 45.6965322701485
    - type: spearman
      value: 49.44860243126726
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark (default)
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: cosine_pearson
      value: 85.0014615648556
    - type: cosine_spearman
      value: 86.65686905435463
    - type: euclidean_pearson
      value: 86.1451324543907
    - type: euclidean_spearman
      value: 86.65685763157673
    - type: main_score
      value: 86.65686905435463
    - type: manhattan_pearson
      value: 86.0861598253851
    - type: manhattan_spearman
      value: 86.61047820278552
    - type: pearson
      value: 85.0014615648556
    - type: spearman
      value: 86.65686905435463
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR (default)
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: main_score
      value: 85.89651013746061
    - type: map
      value: 85.89651013746061
    - type: mrr
      value: 95.99524567661823
    - type: nAUC_map_diff1
      value: -0.0410803569069903
    - type: nAUC_map_max
      value: 53.629827070614546
    - type: nAUC_map_std
      value: 67.22768282404712
    - type: nAUC_mrr_diff1
      value: 40.687943307829606
    - type: nAUC_mrr_max
      value: 85.09337269421229
    - type: nAUC_mrr_std
      value: 79.32454109714799
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SciFact (default)
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: main_score
      value: 73.251
    - type: map_at_1
      value: 59.428000000000004
    - type: map_at_10
      value: 68.959
    - type: map_at_100
      value: 69.484
    - type: map_at_1000
      value: 69.511
    - type: map_at_20
      value: 69.30199999999999
    - type: map_at_3
      value: 66.083
    - type: map_at_5
      value: 67.683
    - type: mrr_at_1
      value: 62.33333333333333
    - type: mrr_at_10
      value: 69.96005291005292
    - type: mrr_at_100
      value: 70.37333611401961
    - type: mrr_at_1000
      value: 70.40109312065698
    - type: mrr_at_20
      value: 70.23336940836941
    - type: mrr_at_3
      value: 67.72222222222221
    - type: mrr_at_5
      value: 69.07222222222222
    - type: nauc_map_at_1000_diff1
      value: 70.13570749625822
    - type: nauc_map_at_1000_max
      value: 52.65674632844235
    - type: nauc_map_at_1000_std
      value: 10.132852161672638
    - type: nauc_map_at_100_diff1
      value: 70.13538095683808
    - type: nauc_map_at_100_max
      value: 52.6884935329599
    - type: nauc_map_at_100_std
      value: 10.14379381633777
    - type: nauc_map_at_10_diff1
      value: 70.36327918679356
    - type: nauc_map_at_10_max
      value: 52.954942802961504
    - type: nauc_map_at_10_std
      value: 10.02209736428799
    - type: nauc_map_at_1_diff1
      value: 73.49594650090174
    - type: nauc_map_at_1_max
      value: 45.82858518993797
    - type: nauc_map_at_1_std
      value: -0.40926083096917837
    - type: nauc_map_at_20_diff1
      value: 70.06837661473298
    - type: nauc_map_at_20_max
      value: 52.76020878212071
    - type: nauc_map_at_20_std
      value: 10.007600191187741
    - type: nauc_map_at_3_diff1
      value: 70.31817155099134
    - type: nauc_map_at_3_max
      value: 48.641969098932314
    - type: nauc_map_at_3_std
      value: 7.073005227799293
    - type: nauc_map_at_5_diff1
      value: 69.91715955939225
    - type: nauc_map_at_5_max
      value: 50.08437399280585
    - type: nauc_map_at_5_std
      value: 8.325142211837317
    - type: nauc_mrr_at_1000_diff1
      value: 70.89523822365368
    - type: nauc_mrr_at_1000_max
      value: 54.566931991503175
    - type: nauc_mrr_at_1000_std
      value: 13.068031822873314
    - type: nauc_mrr_at_100_diff1
      value: 70.89405457859479
    - type: nauc_mrr_at_100_max
      value: 54.5971940226233
    - type: nauc_mrr_at_100_std
      value: 13.075912428577213
    - type: nauc_mrr_at_10_diff1
      value: 71.03623671748012
    - type: nauc_mrr_at_10_max
      value: 54.95069512409659
    - type: nauc_mrr_at_10_std
      value: 13.363315852524071
    - type: nauc_mrr_at_1_diff1
      value: 73.44129679978948
    - type: nauc_mrr_at_1_max
      value: 53.11585866037946
    - type: nauc_mrr_at_1_std
      value: 8.225722407664433
    - type: nauc_mrr_at_20_diff1
      value: 70.83036037320228
    - type: nauc_mrr_at_20_max
      value: 54.65143963366521
    - type: nauc_mrr_at_20_std
      value: 13.136998458127792
    - type: nauc_mrr_at_3_diff1
      value: 71.153158657001
    - type: nauc_mrr_at_3_max
      value: 53.205584683267084
    - type: nauc_mrr_at_3_std
      value: 11.980916718299982
    - type: nauc_mrr_at_5_diff1
      value: 70.66319100789279
    - type: nauc_mrr_at_5_max
      value: 53.64747705626284
    - type: nauc_mrr_at_5_std
      value: 13.158118645048983
    - type: nauc_ndcg_at_1000_diff1
      value: 69.82895027282646
    - type: nauc_ndcg_at_1000_max
      value: 54.52290390511955
    - type: nauc_ndcg_at_1000_std
      value: 13.07433953652383
    - type: nauc_ndcg_at_100_diff1
      value: 69.66603141670811
    - type: nauc_ndcg_at_100_max
      value: 55.33932851097095
    - type: nauc_ndcg_at_100_std
      value: 13.531855815973309
    - type: nauc_ndcg_at_10_diff1
      value: 70.0672222067367
    - type: nauc_ndcg_at_10_max
      value: 56.609848753019875
    - type: nauc_ndcg_at_10_std
      value: 13.801015990958836
    - type: nauc_ndcg_at_1_diff1
      value: 73.44129679978948
    - type: nauc_ndcg_at_1_max
      value: 53.11585866037946
    - type: nauc_ndcg_at_1_std
      value: 8.225722407664433
    - type: nauc_ndcg_at_20_diff1
      value: 69.00029554032444
    - type: nauc_ndcg_at_20_max
      value: 55.77587708778143
    - type: nauc_ndcg_at_20_std
      value: 13.550535479714885
    - type: nauc_ndcg_at_3_diff1
      value: 69.35809356376409
    - type: nauc_ndcg_at_3_max
      value: 50.88753511744564
    - type: nauc_ndcg_at_3_std
      value: 10.376849196217488
    - type: nauc_ndcg_at_5_diff1
      value: 68.7557226824334
    - type: nauc_ndcg_at_5_max
      value: 51.64039917399674
    - type: nauc_ndcg_at_5_std
      value: 11.375060289968888
    - type: nauc_precision_at_1000_diff1
      value: -24.38184345232032
    - type: nauc_precision_at_1000_max
      value: 25.3113664869997
    - type: nauc_precision_at_1000_std
      value: 54.78151801755995
    - type: nauc_precision_at_100_diff1
      value: -10.585088484724002
    - type: nauc_precision_at_100_max
      value: 34.58061719734689
    - type: nauc_precision_at_100_std
      value: 51.08616923594603
    - type: nauc_precision_at_10_diff1
      value: 15.011059571897201
    - type: nauc_precision_at_10_max
      value: 53.380534154853976
    - type: nauc_precision_at_10_std
      value: 46.77574783177469
    - type: nauc_precision_at_1_diff1
      value: 73.44129679978948
    - type: nauc_precision_at_1_max
      value: 53.11585866037946
    - type: nauc_precision_at_1_std
      value: 8.225722407664433
    - type: nauc_precision_at_20_diff1
      value: 3.0375226465875627
    - type: nauc_precision_at_20_max
      value: 46.96352459445593
    - type: nauc_precision_at_20_std
      value: 47.8180732859282
    - type: nauc_precision_at_3_diff1
      value: 41.34820548287889
    - type: nauc_precision_at_3_max
      value: 48.02988164084151
    - type: nauc_precision_at_3_std
      value: 29.8325902163623
    - type: nauc_precision_at_5_diff1
      value: 28.292680467974172
    - type: nauc_precision_at_5_max
      value: 48.2395519867733
    - type: nauc_precision_at_5_std
      value: 36.77307484865436
    - type: nauc_recall_at_1000_diff1
      value: 86.92810457516407
    - type: nauc_recall_at_1000_max
      value: 12.278244631182748
    - type: nauc_recall_at_1000_std
      value: 86.92810457516407
    - type: nauc_recall_at_100_diff1
      value: 64.23902894491097
    - type: nauc_recall_at_100_max
      value: 78.57809790582883
    - type: nauc_recall_at_100_std
      value: 35.47085500866988
    - type: nauc_recall_at_10_diff1
      value: 67.63049621810325
    - type: nauc_recall_at_10_max
      value: 71.99088366956788
    - type: nauc_recall_at_10_std
      value: 25.694634100003483
    - type: nauc_recall_at_1_diff1
      value: 73.49594650090174
    - type: nauc_recall_at_1_max
      value: 45.82858518993797
    - type: nauc_recall_at_1_std
      value: -0.40926083096917837
    - type: nauc_recall_at_20_diff1
      value: 58.91757942656138
    - type: nauc_recall_at_20_max
      value: 70.52947052947034
    - type: nauc_recall_at_20_std
      value: 26.934442802706094
    - type: nauc_recall_at_3_diff1
      value: 66.06848071584821
    - type: nauc_recall_at_3_max
      value: 47.58371405487635
    - type: nauc_recall_at_3_std
      value: 10.115468870167247
    - type: nauc_recall_at_5_diff1
      value: 63.103805010550055
    - type: nauc_recall_at_5_max
      value: 51.85255345215588
    - type: nauc_recall_at_5_std
      value: 15.746356552783283
    - type: ndcg_at_1
      value: 62.333000000000006
    - type: ndcg_at_10
      value: 73.251
    - type: ndcg_at_100
      value: 75.471
    - type: ndcg_at_1000
      value: 76.058
    - type: ndcg_at_20
      value: 74.344
    - type: ndcg_at_3
      value: 68.314
    - type: ndcg_at_5
      value: 70.733
    - type: precision_at_1
      value: 62.333000000000006
    - type: precision_at_10
      value: 9.667
    - type: precision_at_100
      value: 1.083
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_20
      value: 5.067
    - type: precision_at_3
      value: 26.333000000000002
    - type: precision_at_5
      value: 17.4
    - type: recall_at_1
      value: 59.428000000000004
    - type: recall_at_10
      value: 85.422
    - type: recall_at_100
      value: 95.333
    - type: recall_at_1000
      value: 99.667
    - type: recall_at_20
      value: 89.533
    - type: recall_at_3
      value: 72.06099999999999
    - type: recall_at_5
      value: 78.261
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SciFact (default)
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: train
      type: mteb/scifact
    metrics:
    - type: main_score
      value: 76.485
    - type: map_at_1
      value: 62.437
    - type: map_at_10
      value: 72.424
    - type: map_at_100
      value: 72.875
    - type: map_at_1000
      value: 72.894
    - type: map_at_20
      value: 72.699
    - type: map_at_3
      value: 69.929
    - type: map_at_5
      value: 71.41
    - type: mrr_at_1
      value: 65.389369592089
    - type: mrr_at_10
      value: 73.51874742480429
    - type: mrr_at_100
      value: 73.86149719584975
    - type: mrr_at_1000
      value: 73.87817655179401
    - type: mrr_at_20
      value: 73.69712246373606
    - type: mrr_at_3
      value: 72.10548001648127
    - type: mrr_at_5
      value: 72.83477544293366
    - type: nauc_map_at_1000_diff1
      value: 70.88987705012035
    - type: nauc_map_at_1000_max
      value: 46.77717767104366
    - type: nauc_map_at_1000_std
      value: 12.442652616829855
    - type: nauc_map_at_100_diff1
      value: 70.88170091037614
    - type: nauc_map_at_100_max
      value: 46.78841410305628
    - type: nauc_map_at_100_std
      value: 12.472496933804496
    - type: nauc_map_at_10_diff1
      value: 70.97977319347748
    - type: nauc_map_at_10_max
      value: 46.84404169739291
    - type: nauc_map_at_10_std
      value: 12.21031737700784
    - type: nauc_map_at_1_diff1
      value: 73.66858140737193
    - type: nauc_map_at_1_max
      value: 37.72209378868329
    - type: nauc_map_at_1_std
      value: 6.058877150429456
    - type: nauc_map_at_20_diff1
      value: 70.80507181778022
    - type: nauc_map_at_20_max
      value: 46.819460847144114
    - type: nauc_map_at_20_std
      value: 12.472103561158026
    - type: nauc_map_at_3_diff1
      value: 71.58242927801035
    - type: nauc_map_at_3_max
      value: 43.60594750641507
    - type: nauc_map_at_3_std
      value: 8.800606729897389
    - type: nauc_map_at_5_diff1
      value: 71.15709258217167
    - type: nauc_map_at_5_max
      value: 45.724847576243924
    - type: nauc_map_at_5_std
      value: 10.318911927965361
    - type: nauc_mrr_at_1000_diff1
      value: 71.04412576767227
    - type: nauc_mrr_at_1000_max
      value: 48.49663895894284
    - type: nauc_mrr_at_1000_std
      value: 15.61285718843641
    - type: nauc_mrr_at_100_diff1
      value: 71.03490861681165
    - type: nauc_mrr_at_100_max
      value: 48.50439063635205
    - type: nauc_mrr_at_100_std
      value: 15.640711217565325
    - type: nauc_mrr_at_10_diff1
      value: 71.03518493601177
    - type: nauc_mrr_at_10_max
      value: 48.61941531114441
    - type: nauc_mrr_at_10_std
      value: 15.706199493660014
    - type: nauc_mrr_at_1_diff1
      value: 73.60832695813949
    - type: nauc_mrr_at_1_max
      value: 44.578750878677084
    - type: nauc_mrr_at_1_std
      value: 11.890587471184963
    - type: nauc_mrr_at_20_diff1
      value: 70.97955641800446
    - type: nauc_mrr_at_20_max
      value: 48.58739923848605
    - type: nauc_mrr_at_20_std
      value: 15.664657516610061
    - type: nauc_mrr_at_3_diff1
      value: 71.27717189961885
    - type: nauc_mrr_at_3_max
      value: 48.6513411916282
    - type: nauc_mrr_at_3_std
      value: 15.310361808945489
    - type: nauc_mrr_at_5_diff1
      value: 71.20476915325136
    - type: nauc_mrr_at_5_max
      value: 48.441764267472145
    - type: nauc_mrr_at_5_std
      value: 15.365655626467209
    - type: nauc_ndcg_at_1000_diff1
      value: 70.08074385839639
    - type: nauc_ndcg_at_1000_max
      value: 48.6611446591934
    - type: nauc_ndcg_at_1000_std
      value: 15.430653624542611
    - type: nauc_ndcg_at_100_diff1
      value: 69.68550330145398
    - type: nauc_ndcg_at_100_max
      value: 48.88307581467983
    - type: nauc_ndcg_at_100_std
      value: 16.234260889596484
    - type: nauc_ndcg_at_10_diff1
      value: 69.84945527709709
    - type: nauc_ndcg_at_10_max
      value: 49.4084894308013
    - type: nauc_ndcg_at_10_std
      value: 15.695585904151896
    - type: nauc_ndcg_at_1_diff1
      value: 73.60832695813949
    - type: nauc_ndcg_at_1_max
      value: 44.578750878677084
    - type: nauc_ndcg_at_1_std
      value: 11.890587471184963
    - type: nauc_ndcg_at_20_diff1
      value: 69.33301377386857
    - type: nauc_ndcg_at_20_max
      value: 49.35761408825228
    - type: nauc_ndcg_at_20_std
      value: 16.3513166242212
    - type: nauc_ndcg_at_3_diff1
      value: 70.68084301272158
    - type: nauc_ndcg_at_3_max
      value: 46.19757134168426
    - type: nauc_ndcg_at_3_std
      value: 11.440557917517024
    - type: nauc_ndcg_at_5_diff1
      value: 70.22608752669124
    - type: nauc_ndcg_at_5_max
      value: 47.715928046644144
    - type: nauc_ndcg_at_5_std
      value: 12.927681872823138
    - type: nauc_precision_at_1000_diff1
      value: -30.771908331112545
    - type: nauc_precision_at_1000_max
      value: 21.856638608356842
    - type: nauc_precision_at_1000_std
      value: 35.14083908557948
    - type: nauc_precision_at_100_diff1
      value: -21.94474337380867
    - type: nauc_precision_at_100_max
      value: 27.749326522576958
    - type: nauc_precision_at_100_std
      value: 38.74941555088935
    - type: nauc_precision_at_10_diff1
      value: 4.1338368705214705
    - type: nauc_precision_at_10_max
      value: 40.35268389940857
    - type: nauc_precision_at_10_std
      value: 34.86150577835351
    - type: nauc_precision_at_1_diff1
      value: 73.60832695813949
    - type: nauc_precision_at_1_max
      value: 44.578750878677084
    - type: nauc_precision_at_1_std
      value: 11.890587471184963
    - type: nauc_precision_at_20_diff1
      value: -5.308128515414954
    - type: nauc_precision_at_20_max
      value: 34.927193769639246
    - type: nauc_precision_at_20_std
      value: 36.45210990375071
    - type: nauc_precision_at_3_diff1
      value: 38.801243070827766
    - type: nauc_precision_at_3_max
      value: 50.15215786362873
    - type: nauc_precision_at_3_std
      value: 22.902503553912712
    - type: nauc_precision_at_5_diff1
      value: 19.15608744207784
    - type: nauc_precision_at_5_max
      value: 43.451044323440705
    - type: nauc_precision_at_5_std
      value: 26.099168664730975
    - type: nauc_recall_at_1000_diff1
      value: 59.973000734681946
    - type: nauc_recall_at_1000_max
      value: 90.19473173884923
    - type: nauc_recall_at_1000_std
      value: 77.70012495920277
    - type: nauc_recall_at_100_diff1
      value: 49.520208174749534
    - type: nauc_recall_at_100_max
      value: 62.658917735912844
    - type: nauc_recall_at_100_std
      value: 57.59734216892526
    - type: nauc_recall_at_10_diff1
      value: 63.59382135270663
    - type: nauc_recall_at_10_max
      value: 57.66910071241303
    - type: nauc_recall_at_10_std
      value: 26.157501494756524
    - type: nauc_recall_at_1_diff1
      value: 73.66858140737193
    - type: nauc_recall_at_1_max
      value: 37.72209378868329
    - type: nauc_recall_at_1_std
      value: 6.058877150429456
    - type: nauc_recall_at_20_diff1
      value: 58.60290521588567
    - type: nauc_recall_at_20_max
      value: 59.907374912367516
    - type: nauc_recall_at_20_std
      value: 33.91543413688288
    - type: nauc_recall_at_3_diff1
      value: 68.02786476343704
    - type: nauc_recall_at_3_max
      value: 45.954227249575986
    - type: nauc_recall_at_3_std
      value: 10.821057815371045
    - type: nauc_recall_at_5_diff1
      value: 65.83241381992168
    - type: nauc_recall_at_5_max
      value: 50.03082691375689
    - type: nauc_recall_at_5_std
      value: 15.241601072308331
    - type: ndcg_at_1
      value: 65.389
    - type: ndcg_at_10
      value: 76.485
    - type: ndcg_at_100
      value: 78.47
    - type: ndcg_at_1000
      value: 78.875
    - type: ndcg_at_20
      value: 77.321
    - type: ndcg_at_3
      value: 72.51100000000001
    - type: ndcg_at_5
      value: 74.48
    - type: precision_at_1
      value: 65.389
    - type: precision_at_10
      value: 9.937999999999999
    - type: precision_at_100
      value: 1.098
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_20
      value: 5.167
    - type: precision_at_3
      value: 28.224
    - type: precision_at_5
      value: 18.368000000000002
    - type: recall_at_1
      value: 62.437
    - type: recall_at_10
      value: 87.50099999999999
    - type: recall_at_100
      value: 96.518
    - type: recall_at_1000
      value: 99.506
    - type: recall_at_20
      value: 90.606
    - type: recall_at_3
      value: 77.35300000000001
    - type: recall_at_5
      value: 81.811
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions (default)
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 99.86534653465347
    - type: cosine_accuracy_threshold
      value: 87.42109537124634
    - type: cosine_ap
      value: 96.62589824590614
    - type: cosine_f1
      value: 93.1726907630522
    - type: cosine_f1_threshold
      value: 87.26919889450073
    - type: cosine_precision
      value: 93.54838709677419
    - type: cosine_recall
      value: 92.80000000000001
    - type: dot_accuracy
      value: 99.86534653465347
    - type: dot_accuracy_threshold
      value: 174.84219074249268
    - type: dot_ap
      value: 96.62589584517633
    - type: dot_f1
      value: 93.1726907630522
    - type: dot_f1_threshold
      value: 174.53839778900146
    - type: dot_precision
      value: 93.54838709677419
    - type: dot_recall
      value: 92.80000000000001
    - type: euclidean_accuracy
      value: 99.86534653465347
    - type: euclidean_accuracy_threshold
      value: 70.93350887298584
    - type: euclidean_ap
      value: 96.62589584517633
    - type: euclidean_f1
      value: 93.1726907630522
    - type: euclidean_f1_threshold
      value: 71.36050462722778
    - type: euclidean_precision
      value: 93.54838709677419
    - type: euclidean_recall
      value: 92.80000000000001
    - type: main_score
      value: 96.62589824590614
    - type: manhattan_accuracy
      value: 99.86237623762376
    - type: manhattan_accuracy_threshold
      value: 1510.8413696289062
    - type: manhattan_ap
      value: 96.5990356446392
    - type: manhattan_f1
      value: 92.94057897409853
    - type: manhattan_f1_threshold
      value: 1530.6350708007812
    - type: manhattan_precision
      value: 94.42724458204334
    - type: manhattan_recall
      value: 91.5
    - type: max_accuracy
      value: 99.86534653465347
    - type: max_ap
      value: 96.62589824590614
    - type: max_f1
      value: 93.1726907630522
    - type: max_precision
      value: 94.42724458204334
    - type: max_recall
      value: 92.80000000000001
    - type: similarity_accuracy
      value: 99.86534653465347
    - type: similarity_accuracy_threshold
      value: 87.42109537124634
    - type: similarity_ap
      value: 96.62589824590614
    - type: similarity_f1
      value: 93.1726907630522
    - type: similarity_f1_threshold
      value: 87.26919889450073
    - type: similarity_precision
      value: 93.54838709677419
    - type: similarity_recall
      value: 92.80000000000001
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions (default)
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: validation
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 99.84059405940594
    - type: cosine_accuracy_threshold
      value: 87.00189590454102
    - type: cosine_ap
      value: 96.73329740037518
    - type: cosine_f1
      value: 92.0493827160494
    - type: cosine_f1_threshold
      value: 86.32840514183044
    - type: cosine_precision
      value: 90.92682926829269
    - type: cosine_recall
      value: 93.2
    - type: dot_accuracy
      value: 99.84059405940594
    - type: dot_accuracy_threshold
      value: 174.00379180908203
    - type: dot_ap
      value: 96.73329740037518
    - type: dot_f1
      value: 92.0493827160494
    - type: dot_f1_threshold
      value: 172.65679836273193
    - type: dot_precision
      value: 90.92682926829269
    - type: dot_recall
      value: 93.2
    - type: euclidean_accuracy
      value: 99.84059405940594
    - type: euclidean_accuracy_threshold
      value: 72.1057653427124
    - type: euclidean_ap
      value: 96.73329740037518
    - type: euclidean_f1
      value: 92.0493827160494
    - type: euclidean_f1_threshold
      value: 73.95024299621582
    - type: euclidean_precision
      value: 90.92682926829269
    - type: euclidean_recall
      value: 93.2
    - type: main_score
      value: 96.75632821046904
    - type: manhattan_accuracy
      value: 99.84257425742574
    - type: manhattan_accuracy_threshold
      value: 1568.2302474975586
    - type: manhattan_ap
      value: 96.75632821046904
    - type: manhattan_f1
      value: 91.98229217904576
    - type: manhattan_f1_threshold
      value: 1615.3419494628906
    - type: manhattan_precision
      value: 90.51306873184899
    - type: manhattan_recall
      value: 93.5
    - type: max_accuracy
      value: 99.84257425742574
    - type: max_ap
      value: 96.75632821046904
    - type: max_f1
      value: 92.0493827160494
    - type: max_precision
      value: 90.92682926829269
    - type: max_recall
      value: 93.5
    - type: similarity_accuracy
      value: 99.84059405940594
    - type: similarity_accuracy_threshold
      value: 87.00189590454102
    - type: similarity_ap
      value: 96.73329740037518
    - type: similarity_f1
      value: 92.0493827160494
    - type: similarity_f1_threshold
      value: 86.32840514183044
    - type: similarity_precision
      value: 90.92682926829269
    - type: similarity_recall
      value: 93.2
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering (default)
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: main_score
      value: 62.86417213636288
    - type: v_measure
      value: 62.86417213636288
    - type: v_measure_std
      value: 4.26517499407962
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P (default)
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: main_score
      value: 34.49041102464247
    - type: v_measure
      value: 34.49041102464247
    - type: v_measure_std
      value: 1.5008009956624384
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions (default)
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: main_score
      value: 53.56080676583018
    - type: map
      value: 53.56080676583018
    - type: mrr
      value: 54.574155419743654
    - type: nAUC_map_diff1
      value: 38.68676474201522
    - type: nAUC_map_max
      value: 13.538152012883021
    - type: nAUC_map_std
      value: 8.406474170060411
    - type: nAUC_mrr_diff1
      value: 38.27738033427405
    - type: nAUC_mrr_max
      value: 14.313023512543305
    - type: nAUC_mrr_std
      value: 9.482773181023104
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval (default)
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: cosine_pearson
      value: 30.78001838626019
    - type: cosine_spearman
      value: 30.06796987185709
    - type: dot_pearson
      value: 30.78001527942813
    - type: dot_spearman
      value: 30.063748343894524
    - type: main_score
      value: 30.06796987185709
    - type: pearson
      value: 30.78001838626019
    - type: spearman
      value: 30.06796987185709
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB TRECCOVID (default)
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: main_score
      value: 67.647
    - type: map_at_1
      value: 0.192
    - type: map_at_10
      value: 1.678
    - type: map_at_100
      value: 9.362
    - type: map_at_1000
      value: 23.655
    - type: map_at_20
      value: 2.9770000000000003
    - type: map_at_3
      value: 0.5559999999999999
    - type: map_at_5
      value: 0.91
    - type: mrr_at_1
      value: 74.0
    - type: mrr_at_10
      value: 84.07460317460317
    - type: mrr_at_100
      value: 84.07460317460317
    - type: mrr_at_1000
      value: 84.07460317460317
    - type: mrr_at_20
      value: 84.07460317460317
    - type: mrr_at_3
      value: 82.66666666666667
    - type: mrr_at_5
      value: 83.56666666666666
    - type: nauc_map_at_1000_diff1
      value: -1.1098863157023129
    - type: nauc_map_at_1000_max
      value: 48.42614641797866
    - type: nauc_map_at_1000_std
      value: 74.41245113222085
    - type: nauc_map_at_100_diff1
      value: 11.810610128543328
    - type: nauc_map_at_100_max
      value: 45.54012493749073
    - type: nauc_map_at_100_std
      value: 55.216633821552705
    - type: nauc_map_at_10_diff1
      value: 14.706640439003039
    - type: nauc_map_at_10_max
      value: 27.009359341915196
    - type: nauc_map_at_10_std
      value: 12.580248102741749
    - type: nauc_map_at_1_diff1
      value: 18.849085390343852
    - type: nauc_map_at_1_max
      value: 22.147807794097968
    - type: nauc_map_at_1_std
      value: 8.226943075643607
    - type: nauc_map_at_20_diff1
      value: 11.262073635376204
    - type: nauc_map_at_20_max
      value: 29.788086926929736
    - type: nauc_map_at_20_std
      value: 18.831720483995586
    - type: nauc_map_at_3_diff1
      value: 10.591785709689498
    - type: nauc_map_at_3_max
      value: 19.999731080136282
    - type: nauc_map_at_3_std
      value: 8.283426397720875
    - type: nauc_map_at_5_diff1
      value: 13.438781723934065
    - type: nauc_map_at_5_max
      value: 23.771513155136258
    - type: nauc_map_at_5_std
      value: 11.39274226111021
    - type: nauc_mrr_at_1000_diff1
      value: -7.700192607976083
    - type: nauc_mrr_at_1000_max
      value: 58.06999088899807
    - type: nauc_mrr_at_1000_std
      value: 55.498437292780146
    - type: nauc_mrr_at_100_diff1
      value: -7.700192607976083
    - type: nauc_mrr_at_100_max
      value: 58.06999088899807
    - type: nauc_mrr_at_100_std
      value: 55.498437292780146
    - type: nauc_mrr_at_10_diff1
      value: -7.700192607976083
    - type: nauc_mrr_at_10_max
      value: 58.06999088899807
    - type: nauc_mrr_at_10_std
      value: 55.498437292780146
    - type: nauc_mrr_at_1_diff1
      value: 5.8837841125663815
    - type: nauc_mrr_at_1_max
      value: 57.15502209967149
    - type: nauc_mrr_at_1_std
      value: 53.94752848627391
    - type: nauc_mrr_at_20_diff1
      value: -7.700192607976083
    - type: nauc_mrr_at_20_max
      value: 58.06999088899807
    - type: nauc_mrr_at_20_std
      value: 55.498437292780146
    - type: nauc_mrr_at_3_diff1
      value: -9.92939143073178
    - type: nauc_mrr_at_3_max
      value: 59.45162969291663
    - type: nauc_mrr_at_3_std
      value: 56.1706390124621
    - type: nauc_mrr_at_5_diff1
      value: -10.352998992145512
    - type: nauc_mrr_at_5_max
      value: 57.75340046811098
    - type: nauc_mrr_at_5_std
      value: 55.20409055698553
    - type: nauc_ndcg_at_1000_diff1
      value: 1.3886748577056562
    - type: nauc_ndcg_at_1000_max
      value: 45.41548784147603
    - type: nauc_ndcg_at_1000_std
      value: 69.30388009311415
    - type: nauc_ndcg_at_100_diff1
      value: 0.4312493032685509
    - type: nauc_ndcg_at_100_max
      value: 45.2714318986444
    - type: nauc_ndcg_at_100_std
      value: 73.00621559010233
    - type: nauc_ndcg_at_10_diff1
      value: -8.161869949696207
    - type: nauc_ndcg_at_10_max
      value: 44.11896916629053
    - type: nauc_ndcg_at_10_std
      value: 56.814234959093845
    - type: nauc_ndcg_at_1_diff1
      value: 6.616052060737538
    - type: nauc_ndcg_at_1_max
      value: 36.42502274158562
    - type: nauc_ndcg_at_1_std
      value: 50.542299349240814
    - type: nauc_ndcg_at_20_diff1
      value: -10.435311528666439
    - type: nauc_ndcg_at_20_max
      value: 40.17434792292328
    - type: nauc_ndcg_at_20_std
      value: 58.15224379743095
    - type: nauc_ndcg_at_3_diff1
      value: -8.681207709572954
    - type: nauc_ndcg_at_3_max
      value: 42.74075328162171
    - type: nauc_ndcg_at_3_std
      value: 52.252671273049266
    - type: nauc_ndcg_at_5_diff1
      value: -10.760752447599076
    - type: nauc_ndcg_at_5_max
      value: 45.30740412496431
    - type: nauc_ndcg_at_5_std
      value: 58.2580376338619
    - type: nauc_precision_at_1000_diff1
      value: -17.63226899483217
    - type: nauc_precision_at_1000_max
      value: 34.52005297813093
    - type: nauc_precision_at_1000_std
      value: 58.08147588022084
    - type: nauc_precision_at_100_diff1
      value: -1.6026030210260822
    - type: nauc_precision_at_100_max
      value: 46.64263585966634
    - type: nauc_precision_at_100_std
      value: 73.31086780620457
    - type: nauc_precision_at_10_diff1
      value: -7.9280637963804645
    - type: nauc_precision_at_10_max
      value: 49.556338319147216
    - type: nauc_precision_at_10_std
      value: 53.013180728865436
    - type: nauc_precision_at_1_diff1
      value: 5.8837841125663815
    - type: nauc_precision_at_1_max
      value: 57.15502209967149
    - type: nauc_precision_at_1_std
      value: 53.94752848627391
    - type: nauc_precision_at_20_diff1
      value: -12.831360657341229
    - type: nauc_precision_at_20_max
      value: 41.99544599867401
    - type: nauc_precision_at_20_std
      value: 55.9674807351615
    - type: nauc_precision_at_3_diff1
      value: -16.796733759190047
    - type: nauc_precision_at_3_max
      value: 46.054296733759244
    - type: nauc_precision_at_3_std
      value: 49.79209352778117
    - type: nauc_precision_at_5_diff1
      value: -15.871656413523668
    - type: nauc_precision_at_5_max
      value: 52.700458519160634
    - type: nauc_precision_at_5_std
      value: 57.1342030226753
    - type: nauc_recall_at_1000_diff1
      value: -0.8671141204967768
    - type: nauc_recall_at_1000_max
      value: 39.213878637976336
    - type: nauc_recall_at_1000_std
      value: 57.52498157883819
    - type: nauc_recall_at_100_diff1
      value: 13.71539607682519
    - type: nauc_recall_at_100_max
      value: 34.398894963723606
    - type: nauc_recall_at_100_std
      value: 38.15917686169161
    - type: nauc_recall_at_10_diff1
      value: 14.494212708704499
    - type: nauc_recall_at_10_max
      value: 19.727092277749353
    - type: nauc_recall_at_10_std
      value: 5.450799655125242
    - type: nauc_recall_at_1_diff1
      value: 18.849085390343852
    - type: nauc_recall_at_1_max
      value: 22.147807794097968
    - type: nauc_recall_at_1_std
      value: 8.226943075643607
    - type: nauc_recall_at_20_diff1
      value: 9.720808675841297
    - type: nauc_recall_at_20_max
      value: 19.01250825066701
    - type: nauc_recall_at_20_std
      value: 7.725806970920393
    - type: nauc_recall_at_3_diff1
      value: 7.127984664955145
    - type: nauc_recall_at_3_max
      value: 15.524675558616
    - type: nauc_recall_at_3_std
      value: 3.6362524696759704
    - type: nauc_recall_at_5_diff1
      value: 9.773840859655213
    - type: nauc_recall_at_5_max
      value: 17.976145684131815
    - type: nauc_recall_at_5_std
      value: 5.433479951527897
    - type: ndcg_at_1
      value: 68.0
    - type: ndcg_at_10
      value: 67.647
    - type: ndcg_at_100
      value: 52.568000000000005
    - type: ndcg_at_1000
      value: 48.936
    - type: ndcg_at_20
      value: 65.23
    - type: ndcg_at_3
      value: 68.073
    - type: ndcg_at_5
      value: 70.15400000000001
    - type: precision_at_1
      value: 74.0
    - type: precision_at_10
      value: 72.8
    - type: precision_at_100
      value: 54.32
    - type: precision_at_1000
      value: 21.788
    - type: precision_at_20
      value: 69.6
    - type: precision_at_3
      value: 73.333
    - type: precision_at_5
      value: 76.4
    - type: recall_at_1
      value: 0.192
    - type: recall_at_10
      value: 1.926
    - type: recall_at_100
      value: 12.967
    - type: recall_at_1000
      value: 46.414
    - type: recall_at_20
      value: 3.6020000000000003
    - type: recall_at_3
      value: 0.5950000000000001
    - type: recall_at_5
      value: 1.008
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020 (default)
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: main_score
      value: 21.418
    - type: map_at_1
      value: 2.103
    - type: map_at_10
      value: 8.562
    - type: map_at_100
      value: 14.488999999999999
    - type: map_at_1000
      value: 15.966
    - type: map_at_20
      value: 10.862
    - type: map_at_3
      value: 4.922
    - type: map_at_5
      value: 5.771
    - type: mrr_at_1
      value: 26.53061224489796
    - type: mrr_at_10
      value: 41.18561710398445
    - type: mrr_at_100
      value: 42.23103797071357
    - type: mrr_at_1000
      value: 42.23103797071357
    - type: mrr_at_20
      value: 41.99007625028033
    - type: mrr_at_3
      value: 37.414965986394556
    - type: mrr_at_5
      value: 38.843537414965986
    - type: nauc_map_at_1000_diff1
      value: -19.351530359917472
    - type: nauc_map_at_1000_max
      value: -24.507017422899555
    - type: nauc_map_at_1000_std
      value: 4.42198895480301
    - type: nauc_map_at_100_diff1
      value: -18.850998775966502
    - type: nauc_map_at_100_max
      value: -24.362263151537178
    - type: nauc_map_at_100_std
      value: -0.5368896293104107
    - type: nauc_map_at_10_diff1
      value: -26.175172027837572
    - type: nauc_map_at_10_max
      value: -28.43026690361613
    - type: nauc_map_at_10_std
      value: -11.91118017447121
    - type: nauc_map_at_1_diff1
      value: -20.487774952653478
    - type: nauc_map_at_1_max
      value: -27.48651530838805
    - type: nauc_map_at_1_std
      value: -14.850754695409051
    - type: nauc_map_at_20_diff1
      value: -18.37972840319288
    - type: nauc_map_at_20_max
      value: -25.41263310281494
    - type: nauc_map_at_20_std
      value: -14.407088455977735
    - type: nauc_map_at_3_diff1
      value: -18.703214405275403
    - type: nauc_map_at_3_max
      value: -30.055160976096566
    - type: nauc_map_at_3_std
      value: -13.900503759042953
    - type: nauc_map_at_5_diff1
      value: -24.059397135404634
    - type: nauc_map_at_5_max
      value: -31.419338369603224
    - type: nauc_map_at_5_std
      value: -14.081937493608754
    - type: nauc_mrr_at_1000_diff1
      value: -19.253002712346046
    - type: nauc_mrr_at_1000_max
      value: -41.229418795229115
    - type: nauc_mrr_at_1000_std
      value: -8.194012889395678
    - type: nauc_mrr_at_100_diff1
      value: -19.253002712346046
    - type: nauc_mrr_at_100_max
      value: -41.229418795229115
    - type: nauc_mrr_at_100_std
      value: -8.194012889395678
    - type: nauc_mrr_at_10_diff1
      value: -20.181934921966565
    - type: nauc_mrr_at_10_max
      value: -41.52122062813685
    - type: nauc_mrr_at_10_std
      value: -8.517353777317007
    - type: nauc_mrr_at_1_diff1
      value: -14.93163259442193
    - type: nauc_mrr_at_1_max
      value: -28.271418042405944
    - type: nauc_mrr_at_1_std
      value: -8.483373359409944
    - type: nauc_mrr_at_20_diff1
      value: -18.71853810624142
    - type: nauc_mrr_at_20_max
      value: -41.643831727769445
    - type: nauc_mrr_at_20_std
      value: -7.994451407552443
    - type: nauc_mrr_at_3_diff1
      value: -20.10234227022684
    - type: nauc_mrr_at_3_max
      value: -41.481700697105964
    - type: nauc_mrr_at_3_std
      value: -10.1964348120824
    - type: nauc_mrr_at_5_diff1
      value: -22.378294273446333
    - type: nauc_mrr_at_5_max
      value: -42.399016719230765
    - type: nauc_mrr_at_5_std
      value: -9.64387750117273
    - type: nauc_ndcg_at_1000_diff1
      value: -20.46602931039575
    - type: nauc_ndcg_at_1000_max
      value: -29.51388332800775
    - type: nauc_ndcg_at_1000_std
      value: 31.97369133164661
    - type: nauc_ndcg_at_100_diff1
      value: -20.175041013877696
    - type: nauc_ndcg_at_100_max
      value: -36.286223372960904
    - type: nauc_ndcg_at_100_std
      value: 18.299490153297647
    - type: nauc_ndcg_at_10_diff1
      value: -24.02376235671449
    - type: nauc_ndcg_at_10_max
      value: -35.828837894026115
    - type: nauc_ndcg_at_10_std
      value: -4.55634576055288
    - type: nauc_ndcg_at_1_diff1
      value: -17.757931878350778
    - type: nauc_ndcg_at_1_max
      value: -28.882474074071734
    - type: nauc_ndcg_at_1_std
      value: -2.7961892265024058
    - type: nauc_ndcg_at_20_diff1
      value: -14.096289255526088
    - type: nauc_ndcg_at_20_max
      value: -34.41866397107521
    - type: nauc_ndcg_at_20_std
      value: -11.18648918839053
    - type: nauc_ndcg_at_3_diff1
      value: -17.842815168108977
    - type: nauc_ndcg_at_3_max
      value: -38.621085644925195
    - type: nauc_ndcg_at_3_std
      value: -3.8881155902480544
    - type: nauc_ndcg_at_5_diff1
      value: -25.284864428560216
    - type: nauc_ndcg_at_5_max
      value: -38.237375550106336
    - type: nauc_ndcg_at_5_std
      value: -4.911301062236913
    - type: nauc_precision_at_1000_diff1
      value: 8.807028730460438
    - type: nauc_precision_at_1000_max
      value: 37.1813389306755
    - type: nauc_precision_at_1000_std
      value: 50.105218819171206
    - type: nauc_precision_at_100_diff1
      value: -11.451048560927282
    - type: nauc_precision_at_100_max
      value: -18.494269088171183
    - type: nauc_precision_at_100_std
      value: 61.93415991533763
    - type: nauc_precision_at_10_diff1
      value: -20.970160893678482
    - type: nauc_precision_at_10_max
      value: -33.05509638276482
    - type: nauc_precision_at_10_std
      value: -2.7821722336643617
    - type: nauc_precision_at_1_diff1
      value: -14.93163259442193
    - type: nauc_precision_at_1_max
      value: -28.271418042405944
    - type: nauc_precision_at_1_std
      value: -8.483373359409944
    - type: nauc_precision_at_20_diff1
      value: -0.4353890707357106
    - type: nauc_precision_at_20_max
      value: -24.429655423454683
    - type: nauc_precision_at_20_std
      value: -3.4047901749399783
    - type: nauc_precision_at_3_diff1
      value: -12.694326928341601
    - type: nauc_precision_at_3_max
      value: -39.390569182573856
    - type: nauc_precision_at_3_std
      value: -8.824591692422153
    - type: nauc_precision_at_5_diff1
      value: -24.96294483100504
    - type: nauc_precision_at_5_max
      value: -39.857140509888495
    - type: nauc_precision_at_5_std
      value: -8.166429095904583
    - type: nauc_recall_at_1000_diff1
      value: -19.26364200094709
    - type: nauc_recall_at_1000_max
      value: -13.410785253002475
    - type: nauc_recall_at_1000_std
      value: 79.88850839052468
    - type: nauc_recall_at_100_diff1
      value: -24.001850273182704
    - type: nauc_recall_at_100_max
      value: -35.88316231220963
    - type: nauc_recall_at_100_std
      value: 31.815424604607674
    - type: nauc_recall_at_10_diff1
      value: -26.40817358742444
    - type: nauc_recall_at_10_max
      value: -33.727382714288446
    - type: nauc_recall_at_10_std
      value: -14.552547474689526
    - type: nauc_recall_at_1_diff1
      value: -20.487774952653478
    - type: nauc_recall_at_1_max
      value: -27.48651530838805
    - type: nauc_recall_at_1_std
      value: -14.850754695409051
    - type: nauc_recall_at_20_diff1
      value: -12.188115473749033
    - type: nauc_recall_at_20_max
      value: -32.11814820672923
    - type: nauc_recall_at_20_std
      value: -17.398182571029892
    - type: nauc_recall_at_3_diff1
      value: -17.529776818775066
    - type: nauc_recall_at_3_max
      value: -39.34912622762624
    - type: nauc_recall_at_3_std
      value: -17.868268060845814
    - type: nauc_recall_at_5_diff1
      value: -27.32652911017479
    - type: nauc_recall_at_5_max
      value: -39.898687035007576
    - type: nauc_recall_at_5_std
      value: -16.732887465142213
    - type: ndcg_at_1
      value: 23.469
    - type: ndcg_at_10
      value: 21.418
    - type: ndcg_at_100
      value: 34.251
    - type: ndcg_at_1000
      value: 45.371
    - type: ndcg_at_20
      value: 23.238
    - type: ndcg_at_3
      value: 23.886
    - type: ndcg_at_5
      value: 21.11
    - type: precision_at_1
      value: 26.531
    - type: precision_at_10
      value: 20.0
    - type: precision_at_100
      value: 7.388
    - type: precision_at_1000
      value: 1.488
    - type: precision_at_20
      value: 16.02
    - type: precision_at_3
      value: 26.531
    - type: precision_at_5
      value: 21.633
    - type: recall_at_1
      value: 2.103
    - type: recall_at_10
      value: 14.81
    - type: recall_at_100
      value: 46.622
    - type: recall_at_1000
      value: 80.69800000000001
    - type: recall_at_20
      value: 22.861
    - type: recall_at_3
      value: 6.399000000000001
    - type: recall_at_5
      value: 8.23
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification (default)
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 65.7666015625
    - type: ap
      value: 11.843884703213776
    - type: ap_weighted
      value: 11.843884703213776
    - type: f1
      value: 50.277795864693054
    - type: f1_weighted
      value: 73.18095534864581
    - type: main_score
      value: 65.7666015625
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification (default)
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 63.28522920203735
    - type: f1
      value: 63.3721509844546
    - type: f1_weighted
      value: 62.21321405962959
    - type: main_score
      value: 63.28522920203735
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering (default)
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: main_score
      value: 48.905527607381
    - type: v_measure
      value: 48.905527607381
    - type: v_measure_std
      value: 1.6720470024352694
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015 (default)
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 86.44572927221792
    - type: cosine_accuracy_threshold
      value: 87.59676218032837
    - type: cosine_ap
      value: 75.63030766992325
    - type: cosine_f1
      value: 69.44552655499287
    - type: cosine_f1_threshold
      value: 86.22946739196777
    - type: cosine_precision
      value: 68.37126054717464
    - type: cosine_recall
      value: 70.55408970976254
    - type: dot_accuracy
      value: 86.44572927221792
    - type: dot_accuracy_threshold
      value: 175.19352436065674
    - type: dot_ap
      value: 75.63032114657348
    - type: dot_f1
      value: 69.44552655499287
    - type: dot_f1_threshold
      value: 172.45893478393555
    - type: dot_precision
      value: 68.37126054717464
    - type: dot_recall
      value: 70.55408970976254
    - type: euclidean_accuracy
      value: 86.44572927221792
    - type: euclidean_accuracy_threshold
      value: 70.43645977973938
    - type: euclidean_ap
      value: 75.6303708231987
    - type: euclidean_f1
      value: 69.44552655499287
    - type: euclidean_f1_threshold
      value: 74.21733140945435
    - type: euclidean_precision
      value: 68.37126054717464
    - type: euclidean_recall
      value: 70.55408970976254
    - type: main_score
      value: 75.7377286185127
    - type: manhattan_accuracy
      value: 86.55897955534363
    - type: manhattan_accuracy_threshold
      value: 1556.027603149414
    - type: manhattan_ap
      value: 75.7377286185127
    - type: manhattan_f1
      value: 69.66236955187233
    - type: manhattan_f1_threshold
      value: 1654.3787002563477
    - type: manhattan_precision
      value: 65.1435132032147
    - type: manhattan_recall
      value: 74.85488126649076
    - type: max_accuracy
      value: 86.55897955534363
    - type: max_ap
      value: 75.7377286185127
    - type: max_f1
      value: 69.66236955187233
    - type: max_precision
      value: 68.37126054717464
    - type: max_recall
      value: 74.85488126649076
    - type: similarity_accuracy
      value: 86.44572927221792
    - type: similarity_accuracy_threshold
      value: 87.59676218032837
    - type: similarity_ap
      value: 75.63030766992325
    - type: similarity_f1
      value: 69.44552655499287
    - type: similarity_f1_threshold
      value: 86.22946739196777
    - type: similarity_precision
      value: 68.37126054717464
    - type: similarity_recall
      value: 70.55408970976254
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus (default)
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 88.97038848139093
    - type: cosine_accuracy_threshold
      value: 83.80404710769653
    - type: cosine_ap
      value: 85.91804313814289
    - type: cosine_f1
      value: 78.21080602302922
    - type: cosine_f1_threshold
      value: 82.21379518508911
    - type: cosine_precision
      value: 75.10632265381344
    - type: cosine_recall
      value: 81.5829996920234
    - type: dot_accuracy
      value: 88.97038848139093
    - type: dot_accuracy_threshold
      value: 167.60810613632202
    - type: dot_ap
      value: 85.91804480684166
    - type: dot_f1
      value: 78.21080602302922
    - type: dot_f1_threshold
      value: 164.42759037017822
    - type: dot_precision
      value: 75.10632265381344
    - type: dot_recall
      value: 81.5829996920234
    - type: euclidean_accuracy
      value: 88.97038848139093
    - type: euclidean_accuracy_threshold
      value: 80.48837184906006
    - type: euclidean_ap
      value: 85.91804603491305
    - type: euclidean_f1
      value: 78.21080602302922
    - type: euclidean_f1_threshold
      value: 84.34738516807556
    - type: euclidean_precision
      value: 75.10632265381344
    - type: euclidean_recall
      value: 81.5829996920234
    - type: main_score
      value: 86.05361584367344
    - type: manhattan_accuracy
      value: 89.02472154305894
    - type: manhattan_accuracy_threshold
      value: 1732.803726196289
    - type: manhattan_ap
      value: 86.05361584367344
    - type: manhattan_f1
      value: 78.20484500404977
    - type: manhattan_f1_threshold
      value: 1832.084083557129
    - type: manhattan_precision
      value: 74.93297587131367
    - type: manhattan_recall
      value: 81.7754850631352
    - type: max_accuracy
      value: 89.02472154305894
    - type: max_ap
      value: 86.05361584367344
    - type: max_f1
      value: 78.21080602302922
    - type: max_precision
      value: 75.10632265381344
    - type: max_recall
      value: 81.7754850631352
    - type: similarity_accuracy
      value: 88.97038848139093
    - type: similarity_accuracy_threshold
      value: 83.80404710769653
    - type: similarity_ap
      value: 85.91804313814289
    - type: similarity_f1
      value: 78.21080602302922
    - type: similarity_f1_threshold
      value: 82.21379518508911
    - type: similarity_precision
      value: 75.10632265381344
    - type: similarity_recall
      value: 81.5829996920234
    task:
      type: PairClassification
tags:
- mteb
---
