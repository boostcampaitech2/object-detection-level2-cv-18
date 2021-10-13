_base_ = [
    'M_cascade_rcnn_r50_fpn.py',
    'dataset.py',
    '../_base_/schedules/schedule_1x.py',
	'../_base_/default_runtime.py'
]


data = dict(samples_per_gpu=4)

optimizer = dict(lr=0.001)

lr_config = dict(
    policy='CosineAnnealing',
    warmup='linear',
    warmup_iters=1000,
    warmup_ratio=1.0/10,
    min_lr_ratio=4e-6
)

runner = dict(max_epochs=36)
