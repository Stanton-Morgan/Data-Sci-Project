Module(
    body=[
        Expr(
            lineno=2,
            col_offset=0,
            end_lineno=5,
            end_col_offset=3,
            value=Constant(lineno=2, col_offset=0, end_lineno=5, end_col_offset=3, value='Classes extending the populate factory for Companies and related models.\n\nOnly adding specificities of basic accounting applications.\n', kind=None),
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=26,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=31,
            module='odoo.tools',
            names=[alias(name='populate', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=37,
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        Import(
            lineno=10,
            col_offset=0,
            end_lineno=10,
            end_col_offset=14,
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            lineno=11,
            col_offset=0,
            end_lineno=11,
            end_col_offset=31,
            module='functools',
            names=[alias(name='lru_cache', asname=None)],
            level=0,
        ),
        Assign(
            lineno=13,
            col_offset=0,
            end_lineno=13,
            end_col_offset=37,
            targets=[Name(lineno=13, col_offset=0, end_lineno=13, end_col_offset=7, id='_logger', ctx=Store())],
            value=Call(
                lineno=13,
                col_offset=10,
                end_lineno=13,
                end_col_offset=37,
                func=Attribute(
                    lineno=13,
                    col_offset=10,
                    end_lineno=13,
                    end_col_offset=27,
                    value=Name(lineno=13, col_offset=10, end_lineno=13, end_col_offset=17, id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(lineno=13, col_offset=28, end_lineno=13, end_col_offset=36, id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            lineno=16,
            col_offset=0,
            end_lineno=55,
            end_col_offset=22,
            name='ResCompany',
            bases=[
                Attribute(
                    lineno=16,
                    col_offset=17,
                    end_lineno=16,
                    end_col_offset=29,
                    value=Name(lineno=16, col_offset=17, end_lineno=16, end_col_offset=23, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=80,
                    value=Constant(lineno=17, col_offset=4, end_lineno=17, end_col_offset=80, value='Populate factory part for the accountings applications of res.company.', kind=None),
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=28,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=19, col_offset=15, end_lineno=19, end_col_offset=28, value='res.company', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=55,
                    end_col_offset=22,
                    name='_populate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=21, col_offset=18, end_lineno=21, end_col_offset=22, arg='self', annotation=None, type_comment=None),
                            arg(lineno=21, col_offset=24, end_lineno=21, end_col_offset=28, arg='size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            lineno=23,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=97,
                            name='search_coa_ids',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(lineno=23, col_offset=27, end_lineno=23, end_col_offset=38, arg='currency_id', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    lineno=24,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=97,
                                    value=Call(
                                        lineno=24,
                                        col_offset=19,
                                        end_lineno=24,
                                        end_col_offset=97,
                                        func=Attribute(
                                            lineno=24,
                                            col_offset=19,
                                            end_lineno=24,
                                            end_col_offset=60,
                                            value=Subscript(
                                                lineno=24,
                                                col_offset=19,
                                                end_lineno=24,
                                                end_col_offset=53,
                                                value=Attribute(
                                                    lineno=24,
                                                    col_offset=19,
                                                    end_lineno=24,
                                                    end_col_offset=27,
                                                    value=Name(lineno=24, col_offset=19, end_lineno=24, end_col_offset=23, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=24, col_offset=28, end_lineno=24, end_col_offset=52, value='account.chart.template', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                lineno=24,
                                                col_offset=61,
                                                end_lineno=24,
                                                end_col_offset=96,
                                                elts=[
                                                    Tuple(
                                                        lineno=24,
                                                        col_offset=62,
                                                        end_lineno=24,
                                                        end_col_offset=95,
                                                        elts=[
                                                            Constant(lineno=24, col_offset=63, end_lineno=24, end_col_offset=76, value='currency_id', kind=None),
                                                            Constant(lineno=24, col_offset=78, end_lineno=24, end_col_offset=81, value='=', kind=None),
                                                            Name(lineno=24, col_offset=83, end_lineno=24, end_col_offset=94, id='currency_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    lineno=22,
                                    col_offset=9,
                                    end_lineno=22,
                                    end_col_offset=20,
                                    func=Name(lineno=22, col_offset=9, end_lineno=22, end_col_offset=18, id='lru_cache', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=41,
                            targets=[Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=15, id='records', ctx=Store())],
                            value=Call(
                                lineno=26,
                                col_offset=18,
                                end_lineno=26,
                                end_col_offset=41,
                                func=Attribute(
                                    lineno=26,
                                    col_offset=18,
                                    end_lineno=26,
                                    end_col_offset=35,
                                    value=Call(
                                        lineno=26,
                                        col_offset=18,
                                        end_lineno=26,
                                        end_col_offset=25,
                                        func=Name(lineno=26, col_offset=18, end_lineno=26, end_col_offset=23, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_populate',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=26, col_offset=36, end_lineno=26, end_col_offset=40, id='size', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=27,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=46,
                            value=Call(
                                lineno=27,
                                col_offset=8,
                                end_lineno=27,
                                end_col_offset=46,
                                func=Attribute(
                                    lineno=27,
                                    col_offset=8,
                                    end_lineno=27,
                                    end_col_offset=20,
                                    value=Name(lineno=27, col_offset=8, end_lineno=27, end_col_offset=15, id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=27, col_offset=21, end_lineno=27, end_col_offset=45, value='Loading Chart Template', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=28,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=88,
                            targets=[Name(lineno=28, col_offset=8, end_lineno=28, end_col_offset=31, id='default_chart_templates', ctx=Store())],
                            value=Call(
                                lineno=28,
                                col_offset=34,
                                end_lineno=28,
                                end_col_offset=88,
                                func=Attribute(
                                    lineno=28,
                                    col_offset=34,
                                    end_lineno=28,
                                    end_col_offset=75,
                                    value=Subscript(
                                        lineno=28,
                                        col_offset=34,
                                        end_lineno=28,
                                        end_col_offset=68,
                                        value=Attribute(
                                            lineno=28,
                                            col_offset=34,
                                            end_lineno=28,
                                            end_col_offset=42,
                                            value=Name(lineno=28, col_offset=34, end_lineno=28, end_col_offset=38, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=28, col_offset=43, end_lineno=28, end_col_offset=67, value='account.chart.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(lineno=28, col_offset=76, end_lineno=28, end_col_offset=78, elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        lineno=28,
                                        col_offset=80,
                                        end_lineno=28,
                                        end_col_offset=87,
                                        arg='limit',
                                        value=Constant(lineno=28, col_offset=86, end_lineno=28, end_col_offset=87, value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=29,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=14,
                            test=UnaryOp(
                                lineno=29,
                                col_offset=11,
                                end_lineno=29,
                                end_col_offset=38,
                                op=Not(),
                                operand=Name(lineno=29, col_offset=15, end_lineno=29, end_col_offset=38, id='default_chart_templates', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    lineno=31,
                                    col_offset=12,
                                    end_lineno=34,
                                    end_col_offset=14,
                                    exc=Call(
                                        lineno=31,
                                        col_offset=18,
                                        end_lineno=34,
                                        end_col_offset=14,
                                        func=Name(lineno=31, col_offset=18, end_lineno=31, end_col_offset=27, id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=31,
                                                col_offset=28,
                                                end_lineno=34,
                                                end_col_offset=13,
                                                func=Name(lineno=31, col_offset=28, end_lineno=31, end_col_offset=29, id='_', ctx=Load()),
                                                args=[Constant(lineno=32, col_offset=16, end_lineno=33, end_col_offset=42, value='At least one localization is needed to be installed in order to populate the database with accounting', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=35,
                            col_offset=8,
                            end_lineno=35,
                            end_col_offset=71,
                            targets=[Name(lineno=35, col_offset=8, end_lineno=35, end_col_offset=14, id='random', ctx=Store())],
                            value=Call(
                                lineno=35,
                                col_offset=17,
                                end_lineno=35,
                                end_col_offset=71,
                                func=Attribute(
                                    lineno=35,
                                    col_offset=17,
                                    end_lineno=35,
                                    end_col_offset=32,
                                    value=Name(lineno=35, col_offset=17, end_lineno=35, end_col_offset=25, id='populate', ctx=Load()),
                                    attr='Random',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=35, col_offset=33, end_lineno=35, end_col_offset=70, value='res.company+chart_template_selector', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=52,
                            col_offset=8,
                            end_lineno=54,
                            end_col_offset=85,
                            target=Name(lineno=52, col_offset=12, end_lineno=52, end_col_offset=19, id='company', ctx=Store()),
                            iter=Subscript(
                                lineno=52,
                                col_offset=23,
                                end_lineno=52,
                                end_col_offset=34,
                                value=Name(lineno=52, col_offset=23, end_lineno=52, end_col_offset=30, id='records', ctx=Load()),
                                slice=Slice(
                                    lineno=52,
                                    col_offset=31,
                                    end_lineno=52,
                                    end_col_offset=33,
                                    lower=None,
                                    upper=Constant(lineno=52, col_offset=32, end_lineno=52, end_col_offset=33, value=3, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    lineno=53,
                                    col_offset=12,
                                    end_lineno=53,
                                    end_col_offset=99,
                                    targets=[Name(lineno=53, col_offset=12, end_lineno=53, end_col_offset=31, id='chart_templates_cur', ctx=Store())],
                                    value=BoolOp(
                                        lineno=53,
                                        col_offset=34,
                                        end_lineno=53,
                                        end_col_offset=99,
                                        op=Or(),
                                        values=[
                                            Call(
                                                lineno=53,
                                                col_offset=34,
                                                end_lineno=53,
                                                end_col_offset=72,
                                                func=Name(lineno=53, col_offset=34, end_lineno=53, end_col_offset=48, id='search_coa_ids', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        lineno=53,
                                                        col_offset=49,
                                                        end_lineno=53,
                                                        end_col_offset=71,
                                                        value=Attribute(
                                                            lineno=53,
                                                            col_offset=49,
                                                            end_lineno=53,
                                                            end_col_offset=68,
                                                            value=Name(lineno=53, col_offset=49, end_lineno=53, end_col_offset=56, id='company', ctx=Load()),
                                                            attr='currency_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(lineno=53, col_offset=76, end_lineno=53, end_col_offset=99, id='default_chart_templates', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    lineno=54,
                                    col_offset=12,
                                    end_lineno=54,
                                    end_col_offset=85,
                                    value=Call(
                                        lineno=54,
                                        col_offset=12,
                                        end_lineno=54,
                                        end_col_offset=85,
                                        func=Attribute(
                                            lineno=54,
                                            col_offset=12,
                                            end_lineno=54,
                                            end_col_offset=83,
                                            value=Call(
                                                lineno=54,
                                                col_offset=12,
                                                end_lineno=54,
                                                end_col_offset=71,
                                                func=Attribute(
                                                    lineno=54,
                                                    col_offset=12,
                                                    end_lineno=54,
                                                    end_col_offset=59,
                                                    value=Call(
                                                        lineno=54,
                                                        col_offset=12,
                                                        end_lineno=54,
                                                        end_col_offset=46,
                                                        func=Attribute(
                                                            lineno=54,
                                                            col_offset=12,
                                                            end_lineno=54,
                                                            end_col_offset=25,
                                                            value=Name(lineno=54, col_offset=12, end_lineno=54, end_col_offset=18, id='random', ctx=Load()),
                                                            attr='choice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(lineno=54, col_offset=26, end_lineno=54, end_col_offset=45, id='chart_templates_cur', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='with_company',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        lineno=54,
                                                        col_offset=60,
                                                        end_lineno=54,
                                                        end_col_offset=70,
                                                        value=Name(lineno=54, col_offset=60, end_lineno=54, end_col_offset=67, id='company', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='try_loading',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=55,
                            col_offset=8,
                            end_lineno=55,
                            end_col_offset=22,
                            value=Name(lineno=55, col_offset=15, end_lineno=55, end_col_offset=22, id='records', ctx=Load()),
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
