## Preprocessing
Data preprocessing for summarization
```
python3 preprocessing.py --data_dir /path/to/data.jsonl --output_dir_for_training /path/to/processed-data.json
```
Do the following to process the training and validation data
```
python3 preprocessing.py  \
    --data_dir data/train.jsonl \
    --output_dir_for_training data/train_all.json
python3 preprocessing_for_public.py \
    --data_dir data/public.jsonl \
    --output_dir_for_testing data/test.json \
    --test_file data/reference.json
```

## Training
Model training for summarization
```
python3 run_summarization_no_trainer.py \
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
    --num_warmup_steps 500 \
    --output_dir HW2_training_result \
    --seed 228 \
    --num_beams 4 \
    --source_prefix summarize:  \
    --preprocessing_num_workers 1 \
    --num_train_epochs 16

## Prediction
After data preprocessing and model training, simply run the following shell script
```
bash run.sh data/public.jsonl prediction.jsonl
```