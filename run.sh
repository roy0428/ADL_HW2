python3 preprocessing_for_public.py \
    --data_dir ${1} \
    --output_dir_for_testing test.json \
    --test_file reference.json
python3 HW2_predict.py \
    --out_put_jsonl ${2} \
    --test_file test.json \
    --pad_to_max_length \
    --text_column maintext \
    --use_slow_tokenizer \
    --model_name_or_path HW2_training_result \
    --max_target_length 64 \
    --num_beams 4 \
    --source_prefix "summarize: " \
    --preprocessing_num_workers 1 \
    --per_device_eval_batch_size 8