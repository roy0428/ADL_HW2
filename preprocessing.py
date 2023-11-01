from argparse import ArgumentParser
from pathlib import Path
import json
import jsonlines
import random
import ipdb

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--data_dir",
                        default='HW2/data/train.jsonl',
                        type=str)
    parser.add_argument("--output_dir_for_training",
                        default='HW2/data/train_all.json',
                        type=str)
    # parser.add_argument("--output_dir_for_validation",
    #                     default='HW2/data/valid.json',
    #                     type=str)
    # parser.add_argument("--seperate_raito",
    #                     default=0.1,
    #                     type=float)

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    data = []
    training_list = []
    # validation_list = []
    # text_list =[]
    with jsonlines.open(args.data_dir, 'r') as json_file:
        for item in json_file:
            data.append(item)
    # random.shuffle(data)
    for index, item in enumerate(data):
        item.pop("date_publish")
        item.pop("source_domain")
        item.pop("split")
        # text_list.append(len(item['title']))
        # if index < len(data) * args.seperate_raito:
        #     validation_list.append(item)
        # else:
        training_list.append(item)
            
    training_json = {"data": training_list}
    # validation_json = {"data": validation_list}
    json.dump(training_json, open(args.output_dir_for_training, 'w'), indent=2, ensure_ascii=False)
    # json.dump(validation_json, open(args.output_dir_for_validation, 'w'), indent=2, ensure_ascii=False)