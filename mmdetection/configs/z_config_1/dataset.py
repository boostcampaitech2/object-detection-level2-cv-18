# dataset settings
dataset_type = 'CocoDataset'
data_root = '/opt/ml/object-detection-level2-cv-18/dataset' #해당 데이터가 어디에 있는지
classes = (
    'General trash', 'Paper', 'Paper pack', 'Metal', 'Glass', 'Plastic', 'Styrofoam',
    'Plastic bag', 'Battery', 'Clothing'
    )

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'), # 이미지를 파일로 부터 불러온다.
    dict(type='LoadAnnotations', with_bbox=True), # Annotation을 들고오겠다. + bbox까지 가져오겠다(True)
    # 여기서 부터 Augmentation
    dict(type='Resize', img_scale=(1024, 1024), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'), # 테스트 파일은 Annotation을 하지 않는다.
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1024, 1024),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]

data = dict( #실제 config가 작성되는 부분)
    samples_per_gpu=4, #gpu당 batchsize 설정
    workers_per_gpu=2, #dataloader만들 떄 worker개수 선언하는 것과 동일
    train=dict( #Traindata가 어떤 pipeline을 걸칠지
        type=dataset_type,
        ann_file=data_root + '/train.json',
        img_prefix=data_root,
        classes = classes,
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + '/train.json',
        img_prefix=data_root,
        classes = classes,
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + '/test.json',
        img_prefix=data_root,
        classes = classes,
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='bbox')