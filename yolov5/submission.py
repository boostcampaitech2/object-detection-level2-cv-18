import os
import argparse
import pandas as pd
from tqdm import tqdm

def make_file(x):
    file_names = x.split(".")
    return [int(file_names[0]), x]

def make_lines(x):
    x = x.replace("\n", "")
    x = x.split(" ")
    x[1] = float(x[1]) * 1024.0 # x center
    x[2] = float(x[2]) * 1024.0 # y center
    x[3] = float(x[3]) * 1024.0 # w
    x[4] = float(x[4]) * 1024.0 # h
    
    x[1] = x[1] - x[3] / 2
    x[2] = x[2] - x[4] / 2
    x[3] += x[1]
    x[4] += x[2]
    
    x[1] = str(x[1])
    x[2] = str(x[2])
    x[3] = str(x[3])
    x[4] = str(x[4])
    return ' '.join([x[0], x[5], x[1], x[2], x[3], x[4]])


def make_submission(path_dir):
    
    prediction_strings = []
    file_names = []

    file_list = os.listdir(path_dir)
    file_list.remove('labels')
    file_list = list(map(make_file, file_list))
    file_list.sort(key=lambda x:x[0])

    for i,file_name in tqdm(file_list):
        file_name = file_name.replace('.jpg', '.txt')
        if os.path.exists(os.path.join(path_dir, 'labels', file_name)):
            f = open(os.path.join(path_dir, 'labels', file_name), 'r')
            #predictions
            lines = f.readlines()
            lines = list(map(make_lines, lines))
            lines = ' '.join(lines)
            prediction_strings.append(lines)
            f.close()
        else:
            prediction_strings.append("")
        file_name = file_name.split('.')[0]
        file_name = file_name.split('_')
        file_name_f = '_'.join(file_name[:-1])
        file_name = '/'.join([file_name_f,file_name[-1]])
        file_name = 'test' + file_name + '.jpg'
        file_names.append(file_name)
        
    return prediction_strings,file_names


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--runs_dir', type=str, default='/opt/ml/yolov5/runs')
    parser.add_argument('-f', '--fold_dir', type=str, default='exp')
    parser.add_argument('-n', '--submission_name', type=str, default='y_baseline_e43_b32.csv')
    args = parser.parse_args()
  
    prediction_strings, file_names = make_submission(os.path.join(args.runs_dir, 'detect', args.fold_dir))
    
    submission = pd.DataFrame()
    submission['PredictionString'] = prediction_strings
    submission['image_id'] = file_names
    submission.to_csv(os.path.join(args.runs_dir, 'train', args.fold_dir, args.submission_name), index=None)
    
    print(submission.head())
