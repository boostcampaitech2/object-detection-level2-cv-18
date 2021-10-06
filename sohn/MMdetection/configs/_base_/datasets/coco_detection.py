dataset_type = 'CocoDataset'
data_root = '/opt/ml/detection/dataset/'
classes = ('General trash', 'Paper', 'Paper pack', 'Metal', 'Glass', 'Plastic', 'Styrofoam', 'Plastic bag', 'Battery', 'Clothing')

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'), # 이미지 불러오기
    dict(type='LoadAnnotations', with_bbox=True), # COCO 포맷 주석 불러오기, with_bbox=True : annotation에 box까지 가져옴
    # augmentation
    dict(type='Resize', img_scale=(1024, 1024), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32), # 이미지 패딩 처리
    dict(type='DefaultFormatBundle'),  # Default format bundle to gather data in the pipeline
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']), # 감지기에 데이터의 어느 키가 전달되는 지 결정
]
test_pipeline = [ # 어노테이션 없음
    dict(type='LoadImageFromFile'),
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
data = dict(
    samples_per_gpu=4, # gpu 당 배치 사이즈 개수
    workers_per_gpu=4, # 데이터로더에 worker 개수 선언과 동일
    train=dict(
        type=dataset_type,
        ann_file=data_root + 'train.json',
        img_prefix=data_root,
        # img_prefix=data_root + 'train2017/', # Prefix of image path
        classes = classes,
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'test.json',
        img_prefix=data_root,
        classes = classes,
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'test.json',
        # img_prefix=data_root + 'val2017/',
        img_prefix=data_root,
        classes = classes,
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='bbox')
