Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=21,
            module='lxml',
            names=[alias(name='html', asname=None)],
            level=0,
        ),
        Import(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=11,
            names=[alias(name='odoo', asname=None)],
        ),
        Import(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=17,
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=49,
            module='odoo.addons.website.tools',
            names=[alias(name='MockRequest', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=12,
            col_offset=0,
            end_lineno=30,
            end_col_offset=137,
            name='TestSnippets',
            bases=[
                Attribute(
                    lineno=12,
                    col_offset=19,
                    end_lineno=12,
                    end_col_offset=38,
                    value=Attribute(
                        lineno=12,
                        col_offset=19,
                        end_lineno=12,
                        end_col_offset=29,
                        value=Name(lineno=12, col_offset=19, end_lineno=12, end_col_offset=23, id='odoo', ctx=Load()),
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
                    lineno=14,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=94,
                    name='test_01_empty_parents_autoremove',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=41, end_lineno=14, end_col_offset=45, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=94,
                            value=Call(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=94,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=8,
                                    end_lineno=15,
                                    end_col_offset=23,
                                    value=Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=15, col_offset=24, end_lineno=15, end_col_offset=43, value='/?enable_editor=1', kind=None),
                                    Constant(lineno=15, col_offset=45, end_lineno=15, end_col_offset=78, value='snippet_empty_parent_autoremove', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=15,
                                        col_offset=80,
                                        end_lineno=15,
                                        end_col_offset=93,
                                        arg='login',
                                        value=Constant(lineno=15, col_offset=86, end_lineno=15, end_col_offset=93, value='admin', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=17,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=96,
                    name='test_02_default_shape_gets_palette_colors',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=17, col_offset=50, end_lineno=17, end_col_offset=54, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=96,
                            value=Call(
                                lineno=18,
                                col_offset=8,
                                end_lineno=18,
                                end_col_offset=96,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=8,
                                    end_lineno=18,
                                    end_col_offset=23,
                                    value=Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=18, col_offset=24, end_lineno=18, end_col_offset=43, value='/?enable_editor=1', kind=None),
                                    Constant(lineno=18, col_offset=45, end_lineno=18, end_col_offset=80, value='default_shape_gets_palette_colors', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=18,
                                        col_offset=82,
                                        end_lineno=18,
                                        end_col_offset=95,
                                        arg='login',
                                        value=Constant(lineno=18, col_offset=88, end_lineno=18, end_col_offset=95, value='admin', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=20,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=137,
                    name='test_03_snippets_all_drag_and_drop',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=20, col_offset=43, end_lineno=20, end_col_offset=47, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        With(
                            lineno=21,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=94,
                            items=[
                                withitem(
                                    context_expr=Call(
                                        lineno=21,
                                        col_offset=13,
                                        end_lineno=21,
                                        end_col_offset=73,
                                        func=Name(lineno=21, col_offset=13, end_lineno=21, end_col_offset=24, id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                lineno=21,
                                                col_offset=25,
                                                end_lineno=21,
                                                end_col_offset=33,
                                                value=Name(lineno=21, col_offset=25, end_lineno=21, end_col_offset=29, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                lineno=21,
                                                col_offset=35,
                                                end_lineno=21,
                                                end_col_offset=72,
                                                arg='website',
                                                value=Call(
                                                    lineno=21,
                                                    col_offset=43,
                                                    end_lineno=21,
                                                    end_col_offset=72,
                                                    func=Attribute(
                                                        lineno=21,
                                                        col_offset=43,
                                                        end_lineno=21,
                                                        end_col_offset=69,
                                                        value=Subscript(
                                                            lineno=21,
                                                            col_offset=43,
                                                            end_lineno=21,
                                                            end_col_offset=62,
                                                            value=Attribute(
                                                                lineno=21,
                                                                col_offset=43,
                                                                end_lineno=21,
                                                                end_col_offset=51,
                                                                value=Name(lineno=21, col_offset=43, end_lineno=21, end_col_offset=47, id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(lineno=21, col_offset=52, end_lineno=21, end_col_offset=61, value='website', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(lineno=21, col_offset=70, end_lineno=21, end_col_offset=71, value=1, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=94,
                                    targets=[Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=29, id='snippets_template', ctx=Store())],
                                    value=Call(
                                        lineno=22,
                                        col_offset=32,
                                        end_lineno=22,
                                        end_col_offset=94,
                                        func=Attribute(
                                            lineno=22,
                                            col_offset=32,
                                            end_lineno=22,
                                            end_col_offset=74,
                                            value=Subscript(
                                                lineno=22,
                                                col_offset=32,
                                                end_lineno=22,
                                                end_col_offset=54,
                                                value=Attribute(
                                                    lineno=22,
                                                    col_offset=32,
                                                    end_lineno=22,
                                                    end_col_offset=40,
                                                    value=Name(lineno=22, col_offset=32, end_lineno=22, end_col_offset=36, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=22, col_offset=41, end_lineno=22, end_col_offset=53, value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='render_public_asset',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=22, col_offset=75, end_lineno=22, end_col_offset=93, value='website.snippets', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=58,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=21, id='html_template', ctx=Store())],
                            value=Call(
                                lineno=23,
                                col_offset=24,
                                end_lineno=23,
                                end_col_offset=58,
                                func=Attribute(
                                    lineno=23,
                                    col_offset=24,
                                    end_lineno=23,
                                    end_col_offset=39,
                                    value=Name(lineno=23, col_offset=24, end_lineno=23, end_col_offset=28, id='html', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=23, col_offset=40, end_lineno=23, end_col_offset=57, id='snippets_template', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=125,
                            targets=[Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=24, id='data_snippet_els', ctx=Store())],
                            value=Call(
                                lineno=24,
                                col_offset=27,
                                end_lineno=24,
                                end_col_offset=125,
                                func=Attribute(
                                    lineno=24,
                                    col_offset=27,
                                    end_lineno=24,
                                    end_col_offset=46,
                                    value=Name(lineno=24, col_offset=27, end_lineno=24, end_col_offset=40, id='html_template', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=24, col_offset=47, end_lineno=24, end_col_offset=124, value="//*[@class='o_panel' and not(contains(@class, 'd-none'))]//*[@data-snippet]", kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=9,
                            targets=[Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=17, id='blacklist', ctx=Store())],
                            value=List(
                                lineno=25,
                                col_offset=20,
                                end_lineno=28,
                                end_col_offset=9,
                                elts=[
                                    Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=29, value='s_facebook_page', kind=None),
                                    Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=19, value='s_map', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=135,
                            targets=[Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=22, id='snippets_names', ctx=Store())],
                            value=Call(
                                lineno=29,
                                col_offset=25,
                                end_lineno=29,
                                end_col_offset=135,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=25,
                                    end_lineno=29,
                                    end_col_offset=33,
                                    value=Constant(lineno=29, col_offset=25, end_lineno=29, end_col_offset=28, value=',', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        lineno=29,
                                        col_offset=34,
                                        end_lineno=29,
                                        end_col_offset=134,
                                        elt=Subscript(
                                            lineno=29,
                                            col_offset=35,
                                            end_lineno=29,
                                            end_col_offset=60,
                                            value=Attribute(
                                                lineno=29,
                                                col_offset=35,
                                                end_lineno=29,
                                                end_col_offset=44,
                                                value=Name(lineno=29, col_offset=35, end_lineno=29, end_col_offset=37, id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(lineno=29, col_offset=45, end_lineno=29, end_col_offset=59, value='data-snippet', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(lineno=29, col_offset=65, end_lineno=29, end_col_offset=67, id='el', ctx=Store()),
                                                iter=Name(lineno=29, col_offset=71, end_lineno=29, end_col_offset=87, id='data_snippet_els', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        lineno=29,
                                                        col_offset=91,
                                                        end_lineno=29,
                                                        end_col_offset=133,
                                                        left=Subscript(
                                                            lineno=29,
                                                            col_offset=91,
                                                            end_lineno=29,
                                                            end_col_offset=116,
                                                            value=Attribute(
                                                                lineno=29,
                                                                col_offset=91,
                                                                end_lineno=29,
                                                                end_col_offset=100,
                                                                value=Name(lineno=29, col_offset=91, end_lineno=29, end_col_offset=93, id='el', ctx=Load()),
                                                                attr='attrib',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(lineno=29, col_offset=101, end_lineno=29, end_col_offset=115, value='data-snippet', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(lineno=29, col_offset=124, end_lineno=29, end_col_offset=133, id='blacklist', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=137,
                            value=Call(
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=137,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=23,
                                    value=Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        lineno=30,
                                        col_offset=24,
                                        end_lineno=30,
                                        end_col_offset=78,
                                        left=Constant(lineno=30, col_offset=24, end_lineno=30, end_col_offset=61, value='/?enable_editor=1&snippets_names=%s', kind=None),
                                        op=Mod(),
                                        right=Name(lineno=30, col_offset=64, end_lineno=30, end_col_offset=78, id='snippets_names', ctx=Load()),
                                    ),
                                    Constant(lineno=30, col_offset=80, end_lineno=30, end_col_offset=108, value='snippets_all_drag_and_drop', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=30,
                                        col_offset=110,
                                        end_lineno=30,
                                        end_col_offset=123,
                                        arg='login',
                                        value=Constant(lineno=30, col_offset=116, end_lineno=30, end_col_offset=123, value='admin', kind=None),
                                    ),
                                    keyword(
                                        lineno=30,
                                        col_offset=125,
                                        end_lineno=30,
                                        end_col_offset=136,
                                        arg='timeout',
                                        value=Constant(lineno=30, col_offset=133, end_lineno=30, end_col_offset=136, value=300, kind=None),
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
                    lineno=11,
                    col_offset=1,
                    end_lineno=11,
                    end_col_offset=76,
                    func=Attribute(
                        lineno=11,
                        col_offset=1,
                        end_lineno=11,
                        end_col_offset=25,
                        value=Attribute(
                            lineno=11,
                            col_offset=1,
                            end_lineno=11,
                            end_col_offset=18,
                            value=Attribute(
                                lineno=11,
                                col_offset=1,
                                end_lineno=11,
                                end_col_offset=11,
                                value=Name(lineno=11, col_offset=1, end_lineno=11, end_col_offset=5, id='odoo', ctx=Load()),
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
                        Constant(lineno=11, col_offset=26, end_lineno=11, end_col_offset=40, value='post_install', kind=None),
                        Constant(lineno=11, col_offset=42, end_lineno=11, end_col_offset=55, value='-at_install', kind=None),
                        Constant(lineno=11, col_offset=57, end_lineno=11, end_col_offset=75, value='website_snippets', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
