Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=31,
            module='odoo.tests',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=12,
            end_col_offset=56,
            name='TestWebController',
            bases=[Name(lineno=6, col_offset=24, end_lineno=6, end_col_offset=32, id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=7,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=56,
                    name='test_health',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=7, col_offset=20, end_lineno=7, end_col_offset=24, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=8,
                            col_offset=8,
                            end_lineno=8,
                            end_col_offset=47,
                            targets=[Name(lineno=8, col_offset=8, end_lineno=8, end_col_offset=16, id='response', ctx=Store())],
                            value=Call(
                                lineno=8,
                                col_offset=19,
                                end_lineno=8,
                                end_col_offset=47,
                                func=Attribute(
                                    lineno=8,
                                    col_offset=19,
                                    end_lineno=8,
                                    end_col_offset=32,
                                    value=Name(lineno=8, col_offset=19, end_lineno=8, end_col_offset=23, id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=8, col_offset=33, end_lineno=8, end_col_offset=46, value='/web/health', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=9,
                            col_offset=8,
                            end_lineno=9,
                            end_col_offset=51,
                            value=Call(
                                lineno=9,
                                col_offset=8,
                                end_lineno=9,
                                end_col_offset=51,
                                func=Attribute(
                                    lineno=9,
                                    col_offset=8,
                                    end_lineno=9,
                                    end_col_offset=24,
                                    value=Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=9,
                                        col_offset=25,
                                        end_lineno=9,
                                        end_col_offset=45,
                                        value=Name(lineno=9, col_offset=25, end_lineno=9, end_col_offset=33, id='response', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=9, col_offset=47, end_lineno=9, end_col_offset=50, value=200, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=10,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=33,
                            targets=[Name(lineno=10, col_offset=8, end_lineno=10, end_col_offset=15, id='payload', ctx=Store())],
                            value=Call(
                                lineno=10,
                                col_offset=18,
                                end_lineno=10,
                                end_col_offset=33,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=18,
                                    end_lineno=10,
                                    end_col_offset=31,
                                    value=Name(lineno=10, col_offset=18, end_lineno=10, end_col_offset=26, id='response', ctx=Load()),
                                    attr='json',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=51,
                            value=Call(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=51,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=8,
                                    end_lineno=11,
                                    end_col_offset=24,
                                    value=Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        lineno=11,
                                        col_offset=25,
                                        end_lineno=11,
                                        end_col_offset=42,
                                        value=Name(lineno=11, col_offset=25, end_lineno=11, end_col_offset=32, id='payload', ctx=Load()),
                                        slice=Constant(lineno=11, col_offset=33, end_lineno=11, end_col_offset=41, value='status', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=11, col_offset=44, end_lineno=11, end_col_offset=50, value='pass', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=56,
                            value=Call(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=56,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=24,
                                    value=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=12, col_offset=25, end_lineno=12, end_col_offset=37, value='session_id', kind=None),
                                    Attribute(
                                        lineno=12,
                                        col_offset=39,
                                        end_lineno=12,
                                        end_col_offset=55,
                                        value=Name(lineno=12, col_offset=39, end_lineno=12, end_col_offset=47, id='response', ctx=Load()),
                                        attr='cookies',
                                        ctx=Load(),
                                    ),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
