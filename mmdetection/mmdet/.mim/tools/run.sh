python tools/train.py configs/trash/swin/cascade_rcnn_swin_large_F_D_adamw.py --cfg-options model.pretrained=https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_large_patch4_window7_224_22k.pth

python tools/test.py confings/trash/swin/cascade_rcnn_swin_large_F_D_adamw.py work_dirs/cascade_rcnn_swin_large_F_D_adamw/best*.pth --out work_dirs/cascade_rcnn_swin_large_F_D_adamw/best.pkl

python tools/pkl_to_submission.py --pkl work_dirs/cascade_rcnn_swin_large_F_D_adamw/best.pkl --csv work_dirs/cascade_rcnn_swin_large_F_D_adamw.csv
