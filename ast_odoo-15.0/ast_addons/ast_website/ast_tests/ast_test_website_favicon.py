Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=21,
            module='PIL',
            names=[alias(name='Image', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=29,
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=45,
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=55,
            module='odoo.tools',
            names=[
                alias(name='base64_to_image', asname=None),
                alias(name='image_to_base64', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=12,
            col_offset=0,
            end_lineno=36,
            end_col_offset=58,
            name='TestWebsiteResetPassword',
            bases=[Name(lineno=12, col_offset=31, end_lineno=12, end_col_offset=46, id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=36,
                    end_col_offset=58,
                    name='test_01_website_favicon',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=32, end_lineno=14, end_col_offset=36, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=16,
                            end_col_offset=34,
                            value=Constant(lineno=15, col_offset=8, end_lineno=16, end_col_offset=34, value='The goal of this test is to make sure the favicon is correctly\n        handled on the website.', kind=None),
                        ),
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=37,
                            targets=[Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=15, id='Website', ctx=Store())],
                            value=Subscript(
                                lineno=19,
                                col_offset=18,
                                end_lineno=19,
                                end_col_offset=37,
                                value=Attribute(
                                    lineno=19,
                                    col_offset=18,
                                    end_lineno=19,
                                    end_col_offset=26,
                                    value=Name(lineno=19, col_offset=18, end_lineno=19, end_col_offset=22, id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(lineno=19, col_offset=27, end_lineno=19, end_col_offset=36, value='website', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=21,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=10,
                            targets=[Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=15, id='website', ctx=Store())],
                            value=Call(
                                lineno=21,
                                col_offset=18,
                                end_lineno=24,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=18,
                                    end_lineno=21,
                                    end_col_offset=32,
                                    value=Name(lineno=21, col_offset=18, end_lineno=21, end_col_offset=25, id='Website', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=21,
                                        col_offset=33,
                                        end_lineno=24,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=22, col_offset=12, end_lineno=22, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=23, col_offset=12, end_lineno=23, end_col_offset=21, value='favicon', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=22, col_offset=20, end_lineno=22, end_col_offset=34, value='Test Website', kind=None),
                                            Call(
                                                lineno=23,
                                                col_offset=23,
                                                end_lineno=23,
                                                end_col_offset=49,
                                                func=Attribute(
                                                    lineno=23,
                                                    col_offset=23,
                                                    end_lineno=23,
                                                    end_col_offset=47,
                                                    value=Name(lineno=23, col_offset=23, end_lineno=23, end_col_offset=30, id='Website', ctx=Load()),
                                                    attr='_default_favicon',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=48,
                            targets=[Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=13, id='image', ctx=Store())],
                            value=Call(
                                lineno=26,
                                col_offset=16,
                                end_lineno=26,
                                end_col_offset=48,
                                func=Name(lineno=26, col_offset=16, end_lineno=26, end_col_offset=31, id='base64_to_image', ctx=Load()),
                                args=[
                                    Attribute(
                                        lineno=26,
                                        col_offset=32,
                                        end_lineno=26,
                                        end_col_offset=47,
                                        value=Name(lineno=26, col_offset=32, end_lineno=26, end_col_offset=39, id='website', ctx=Load()),
                                        attr='favicon',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=27,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=45,
                            value=Call(
                                lineno=27,
                                col_offset=8,
                                end_lineno=27,
                                end_col_offset=45,
                                func=Attribute(
                                    lineno=27,
                                    col_offset=8,
                                    end_lineno=27,
                                    end_col_offset=24,
                                    value=Name(lineno=27, col_offset=8, end_lineno=27, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=27,
                                        col_offset=25,
                                        end_lineno=27,
                                        end_col_offset=37,
                                        value=Name(lineno=27, col_offset=25, end_lineno=27, end_col_offset=30, id='image', ctx=Load()),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=27, col_offset=39, end_lineno=27, end_col_offset=44, value='ICO', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=33,
                            targets=[Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=16, id='bg_color', ctx=Store())],
                            value=Tuple(
                                lineno=30,
                                col_offset=19,
                                end_lineno=30,
                                end_col_offset=33,
                                elts=[
                                    Constant(lineno=30, col_offset=20, end_lineno=30, end_col_offset=23, value=135, kind=None),
                                    Constant(lineno=30, col_offset=25, end_lineno=30, end_col_offset=27, value=90, kind=None),
                                    Constant(lineno=30, col_offset=29, end_lineno=30, end_col_offset=32, value=123, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=62,
                            targets=[Name(lineno=31, col_offset=8, end_lineno=31, end_col_offset=13, id='image', ctx=Store())],
                            value=Call(
                                lineno=31,
                                col_offset=16,
                                end_lineno=31,
                                end_col_offset=62,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=16,
                                    end_lineno=31,
                                    end_col_offset=25,
                                    value=Name(lineno=31, col_offset=16, end_lineno=31, end_col_offset=21, id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=31, col_offset=26, end_lineno=31, end_col_offset=31, value='RGB', kind=None),
                                    Tuple(
                                        lineno=31,
                                        col_offset=33,
                                        end_lineno=31,
                                        end_col_offset=45,
                                        elts=[
                                            Constant(lineno=31, col_offset=34, end_lineno=31, end_col_offset=38, value=1920, kind=None),
                                            Constant(lineno=31, col_offset=40, end_lineno=31, end_col_offset=44, value=1080, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=31,
                                        col_offset=47,
                                        end_lineno=31,
                                        end_col_offset=61,
                                        arg='color',
                                        value=Name(lineno=31, col_offset=53, end_lineno=31, end_col_offset=61, id='bg_color', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=56,
                            targets=[
                                Attribute(
                                    lineno=32,
                                    col_offset=8,
                                    end_lineno=32,
                                    end_col_offset=23,
                                    value=Name(lineno=32, col_offset=8, end_lineno=32, end_col_offset=15, id='website', ctx=Load()),
                                    attr='favicon',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=32,
                                col_offset=26,
                                end_lineno=32,
                                end_col_offset=56,
                                func=Name(lineno=32, col_offset=26, end_lineno=32, end_col_offset=41, id='image_to_base64', ctx=Load()),
                                args=[
                                    Name(lineno=32, col_offset=42, end_lineno=32, end_col_offset=47, id='image', ctx=Load()),
                                    Constant(lineno=32, col_offset=49, end_lineno=32, end_col_offset=55, value='JPEG', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=33,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=48,
                            targets=[Name(lineno=33, col_offset=8, end_lineno=33, end_col_offset=13, id='image', ctx=Store())],
                            value=Call(
                                lineno=33,
                                col_offset=16,
                                end_lineno=33,
                                end_col_offset=48,
                                func=Name(lineno=33, col_offset=16, end_lineno=33, end_col_offset=31, id='base64_to_image', ctx=Load()),
                                args=[
                                    Attribute(
                                        lineno=33,
                                        col_offset=32,
                                        end_lineno=33,
                                        end_col_offset=47,
                                        value=Name(lineno=33, col_offset=32, end_lineno=33, end_col_offset=39, id='website', ctx=Load()),
                                        attr='favicon',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=45,
                            value=Call(
                                lineno=34,
                                col_offset=8,
                                end_lineno=34,
                                end_col_offset=45,
                                func=Attribute(
                                    lineno=34,
                                    col_offset=8,
                                    end_lineno=34,
                                    end_col_offset=24,
                                    value=Name(lineno=34, col_offset=8, end_lineno=34, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=34,
                                        col_offset=25,
                                        end_lineno=34,
                                        end_col_offset=37,
                                        value=Name(lineno=34, col_offset=25, end_lineno=34, end_col_offset=30, id='image', ctx=Load()),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=34, col_offset=39, end_lineno=34, end_col_offset=44, value='ICO', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=35,
                            col_offset=8,
                            end_lineno=35,
                            end_col_offset=48,
                            value=Call(
                                lineno=35,
                                col_offset=8,
                                end_lineno=35,
                                end_col_offset=48,
                                func=Attribute(
                                    lineno=35,
                                    col_offset=8,
                                    end_lineno=35,
                                    end_col_offset=24,
                                    value=Name(lineno=35, col_offset=8, end_lineno=35, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=35,
                                        col_offset=25,
                                        end_lineno=35,
                                        end_col_offset=35,
                                        value=Name(lineno=35, col_offset=25, end_lineno=35, end_col_offset=30, id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=35,
                                        col_offset=37,
                                        end_lineno=35,
                                        end_col_offset=47,
                                        elts=[
                                            Constant(lineno=35, col_offset=38, end_lineno=35, end_col_offset=41, value=256, kind=None),
                                            Constant(lineno=35, col_offset=43, end_lineno=35, end_col_offset=46, value=256, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=36,
                            col_offset=8,
                            end_lineno=36,
                            end_col_offset=58,
                            value=Call(
                                lineno=36,
                                col_offset=8,
                                end_lineno=36,
                                end_col_offset=58,
                                func=Attribute(
                                    lineno=36,
                                    col_offset=8,
                                    end_lineno=36,
                                    end_col_offset=24,
                                    value=Name(lineno=36, col_offset=8, end_lineno=36, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=36,
                                        col_offset=25,
                                        end_lineno=36,
                                        end_col_offset=47,
                                        func=Attribute(
                                            lineno=36,
                                            col_offset=25,
                                            end_lineno=36,
                                            end_col_offset=39,
                                            value=Name(lineno=36, col_offset=25, end_lineno=36, end_col_offset=30, id='image', ctx=Load()),
                                            attr='getpixel',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                lineno=36,
                                                col_offset=40,
                                                end_lineno=36,
                                                end_col_offset=46,
                                                elts=[
                                                    Constant(lineno=36, col_offset=41, end_lineno=36, end_col_offset=42, value=0, kind=None),
                                                    Constant(lineno=36, col_offset=44, end_lineno=36, end_col_offset=45, value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(lineno=36, col_offset=49, end_lineno=36, end_col_offset=57, id='bg_color', ctx=Load()),
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
