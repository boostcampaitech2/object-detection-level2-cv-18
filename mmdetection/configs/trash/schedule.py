optimizer = dict(type='SGD', lr=1e-3, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

lr_config = dict(
		policy='CosineAnnealing',
		warmup='linear',
		warmup_iters=1000,
		warmup_ratio=1.0 / 10,
		min_lr=5e-6
)

runner = dict(type='EpochBasedRunner', max_epochs=36)
