# optimizer
# optimizer = dict(type='SGD', lr=2e-3, momentum=0.9, weight_decay=0.0001)
# optimizer_config = dict(grad_clip=None)
# # learning policy
# lr_config = dict(
#     policy='step',
#     warmup='linear',
#     warmup_iters=500,
#     warmup_ratio=0.001,
#     step=[16, 22])
# runner = dict(type='EpochBasedRunner', max_epochs=30)

# CosineAnnealing
optimizer = dict(type='AdamW', lr=5e-5, weight_decay=0.01)
optimizer_config = dict(grad_clip=None)

lr_config = dict(
    policy='CosineAnnealing',
    warmup='linear',
    warmup_iters=1000,
    warmup_ratio=1.0 / 10,
    min_lr=4e-6 # min learning rate
)
runner = dict(type='EpochBasedRunner', max_epochs=20)
