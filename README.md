# 0. Quick Start
```bash
$ sh run.sh
```

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

## 1.2. Prepare Dataset
```bash
$ wget https://aistages-prod-server-public.s3.amazonaws.com/app/Competitions/000076/data/data.tar.gz
$ tar xvfz data.tar.gz
$ mv ./data/ ./dataset
$ rm ./data.tar.gz
$ rm -rf ./dataset/*/.*.jpg
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
	$ cd ./mmdetection
	$ pip install -v -e . 
	```
2. YOLOv5
	```bash
	$ cd ./yolov5
	$ pip install -r requirements.txt
	```

3. convert2Yolo
	```bash
	$ git clone https://github.com/ssaru/convert2Yolo.git
	$ cd ./convert2Yolo
	$ pip3 install -r requirements.txt
	```

4. WBF (Weighted Boxes Fusion)
	```bash
	$ pip install ensemble-boxes
	```
	> ref: [WBF](https://github.com/ZFTurbo/Weighted-Boxes-Fusion)

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
├─submissions_for_single_model/
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
* Prepare the `*.names` file as below.
	```bash
	$ cat ./dataset/trash_coco.names
	General trash
	Paper
	Paper pack
	Metal
	Glass
	Plastic
	Styrofoam
	Plastic bag
	Battery
	Clothing
	```

* Convert dataset format by using `convert2Yolo`
	```bash
	$ cd ./convert2Yolo
	$ python3 example.py \
		--datasets COCO \
		--img_path ../dataset/ \
		--label ../dataset/train.json \
		--convert_output_path ../dataset/ \
		--img_type ".jpg" \
		--manifest_path ../dataset \
		--cls_list_file ../dataset/trash_coco.names
	```

* Then, we have the following structure.
	```plain text
	./
	├─dataset/
	|    ├─train/
	|    |   ├─0000.jpg
	|    |   ├─0000.txt # YOLO format
	|    |   ├─ ...
	|    |   ├─48xx.jpg
	|    |   └─48xx.txt # YOLO format
	|    ├─test/
	|    |   ├─0000.jpg
	|    |   ├─ ...
	|    |   └─4870.jpg
	|    ├─train.json # COCO format
	|    └─test.json  # COCO format
	|
	├─mmdetection/
	├─yolov5/
	├─convert2Yolo
	|
	├─submissions_for_single_model/
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

## 2.2. Train 4 models
1. detectors-cascade-rcnn-r50
	```bash
	$ cd ./mmdetection
	$ python tools/train.py \
		configs/trash/detectors_cascade_rcnn_r50.py
	```

2. cascade-rcnn-swin-base
	```bash
	$ cd ./mmdetection
	$ python tools/train.py \
		configs/trash/swin/cascade_rcnn_swin_base_fpn.py
	```

3. cascade-rcnn-r50-fpn
	```bash
	$ cd ./mmdetection
	$ python tools/train.py \
		configs/trash/cascade_rcnn_r50_fpn.py 
	```

4. YOLOv5x6
	* Train pre-trained model for 10-epochs
	* Train pre-trained model for 20-epochs

# 3. Inference and Make Submission
1. detectors-cascade-rcnn-r50
	```bash
	$ cd ./mmdetection
	$ python tools/test.py \
		confings/trash/detectors_cascade_rcnn_r50.py \
		work_dirs/detectors_cascade_rcnn_r50/best*.pth \
		--out work_dirs/detectors_cascade_rcnn_r50/best.pkl
	$ python tools/pkl_to_submission.py \
		--pkl work_dirs/detectors_cascade_rcnn_r50/best.pkl \
		--csv work_dirs/detectors_cascade_rcnn_r50.csv
	$ cp work_dirs/detectors_cascade_rcnn_r50.csv \
		../submissions_for_single_model/submission_detectors_cascade_rcnn_r50.csv
	```

2. cascade-rcnn-r50-fpn
	```bash
	$ cd ./mmdetection
	$ python confings/trash/cascade_rcnn_r50_fpn.py \
		work_dirs/cascade_rcnn_r50_fpn/best*.pth \
		--out work_dirs/cascade_rcnn_r50_fpn/best.pkl
	$ python tools/pkl_to_submission.py \
		--pkl work_dirs/cascade_rcnn_r50_fpn/best.pkl \
		--csv work_dirs/cascade_rcnn_r50_fpn.csv
	$ cp work_dirs/cascade_rcnn_r50_fpn.csv \
		../submissions_for_single_model/submission_cascade_rcnn_r50_fpn.csv
	```

3. cascade-rcnn-swin-base
	```bash
	$ cd ./mmdetection
	$ python confings/trash/swin/cascade_rcnn_swin_base_fpn.py \
		work_dirs/cascade_rcnn_swin_base_fpn/best*.pth \
		--out work_dirs/cascade_rcnn_swin_base_fpn/best.pkl
	$ python tools/pkl_to_submission.py \
		--pkl work_dirs/cascade_rcnn_swin_base_fpn/best.pkl \
		--csv work_dirs/cascade_rcnn_swin_base_fpn.csv
	$ cp work_dirs/cascade_rcnn_swin_base_fpn.csv \
		../submissions_for_single_model/submission_cascade_rcnn_r50_fpn.csv
	```

4. YOLOv5x6
	* Ensemble 2 models (Use YOLOv5 built-in ensemble)


# 4. Ensembling
* WBF (Weighted Boxes Fusion)
	* Config Format
		```json
		{
    		"csvs": ["./output_0.csv", 
    		         "./output_1.csv",
    		         "./output_2.csv",
    		         "./output_3.csv",
    		         "./output_4.csv",
    		         "./output_5.csv"
    		         ],
    		"save_path": "./result_outputs.csv",
    		"ensemble_mode": "wbf",
    		"weights": "None",
    		"iou_thr": 0.5,
    		"skip_box_thr": 0.0001,
    		"sigma": 0.1,
    		"img_size": 1024
		}
		```
		> **csvs:** 단일 모델이 예측한 결과 `csv` 파일들  
		> **ensemble_mode:** Choose the ensemble mode (`wbf`, `nms`, `nmw`, `snms`)  

# 5. Get the `submission.csv`
```bash
$ python ensemble.py
```

# 6. Participants
|name|김서기|김승훈|손지아|이상은|조익수|배민한|
|:--:|:----:|:----:|:----:|:----:|:----:|:----:|

