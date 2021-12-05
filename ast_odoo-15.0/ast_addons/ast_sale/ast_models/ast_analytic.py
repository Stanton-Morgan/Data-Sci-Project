Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=16,
            end_col_offset=129,
            name='AccountAnalyticLine',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=26,
                    end_lineno=7,
                    end_col_offset=38,
                    value=Name(lineno=7, col_offset=26, end_lineno=7, end_col_offset=32, id='models', ctx=Load()),
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
                    end_col_offset=38,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=38, value='account.analytic.line', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=58,
                    name='_default_sale_line_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=34, end_lineno=10, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=13,
                            end_col_offset=11,
                            value=Constant(lineno=11, col_offset=8, end_lineno=13, end_col_offset=11, value=' This is only used for delivered quantity of SO line based on analytic line, and timesheet\n            (see sale_timesheet). This can be override to allow further customization.\n        ', kind=None),
                        ),
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=58,
                            value=List(
                                lineno=14,
                                col_offset=15,
                                end_lineno=14,
                                end_col_offset=58,
                                elts=[
                                    Tuple(
                                        lineno=14,
                                        col_offset=16,
                                        end_lineno=14,
                                        end_col_offset=57,
                                        elts=[
                                            Constant(lineno=14, col_offset=17, end_lineno=14, end_col_offset=39, value='qty_delivered_method', kind=None),
                                            Constant(lineno=14, col_offset=41, end_lineno=14, end_col_offset=44, value='=', kind=None),
                                            Constant(lineno=14, col_offset=46, end_lineno=14, end_col_offset=56, value='analytic', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=129,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=11, id='so_line', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=14,
                        end_lineno=16,
                        end_col_offset=129,
                        func=Attribute(
                            lineno=16,
                            col_offset=14,
                            end_lineno=16,
                            end_col_offset=29,
                            value=Name(lineno=16, col_offset=14, end_lineno=16, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=16, col_offset=30, end_lineno=16, end_col_offset=47, value='sale.order.line', kind=None)],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=49,
                                end_lineno=16,
                                end_col_offset=74,
                                arg='string',
                                value=Constant(lineno=16, col_offset=56, end_lineno=16, end_col_offset=74, value='Sales Order Item', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=76,
                                end_lineno=16,
                                end_col_offset=128,
                                arg='domain',
                                value=Lambda(
                                    lineno=16,
                                    col_offset=83,
                                    end_lineno=16,
                                    end_col_offset=128,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=16, col_offset=90, end_lineno=16, end_col_offset=94, arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        lineno=16,
                                        col_offset=96,
                                        end_lineno=16,
                                        end_col_offset=128,
                                        func=Attribute(
                                            lineno=16,
                                            col_offset=96,
                                            end_lineno=16,
                                            end_col_offset=126,
                                            value=Name(lineno=16, col_offset=96, end_lineno=16, end_col_offset=100, id='self', ctx=Load()),
                                            attr='_default_sale_line_domain',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)