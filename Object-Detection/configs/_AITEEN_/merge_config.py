_base_ = [
    'cascade_mask_rcnn_swin_base_patch4_window7_mstrain_480-800_giou_4conv1f_adamw_3x_coco.py',
    'dataset.py',
    'schedules/schedule_1x.py',
    'default_runtime.py'
]

# python tools/train.py configs/_AITEEN_/merge_config.py