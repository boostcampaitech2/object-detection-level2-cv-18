_base_ = [
    'M_cascade_rcnn_r50_fpn_1.py',
    'dataset.py',
    'schedule.py',
	'../_base_/default_runtime.py'
]


data = dict(samples_per_gpu=4)
checkpoint_config = dict(max_keep_ckpts=3, interval=1)
