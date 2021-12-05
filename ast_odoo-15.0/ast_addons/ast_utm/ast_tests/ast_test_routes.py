Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=17,
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=14,
            end_col_offset=46,
            name='TestRoutes',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=17,
                    end_lineno=8,
                    end_col_offset=36,
                    value=Attribute(
                        lineno=8,
                        col_offset=17,
                        end_lineno=8,
                        end_col_offset=27,
                        value=Name(lineno=8, col_offset=17, end_lineno=8, end_col_offset=21, id='odoo', ctx=Load()),
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
                    lineno=10,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=46,
                    name='test_01_web_session_destroy',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=36, end_lineno=10, end_col_offset=40, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=83,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=16, id='base_url', ctx=Store())],
                            value=Call(
                                lineno=11,
                                col_offset=19,
                                end_lineno=11,
                                end_col_offset=83,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=19,
                                    end_lineno=11,
                                    end_col_offset=67,
                                    value=Call(
                                        lineno=11,
                                        col_offset=19,
                                        end_lineno=11,
                                        end_col_offset=57,
                                        func=Attribute(
                                            lineno=11,
                                            col_offset=19,
                                            end_lineno=11,
                                            end_col_offset=55,
                                            value=Subscript(
                                                lineno=11,
                                                col_offset=19,
                                                end_lineno=11,
                                                end_col_offset=50,
                                                value=Attribute(
                                                    lineno=11,
                                                    col_offset=19,
                                                    end_lineno=11,
                                                    end_col_offset=27,
                                                    value=Name(lineno=11, col_offset=19, end_lineno=11, end_col_offset=23, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=11, col_offset=28, end_lineno=11, end_col_offset=49, value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=11, col_offset=68, end_lineno=11, end_col_offset=82, value='web.base.url', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=41,
                            value=Call(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=41,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=25,
                                    value=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=12, id='self', ctx=Load()),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=12, col_offset=26, end_lineno=12, end_col_offset=32, value='demo', kind=None),
                                    Constant(lineno=12, col_offset=34, end_lineno=12, end_col_offset=40, value='demo', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=78,
                            targets=[Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=13,
                                col_offset=14,
                                end_lineno=13,
                                end_col_offset=78,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=14,
                                    end_lineno=13,
                                    end_col_offset=30,
                                    value=Attribute(
                                        lineno=13,
                                        col_offset=14,
                                        end_lineno=13,
                                        end_col_offset=25,
                                        value=Name(lineno=13, col_offset=14, end_lineno=13, end_col_offset=18, id='self', ctx=Load()),
                                        attr='opener',
                                        ctx=Load(),
                                    ),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=13,
                                        col_offset=31,
                                        end_lineno=13,
                                        end_col_offset=68,
                                        arg='url',
                                        value=BinOp(
                                            lineno=13,
                                            col_offset=35,
                                            end_lineno=13,
                                            end_col_offset=68,
                                            left=Name(lineno=13, col_offset=35, end_lineno=13, end_col_offset=43, id='base_url', ctx=Load()),
                                            op=Add(),
                                            right=Constant(lineno=13, col_offset=46, end_lineno=13, end_col_offset=68, value='/web/session/destroy', kind=None),
                                        ),
                                    ),
                                    keyword(
                                        lineno=13,
                                        col_offset=70,
                                        end_lineno=13,
                                        end_col_offset=77,
                                        arg='json',
                                        value=Dict(lineno=13, col_offset=75, end_lineno=13, end_col_offset=77, keys=[], values=[]),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=46,
                            value=Call(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=46,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=24,
                                    value=Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=14,
                                        col_offset=25,
                                        end_lineno=14,
                                        end_col_offset=40,
                                        value=Name(lineno=14, col_offset=25, end_lineno=14, end_col_offset=28, id='res', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=14, col_offset=42, end_lineno=14, end_col_offset=45, value=200, kind=None),
                                ],
                                keywords=[],
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
                    lineno=7,
                    col_offset=1,
                    end_lineno=7,
                    end_col_offset=49,
                    func=Attribute(
                        lineno=7,
                        col_offset=1,
                        end_lineno=7,
                        end_col_offset=18,
                        value=Attribute(
                            lineno=7,
                            col_offset=1,
                            end_lineno=7,
                            end_col_offset=11,
                            value=Name(lineno=7, col_offset=1, end_lineno=7, end_col_offset=5, id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(lineno=7, col_offset=19, end_lineno=7, end_col_offset=33, value='post_install', kind=None),
                        Constant(lineno=7, col_offset=35, end_lineno=7, end_col_offset=48, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
