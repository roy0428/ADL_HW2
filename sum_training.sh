#!/usr/bin/env bash

python3 /home/p0428q/usr/ADL/transformers-main/examples/pytorch/summarization/run_summarization_no_trainer.py \
    --train_file  data/train_all.json \
    --validation_file data/reference.json \
    --max_source_length 2048 \
    --max_target_length 64 \
    --pad_to_max_length \
    --model_name_or_path google/mt5-small \
    --text_column maintext \
    --summary_column title \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --num_warmup_steps 60 \
    --output_dir HW2_training_result \
    --seed 228 \
    --num_beams 4 \
    --source_prefix summarize:  \
    --preprocessing_num_workers 1 \
    --num_train_epochs 2