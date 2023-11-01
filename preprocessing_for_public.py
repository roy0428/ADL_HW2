from argparse import ArgumentParser
from pathlib import Path
import json
import jsonlines
import random
import ipdb
import copy

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--data_dir",
                        default='HW2/data/public.jsonl',
                        type=str)
    parser.add_argument("--output_dir_for_testing",
                        default='HW2/data/test.json',
                        type=str)
    parser.add_argument("--output_dir_for_reference",
                        default='HW2/data/reference.json',
                        type=str)

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    data = []
    testing_list = []
    reference_list = []
    
    with jsonlines.open(args.data_dir, 'r') as json_file:
        for item in json_file:
            data.append(item)
            
    for item in data:
        item.pop("date_publish")
        item.pop("source_domain")
        item.pop("split")
        reference_list.append(copy.copy(item))
        item.pop("title")
        testing_list.append(item)

    testing_json = {"data": testing_list}
    reference_json = {"data": reference_list}
    json.dump(testing_json, open(args.output_dir_for_testing, 'w'), indent=2, ensure_ascii=False)
    json.dump(reference_json, open(args.output_dir_for_reference, 'w'), indent=2, ensure_ascii=False)