Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=20,
            end_col_offset=91,
            name='SaleOrderCancel',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=22,
                    end_lineno=7,
                    end_col_offset=43,
                    value=Name(lineno=7, col_offset=22, end_lineno=7, end_col_offset=28, id='models', ctx=Load()),
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
                    end_col_offset=31,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=31, value='sale.order.cancel', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=39,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=39, value='Sales Order Cancel', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=100,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=12, id='order_id', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=15,
                        end_lineno=11,
                        end_col_offset=100,
                        func=Attribute(
                            lineno=11,
                            col_offset=15,
                            end_lineno=11,
                            end_col_offset=30,
                            value=Name(lineno=11, col_offset=15, end_lineno=11, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=31, end_lineno=11, end_col_offset=43, value='sale.order', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=45,
                                end_lineno=11,
                                end_col_offset=64,
                                arg='string',
                                value=Constant(lineno=11, col_offset=52, end_lineno=11, end_col_offset=64, value='Sale Order', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=66,
                                end_lineno=11,
                                end_col_offset=79,
                                arg='required',
                                value=Constant(lineno=11, col_offset=75, end_lineno=11, end_col_offset=79, value=True, kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=81,
                                end_lineno=11,
                                end_col_offset=99,
                                arg='ondelete',
                                value=Constant(lineno=11, col_offset=90, end_lineno=11, end_col_offset=99, value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=101,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=25, id='display_invoice_alert', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=28,
                        end_lineno=12,
                        end_col_offset=101,
                        func=Attribute(
                            lineno=12,
                            col_offset=28,
                            end_lineno=12,
                            end_col_offset=42,
                            value=Name(lineno=12, col_offset=28, end_lineno=12, end_col_offset=34, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=43, end_lineno=12, end_col_offset=58, value='Invoice Alert', kind=None)],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=60,
                                end_lineno=12,
                                end_col_offset=100,
                                arg='compute',
                                value=Constant(lineno=12, col_offset=68, end_lineno=12, end_col_offset=100, value='_compute_display_invoice_alert', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=119,
                    name='_compute_display_invoice_alert',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=15, col_offset=39, end_lineno=15, end_col_offset=43, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            lineno=16,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=119,
                            target=Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=18, id='wizard', ctx=Store()),
                            iter=Name(lineno=16, col_offset=22, end_lineno=16, end_col_offset=26, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=119,
                                    targets=[
                                        Attribute(
                                            lineno=17,
                                            col_offset=12,
                                            end_lineno=17,
                                            end_col_offset=40,
                                            value=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, id='wizard', ctx=Load()),
                                            attr='display_invoice_alert',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=17,
                                        col_offset=43,
                                        end_lineno=17,
                                        end_col_offset=119,
                                        func=Name(lineno=17, col_offset=43, end_lineno=17, end_col_offset=47, id='bool', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=17,
                                                col_offset=48,
                                                end_lineno=17,
                                                end_col_offset=118,
                                                func=Attribute(
                                                    lineno=17,
                                                    col_offset=48,
                                                    end_lineno=17,
                                                    end_col_offset=84,
                                                    value=Attribute(
                                                        lineno=17,
                                                        col_offset=48,
                                                        end_lineno=17,
                                                        end_col_offset=75,
                                                        value=Attribute(
                                                            lineno=17,
                                                            col_offset=48,
                                                            end_lineno=17,
                                                            end_col_offset=63,
                                                            value=Name(lineno=17, col_offset=48, end_lineno=17, end_col_offset=54, id='wizard', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='invoice_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        lineno=17,
                                                        col_offset=85,
                                                        end_lineno=17,
                                                        end_col_offset=117,
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(lineno=17, col_offset=92, end_lineno=17, end_col_offset=95, arg='inv', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            lineno=17,
                                                            col_offset=97,
                                                            end_lineno=17,
                                                            end_col_offset=117,
                                                            left=Attribute(
                                                                lineno=17,
                                                                col_offset=97,
                                                                end_lineno=17,
                                                                end_col_offset=106,
                                                                value=Name(lineno=17, col_offset=97, end_lineno=17, end_col_offset=100, id='inv', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(lineno=17, col_offset=110, end_lineno=17, end_col_offset=117, value='draft', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=14,
                            col_offset=5,
                            end_lineno=14,
                            end_col_offset=28,
                            func=Attribute(
                                lineno=14,
                                col_offset=5,
                                end_lineno=14,
                                end_col_offset=16,
                                value=Name(lineno=14, col_offset=5, end_lineno=14, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=14, col_offset=17, end_lineno=14, end_col_offset=27, value='order_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=19,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=91,
                    name='action_cancel',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=19, col_offset=22, end_lineno=19, end_col_offset=26, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=91,
                            value=Call(
                                lineno=20,
                                col_offset=15,
                                end_lineno=20,
                                end_col_offset=91,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=15,
                                    end_lineno=20,
                                    end_col_offset=89,
                                    value=Call(
                                        lineno=20,
                                        col_offset=15,
                                        end_lineno=20,
                                        end_col_offset=75,
                                        func=Attribute(
                                            lineno=20,
                                            col_offset=15,
                                            end_lineno=20,
                                            end_col_offset=41,
                                            value=Attribute(
                                                lineno=20,
                                                col_offset=15,
                                                end_lineno=20,
                                                end_col_offset=28,
                                                value=Name(lineno=20, col_offset=15, end_lineno=20, end_col_offset=19, id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=20,
                                                col_offset=42,
                                                end_lineno=20,
                                                end_col_offset=74,
                                                keys=[Constant(lineno=20, col_offset=43, end_lineno=20, end_col_offset=67, value='disable_cancel_warning', kind=None)],
                                                values=[Constant(lineno=20, col_offset=69, end_lineno=20, end_col_offset=73, value=True, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='action_cancel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
