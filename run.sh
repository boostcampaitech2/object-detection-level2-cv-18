# 1.1. dataset prepare
wget https://aistages-prod-server-public.s3.amazonaws.com/app/Competitions/000076/data/data.tar.gz
tar xvfz data.tar.gz
rm ./data.tar.gz
rm -rf ./data/*/.*.jpg
mv ./data/ ./dataset
cp ./trash_coco.names ./dataset

# 1.2. libraries prepare
cd ./mmdetection
pip install -v -e .

cd ../yolov5
pip install -r requirements.txt

cd ../convert2Yolo
pip3 install -r requirements.txt

cd ..
pip install ensemble-boxes


# 2.1. Convert format (coco $\rightarrow$ yolo)
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
cd ./mmdetection
python tools/train.py \
	configs/trash/detectors_cascade_rcnn_r50.py
python tools/train.py \
	configs/trash/swin/cascade_rcnn_swin_base_fpn.py
python tools/train.py \
	configs/trash/cascade_rcnn_r50_fpn.py 
python tools/train.py \
	configs/z_config_1/base1008_2.py
cd ..


# 3.1. inference and submission for single models
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

python configs/z_config_1/base1008_2.py \
	work_dirs/base1008_2/best.pkl \
	--out work_dirs/base1008_2.py/best.pkl
python tools/pkl_to_submission.py \
	--pkl work_dirs/base1008_2/best.pkl \
	--csv work_dirs/base1008_2/submissions_best.csv
cp work_dirs/best.csv \
	../submissions_for_single_model/submissions_best.csv

# Train and Inference for single model
# sh tools/tun_detectros.sh
# cp work_dirs/detectors_cascade_rcnn_r50.csv \
#	../submissions_for_single_model/submission_detectors_cascade_rcnn_r50.csv
# sh tools/run_cascade.sh
# cp work_dirs/cascade_rcnn_r50_fpn.csv \
#	../submissions_for_single_model/submission_cascade_rcnn_r50_fpn.csv
# sh tools/run_swin.sh
# cp work_dirs/cascade_rcnn_swin_base_fpn.csv \
#	../submissions_for_single_model/submission_cascade_rcnn_r50_fpn.csv


# 4. ensemble and get final submission
python ensemble.py
