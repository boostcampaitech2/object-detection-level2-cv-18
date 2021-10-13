#!/usr/bin/bash

python tools/train.py configs/trash/swin/base_F_D_W_256.py --cfg-options model.pretrained=https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_base_patch4_window7_224_22k.pth

python tools/test.py confings/trash/swin/base_F_D_W_256.py work_dirs/base_F_D_W_256/best*.pth --out work_dirs/base_F_D_W_256/best.pkl

python tools/pkl_to_submission.py --pkl work_dirs/base_F_D_W_256/best.pkl --csv work_dirs/base_F_D_W_256.csv
