Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=46,
            module='odoo.tests.common',
            names=[
                alias(name='HttpCase', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=16,
            end_col_offset=56,
            name='TestMultiCompany',
            bases=[Name(lineno=8, col_offset=23, end_lineno=8, end_col_offset=31, id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=56,
                    name='test_company_in_context',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=32, end_lineno=10, end_col_offset=36, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=54,
                            value=Constant(lineno=11, col_offset=8, end_lineno=11, end_col_offset=54, value=' Test website company is set in context ', kind=None),
                        ),
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=57,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=15, id='website', ctx=Store())],
                            value=Call(
                                lineno=12,
                                col_offset=18,
                                end_lineno=12,
                                end_col_offset=57,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=18,
                                    end_lineno=12,
                                    end_col_offset=30,
                                    value=Attribute(
                                        lineno=12,
                                        col_offset=18,
                                        end_lineno=12,
                                        end_col_offset=26,
                                        value=Name(lineno=12, col_offset=18, end_lineno=12, end_col_offset=22, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=12, col_offset=31, end_lineno=12, end_col_offset=56, value='website.default_website', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=66,
                            targets=[Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=15, id='company', ctx=Store())],
                            value=Call(
                                lineno=13,
                                col_offset=18,
                                end_lineno=13,
                                end_col_offset=66,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=18,
                                    end_lineno=13,
                                    end_col_offset=48,
                                    value=Subscript(
                                        lineno=13,
                                        col_offset=18,
                                        end_lineno=13,
                                        end_col_offset=41,
                                        value=Attribute(
                                            lineno=13,
                                            col_offset=18,
                                            end_lineno=13,
                                            end_col_offset=26,
                                            value=Name(lineno=13, col_offset=18, end_lineno=13, end_col_offset=22, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=13, col_offset=27, end_lineno=13, end_col_offset=40, value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=13,
                                        col_offset=49,
                                        end_lineno=13,
                                        end_col_offset=65,
                                        keys=[Constant(lineno=13, col_offset=50, end_lineno=13, end_col_offset=56, value='name', kind=None)],
                                        values=[Constant(lineno=13, col_offset=58, end_lineno=13, end_col_offset=64, value='Adaa', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=36,
                            targets=[
                                Attribute(
                                    lineno=14,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=26,
                                    value=Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=15, id='website', ctx=Load()),
                                    attr='company_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(lineno=14, col_offset=29, end_lineno=14, end_col_offset=36, id='company', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=58,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=16, id='response', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=19,
                                end_lineno=15,
                                end_col_offset=58,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=19,
                                    end_lineno=15,
                                    end_col_offset=32,
                                    value=Name(lineno=15, col_offset=19, end_lineno=15, end_col_offset=23, id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=15, col_offset=33, end_lineno=15, end_col_offset=57, value='/multi_company_website', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=56,
                            value=Call(
                                lineno=16,
                                col_offset=8,
                                end_lineno=16,
                                end_col_offset=56,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=8,
                                    end_lineno=16,
                                    end_col_offset=24,
                                    value=Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        lineno=16,
                                        col_offset=25,
                                        end_lineno=16,
                                        end_col_offset=43,
                                        value=Call(
                                            lineno=16,
                                            col_offset=25,
                                            end_lineno=16,
                                            end_col_offset=40,
                                            func=Attribute(
                                                lineno=16,
                                                col_offset=25,
                                                end_lineno=16,
                                                end_col_offset=38,
                                                value=Name(lineno=16, col_offset=25, end_lineno=16, end_col_offset=33, id='response', ctx=Load()),
                                                attr='json',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Constant(lineno=16, col_offset=41, end_lineno=16, end_col_offset=42, value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=16,
                                        col_offset=45,
                                        end_lineno=16,
                                        end_col_offset=55,
                                        value=Name(lineno=16, col_offset=45, end_lineno=16, end_col_offset=52, id='company', ctx=Load()),
                                        attr='id',
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
            decorator_list=[
                Call(
                    lineno=7,
                    col_offset=1,
                    end_lineno=7,
                    end_col_offset=38,
                    func=Name(lineno=7, col_offset=1, end_lineno=7, end_col_offset=7, id='tagged', ctx=Load()),
                    args=[
                        Constant(lineno=7, col_offset=8, end_lineno=7, end_col_offset=22, value='post_install', kind=None),
                        Constant(lineno=7, col_offset=24, end_lineno=7, end_col_offset=37, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)