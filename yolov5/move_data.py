import shutil
import json
import os
import argparse
from tqdm import tqdm

def move_data(data_path, json_path, folder_name, is_test=False):

    if not os.path.exists(os.path.join(data_path, "images")):
        os.makedirs(os.path.join(data_path, "images"))
    if not os.path.exists(os.path.join(data_path,"images", folder_name)):
        os.makedirs(os.path.join(data_path,"images", folder_name))

    if not is_test:
        if not os.path.exists(os.path.join(data_path, "labels")):
            os.makedirs(os.path.join(data_path, "labels"))
        if not os.path.exists(os.path.join(data_path,"labels", folder_name)):
            os.makedirs(os.path.join(data_path, "labels",folder_name))

    with open(json_path) as json_file:
        json_data = json.load(json_file)
        save = {}
        for t in json_data["images"]:
            change = t["file_name"].replace("/","_")
            save[t['id']]= change
            shutil.copy(os.path.join(data_path, t["file_name"]), os.path.join(data_path, "images", folder_name, change))
            
        if not is_test:
            an_save={}
            for t in json_data["annotations"]:
                if an_save.get(t['image_id'])==None:
                    an_save[t['image_id']] = []
                an_save[t['image_id']].append([t['category_id'], *t["bbox"]])
                
            for i,v in tqdm(an_save.items()):
                name = save[i]
                name = name.replace(".jpg", ".txt")
                data = []
                for b in v:
                    cat_id = b[0]
                    b[1] = b[1] + b[3] / 2
                    b[2] = b[2] + b[4] / 2
                    b[1] /= 1024.0
                    b[2] /= 1024.0
                    b[3] /= 1024.0
                    b[4] /= 1024.0
                    b = list(map(str, b))
                    data.append(' '.join(b))
                write_data = '\n'.join(data)
                f = open(os.path.join(data_path, "labels", folder_name, name), 'w')
                f.write(write_data)
                f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data_path', type=str, default='/opt/ml/detection/dataset')
    parser.add_argument('-j', '--json_path', type=str, default='/opt/ml/detection/dataset/train.json')
    parser.add_argument('-f', '--folder_name', type=str, default='train')
    args = parser.parse_args()

    move_data(args.data_path, args.json_path, args.folder_name)
