import argparse
import shutil
import os

def custom_filename(x):
    x = x.split(".")[1]
    x = x.split("_")
    x_f = '_'.join(x[:-1])
    x = "/".join([x_f, x[-1]])
    x = x + ".jpg"
    return x

def move_files(arg):

    file_list = []
    file_list = os.listdir(arg.source)

    if not os.path.exists(arg.dst):
        os.makedirs(arg.dst)
    
    for i, name in enumerate(file_list):
        label_name = 'test_' + name
        shutil.copy(os.path.join(arg.source, name), os.path.join(arg.dst, label_name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='runs/detect/psudo/labels', help='source')
    parser.add_argument('--dst', type=str, default='/opt/ml/detection/dataset/labels/test', help='dst')
    arg = parser.parse_args()
    
    move_files(arg)
