import json
import os
import random
import argparse
from utils.seed_everything import seed_everything

def split_dataset(input_json, output_dir, val_ratio, random_seed):
    with open(input_json) as json_reader:
        dataset = json.load(json_reader)

    images = dataset['images']
    annotations = dataset['annotations']
    categories = dataset['categories']
    image_ids = [x.get('id') for x in images]
    image_ids.sort()
    random.shuffle(image_ids)

    num_val = int(len(image_ids) * val_ratio)
    num_train = len(image_ids) - num_val

    image_ids_val, image_ids_train = set(image_ids[:num_val]), set(image_ids[num_val:])

    train_images = [x for x in images if x.get('id') in image_ids_train]
    val_images = [x for x in images if x.get('id') in image_ids_val]
    train_annotations = [x for x in annotations if x.get('image_id') in image_ids_train]
    val_annotations = [x for x in annotations if x.get('image_id') in image_ids_val]

    train_data = {
        'images': train_images,
        'categories': categories,
        'annotations': train_annotations,
    }
    val_data = {
        'images': val_images,
        'categories': categories,
        'annotations': val_annotations,
    }

    output_seed_dir = os.path.join(output_dir, f'seed{random_seed}')
    os.makedirs(output_seed_dir, exist_ok=True)
    output_train_json = os.path.join(output_seed_dir, 'train.json')
    output_val_json = os.path.join(output_seed_dir, 'val.json')
    output_train_csv = os.path.join(output_seed_dir, 'train.csv')
    output_val_csv = os.path.join(output_seed_dir, 'val.csv')

    print(f'write {output_train_json}')
    with open(output_train_json, 'w') as train_writer:
        json.dump(train_data, train_writer)

    print(f'write {output_val_json}')
    with open(output_val_json, 'w') as val_writer:
        json.dump(val_data, val_writer)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-j', '--input_json', type=str, default='/opt/ml/detection/dataset/train.json')
    parser.add_argument('-d', '--output_dir', type=str, default='/opt/ml/detection/dataset/')
    parser.add_argument('-val', '--val_ratio', type=float, default=0.1)
    parser.add_argument('-s', '--random_seed', type=int, default=2021)

    args = parser.parse_args()

    seed_everything(2021)
    split_dataset(args.input_json, args.output_dir, args.val_ratio, args.random_seed)
