#!/usr/bin/env bash

python3 HW2_predict.py \
    --out_put_jsonl prediction.jsonl \
    --test_file data/test.json \
    --pad_to_max_length \
    --text_column maintext \
    --use_slow_tokenizer \
    --model_name_or_path HW2_training_result \
    --max_target_length 64 \
    --num_beams 10 \
    --source_prefix "summarize: " \
    --preprocessing_num_workers 1 \
    --per_device_eval_batch_size 8



