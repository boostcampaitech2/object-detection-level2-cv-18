#!/usr/bin/bash

python tools/train.py configs/trash/detectors_cascade_rcnn_r50.py

python tools/test.py confings/trash/detectors_cascade_rcnn_r50.py work_dirs/detectors_cascade_rcnn_r50/best*.pth --out work_dirs/detectors_cascade_rcnn_r50/best.pkl

python tools/pkl_to_submission.py --pkl work_dirs/detectors_cascade_rcnn_r50/best.pkl --csv work_dirs/detectors_cascade_rcnn_r50.csv
