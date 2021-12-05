Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=23,
            end_col_offset=12,
            name='ChannelPartner',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=21,
                    end_lineno=7,
                    end_col_offset=33,
                    value=Name(lineno=7, col_offset=21, end_lineno=7, end_col_offset=27, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=37,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=37, value='mail.channel.partner', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=12,
                    name='_gc_unpin_livechat_sessions',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=36, end_lineno=11, end_col_offset=40, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=46,
                            value=Constant(lineno=12, col_offset=8, end_lineno=13, end_col_offset=46, value=" Unpin livechat sessions with no activity for at least one day to\n            clean the operator's interface ", kind=None),
                        ),
                        Expr(
                            lineno=14,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=12,
                            value=Call(
                                lineno=14,
                                col_offset=8,
                                end_lineno=23,
                                end_col_offset=12,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=27,
                                    value=Attribute(
                                        lineno=14,
                                        col_offset=8,
                                        end_lineno=14,
                                        end_col_offset=19,
                                        value=Attribute(
                                            lineno=14,
                                            col_offset=8,
                                            end_lineno=14,
                                            end_col_offset=16,
                                            value=Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=14, col_offset=28, end_lineno=23, end_col_offset=11, value="\n            UPDATE mail_channel_partner\n            SET is_pinned = false\n            WHERE id in (\n                SELECT cp.id FROM mail_channel_partner cp\n                INNER JOIN mail_channel c on c.id = cp.channel_id\n                WHERE c.channel_type = 'livechat' AND cp.is_pinned is true AND\n                    cp.write_date < current_timestamp - interval '1 day'\n            )\n        ", kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=10,
                            col_offset=5,
                            end_lineno=10,
                            end_col_offset=19,
                            value=Name(lineno=10, col_offset=5, end_lineno=10, end_col_offset=8, id='api', ctx=Load()),
                            attr='autovacuum',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)