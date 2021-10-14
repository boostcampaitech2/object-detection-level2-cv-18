# 1. Preparing

## 1.1. Environments
0. System
	* OS
	```plain text
	$ uname -a
	Linux 78709cb2ea9c 4.4.0-59-generic #80-Ubuntu SMP Fri Jan 6 17:47:47 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
	```
	> **커널:** 4.4.0-59-generic 버전  
	> **OS:** x86 계열의 64bit 운영체제
	
	* CPU
	```plain text
	$ cat /proc/cpuinfo 
	Intel(R) Xeon(R) Gold 5120 CPU @ 2.20GHz
	```
	* GPU: v100
1. Python
2. PyTorch


## 1.2. Prepare Dataset
```bash
$ wget https://aistages-prod-server-public.s3.amazonaws.com/app/Competitions/000076/data/data.tar.gz
$ tar xvfz data.tar.gz dataset
$ rm data.tar.gz
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
> **Trash Dataset Copy Rights:** [Naver Connect](https://connect.or.kr)  
> **Trash Dataset Copy Rights License:** CC-BY-2.0

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

## 2.1. Before training, convert dataset format (**From COCO To YOLO**)

## 2.2. Train 4 models
1. detectors-cascade-rcnn-r50

2. cascade-rcnn-swin-base

3. cascade-rcnn-r50-fpn

4. YOLOv5x6
	* Train pre-trained model for 10-epochs
	* Train pre-trained model for 20-epochs
	* Ensemble 2 models (Use YOLOv5 built-in ensemble)

# 3. Inferencing

# 4. Ensembling
1. WBF (Weighted Boxes Fusion)

# 5. From train To submission
```bash
$ python run.py
```
OR
```bash
$ sh run.sh
```

6. Participants
---
participants : [김서기, 김승훈, 손지아, 이상은, 조익수, 배민한]
---
