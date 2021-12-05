Module(
    body=[
        Import(
            lineno=1,
            col_offset=0,
            end_lineno=1,
            end_col_offset=17,
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=34,
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=10,
            end_col_offset=65,
            name='TestWebsiteError',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=23,
                    end_lineno=6,
                    end_col_offset=42,
                    value=Attribute(
                        lineno=6,
                        col_offset=23,
                        end_lineno=6,
                        end_col_offset=33,
                        value=Name(lineno=6, col_offset=23, end_lineno=6, end_col_offset=27, id='odoo', ctx=Load()),
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
                    lineno=9,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=65,
                    name='test_01_run_test',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=25, end_lineno=9, end_col_offset=29, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=10,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=65,
                            value=Call(
                                lineno=10,
                                col_offset=8,
                                end_lineno=10,
                                end_col_offset=65,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=8,
                                    end_lineno=10,
                                    end_col_offset=23,
                                    value=Name(lineno=10, col_offset=8, end_lineno=10, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=10, col_offset=24, end_lineno=10, end_col_offset=42, value='/test_error_view', kind=None),
                                    Constant(lineno=10, col_offset=44, end_lineno=10, end_col_offset=64, value='test_error_website', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=8,
                            col_offset=5,
                            end_lineno=8,
                            end_col_offset=72,
                            func=Name(lineno=8, col_offset=5, end_lineno=8, end_col_offset=16, id='mute_logger', ctx=Load()),
                            args=[
                                Constant(lineno=8, col_offset=17, end_lineno=8, end_col_offset=58, value='odoo.addons.http_routing.models.ir_http', kind=None),
                                Constant(lineno=8, col_offset=60, end_lineno=8, end_col_offset=71, value='odoo.http', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    lineno=5,
                    col_offset=1,
                    end_lineno=5,
                    end_col_offset=56,
                    func=Attribute(
                        lineno=5,
                        col_offset=1,
                        end_lineno=5,
                        end_col_offset=25,
                        value=Attribute(
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
                            attr='common',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(lineno=5, col_offset=26, end_lineno=5, end_col_offset=40, value='post_install', kind=None),
                        Constant(lineno=5, col_offset=42, end_lineno=5, end_col_offset=55, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
