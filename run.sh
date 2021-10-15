# 1.1. dataset prepare
# seunghun
wget https://aistages-prod-server-public.s3.amazonaws.com/app/Competitions/000076/data/data.tar.gz
tar xvfz data.tar.gz
rm ./data.tar.gz
rm -rf ./data/*/.*.jpg
mv ./data/ ./dataset
cp ./trash_coco.names ./dataset

# 1.2. libraries prepare
# seunghun
cd ./mmdetection
pip install -v -e .

cd ../yolov5
pip install -r requirements.txt

cd ../convert2Yolo
pip3 install -r requirements.txt

cd ..
pip install ensemble-boxes


# 2.1. Convert format (coco -> yolo)
# seunghun
cd ./convert2Yolo
python3 example.py \
 	--datasets COCO \
 	--img_path ../dataset/ \
 	--label ../dataset/train.json \
 	--convert_output_path ../dataset/ \
 	--img_type ".jpg" \
 	--manifest_path ../dataset \
 	--cls_list_file ../dataset/trash_coco.names
cd ..

# 2.2. Train 4 models
# sangeun
cd ./mmdetection
python tools/train.py \
	configs/trash/detectors_cascade_rcnn_r50.py
python tools/train.py \
	configs/trash/swin/cascade_rcnn_swin_base_fpn.py
python tools/train.py \
	configs/trash/cascade_rcnn_r50_fpn.py 

# minhan
python tools/train.py \
	configs/z_config_1/base1008_2.py
cd ..

# seogi
cd ./yolov5
python train.py \
	--img 1024 --batch 4 --epochs 10 --data custom.yaml \
	--weights yolov5x6.pt --cache --name 10epoch
python train.py \
	--img 1024 --batch 4 --epochs 20 --data custom.yaml \
	--weights yolov5x6.pt --cache --name 20epochs
cd ..


# 3.1. inference and submission for single models
# sangeun
cd ./mmdetection
python tools/test.py \
	confings/trash/detectors_cascade_rcnn_r50.py \
	work_dirs/detectors_cascade_rcnn_r50/best*.pth \
	--out work_dirs/detectors_cascade_rcnn_r50/best.pkl
python tools/pkl_to_submission.py \
	--pkl work_dirs/detectors_cascade_rcnn_r50/best.pkl \
	--csv work_dirs/detectors_cascade_rcnn_r50.csv
cp work_dirs/detectors_cascade_rcnn_r50.csv \
	../submissions_for_single_model/submission_detectors_cascade_rcnn_r50.csv

python confings/trash/cascade_rcnn_r50_fpn.py \
	work_dirs/cascade_rcnn_r50_fpn/best*.pth \
	--out work_dirs/cascade_rcnn_r50_fpn/best.pkl
python tools/pkl_to_submission.py \
	--pkl work_dirs/cascade_rcnn_r50_fpn/best.pkl \
	--csv work_dirs/cascade_rcnn_r50_fpn.csv
cp work_dirs/cascade_rcnn_r50_fpn.csv \
	../submissions_for_single_model/submission_cascade_rcnn_r50_fpn.csv

python confings/trash/swin/cascade_rcnn_swin_base_fpn.py \
	work_dirs/cascade_rcnn_swin_base_fpn/best*.pth \
	--out work_dirs/cascade_rcnn_swin_base_fpn/best.pkl
python tools/pkl_to_submission.py \
	--pkl work_dirs/cascade_rcnn_swin_base_fpn/best.pkl \
	--csv work_dirs/cascade_rcnn_swin_base_fpn.csv
cp work_dirs/cascade_rcnn_swin_base_fpn.csv \
	../submissions_for_single_model/submission_cascade_rcnn_r50_fpn.csv

# minhan
python configs/z_config_1/base1008_2.py \
	work_dirs/base1008_2/best.pkl \
	--out work_dirs/base1008_2.py/best.pkl
python tools/pkl_to_submission.py \
	--pkl work_dirs/base1008_2/best.pkl \
	--csv work_dirs/base1008_2/submission_base1008_2_best.csv
cp work_dirs/base1008_2/submission_base1008_2_best.csv \
	../submissions_for_single_model/submission_bbase1008_2_best.csv
cd..

# seogi
cd ./yolov5
python detect.py \
	--weights ./weights/runs/10epoch/train/best.pt ./weights/runs/20epoch/train/best.pt \
	 --source ../dataset/test/ \
	--imgsz 1024 \
	--max-det 100 \
	--device 0 \
	--classes 0 1 2 3 4 5 6 7 8 9 \
	--save-txt --save-conf \
	--nosave \
	--augment
python convertcsv.py
cd..

# 4. ensemble and get final submission
# seunghun
python ensemble.py

