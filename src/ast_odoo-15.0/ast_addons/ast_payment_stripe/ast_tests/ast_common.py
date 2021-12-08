Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=58,
            module='odoo.addons.payment.tests.common',
            names=[alias(name='PaymentCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=18,
            end_col_offset=33,
            name='StripeCommon',
            bases=[Name(lineno=5, col_offset=19, end_lineno=5, end_col_offset=32, id='PaymentCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=8,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=33,
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=8, col_offset=19, end_lineno=8, end_col_offset=22, arg='cls', annotation=None, type_comment=None),
                            arg(lineno=8, col_offset=24, end_lineno=8, end_col_offset=42, arg='chart_template_ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=8, col_offset=43, end_lineno=8, end_col_offset=47, value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            lineno=9,
                            col_offset=8,
                            end_lineno=9,
                            end_col_offset=65,
                            value=Call(
                                lineno=9,
                                col_offset=8,
                                end_lineno=9,
                                end_col_offset=65,
                                func=Attribute(
                                    lineno=9,
                                    col_offset=8,
                                    end_lineno=9,
                                    end_col_offset=26,
                                    value=Call(
                                        lineno=9,
                                        col_offset=8,
                                        end_lineno=9,
                                        end_col_offset=15,
                                        func=Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=13, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=9,
                                        col_offset=27,
                                        end_lineno=9,
                                        end_col_offset=64,
                                        arg='chart_template_ref',
                                        value=Name(lineno=9, col_offset=46, end_lineno=9, end_col_offset=64, id='chart_template_ref', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=10,
                            targets=[
                                Attribute(
                                    lineno=11,
                                    col_offset=8,
                                    end_lineno=11,
                                    end_col_offset=18,
                                    value=Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='stripe',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=11,
                                col_offset=21,
                                end_lineno=16,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=21,
                                    end_lineno=11,
                                    end_col_offset=42,
                                    value=Name(lineno=11, col_offset=21, end_lineno=11, end_col_offset=24, id='cls', ctx=Load()),
                                    attr='_prepare_acquirer',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=11, col_offset=43, end_lineno=11, end_col_offset=51, value='stripe', kind=None)],
                                keywords=[
                                    keyword(
                                        lineno=11,
                                        col_offset=53,
                                        end_lineno=16,
                                        end_col_offset=9,
                                        arg='update_values',
                                        value=Dict(
                                            lineno=11,
                                            col_offset=67,
                                            end_lineno=16,
                                            end_col_offset=9,
                                            keys=[
                                                Constant(lineno=12, col_offset=12, end_lineno=12, end_col_offset=31, value='stripe_secret_key', kind=None),
                                                Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=36, value='stripe_publishable_key', kind=None),
                                                Constant(lineno=14, col_offset=12, end_lineno=14, end_col_offset=35, value='stripe_webhook_secret', kind=None),
                                                Constant(lineno=15, col_offset=12, end_lineno=15, end_col_offset=30, value='payment_icon_ids', kind=None),
                                            ],
                                            values=[
                                                Constant(lineno=12, col_offset=33, end_lineno=12, end_col_offset=67, value='sk_test_KJtHgNwt2KS3xM7QJPr4O5E8', kind=None),
                                                Constant(lineno=13, col_offset=38, end_lineno=13, end_col_offset=72, value='pk_test_QSPnimmb4ZhtkEy3Uhdm4S6J', kind=None),
                                                Constant(lineno=14, col_offset=37, end_lineno=14, end_col_offset=77, value='whsec_vG1fL6CMUouQ7cObF2VJprLVXT5jBLxB', kind=None),
                                                List(
                                                    lineno=15,
                                                    col_offset=32,
                                                    end_lineno=15,
                                                    end_col_offset=43,
                                                    elts=[
                                                        Tuple(
                                                            lineno=15,
                                                            col_offset=33,
                                                            end_lineno=15,
                                                            end_col_offset=42,
                                                            elts=[
                                                                Constant(lineno=15, col_offset=34, end_lineno=15, end_col_offset=35, value=5, kind=None),
                                                                Constant(lineno=15, col_offset=37, end_lineno=15, end_col_offset=38, value=0, kind=None),
                                                                Constant(lineno=15, col_offset=40, end_lineno=15, end_col_offset=41, value=0, kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
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
                            end_col_offset=33,
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
                                end_col_offset=33,
                                value=Name(lineno=18, col_offset=23, end_lineno=18, end_col_offset=26, id='cls', ctx=Load()),
                                attr='stripe',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(lineno=7, col_offset=5, end_lineno=7, end_col_offset=16, id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)