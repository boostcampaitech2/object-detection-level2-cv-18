# Object Detection

## :one: Abstract



## :two: Models

> **Run in 'mmdetection' folder**  
> (Architecture / backbone / Neck)

### Cascade R-CNN / ResNet50 / FPN

`sh tools/run_cascade.sh`

```bash
# train
python tools/train.py configs/trash/detectors_cascade_rcnn_r50.py
# test
python tools/test.py confings/trash/detectors_cascade_rcnn_r50.py work_dirs/detectors_cascade_rcnn_r50/best*.pth --out work_dirs/detectors_cascade_rcnn_r50/best.pkl
# make submission
python tools/pkl_to_submission.py --pkl work_dirs/detectors_cascade_rcnn_r50/best.pkl --csv work_dirs/detectors_cascade_rcnn_r50.csv
```

###  Cascade R-CNN / ResNet50 / RFP+SAC  (DetectoRS)

`sh tools/run_detectros.sh`

```bash
# train
python tools/train.py configs/trash/cascade_rcnn_r50_fpn.py
# test
python tools/test.py confings/trash/cascade_rcnn_r50_fpn.py work_dirs/cascade_rcnn_r50_fpn/best*.pth --out work_dirs/cascade_rcnn_r50_fpn/best.pkl
# make submission
python tools/pkl_to_submission.py --pkl work_dirs/cascade_rcnn_r50_fpn/best.pkl --csv work_dirs/cascade_rcnn_r50_fpn.csv
```

### Cascade R-CNN / Swin base / FPN

`sh tools/run_swin.sh`

```bash
# train
python tools/train.py configs/trash/swin/cascade_rcnn_swin_base_fpn.py
# test
python tools/test.py confings/trash/swin/cascade_rcnn_swin_base_fpn.py work_dirs/cascade_rcnn_swin_base_fpn/best*.pth --out work_dirs/cascade_rcnn_swin_base_fpn/best.pkl
# make submission
python tools/pkl_to_submission.py --pkl work_dirs/cascade_rcnn_swin_base_fpn/best.pkl --csv work_dirs/cascade_rcnn_swin_base_fpn.csv
```

---

> **Run in 'yolov5' folder**




## :three:

