Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=39,
            module='odoo.tests',
            names=[
                alias(name='HttpCase', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=25,
            end_col_offset=121,
            name='TestSitemap',
            bases=[Name(lineno=7, col_offset=18, end_lineno=7, end_col_offset=26, id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=48,
                    name='setUp',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=14, end_lineno=9, end_col_offset=18, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=40,
                            value=Call(
                                lineno=10,
                                col_offset=8,
                                end_lineno=10,
                                end_col_offset=40,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=8,
                                    end_lineno=10,
                                    end_col_offset=38,
                                    value=Call(
                                        lineno=10,
                                        col_offset=8,
                                        end_lineno=10,
                                        end_col_offset=32,
                                        func=Name(lineno=10, col_offset=8, end_lineno=10, end_col_offset=13, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=10, col_offset=14, end_lineno=10, end_col_offset=25, id='TestSitemap', ctx=Load()),
                                            Name(lineno=10, col_offset=27, end_lineno=10, end_col_offset=31, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=11,
                            targets=[
                                Attribute(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=17,
                                    value=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=12, id='self', ctx=Load()),
                                    attr='cats',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=12,
                                col_offset=20,
                                end_lineno=18,
                                end_col_offset=11,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=20,
                                    end_lineno=12,
                                    end_col_offset=62,
                                    value=Subscript(
                                        lineno=12,
                                        col_offset=20,
                                        end_lineno=12,
                                        end_col_offset=55,
                                        value=Attribute(
                                            lineno=12,
                                            col_offset=20,
                                            end_lineno=12,
                                            end_col_offset=28,
                                            value=Name(lineno=12, col_offset=20, end_lineno=12, end_col_offset=24, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=12, col_offset=29, end_lineno=12, end_col_offset=54, value='product.public.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=12,
                                        col_offset=63,
                                        end_lineno=18,
                                        end_col_offset=10,
                                        elts=[
                                            Dict(
                                                lineno=12,
                                                col_offset=64,
                                                end_lineno=14,
                                                end_col_offset=9,
                                                keys=[Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=18, value='name', kind=None)],
                                                values=[Constant(lineno=13, col_offset=20, end_lineno=13, end_col_offset=29, value='Level 0', kind=None)],
                                            ),
                                            Dict(
                                                lineno=14,
                                                col_offset=11,
                                                end_lineno=16,
                                                end_col_offset=9,
                                                keys=[Constant(lineno=15, col_offset=12, end_lineno=15, end_col_offset=18, value='name', kind=None)],
                                                values=[Constant(lineno=15, col_offset=20, end_lineno=15, end_col_offset=29, value='Level 1', kind=None)],
                                            ),
                                            Dict(
                                                lineno=16,
                                                col_offset=11,
                                                end_lineno=18,
                                                end_col_offset=9,
                                                keys=[Constant(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, value='name', kind=None)],
                                                values=[Constant(lineno=17, col_offset=20, end_lineno=17, end_col_offset=29, value='Level 2', kind=None)],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=48,
                            targets=[
                                Attribute(
                                    lineno=19,
                                    col_offset=8,
                                    end_lineno=19,
                                    end_col_offset=30,
                                    value=Subscript(
                                        lineno=19,
                                        col_offset=8,
                                        end_lineno=19,
                                        end_col_offset=20,
                                        value=Attribute(
                                            lineno=19,
                                            col_offset=8,
                                            end_lineno=19,
                                            end_col_offset=17,
                                            value=Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=12, id='self', ctx=Load()),
                                            attr='cats',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=19, col_offset=18, end_lineno=19, end_col_offset=19, value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='parent_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                lineno=19,
                                col_offset=33,
                                end_lineno=19,
                                end_col_offset=48,
                                value=Subscript(
                                    lineno=19,
                                    col_offset=33,
                                    end_lineno=19,
                                    end_col_offset=45,
                                    value=Attribute(
                                        lineno=19,
                                        col_offset=33,
                                        end_lineno=19,
                                        end_col_offset=42,
                                        value=Name(lineno=19, col_offset=33, end_lineno=19, end_col_offset=37, id='self', ctx=Load()),
                                        attr='cats',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(lineno=19, col_offset=43, end_lineno=19, end_col_offset=44, value=1, kind=None),
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=48,
                            targets=[
                                Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=30,
                                    value=Subscript(
                                        lineno=20,
                                        col_offset=8,
                                        end_lineno=20,
                                        end_col_offset=20,
                                        value=Attribute(
                                            lineno=20,
                                            col_offset=8,
                                            end_lineno=20,
                                            end_col_offset=17,
                                            value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=12, id='self', ctx=Load()),
                                            attr='cats',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=20, col_offset=18, end_lineno=20, end_col_offset=19, value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='parent_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                lineno=20,
                                col_offset=33,
                                end_lineno=20,
                                end_col_offset=48,
                                value=Subscript(
                                    lineno=20,
                                    col_offset=33,
                                    end_lineno=20,
                                    end_col_offset=45,
                                    value=Attribute(
                                        lineno=20,
                                        col_offset=33,
                                        end_lineno=20,
                                        end_col_offset=42,
                                        value=Name(lineno=20, col_offset=33, end_lineno=20, end_col_offset=37, id='self', ctx=Load()),
                                        attr='cats',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(lineno=20, col_offset=43, end_lineno=20, end_col_offset=44, value=0, kind=None),
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=22,
                    col_offset=4,
                    end_lineno=25,
                    end_col_offset=121,
                    name='test_01_shop_route_sitemap',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=22, col_offset=35, end_lineno=22, end_col_offset=39, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=44,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=12, id='resp', ctx=Store())],
                            value=Call(
                                lineno=23,
                                col_offset=15,
                                end_lineno=23,
                                end_col_offset=44,
                                func=Attribute(
                                    lineno=23,
                                    col_offset=15,
                                    end_lineno=23,
                                    end_col_offset=28,
                                    value=Name(lineno=23, col_offset=15, end_lineno=23, end_col_offset=19, id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=23, col_offset=29, end_lineno=23, end_col_offset=43, value='/sitemap.xml', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=82,
                            targets=[Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=18, id='level2_url', ctx=Store())],
                            value=BinOp(
                                lineno=24,
                                col_offset=21,
                                end_lineno=24,
                                end_col_offset=82,
                                left=Constant(lineno=24, col_offset=21, end_lineno=24, end_col_offset=64, value='/shop/category/level-0-level-1-level-2-%s', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    lineno=24,
                                    col_offset=67,
                                    end_lineno=24,
                                    end_col_offset=82,
                                    value=Subscript(
                                        lineno=24,
                                        col_offset=67,
                                        end_lineno=24,
                                        end_col_offset=79,
                                        value=Attribute(
                                            lineno=24,
                                            col_offset=67,
                                            end_lineno=24,
                                            end_col_offset=76,
                                            value=Name(lineno=24, col_offset=67, end_lineno=24, end_col_offset=71, id='self', ctx=Load()),
                                            attr='cats',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=24, col_offset=77, end_lineno=24, end_col_offset=78, value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=121,
                            value=Call(
                                lineno=25,
                                col_offset=8,
                                end_lineno=25,
                                end_col_offset=121,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=8,
                                    end_lineno=25,
                                    end_col_offset=23,
                                    value=Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        lineno=25,
                                        col_offset=24,
                                        end_lineno=25,
                                        end_col_offset=47,
                                        left=Name(lineno=25, col_offset=24, end_lineno=25, end_col_offset=34, id='level2_url', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                lineno=25,
                                                col_offset=38,
                                                end_lineno=25,
                                                end_col_offset=47,
                                                value=Name(lineno=25, col_offset=38, end_lineno=25, end_col_offset=42, id='resp', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(lineno=25, col_offset=49, end_lineno=25, end_col_offset=120, value='Category entry in sitemap should be prefixed by its parent hierarchy.', kind=None),
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
                    lineno=6,
                    col_offset=1,
                    end_lineno=6,
                    end_col_offset=38,
                    func=Name(lineno=6, col_offset=1, end_lineno=6, end_col_offset=7, id='tagged', ctx=Load()),
                    args=[
                        Constant(lineno=6, col_offset=8, end_lineno=6, end_col_offset=22, value='post_install', kind=None),
                        Constant(lineno=6, col_offset=24, end_lineno=6, end_col_offset=37, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)