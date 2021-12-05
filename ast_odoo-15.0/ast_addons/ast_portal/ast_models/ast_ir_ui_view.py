Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=59,
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='url_for', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=36,
            module='odoo.tools',
            names=[alias(name='is_html_empty', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=10,
            col_offset=0,
            end_lineno=30,
            end_col_offset=23,
            name='View',
            bases=[
                Attribute(
                    lineno=10,
                    col_offset=11,
                    end_lineno=10,
                    end_col_offset=23,
                    value=Name(lineno=10, col_offset=11, end_lineno=10, end_col_offset=17, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=27,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=11, col_offset=15, end_lineno=11, end_col_offset=27, value='ir.ui.view', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=78,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=18, id='customize_show', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=21,
                        end_lineno=13,
                        end_col_offset=78,
                        func=Attribute(
                            lineno=13,
                            col_offset=21,
                            end_lineno=13,
                            end_col_offset=35,
                            value=Name(lineno=13, col_offset=21, end_lineno=13, end_col_offset=27, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=36, end_lineno=13, end_col_offset=62, value='Show As Optional Inherit', kind=None)],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=64,
                                end_lineno=13,
                                end_col_offset=77,
                                arg='default',
                                value=Constant(lineno=13, col_offset=72, end_lineno=13, end_col_offset=77, value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=23,
                    name='_prepare_qcontext',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=26, end_lineno=16, end_col_offset=30, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=17,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=11,
                            value=Constant(lineno=17, col_offset=8, end_lineno=19, end_col_offset=11, value=' Returns the qcontext : rendering context with portal specific value (required\n            to render portal layout template)\n        ', kind=None),
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=56,
                            targets=[Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=16, id='qcontext', ctx=Store())],
                            value=Call(
                                lineno=20,
                                col_offset=19,
                                end_lineno=20,
                                end_col_offset=56,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=19,
                                    end_lineno=20,
                                    end_col_offset=54,
                                    value=Call(
                                        lineno=20,
                                        col_offset=19,
                                        end_lineno=20,
                                        end_col_offset=36,
                                        func=Name(lineno=20, col_offset=19, end_lineno=20, end_col_offset=24, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=20, col_offset=25, end_lineno=20, end_col_offset=29, id='View', ctx=Load()),
                                            Name(lineno=20, col_offset=31, end_lineno=20, end_col_offset=35, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_qcontext',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=21,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=14,
                            test=BoolOp(
                                lineno=21,
                                col_offset=11,
                                end_lineno=21,
                                end_col_offset=61,
                                op=And(),
                                values=[
                                    Name(lineno=21, col_offset=11, end_lineno=21, end_col_offset=18, id='request', ctx=Load()),
                                    Call(
                                        lineno=21,
                                        col_offset=23,
                                        end_lineno=21,
                                        end_col_offset=61,
                                        func=Name(lineno=21, col_offset=23, end_lineno=21, end_col_offset=30, id='getattr', ctx=Load()),
                                        args=[
                                            Name(lineno=21, col_offset=31, end_lineno=21, end_col_offset=38, id='request', ctx=Load()),
                                            Constant(lineno=21, col_offset=40, end_lineno=21, end_col_offset=53, value='is_frontend', kind=None),
                                            Constant(lineno=21, col_offset=55, end_lineno=21, end_col_offset=60, value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=42,
                                    targets=[Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=16, id='Lang', ctx=Store())],
                                    value=Subscript(
                                        lineno=22,
                                        col_offset=19,
                                        end_lineno=22,
                                        end_col_offset=42,
                                        value=Attribute(
                                            lineno=22,
                                            col_offset=19,
                                            end_lineno=22,
                                            end_col_offset=30,
                                            value=Name(lineno=22, col_offset=19, end_lineno=22, end_col_offset=26, id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=22, col_offset=31, end_lineno=22, end_col_offset=41, value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=23,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=75,
                                    targets=[Name(lineno=23, col_offset=12, end_lineno=23, end_col_offset=28, id='portal_lang_code', ctx=Store())],
                                    value=Call(
                                        lineno=23,
                                        col_offset=31,
                                        end_lineno=23,
                                        end_col_offset=75,
                                        func=Attribute(
                                            lineno=23,
                                            col_offset=31,
                                            end_lineno=23,
                                            end_col_offset=73,
                                            value=Subscript(
                                                lineno=23,
                                                col_offset=31,
                                                end_lineno=23,
                                                end_col_offset=53,
                                                value=Attribute(
                                                    lineno=23,
                                                    col_offset=31,
                                                    end_lineno=23,
                                                    end_col_offset=42,
                                                    value=Name(lineno=23, col_offset=31, end_lineno=23, end_col_offset=38, id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=23, col_offset=43, end_lineno=23, end_col_offset=52, value='ir.http', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_frontend_langs',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    lineno=24,
                                    col_offset=12,
                                    end_lineno=29,
                                    end_col_offset=14,
                                    value=Call(
                                        lineno=24,
                                        col_offset=12,
                                        end_lineno=29,
                                        end_col_offset=14,
                                        func=Attribute(
                                            lineno=24,
                                            col_offset=12,
                                            end_lineno=24,
                                            end_col_offset=27,
                                            value=Name(lineno=24, col_offset=12, end_lineno=24, end_col_offset=20, id='qcontext', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                lineno=24,
                                                col_offset=28,
                                                end_lineno=29,
                                                end_col_offset=13,
                                                func=Name(lineno=24, col_offset=28, end_lineno=24, end_col_offset=32, id='dict', ctx=Load()),
                                                args=[
                                                    Call(
                                                        lineno=25,
                                                        col_offset=16,
                                                        end_lineno=25,
                                                        end_col_offset=36,
                                                        func=Attribute(
                                                            lineno=25,
                                                            col_offset=16,
                                                            end_lineno=25,
                                                            end_col_offset=34,
                                                            value=Attribute(
                                                                lineno=25,
                                                                col_offset=16,
                                                                end_lineno=25,
                                                                end_col_offset=29,
                                                                value=Name(lineno=25, col_offset=16, end_lineno=25, end_col_offset=20, id='self', ctx=Load()),
                                                                attr='_context',
                                                                ctx=Load(),
                                                            ),
                                                            attr='copy',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        lineno=26,
                                                        col_offset=16,
                                                        end_lineno=26,
                                                        end_col_offset=96,
                                                        arg='languages',
                                                        value=ListComp(
                                                            lineno=26,
                                                            col_offset=26,
                                                            end_lineno=26,
                                                            end_col_offset=96,
                                                            elt=Name(lineno=26, col_offset=27, end_lineno=26, end_col_offset=31, id='lang', ctx=Load()),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(lineno=26, col_offset=36, end_lineno=26, end_col_offset=40, id='lang', ctx=Store()),
                                                                    iter=Call(
                                                                        lineno=26,
                                                                        col_offset=44,
                                                                        end_lineno=26,
                                                                        end_col_offset=64,
                                                                        func=Attribute(
                                                                            lineno=26,
                                                                            col_offset=44,
                                                                            end_lineno=26,
                                                                            end_col_offset=62,
                                                                            value=Name(lineno=26, col_offset=44, end_lineno=26, end_col_offset=48, id='Lang', ctx=Load()),
                                                                            attr='get_available',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    ifs=[
                                                                        Compare(
                                                                            lineno=26,
                                                                            col_offset=68,
                                                                            end_lineno=26,
                                                                            end_col_offset=95,
                                                                            left=Subscript(
                                                                                lineno=26,
                                                                                col_offset=68,
                                                                                end_lineno=26,
                                                                                end_col_offset=75,
                                                                                value=Name(lineno=26, col_offset=68, end_lineno=26, end_col_offset=72, id='lang', ctx=Load()),
                                                                                slice=Constant(lineno=26, col_offset=73, end_lineno=26, end_col_offset=74, value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[In()],
                                                                            comparators=[Name(lineno=26, col_offset=79, end_lineno=26, end_col_offset=95, id='portal_lang_code', ctx=Load())],
                                                                        ),
                                                                    ],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        lineno=27,
                                                        col_offset=16,
                                                        end_lineno=27,
                                                        end_col_offset=31,
                                                        arg='url_for',
                                                        value=Name(lineno=27, col_offset=24, end_lineno=27, end_col_offset=31, id='url_for', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        lineno=28,
                                                        col_offset=16,
                                                        end_lineno=28,
                                                        end_col_offset=43,
                                                        arg='is_html_empty',
                                                        value=Name(lineno=28, col_offset=30, end_lineno=28, end_col_offset=43, id='is_html_empty', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=23,
                            value=Name(lineno=30, col_offset=15, end_lineno=30, end_col_offset=23, id='qcontext', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=15,
                            col_offset=5,
                            end_lineno=15,
                            end_col_offset=14,
                            value=Name(lineno=15, col_offset=5, end_lineno=15, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
