Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=58,
            module='odoo.addons.payment.tests.common',
            names=[alias(name='PaymentCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=19,
            end_col_offset=40,
            name='BuckarooCommon',
            bases=[Name(lineno=6, col_offset=21, end_lineno=6, end_col_offset=34, id='PaymentCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=40,
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=9, col_offset=19, end_lineno=9, end_col_offset=22, arg='cls', annotation=None, type_comment=None),
                            arg(lineno=9, col_offset=24, end_lineno=9, end_col_offset=42, arg='chart_template_ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=9, col_offset=43, end_lineno=9, end_col_offset=47, value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            lineno=10,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=65,
                            value=Call(
                                lineno=10,
                                col_offset=8,
                                end_lineno=10,
                                end_col_offset=65,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=8,
                                    end_lineno=10,
                                    end_col_offset=26,
                                    value=Call(
                                        lineno=10,
                                        col_offset=8,
                                        end_lineno=10,
                                        end_col_offset=15,
                                        func=Name(lineno=10, col_offset=8, end_lineno=10, end_col_offset=13, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=10,
                                        col_offset=27,
                                        end_lineno=10,
                                        end_col_offset=64,
                                        arg='chart_template_ref',
                                        value=Name(lineno=10, col_offset=46, end_lineno=10, end_col_offset=64, id='chart_template_ref', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=10,
                            targets=[
                                Attribute(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=20,
                                    value=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='buckaroo',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=12,
                                col_offset=23,
                                end_lineno=15,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=23,
                                    end_lineno=12,
                                    end_col_offset=44,
                                    value=Name(lineno=12, col_offset=23, end_lineno=12, end_col_offset=26, id='cls', ctx=Load()),
                                    attr='_prepare_acquirer',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=12, col_offset=45, end_lineno=12, end_col_offset=55, value='buckaroo', kind=None)],
                                keywords=[
                                    keyword(
                                        lineno=12,
                                        col_offset=57,
                                        end_lineno=15,
                                        end_col_offset=9,
                                        arg='update_values',
                                        value=Dict(
                                            lineno=12,
                                            col_offset=71,
                                            end_lineno=15,
                                            end_col_offset=9,
                                            keys=[
                                                Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=34, value='buckaroo_website_key', kind=None),
                                                Constant(lineno=14, col_offset=12, end_lineno=14, end_col_offset=33, value='buckaroo_secret_key', kind=None),
                                            ],
                                            values=[
                                                Constant(lineno=13, col_offset=36, end_lineno=13, end_col_offset=43, value='dummy', kind=None),
                                                Constant(lineno=14, col_offset=35, end_lineno=14, end_col_offset=42, value='dummy', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=35,
                            targets=[
                                Attribute(
                                    lineno=18,
                                    col_offset=8,
                                    end_lineno=18,
                                    end_col_offset=20,
                                    value=Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='acquirer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                lineno=18,
                                col_offset=23,
                                end_lineno=18,
                                end_col_offset=35,
                                value=Name(lineno=18, col_offset=23, end_lineno=18, end_col_offset=26, id='cls', ctx=Load()),
                                attr='buckaroo',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=40,
                            targets=[
                                Attribute(
                                    lineno=19,
                                    col_offset=8,
                                    end_lineno=19,
                                    end_col_offset=20,
                                    value=Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='currency',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                lineno=19,
                                col_offset=23,
                                end_lineno=19,
                                end_col_offset=40,
                                value=Name(lineno=19, col_offset=23, end_lineno=19, end_col_offset=26, id='cls', ctx=Load()),
                                attr='currency_euro',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(lineno=8, col_offset=5, end_lineno=8, end_col_offset=16, id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)