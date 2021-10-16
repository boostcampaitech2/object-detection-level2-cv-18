#!/usr/bin/bash

python tools/train.py configs/trash/swin/cascade_rcnn_swin_base_fpn.py

python tools/test.py confings/trash/swin/cascade_rcnn_swin_base_fpn.py work_dirs/cascade_rcnn_swin_base_fpn/best*.pth --out work_dirs/cascade_rcnn_swin_base_fpn/best.pkl

python tools/pkl_to_submission.py --pkl work_dirs/cascade_rcnn_swin_base_fpn/best.pkl --csv work_dirs/cascade_rcnn_swin_base_fpn.csv
