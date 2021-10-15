# dataset settings
dataset_type = 'CocoDataset'
data_root = '../dataset/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)

albu_train_transforms = [
	dict(type='RandomRotate90'),
	dict(type='GaussNoise', p=0.5),
	dict(
			type='OneOf',
			transforms=[
				dict(type='Blur'),
				dict(type='MedianBlur'),
			],
			p=0.5,
		),
	dict(
			type='OneOf',
			transforms=[
				dict(type='RandomBrightnessContrast'),
				dict(type='CLAHE'),
				dict(type='RandomGamma'),
			],
			p=0.5,
		),
	dict(
			type='OneOf',
			transforms=[
				dict(type='HueSaturationValue'),
				dict(type='RGBShift'),
			],
			p=0.5,
		)
]

img_scale = (1024, 1024)

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=img_scale, keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
	dict(
		type='Albu',
		transforms=albu_train_transforms,
		bbox_params=dict(
			type='BboxParams',
			format='pascal_voc',
			label_fields=['gt_labels'],
			min_visibility=0.0,
			filter_lost_elements=True
			),
		keymap={'img': 'image', 'gt_bboxes': 'bboxes'},
		update_pad_shape=False,
		skip_img_without_anno=True
	),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=img_scale,
        flip=True,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]

classes = ("General trash", "Paper", "Paper pack", "Metal", "Glass",
		"Plastic", "Styrofoam", "Plastic bag", "Battery", "Clothing")

data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
		classes=classes,
        ann_file=data_root + 'train.json',
        img_prefix=data_root,
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
		classes=classes,
        ann_file=data_root + 'train.json',
        img_prefix=data_root,
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
		classes=classes,
        ann_file=data_root + 'test.json',
        img_prefix=data_root,
        pipeline=test_pipeline))

# evaluation = dict(interval=1, metric='bbox')
evaluation = dict(
		    interval=1,
			save_best='bbox_mAP_50',
			metric='bbox'
			)
