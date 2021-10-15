# Train에 영향을 미치지 않기에 default를 가져온다.
checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(
            type='WandbLoggerHook',
            init_kwargs=dict(
            project='Han_T2260',
            name='Cascade_rcnn_r50_fpn')),
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]
# evaluation = [dict(interval=1, metric='bbox_mAP_50')]
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]

# checkpoint_config = dict(interval=1)
# # yapf:disable
# log_config = dict(
#     interval=200,
#     hooks=[
#         dict(type='TextLoggerHook'),
#         dict(type='WandbLoggerHook', interval=1000,
#             init_kwarges=dict(
#                 project = 'Han_T2260',
#                 entity = 'ai_tech_level2-cv-18',
#                 name = 'c'
#             ))
            
#     ])
# # yapf:enable
# custom_hooks = [dict(type='NumClassCheckHook')]

# dist_params = dict(backend='nccl')
# log_level = 'INFO'
# load_from = None
# resume_from = None
# workflow = [('train', 1)]
