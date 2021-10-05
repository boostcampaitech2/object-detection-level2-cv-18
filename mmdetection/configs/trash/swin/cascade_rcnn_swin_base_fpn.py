_base_ = [
    '../M_cascade_rcnn_r50_fpn.py',
	'../dataset.py',
    'swin_schedule_warm_restarts.py',
    '../../_base_/default_runtime.py'
]

pretrained = 'https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_base_patch4_window7_224_22k.pth'
model = dict(
	backbone=dict(
		_delete_=True,
        type='SwinTransformer',
        embed_dims=128,
        depths=[2, 2, 18, 2],
        num_heads=[4, 8, 16, 32],
        window_size=7,
        mlp_ratio=4,
        qkv_bias=True,
        qk_scale=None,
        drop_rate=0.,
        attn_drop_rate=0.,
        drop_path_rate=0.2,
        patch_norm=True,
        out_indices=(0, 1, 2, 3),
        with_cp=False,
        convert_weights=True,
        init_cfg=dict(type='Pretrained', checkpoint=pretrained)),
   neck=dict(in_channels=[128, 256, 512, 1024]))

data = dict(samples_per_gpu=4)

log_config = dict(
    hooks=[
        dict(
            type='WandbLoggerHook',
            init_kwargs=dict(
                project='Pstage3_detection',
                name='cascade_rcnn_swin_base_fpn_soft_nms_warmrestarts_adamw_folcal_DIoU')
        )
    ])

