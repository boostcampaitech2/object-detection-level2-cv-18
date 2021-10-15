optimizer = dict(type='AdamW', lr=1e-5, betas=(0.9, 0.999), weight_decay=0.05)
                 # paramwise_cfg=dict(custom_keys={'absolute_pos_embed': dict(decay_mult=0.),
                 #                                 'relative_position_bias_table': dict(decay_mult=0.),
                 #                                 'norm': dict(decay_mult=0.)}))
            
optimizer_config = dict(grad_clip=None)

lr_config = dict(
    policy='CosineAnnealing',
    warmup='linear',
    warmup_iters=1000,
    warmup_ratio=1.0/10,
    min_lr_ratio=5e-6
)

runner = dict(type='EpochBasedRunner', max_epochs=36)
