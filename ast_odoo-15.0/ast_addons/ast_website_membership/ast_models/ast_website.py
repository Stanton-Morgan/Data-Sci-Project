Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=26,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=59,
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='url_for', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=14,
            end_col_offset=36,
            name='Website',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=14,
                    end_lineno=8,
                    end_col_offset=26,
                    value=Name(lineno=8, col_offset=14, end_lineno=8, end_col_offset=20, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=24,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=24, value='website', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=36,
                    name='get_suggested_controllers',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=34, end_lineno=11, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=80,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=29, id='suggested_controllers', ctx=Store())],
                            value=Call(
                                lineno=12,
                                col_offset=32,
                                end_lineno=12,
                                end_col_offset=80,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=32,
                                    end_lineno=12,
                                    end_col_offset=78,
                                    value=Call(
                                        lineno=12,
                                        col_offset=32,
                                        end_lineno=12,
                                        end_col_offset=52,
                                        func=Name(lineno=12, col_offset=32, end_lineno=12, end_col_offset=37, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=12, col_offset=38, end_lineno=12, end_col_offset=45, id='Website', ctx=Load()),
                                            Name(lineno=12, col_offset=47, end_lineno=12, end_col_offset=51, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_suggested_controllers',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=95,
                            value=Call(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=95,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=8,
                                    end_lineno=13,
                                    end_col_offset=36,
                                    value=Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=29, id='suggested_controllers', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        lineno=13,
                                        col_offset=37,
                                        end_lineno=13,
                                        end_col_offset=94,
                                        elts=[
                                            Call(
                                                lineno=13,
                                                col_offset=38,
                                                end_lineno=13,
                                                end_col_offset=50,
                                                func=Name(lineno=13, col_offset=38, end_lineno=13, end_col_offset=39, id='_', ctx=Load()),
                                                args=[Constant(lineno=13, col_offset=40, end_lineno=13, end_col_offset=49, value='Members', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                lineno=13,
                                                col_offset=52,
                                                end_lineno=13,
                                                end_col_offset=71,
                                                func=Name(lineno=13, col_offset=52, end_lineno=13, end_col_offset=59, id='url_for', ctx=Load()),
                                                args=[Constant(lineno=13, col_offset=60, end_lineno=13, end_col_offset=70, value='/members', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(lineno=13, col_offset=73, end_lineno=13, end_col_offset=93, value='website_membership', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=36,
                            value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=36, id='suggested_controllers', ctx=Load()),
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
