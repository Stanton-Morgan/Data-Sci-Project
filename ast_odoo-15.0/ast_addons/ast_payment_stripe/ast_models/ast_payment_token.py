Module(
    body=[
        Import(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=14,
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=13,
            names=[alias(name='pprint', asname=None)],
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=34,
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=43,
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        Assign(
            lineno=9,
            col_offset=0,
            end_lineno=9,
            end_col_offset=37,
            targets=[Name(lineno=9, col_offset=0, end_lineno=9, end_col_offset=7, id='_logger', ctx=Store())],
            value=Call(
                lineno=9,
                col_offset=10,
                end_lineno=9,
                end_col_offset=37,
                func=Attribute(
                    lineno=9,
                    col_offset=10,
                    end_lineno=9,
                    end_col_offset=27,
                    value=Name(lineno=9, col_offset=10, end_lineno=9, end_col_offset=17, id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(lineno=9, col_offset=28, end_lineno=9, end_col_offset=36, id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            lineno=12,
            col_offset=0,
            end_lineno=50,
            end_col_offset=70,
            name='PaymentToken',
            bases=[
                Attribute(
                    lineno=12,
                    col_offset=19,
                    end_lineno=12,
                    end_col_offset=31,
                    value=Name(lineno=12, col_offset=19, end_lineno=12, end_col_offset=25, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=30,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=13, col_offset=15, end_lineno=13, end_col_offset=30, value='payment.token', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=89,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=25, id='stripe_payment_method', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=28,
                        end_lineno=15,
                        end_col_offset=89,
                        func=Attribute(
                            lineno=15,
                            col_offset=28,
                            end_lineno=15,
                            end_col_offset=39,
                            value=Name(lineno=15, col_offset=28, end_lineno=15, end_col_offset=34, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=40,
                                end_lineno=15,
                                end_col_offset=73,
                                arg='string',
                                value=Constant(lineno=15, col_offset=47, end_lineno=15, end_col_offset=73, value='Stripe Payment Method ID', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=75,
                                end_lineno=15,
                                end_col_offset=88,
                                arg='readonly',
                                value=Constant(lineno=15, col_offset=84, end_lineno=15, end_col_offset=88, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=17,
                    col_offset=4,
                    end_lineno=50,
                    end_col_offset=70,
                    name='_stripe_sca_migrate_customer',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=17, col_offset=37, end_lineno=17, end_col_offset=41, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=29,
                            end_col_offset=11,
                            value=Constant(lineno=18, col_offset=8, end_lineno=29, end_col_offset=11, value=' Migrate a token from the old implementation of Stripe to the SCA-compliant one.\n\n        In the old implementation, it was possible to create a Charge by giving only the customer id\n        and let Stripe use the default source (= default payment method). Stripe now requires to\n        specify the payment method for each new PaymentIntent. To do so, we fetch the payment method\n        associated to a customer and save its id on the token.\n        This migration happens once per token created with the old implementation.\n\n        Note: self.ensure_one()\n\n        :return: None\n        ', kind=None),
                        ),
                        Expr(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=25,
                            value=Call(
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=23,
                                    value=Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=33,
                            col_offset=8,
                            end_lineno=41,
                            end_col_offset=9,
                            targets=[Name(lineno=33, col_offset=8, end_lineno=33, end_col_offset=24, id='response_content', ctx=Store())],
                            value=Call(
                                lineno=33,
                                col_offset=27,
                                end_lineno=41,
                                end_col_offset=9,
                                func=Attribute(
                                    lineno=33,
                                    col_offset=27,
                                    end_lineno=33,
                                    end_col_offset=64,
                                    value=Attribute(
                                        lineno=33,
                                        col_offset=27,
                                        end_lineno=33,
                                        end_col_offset=43,
                                        value=Name(lineno=33, col_offset=27, end_lineno=33, end_col_offset=31, id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                    attr='_stripe_make_request',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=34, col_offset=12, end_lineno=34, end_col_offset=29, value='payment_methods', kind=None)],
                                keywords=[
                                    keyword(
                                        lineno=35,
                                        col_offset=12,
                                        end_lineno=39,
                                        end_col_offset=13,
                                        arg='payload',
                                        value=Dict(
                                            lineno=35,
                                            col_offset=20,
                                            end_lineno=39,
                                            end_col_offset=13,
                                            keys=[
                                                Constant(lineno=36, col_offset=16, end_lineno=36, end_col_offset=26, value='customer', kind=None),
                                                Constant(lineno=37, col_offset=16, end_lineno=37, end_col_offset=22, value='type', kind=None),
                                                Constant(lineno=38, col_offset=16, end_lineno=38, end_col_offset=23, value='limit', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    lineno=36,
                                                    col_offset=28,
                                                    end_lineno=36,
                                                    end_col_offset=45,
                                                    value=Name(lineno=36, col_offset=28, end_lineno=36, end_col_offset=32, id='self', ctx=Load()),
                                                    attr='acquirer_ref',
                                                    ctx=Load(),
                                                ),
                                                Constant(lineno=37, col_offset=24, end_lineno=37, end_col_offset=30, value='card', kind=None),
                                                Constant(lineno=38, col_offset=25, end_lineno=38, end_col_offset=26, value=1, kind=None),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        lineno=40,
                                        col_offset=12,
                                        end_lineno=40,
                                        end_col_offset=24,
                                        arg='method',
                                        value=Constant(lineno=40, col_offset=19, end_lineno=40, end_col_offset=24, value='GET', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=42,
                            col_offset=8,
                            end_lineno=42,
                            end_col_offset=96,
                            value=Call(
                                lineno=42,
                                col_offset=8,
                                end_lineno=42,
                                end_col_offset=96,
                                func=Attribute(
                                    lineno=42,
                                    col_offset=8,
                                    end_lineno=42,
                                    end_col_offset=20,
                                    value=Name(lineno=42, col_offset=8, end_lineno=42, end_col_offset=15, id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=42, col_offset=21, end_lineno=42, end_col_offset=61, value='received payment_methods response:\n%s', kind=None),
                                    Call(
                                        lineno=42,
                                        col_offset=63,
                                        end_lineno=42,
                                        end_col_offset=95,
                                        func=Attribute(
                                            lineno=42,
                                            col_offset=63,
                                            end_lineno=42,
                                            end_col_offset=77,
                                            value=Name(lineno=42, col_offset=63, end_lineno=42, end_col_offset=69, id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=42, col_offset=78, end_lineno=42, end_col_offset=94, id='response_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=45,
                            col_offset=8,
                            end_lineno=45,
                            end_col_offset=58,
                            targets=[Name(lineno=45, col_offset=8, end_lineno=45, end_col_offset=23, id='payment_methods', ctx=Store())],
                            value=Call(
                                lineno=45,
                                col_offset=26,
                                end_lineno=45,
                                end_col_offset=58,
                                func=Attribute(
                                    lineno=45,
                                    col_offset=26,
                                    end_lineno=45,
                                    end_col_offset=46,
                                    value=Name(lineno=45, col_offset=26, end_lineno=45, end_col_offset=42, id='response_content', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=45, col_offset=47, end_lineno=45, end_col_offset=53, value='data', kind=None),
                                    List(lineno=45, col_offset=55, end_lineno=45, end_col_offset=57, elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=46,
                            col_offset=8,
                            end_lineno=46,
                            end_col_offset=76,
                            targets=[Name(lineno=46, col_offset=8, end_lineno=46, end_col_offset=25, id='payment_method_id', ctx=Store())],
                            value=BoolOp(
                                lineno=46,
                                col_offset=28,
                                end_lineno=46,
                                end_col_offset=76,
                                op=And(),
                                values=[
                                    Name(lineno=46, col_offset=28, end_lineno=46, end_col_offset=43, id='payment_methods', ctx=Load()),
                                    Call(
                                        lineno=46,
                                        col_offset=48,
                                        end_lineno=46,
                                        end_col_offset=76,
                                        func=Attribute(
                                            lineno=46,
                                            col_offset=48,
                                            end_lineno=46,
                                            end_col_offset=70,
                                            value=Subscript(
                                                lineno=46,
                                                col_offset=48,
                                                end_lineno=46,
                                                end_col_offset=66,
                                                value=Name(lineno=46, col_offset=48, end_lineno=46, end_col_offset=63, id='payment_methods', ctx=Load()),
                                                slice=Constant(lineno=46, col_offset=64, end_lineno=46, end_col_offset=65, value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=46, col_offset=71, end_lineno=46, end_col_offset=75, value='id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=47,
                            col_offset=8,
                            end_lineno=48,
                            end_col_offset=96,
                            test=UnaryOp(
                                lineno=47,
                                col_offset=11,
                                end_lineno=47,
                                end_col_offset=32,
                                op=Not(),
                                operand=Name(lineno=47, col_offset=15, end_lineno=47, end_col_offset=32, id='payment_method_id', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    lineno=48,
                                    col_offset=12,
                                    end_lineno=48,
                                    end_col_offset=96,
                                    exc=Call(
                                        lineno=48,
                                        col_offset=18,
                                        end_lineno=48,
                                        end_col_offset=96,
                                        func=Name(lineno=48, col_offset=18, end_lineno=48, end_col_offset=33, id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                lineno=48,
                                                col_offset=34,
                                                end_lineno=48,
                                                end_col_offset=95,
                                                left=Constant(lineno=48, col_offset=34, end_lineno=48, end_col_offset=44, value='Stripe: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    lineno=48,
                                                    col_offset=47,
                                                    end_lineno=48,
                                                    end_col_offset=95,
                                                    func=Name(lineno=48, col_offset=47, end_lineno=48, end_col_offset=48, id='_', ctx=Load()),
                                                    args=[Constant(lineno=48, col_offset=49, end_lineno=48, end_col_offset=94, value='Unable to convert payment token to new API.', kind=None)],
                                                    keywords=[],
                                                ),
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
                            lineno=49,
                            col_offset=8,
                            end_lineno=49,
                            end_col_offset=54,
                            targets=[
                                Attribute(
                                    lineno=49,
                                    col_offset=8,
                                    end_lineno=49,
                                    end_col_offset=34,
                                    value=Name(lineno=49, col_offset=8, end_lineno=49, end_col_offset=12, id='self', ctx=Load()),
                                    attr='stripe_payment_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(lineno=49, col_offset=37, end_lineno=49, end_col_offset=54, id='payment_method_id', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=50,
                            col_offset=8,
                            end_lineno=50,
                            end_col_offset=70,
                            value=Call(
                                lineno=50,
                                col_offset=8,
                                end_lineno=50,
                                end_col_offset=70,
                                func=Attribute(
                                    lineno=50,
                                    col_offset=8,
                                    end_lineno=50,
                                    end_col_offset=20,
                                    value=Name(lineno=50, col_offset=8, end_lineno=50, end_col_offset=15, id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=50, col_offset=21, end_lineno=50, end_col_offset=60, value='converted token with id %s to new API', kind=None),
                                    Attribute(
                                        lineno=50,
                                        col_offset=62,
                                        end_lineno=50,
                                        end_col_offset=69,
                                        value=Name(lineno=50, col_offset=62, end_lineno=50, end_col_offset=66, id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
