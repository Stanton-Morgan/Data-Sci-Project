Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        Import(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=11,
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=29,
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=38,
            module='odoo.tests.common',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=12,
            col_offset=0,
            end_lineno=31,
            end_col_offset=60,
            name='TestWebsiteSaleMail',
            bases=[Name(lineno=12, col_offset=26, end_lineno=12, end_col_offset=34, id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=31,
                    end_col_offset=60,
                    name='test_01_shop_mail_tour',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=31, end_lineno=14, end_col_offset=35, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=78,
                            value=Constant(lineno=15, col_offset=8, end_lineno=15, end_col_offset=78, value='The goal of this test is to make sure sending SO by email works.', kind=None),
                        ),
                        Expr(
                            lineno=17,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=10,
                            value=Call(
                                lineno=17,
                                col_offset=8,
                                end_lineno=21,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=17,
                                    col_offset=8,
                                    end_lineno=17,
                                    end_col_offset=42,
                                    value=Subscript(
                                        lineno=17,
                                        col_offset=8,
                                        end_lineno=17,
                                        end_col_offset=35,
                                        value=Attribute(
                                            lineno=17,
                                            col_offset=8,
                                            end_lineno=17,
                                            end_col_offset=16,
                                            value=Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=17, col_offset=17, end_lineno=17, end_col_offset=34, value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=17,
                                        col_offset=43,
                                        end_lineno=21,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=18, col_offset=12, end_lineno=18, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=19, col_offset=12, end_lineno=19, end_col_offset=24, value='list_price', kind=None),
                                            Constant(lineno=20, col_offset=12, end_lineno=20, end_col_offset=31, value='website_published', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=18, col_offset=20, end_lineno=18, end_col_offset=43, value='Acoustic Bloc Screens', kind=None),
                                            Constant(lineno=19, col_offset=26, end_lineno=19, end_col_offset=32, value=2950.0, kind=None),
                                            Constant(lineno=20, col_offset=33, end_lineno=20, end_col_offset=37, value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=22,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=10,
                            value=Call(
                                lineno=22,
                                col_offset=8,
                                end_lineno=25,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=22,
                                    col_offset=8,
                                    end_lineno=22,
                                    end_col_offset=38,
                                    value=Subscript(
                                        lineno=22,
                                        col_offset=8,
                                        end_lineno=22,
                                        end_col_offset=31,
                                        value=Attribute(
                                            lineno=22,
                                            col_offset=8,
                                            end_lineno=22,
                                            end_col_offset=16,
                                            value=Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=22, col_offset=17, end_lineno=22, end_col_offset=30, value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=22,
                                        col_offset=39,
                                        end_lineno=25,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=23, col_offset=12, end_lineno=23, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=24, col_offset=12, end_lineno=24, end_col_offset=19, value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=23, col_offset=20, end_lineno=23, end_col_offset=36, value='Azure Interior', kind=None),
                                            Constant(lineno=24, col_offset=21, end_lineno=24, end_col_offset=51, value='azure.Interior24@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=28,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=61,
                            targets=[Name(lineno=28, col_offset=8, end_lineno=28, end_col_offset=16, id='MailMail', ctx=Store())],
                            value=Attribute(
                                lineno=28,
                                col_offset=19,
                                end_lineno=28,
                                end_col_offset=61,
                                value=Attribute(
                                    lineno=28,
                                    col_offset=19,
                                    end_lineno=28,
                                    end_col_offset=52,
                                    value=Attribute(
                                        lineno=28,
                                        col_offset=19,
                                        end_lineno=28,
                                        end_col_offset=42,
                                        value=Attribute(
                                            lineno=28,
                                            col_offset=19,
                                            end_lineno=28,
                                            end_col_offset=35,
                                            value=Attribute(
                                                lineno=28,
                                                col_offset=19,
                                                end_lineno=28,
                                                end_col_offset=30,
                                                value=Name(lineno=28, col_offset=19, end_lineno=28, end_col_offset=23, id='odoo', ctx=Load()),
                                                attr='addons',
                                                ctx=Load(),
                                            ),
                                            attr='mail',
                                            ctx=Load(),
                                        ),
                                        attr='models',
                                        ctx=Load(),
                                    ),
                                    attr='mail_mail',
                                    ctx=Load(),
                                ),
                                attr='MailMail',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        With(
                            lineno=30,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=60,
                            items=[
                                withitem(
                                    context_expr=Call(
                                        lineno=30,
                                        col_offset=13,
                                        end_lineno=30,
                                        end_col_offset=64,
                                        func=Attribute(
                                            lineno=30,
                                            col_offset=13,
                                            end_lineno=30,
                                            end_col_offset=25,
                                            value=Name(lineno=30, col_offset=13, end_lineno=30, end_col_offset=18, id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(lineno=30, col_offset=26, end_lineno=30, end_col_offset=34, id='MailMail', ctx=Load()),
                                            Constant(lineno=30, col_offset=36, end_lineno=30, end_col_offset=44, value='unlink', kind=None),
                                            Lambda(
                                                lineno=30,
                                                col_offset=46,
                                                end_lineno=30,
                                                end_col_offset=63,
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(lineno=30, col_offset=53, end_lineno=30, end_col_offset=57, arg='self', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Constant(lineno=30, col_offset=59, end_lineno=30, end_col_offset=63, value=None, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    lineno=31,
                                    col_offset=12,
                                    end_lineno=31,
                                    end_col_offset=60,
                                    value=Call(
                                        lineno=31,
                                        col_offset=12,
                                        end_lineno=31,
                                        end_col_offset=60,
                                        func=Attribute(
                                            lineno=31,
                                            col_offset=12,
                                            end_lineno=31,
                                            end_col_offset=27,
                                            value=Name(lineno=31, col_offset=12, end_lineno=31, end_col_offset=16, id='self', ctx=Load()),
                                            attr='start_tour',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(lineno=31, col_offset=28, end_lineno=31, end_col_offset=31, value='/', kind=None),
                                            Constant(lineno=31, col_offset=33, end_lineno=31, end_col_offset=44, value='shop_mail', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                lineno=31,
                                                col_offset=46,
                                                end_lineno=31,
                                                end_col_offset=59,
                                                arg='login',
                                                value=Constant(lineno=31, col_offset=52, end_lineno=31, end_col_offset=59, value='admin', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    lineno=11,
                    col_offset=1,
                    end_lineno=11,
                    end_col_offset=38,
                    func=Name(lineno=11, col_offset=1, end_lineno=11, end_col_offset=7, id='tagged', ctx=Load()),
                    args=[
                        Constant(lineno=11, col_offset=8, end_lineno=11, end_col_offset=22, value='post_install', kind=None),
                        Constant(lineno=11, col_offset=24, end_lineno=11, end_col_offset=37, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)