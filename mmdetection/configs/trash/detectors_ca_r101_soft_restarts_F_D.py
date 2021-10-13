_base_ = [
    'M_cascade_rcnn_r101_fpn.py',
    'dataset.py',
	'swin/swin_schedule_warm_restarts.py',
	'../_base_/default_runtime.py'
]

model = dict(
    backbone=dict(
        type='DetectoRS_ResNet',
        conv_cfg=dict(type='ConvAWS'),
        sac=dict(type='SAC', use_deform=True),
        stage_with_sac=(False, True, True, True),
        output_img=True),
    neck=dict(
        type='RFP',
        rfp_steps=2,
        aspp_out_channels=64,
        aspp_dilations=(1, 3, 6, 1),
        rfp_backbone=dict(
            rfp_inplanes=256,
            type='DetectoRS_ResNet',
            depth=101,
            num_stages=4,
            out_indices=(0, 1, 2, 3),
            frozen_stages=1,
            norm_cfg=dict(type='BN', requires_grad=True),
            norm_eval=True,
            conv_cfg=dict(type='ConvAWS'),
            sac=dict(type='SAC', use_deform=True),
            stage_with_sac=(False, True, True, True),
            pretrained='torchvision://resnet101',
            style='pytorch'
			)))

data = dict(samples_per_gpu=4)
runner = dict(max_epochs=48)

log_config = dict(
    hooks=[
        dict(
            type='WandbLoggerHook',
            init_kwargs=dict(
                project='Pstage3_detection',
                name='detectoRS_ca_r101_anchor_soft_warmstarts_adamW_F_D')
        )
    ])

checkpoint_config = dict(max_keep_ckpts=3, interval=1)

