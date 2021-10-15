#!/usr/bin/bash

python tools/train.py configs/trash/cascade_rcnn_r50_fpn.py

python tools/test.py confings/trash/cascade_rcnn_r50_fpn.py work_dirs/cascade_rcnn_r50_fpn/best*.pth --out work_dirs/cascade_rcnn_r50_fpn/best.pkl

python tools/pkl_to_submission.py --pkl work_dirs/cascade_rcnn_r50_fpn/best.pkl --csv work_dirs/cascade_rcnn_r50_fpn.csv
