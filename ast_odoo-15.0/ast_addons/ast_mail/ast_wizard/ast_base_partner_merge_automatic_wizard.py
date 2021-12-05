Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=12,
            end_col_offset=178,
            name='MergePartnerAutomatic',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=28,
                    end_lineno=6,
                    end_col_offset=49,
                    value=Name(lineno=6, col_offset=28, end_lineno=6, end_col_offset=34, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=52,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=52, value='base.partner.merge.automatic.wizard', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=178,
                    name='_log_merge_operation',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=10, col_offset=29, end_lineno=10, end_col_offset=33, arg='self', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=35, end_lineno=10, end_col_offset=47, arg='src_partners', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=49, end_lineno=10, end_col_offset=60, arg='dst_partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=90,
                            value=Call(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=90,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=8,
                                    end_lineno=11,
                                    end_col_offset=63,
                                    value=Call(
                                        lineno=11,
                                        col_offset=8,
                                        end_lineno=11,
                                        end_col_offset=42,
                                        func=Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=13, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=11, col_offset=14, end_lineno=11, end_col_offset=35, id='MergePartnerAutomatic', ctx=Load()),
                                            Name(lineno=11, col_offset=37, end_lineno=11, end_col_offset=41, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_log_merge_operation',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=11, col_offset=64, end_lineno=11, end_col_offset=76, id='src_partners', ctx=Load()),
                                    Name(lineno=11, col_offset=78, end_lineno=11, end_col_offset=89, id='dst_partner', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=178,
                            value=Call(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=178,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=32,
                                    value=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=19, id='dst_partner', ctx=Load()),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=12,
                                        col_offset=33,
                                        end_lineno=12,
                                        end_col_offset=177,
                                        arg='body',
                                        value=BinOp(
                                            lineno=12,
                                            col_offset=38,
                                            end_lineno=12,
                                            end_col_offset=177,
                                            left=Constant(lineno=12, col_offset=38, end_lineno=12, end_col_offset=45, value='%s %s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                lineno=12,
                                                col_offset=48,
                                                end_lineno=12,
                                                end_col_offset=177,
                                                elts=[
                                                    Call(
                                                        lineno=12,
                                                        col_offset=49,
                                                        end_lineno=12,
                                                        end_col_offset=89,
                                                        func=Name(lineno=12, col_offset=49, end_lineno=12, end_col_offset=50, id='_', ctx=Load()),
                                                        args=[Constant(lineno=12, col_offset=51, end_lineno=12, end_col_offset=88, value='Merged with the following partners:', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        lineno=12,
                                                        col_offset=91,
                                                        end_lineno=12,
                                                        end_col_offset=176,
                                                        func=Attribute(
                                                            lineno=12,
                                                            col_offset=91,
                                                            end_lineno=12,
                                                            end_col_offset=100,
                                                            value=Constant(lineno=12, col_offset=91, end_lineno=12, end_col_offset=95, value=', ', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            GeneratorExp(
                                                                lineno=12,
                                                                col_offset=100,
                                                                end_lineno=12,
                                                                end_col_offset=176,
                                                                elt=BinOp(
                                                                    lineno=12,
                                                                    col_offset=101,
                                                                    end_lineno=12,
                                                                    end_col_offset=153,
                                                                    left=Constant(lineno=12, col_offset=101, end_lineno=12, end_col_offset=118, value='%s <%s> (ID %s)', kind=None),
                                                                    op=Mod(),
                                                                    right=Tuple(
                                                                        lineno=12,
                                                                        col_offset=121,
                                                                        end_lineno=12,
                                                                        end_col_offset=153,
                                                                        elts=[
                                                                            Attribute(
                                                                                lineno=12,
                                                                                col_offset=122,
                                                                                end_lineno=12,
                                                                                end_col_offset=128,
                                                                                value=Name(lineno=12, col_offset=122, end_lineno=12, end_col_offset=123, id='p', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            BoolOp(
                                                                                lineno=12,
                                                                                col_offset=130,
                                                                                end_lineno=12,
                                                                                end_col_offset=146,
                                                                                op=Or(),
                                                                                values=[
                                                                                    Attribute(
                                                                                        lineno=12,
                                                                                        col_offset=130,
                                                                                        end_lineno=12,
                                                                                        end_col_offset=137,
                                                                                        value=Name(lineno=12, col_offset=130, end_lineno=12, end_col_offset=131, id='p', ctx=Load()),
                                                                                        attr='email',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(lineno=12, col_offset=141, end_lineno=12, end_col_offset=146, value='n/a', kind=None),
                                                                                ],
                                                                            ),
                                                                            Attribute(
                                                                                lineno=12,
                                                                                col_offset=148,
                                                                                end_lineno=12,
                                                                                end_col_offset=152,
                                                                                value=Name(lineno=12, col_offset=148, end_lineno=12, end_col_offset=149, id='p', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(lineno=12, col_offset=158, end_lineno=12, end_col_offset=159, id='p', ctx=Store()),
                                                                        iter=Name(lineno=12, col_offset=163, end_lineno=12, end_col_offset=175, id='src_partners', ctx=Load()),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
