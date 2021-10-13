#!/bin/bash

#python valid.py
#python move_data.py
#python move_data.py -j /opt/ml/detection/dataset/seed2021/train.json -f train_seed2021
#python move_data.py -j /opt/ml/detection/dataset/seed2021/val.json -f val_seed2021
#bash weights/download_weights.sh

#python train.py --img-size 512 --batch-size 32 --epochs 100 --data trash_all.yaml --multi-scale --weights yolov5l.pt --cache --name test

#python detect.py --img-size 512 --source /opt/ml/detection/dataset/test --weights runs/train/test/weights/best.pt --augment --save-txt --save-conf --name test

#python submission.py -f test -n test.csv

#python detect_pseudo.py --img-size 512 --source /opt/ml/detection/dataset/test --weights runs/train/test/weights/best.pt --augment --save-txt --nosave --name pre_test_pseudo

#python move_pseudo.py --source runs/detect/pre_test_pseudo/labels --dst /opt/ml/detection/dataset/labels/test
#python move_data.py -j /opt/ml/detection/dataset/test.json -f test

python train.py --img-size 512 --batch-size 32 --epochs 100 --data trash_pseudo.yaml --multi-scale --weights yolov5l.pt --name test_pseudo

python detect.py --img-size 512 --source /opt/ml/detection/dataset/test --weights runs/train/test_pseudo/weights/best.pt --augment --save-txt --save-conf --name test_pseudo

python submission.py -f test_pseudo -n test_pseudo.csv
