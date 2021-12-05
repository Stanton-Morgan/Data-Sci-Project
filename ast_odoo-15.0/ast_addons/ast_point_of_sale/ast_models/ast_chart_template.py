Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=18,
            end_col_offset=21,
            name='AccountChartTemplate',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=27,
                    end_lineno=5,
                    end_col_offset=39,
                    value=Name(lineno=5, col_offset=27, end_lineno=5, end_col_offset=33, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=6,
                    col_offset=4,
                    end_lineno=6,
                    end_col_offset=39,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=6, col_offset=15, end_lineno=6, end_col_offset=39, value='account.chart.template', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=8,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=21,
                    name='_load',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=8, col_offset=14, end_lineno=8, end_col_offset=18, arg='self', annotation=None, type_comment=None),
                            arg(lineno=8, col_offset=20, end_lineno=8, end_col_offset=33, arg='sale_tax_rate', annotation=None, type_comment=None),
                            arg(lineno=8, col_offset=35, end_lineno=8, end_col_offset=52, arg='purchase_tax_rate', annotation=None, type_comment=None),
                            arg(lineno=8, col_offset=54, end_lineno=8, end_col_offset=61, arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=9,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=11,
                            value=Constant(lineno=9, col_offset=8, end_lineno=14, end_col_offset=11, value='Remove the payment methods that are created for the company before installing the chart of accounts.\n\n        Keeping these existing pos.payment.method records interferes with the installation of chart of accounts\n        because pos.payment.method model has fields linked to account.journal and account.account records that are\n        deleted during the loading of chart of accounts.\n        ', kind=None),
                        ),
                        Expr(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=89,
                            value=Call(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=89,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=8,
                                    end_lineno=15,
                                    end_col_offset=87,
                                    value=Call(
                                        lineno=15,
                                        col_offset=8,
                                        end_lineno=15,
                                        end_col_offset=80,
                                        func=Attribute(
                                            lineno=15,
                                            col_offset=8,
                                            end_lineno=15,
                                            end_col_offset=45,
                                            value=Subscript(
                                                lineno=15,
                                                col_offset=8,
                                                end_lineno=15,
                                                end_col_offset=38,
                                                value=Attribute(
                                                    lineno=15,
                                                    col_offset=8,
                                                    end_lineno=15,
                                                    end_col_offset=16,
                                                    value=Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=12, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=15, col_offset=17, end_lineno=15, end_col_offset=37, value='pos.payment.method', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                lineno=15,
                                                col_offset=46,
                                                end_lineno=15,
                                                end_col_offset=79,
                                                elts=[
                                                    Tuple(
                                                        lineno=15,
                                                        col_offset=47,
                                                        end_lineno=15,
                                                        end_col_offset=78,
                                                        elts=[
                                                            Constant(lineno=15, col_offset=48, end_lineno=15, end_col_offset=60, value='company_id', kind=None),
                                                            Constant(lineno=15, col_offset=62, end_lineno=15, end_col_offset=65, value='=', kind=None),
                                                            Attribute(
                                                                lineno=15,
                                                                col_offset=67,
                                                                end_lineno=15,
                                                                end_col_offset=77,
                                                                value=Name(lineno=15, col_offset=67, end_lineno=15, end_col_offset=74, id='company', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=99,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=14, id='result', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=17,
                                end_lineno=16,
                                end_col_offset=99,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=17,
                                    end_lineno=16,
                                    end_col_offset=56,
                                    value=Call(
                                        lineno=16,
                                        col_offset=17,
                                        end_lineno=16,
                                        end_col_offset=50,
                                        func=Name(lineno=16, col_offset=17, end_lineno=16, end_col_offset=22, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=16, col_offset=23, end_lineno=16, end_col_offset=43, id='AccountChartTemplate', ctx=Load()),
                                            Name(lineno=16, col_offset=45, end_lineno=16, end_col_offset=49, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_load',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=16, col_offset=57, end_lineno=16, end_col_offset=70, id='sale_tax_rate', ctx=Load()),
                                    Name(lineno=16, col_offset=72, end_lineno=16, end_col_offset=89, id='purchase_tax_rate', ctx=Load()),
                                    Name(lineno=16, col_offset=91, end_lineno=16, end_col_offset=98, id='company', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=79,
                            value=Call(
                                lineno=17,
                                col_offset=8,
                                end_lineno=17,
                                end_col_offset=79,
                                func=Attribute(
                                    lineno=17,
                                    col_offset=8,
                                    end_lineno=17,
                                    end_col_offset=60,
                                    value=Subscript(
                                        lineno=17,
                                        col_offset=8,
                                        end_lineno=17,
                                        end_col_offset=30,
                                        value=Attribute(
                                            lineno=17,
                                            col_offset=8,
                                            end_lineno=17,
                                            end_col_offset=16,
                                            value=Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=17, col_offset=17, end_lineno=17, end_col_offset=29, value='pos.config', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='post_install_pos_localisation',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=17,
                                        col_offset=61,
                                        end_lineno=17,
                                        end_col_offset=78,
                                        arg='companies',
                                        value=Name(lineno=17, col_offset=71, end_lineno=17, end_col_offset=78, id='company', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=21,
                            value=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=21, id='result', ctx=Load()),
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
