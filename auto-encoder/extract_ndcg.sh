#!/bin/bash

json_file=$(find results/$1 -name "NFCorpus.json")
ndcg_score=$(grep -oP '"ndcg_at_10"\s*:\s*\K[0-9.]+' "$json_file")
echo "NDCG@10 score: $ndcg_score"

