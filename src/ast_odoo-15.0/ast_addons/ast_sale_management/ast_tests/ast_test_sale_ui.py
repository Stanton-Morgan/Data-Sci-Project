Module(
    body=[
        Import(
            lineno=1,
            col_offset=0,
            end_lineno=1,
            end_col_offset=17,
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=9,
            end_col_offset=75,
            name='TestUi',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=13,
                    end_lineno=6,
                    end_col_offset=32,
                    value=Attribute(
                        lineno=6,
                        col_offset=13,
                        end_lineno=6,
                        end_col_offset=23,
                        value=Name(lineno=6, col_offset=13, end_lineno=6, end_col_offset=17, id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=8,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=75,
                    name='test_01_sale_tour',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=8, col_offset=26, end_lineno=8, end_col_offset=30, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=9,
                            col_offset=8,
                            end_lineno=9,
                            end_col_offset=75,
                            value=Call(
                                lineno=9,
                                col_offset=8,
                                end_lineno=9,
                                end_col_offset=75,
                                func=Attribute(
                                    lineno=9,
                                    col_offset=8,
                                    end_lineno=9,
                                    end_col_offset=23,
                                    value=Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=9, col_offset=24, end_lineno=9, end_col_offset=30, value='/web', kind=None),
                                    Constant(lineno=9, col_offset=32, end_lineno=9, end_col_offset=43, value='sale_tour', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=9,
                                        col_offset=45,
                                        end_lineno=9,
                                        end_col_offset=58,
                                        arg='login',
                                        value=Constant(lineno=9, col_offset=51, end_lineno=9, end_col_offset=58, value='admin', kind=None),
                                    ),
                                    keyword(
                                        lineno=9,
                                        col_offset=60,
                                        end_lineno=9,
                                        end_col_offset=74,
                                        arg='step_delay',
                                        value=Constant(lineno=9, col_offset=71, end_lineno=9, end_col_offset=74, value=100, kind=None),
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
            decorator_list=[
                Call(
                    lineno=5,
                    col_offset=1,
                    end_lineno=5,
                    end_col_offset=49,
                    func=Attribute(
                        lineno=5,
                        col_offset=1,
                        end_lineno=5,
                        end_col_offset=18,
                        value=Attribute(
                            lineno=5,
                            col_offset=1,
                            end_lineno=5,
                            end_col_offset=11,
                            value=Name(lineno=5, col_offset=1, end_lineno=5, end_col_offset=5, id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(lineno=5, col_offset=19, end_lineno=5, end_col_offset=33, value='post_install', kind=None),
                        Constant(lineno=5, col_offset=35, end_lineno=5, end_col_offset=48, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)