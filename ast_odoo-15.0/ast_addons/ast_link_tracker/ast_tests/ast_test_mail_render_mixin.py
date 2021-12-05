Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=29,
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=52,
            end_col_offset=78,
            name='TestMailRenderMixin',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=26,
                    end_lineno=7,
                    end_col_offset=48,
                    value=Name(lineno=7, col_offset=26, end_lineno=7, end_col_offset=32, id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=8,
                    col_offset=4,
                    end_lineno=52,
                    end_col_offset=78,
                    name='test_shorten_links',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=8, col_offset=27, end_lineno=8, end_col_offset=31, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=9,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=9,
                            targets=[Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=18, id='test_links', ctx=Store())],
                            value=List(
                                lineno=9,
                                col_offset=21,
                                end_lineno=24,
                                end_col_offset=9,
                                elts=[
                                    Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=83, value='<a href="https://gitlab.com" title="title" fake="fake">test_label</a>', kind=None),
                                    Constant(lineno=11, col_offset=12, end_lineno=11, end_col_offset=55, value='<a href="https://test_542152qsdqsd.com"/>', kind=None),
                                    Constant(lineno=12, col_offset=12, end_lineno=15, end_col_offset=15, value='<a href="https://third_test_54212.com">\n                    <img src="imagesrc"/>\n                </a>\n            ', kind=None),
                                    Constant(lineno=16, col_offset=12, end_lineno=21, end_col_offset=15, value='<a\n                    href="https://test_strange_html.com"       title="title"\n                fake=\'fake\'\n                > test_strange_html_label\n                </a>\n            ', kind=None),
                                    Constant(lineno=22, col_offset=12, end_lineno=22, end_col_offset=103, value='<a href="https://test_escaped.com" title="title" fake="fake"> test_escaped &lt; &gt; </a>', kind=None),
                                    Constant(lineno=23, col_offset=12, end_lineno=23, end_col_offset=69, value='<a href="https://url_with_params.com?a=b&c=d">label</a>', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=77,
                            value=Call(
                                lineno=26,
                                col_offset=8,
                                end_lineno=26,
                                end_col_offset=77,
                                func=Attribute(
                                    lineno=26,
                                    col_offset=8,
                                    end_lineno=26,
                                    end_col_offset=52,
                                    value=Subscript(
                                        lineno=26,
                                        col_offset=8,
                                        end_lineno=26,
                                        end_col_offset=37,
                                        value=Attribute(
                                            lineno=26,
                                            col_offset=8,
                                            end_lineno=26,
                                            end_col_offset=16,
                                            value=Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=26, col_offset=17, end_lineno=26, end_col_offset=36, value='mail.render.mixin', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_shorten_links',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=26,
                                        col_offset=53,
                                        end_lineno=26,
                                        end_col_offset=72,
                                        func=Attribute(
                                            lineno=26,
                                            col_offset=53,
                                            end_lineno=26,
                                            end_col_offset=60,
                                            value=Constant(lineno=26, col_offset=53, end_lineno=26, end_col_offset=55, value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=26, col_offset=61, end_lineno=26, end_col_offset=71, id='test_links', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Dict(lineno=26, col_offset=74, end_lineno=26, end_col_offset=76, keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=28,
                            col_offset=8,
                            end_lineno=43,
                            end_col_offset=9,
                            targets=[Name(lineno=28, col_offset=8, end_lineno=28, end_col_offset=24, id='trackers_to_find', ctx=Store())],
                            value=List(
                                lineno=28,
                                col_offset=27,
                                end_lineno=43,
                                end_col_offset=9,
                                elts=[
                                    List(
                                        lineno=29,
                                        col_offset=12,
                                        end_lineno=29,
                                        end_col_offset=78,
                                        elts=[
                                            Tuple(
                                                lineno=29,
                                                col_offset=13,
                                                end_lineno=29,
                                                end_col_offset=47,
                                                elts=[
                                                    Constant(lineno=29, col_offset=14, end_lineno=29, end_col_offset=19, value='url', kind=None),
                                                    Constant(lineno=29, col_offset=21, end_lineno=29, end_col_offset=24, value='=', kind=None),
                                                    Constant(lineno=29, col_offset=26, end_lineno=29, end_col_offset=46, value='https://gitlab.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=29,
                                                col_offset=49,
                                                end_lineno=29,
                                                end_col_offset=77,
                                                elts=[
                                                    Constant(lineno=29, col_offset=50, end_lineno=29, end_col_offset=57, value='label', kind=None),
                                                    Constant(lineno=29, col_offset=59, end_lineno=29, end_col_offset=62, value='=', kind=None),
                                                    Constant(lineno=29, col_offset=64, end_lineno=29, end_col_offset=76, value='test_label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=30,
                                        col_offset=12,
                                        end_lineno=30,
                                        end_col_offset=59,
                                        elts=[
                                            Tuple(
                                                lineno=30,
                                                col_offset=13,
                                                end_lineno=30,
                                                end_col_offset=58,
                                                elts=[
                                                    Constant(lineno=30, col_offset=14, end_lineno=30, end_col_offset=19, value='url', kind=None),
                                                    Constant(lineno=30, col_offset=21, end_lineno=30, end_col_offset=24, value='=', kind=None),
                                                    Constant(lineno=30, col_offset=26, end_lineno=30, end_col_offset=57, value='https://test_542152qsdqsd.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=31,
                                        col_offset=12,
                                        end_lineno=34,
                                        end_col_offset=13,
                                        elts=[
                                            Tuple(
                                                lineno=32,
                                                col_offset=16,
                                                end_lineno=32,
                                                end_col_offset=61,
                                                elts=[
                                                    Constant(lineno=32, col_offset=17, end_lineno=32, end_col_offset=22, value='url', kind=None),
                                                    Constant(lineno=32, col_offset=24, end_lineno=32, end_col_offset=27, value='=', kind=None),
                                                    Constant(lineno=32, col_offset=29, end_lineno=32, end_col_offset=60, value='https://test_strange_html.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=33,
                                                col_offset=16,
                                                end_lineno=33,
                                                end_col_offset=57,
                                                elts=[
                                                    Constant(lineno=33, col_offset=17, end_lineno=33, end_col_offset=24, value='label', kind=None),
                                                    Constant(lineno=33, col_offset=26, end_lineno=33, end_col_offset=29, value='=', kind=None),
                                                    Constant(lineno=33, col_offset=31, end_lineno=33, end_col_offset=56, value='test_strange_html_label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=35,
                                        col_offset=12,
                                        end_lineno=38,
                                        end_col_offset=13,
                                        elts=[
                                            Tuple(
                                                lineno=36,
                                                col_offset=16,
                                                end_lineno=36,
                                                end_col_offset=56,
                                                elts=[
                                                    Constant(lineno=36, col_offset=17, end_lineno=36, end_col_offset=22, value='url', kind=None),
                                                    Constant(lineno=36, col_offset=24, end_lineno=36, end_col_offset=27, value='=', kind=None),
                                                    Constant(lineno=36, col_offset=29, end_lineno=36, end_col_offset=55, value='https://test_escaped.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=37,
                                                col_offset=16,
                                                end_lineno=37,
                                                end_col_offset=50,
                                                elts=[
                                                    Constant(lineno=37, col_offset=17, end_lineno=37, end_col_offset=24, value='label', kind=None),
                                                    Constant(lineno=37, col_offset=26, end_lineno=37, end_col_offset=29, value='=', kind=None),
                                                    Constant(lineno=37, col_offset=31, end_lineno=37, end_col_offset=49, value='test_escaped < >', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=39,
                                        col_offset=12,
                                        end_lineno=42,
                                        end_col_offset=13,
                                        elts=[
                                            Tuple(
                                                lineno=40,
                                                col_offset=16,
                                                end_lineno=40,
                                                end_col_offset=67,
                                                elts=[
                                                    Constant(lineno=40, col_offset=17, end_lineno=40, end_col_offset=22, value='url', kind=None),
                                                    Constant(lineno=40, col_offset=24, end_lineno=40, end_col_offset=27, value='=', kind=None),
                                                    Constant(lineno=40, col_offset=29, end_lineno=40, end_col_offset=66, value='https://url_with_params.com?a=b&c=d', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=41,
                                                col_offset=16,
                                                end_lineno=41,
                                                end_col_offset=39,
                                                elts=[
                                                    Constant(lineno=41, col_offset=17, end_lineno=41, end_col_offset=24, value='label', kind=None),
                                                    Constant(lineno=41, col_offset=26, end_lineno=41, end_col_offset=29, value='=', kind=None),
                                                    Constant(lineno=41, col_offset=31, end_lineno=41, end_col_offset=38, value='label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=44,
                            col_offset=8,
                            end_lineno=46,
                            end_col_offset=9,
                            targets=[Name(lineno=44, col_offset=8, end_lineno=44, end_col_offset=24, id='trackers_to_fail', ctx=Store())],
                            value=List(
                                lineno=44,
                                col_offset=27,
                                end_lineno=46,
                                end_col_offset=9,
                                elts=[
                                    List(
                                        lineno=45,
                                        col_offset=12,
                                        end_lineno=45,
                                        end_col_offset=84,
                                        elts=[
                                            Tuple(
                                                lineno=45,
                                                col_offset=13,
                                                end_lineno=45,
                                                end_col_offset=58,
                                                elts=[
                                                    Constant(lineno=45, col_offset=14, end_lineno=45, end_col_offset=19, value='url', kind=None),
                                                    Constant(lineno=45, col_offset=21, end_lineno=45, end_col_offset=24, value='=', kind=None),
                                                    Constant(lineno=45, col_offset=26, end_lineno=45, end_col_offset=57, value='https://test_542152qsdqsd.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=45,
                                                col_offset=60,
                                                end_lineno=45,
                                                end_col_offset=83,
                                                elts=[
                                                    Constant(lineno=45, col_offset=61, end_lineno=45, end_col_offset=68, value='label', kind=None),
                                                    Constant(lineno=45, col_offset=70, end_lineno=45, end_col_offset=77, value='ilike', kind=None),
                                                    Constant(lineno=45, col_offset=79, end_lineno=45, end_col_offset=82, value='_', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=48,
                            col_offset=8,
                            end_lineno=49,
                            end_col_offset=77,
                            target=Name(lineno=48, col_offset=12, end_lineno=48, end_col_offset=27, id='tracker_to_find', ctx=Store()),
                            iter=Name(lineno=48, col_offset=31, end_lineno=48, end_col_offset=47, id='trackers_to_find', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=49,
                                    col_offset=12,
                                    end_lineno=49,
                                    end_col_offset=77,
                                    value=Call(
                                        lineno=49,
                                        col_offset=12,
                                        end_lineno=49,
                                        end_col_offset=77,
                                        func=Attribute(
                                            lineno=49,
                                            col_offset=12,
                                            end_lineno=49,
                                            end_col_offset=27,
                                            value=Name(lineno=49, col_offset=12, end_lineno=49, end_col_offset=16, id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                lineno=49,
                                                col_offset=28,
                                                end_lineno=49,
                                                end_col_offset=76,
                                                func=Attribute(
                                                    lineno=49,
                                                    col_offset=28,
                                                    end_lineno=49,
                                                    end_col_offset=59,
                                                    value=Subscript(
                                                        lineno=49,
                                                        col_offset=28,
                                                        end_lineno=49,
                                                        end_col_offset=52,
                                                        value=Attribute(
                                                            lineno=49,
                                                            col_offset=28,
                                                            end_lineno=49,
                                                            end_col_offset=36,
                                                            value=Name(lineno=49, col_offset=28, end_lineno=49, end_col_offset=32, id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(lineno=49, col_offset=37, end_lineno=49, end_col_offset=51, value='link.tracker', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(lineno=49, col_offset=60, end_lineno=49, end_col_offset=75, id='tracker_to_find', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            lineno=51,
                            col_offset=8,
                            end_lineno=52,
                            end_col_offset=78,
                            target=Name(lineno=51, col_offset=12, end_lineno=51, end_col_offset=27, id='tracker_to_fail', ctx=Store()),
                            iter=Name(lineno=51, col_offset=31, end_lineno=51, end_col_offset=47, id='trackers_to_fail', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=52,
                                    col_offset=12,
                                    end_lineno=52,
                                    end_col_offset=78,
                                    value=Call(
                                        lineno=52,
                                        col_offset=12,
                                        end_lineno=52,
                                        end_col_offset=78,
                                        func=Attribute(
                                            lineno=52,
                                            col_offset=12,
                                            end_lineno=52,
                                            end_col_offset=28,
                                            value=Name(lineno=52, col_offset=12, end_lineno=52, end_col_offset=16, id='self', ctx=Load()),
                                            attr='assertFalse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                lineno=52,
                                                col_offset=29,
                                                end_lineno=52,
                                                end_col_offset=77,
                                                func=Attribute(
                                                    lineno=52,
                                                    col_offset=29,
                                                    end_lineno=52,
                                                    end_col_offset=60,
                                                    value=Subscript(
                                                        lineno=52,
                                                        col_offset=29,
                                                        end_lineno=52,
                                                        end_col_offset=53,
                                                        value=Attribute(
                                                            lineno=52,
                                                            col_offset=29,
                                                            end_lineno=52,
                                                            end_col_offset=37,
                                                            value=Name(lineno=52, col_offset=29, end_lineno=52, end_col_offset=33, id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(lineno=52, col_offset=38, end_lineno=52, end_col_offset=52, value='link.tracker', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(lineno=52, col_offset=61, end_lineno=52, end_col_offset=76, id='tracker_to_fail', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
