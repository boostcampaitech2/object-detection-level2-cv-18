# 1. Preparing

## 1.1. Environments
1. Python
2. PyTorch
3. Hardware
  * v100


## 1.2. Prepare Dataset
```bash
$ wget wget https://aistages-prod-server-public.s3.amazonaws.com/app/Competitions/000076/data/data.tar.gz
$ tar -xvfz data.tar.gz dataset
```
* dataset(*COCO Format*) structure
```plain text
./
└─dataset/
    ├─train/
    |   ├─0000.jpg
    |   ├─ ...
    |   └─48xx.jpg
    ├─test/
    |   ├─0000.jpg
    |   ├─ ...
    |   └─4870.jpg
    ├─train.json
    └─test.json
```
> *Trash Dataset Copy Rights:* ![Naver Connect](https://connect.or.kr)

## 1.3. Prepare Libraries
1. MMDetection
```bash
$ git clone https://github.com/open-mmlab/mmdetection.git
$ cd mmdetection
$ pip install -v -e . 
```
2. YOLOv5
```bash
$ git clone https://github.com/ultralytics/yolov5.git
$ cd yolov5
$ pip install -r requirements.txt
```

3. convert2Yolo
```bash
$ git clone https://github.com/ssaru/convert2Yolo.git
$ cd convert2Yolo
$ pip3 install -r requirements.txt
```

## 1.4. Completed Structure
```plain text
./
├─dataset/
|    ├─train/
|    |   ├─0000.jpg
|    |   ├─ ...
|    |   └─48xx.jpg
|    ├─test/
|    |   ├─0000.jpg
|    |   ├─ ...
|    |   └─4870.jpg
|    ├─train.json
|    └─test.json
|
├─mmdetection/
|    ├─
├─yolov5/
├─convert2Yolo
|
├─submissions_for_sigle_model/
|    ├─submission_yolov5s.csv
|    ├─submission_faster_rcnn.csv
|    ├─...
|    └─submission_swin.csv
|
├─run.py 
├─run.sh
|
└─submission.csv # Result of "python run.py" or "sh run.sh"
```

# 2. Training

# 3. Inferencing

# 4. Ensembling

# 5. From train To submission

