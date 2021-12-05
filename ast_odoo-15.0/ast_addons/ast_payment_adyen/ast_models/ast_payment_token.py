Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
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
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=54,
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=54,
            end_col_offset=99,
            name='PaymentToken',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=19,
                    end_lineno=7,
                    end_col_offset=31,
                    value=Name(lineno=7, col_offset=19, end_lineno=7, end_col_offset=25, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=30,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=30, value='payment.token', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=22,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=27, id='adyen_shopper_reference', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=30,
                        end_lineno=12,
                        end_col_offset=22,
                        func=Attribute(
                            lineno=10,
                            col_offset=30,
                            end_lineno=10,
                            end_col_offset=41,
                            value=Name(lineno=10, col_offset=30, end_lineno=10, end_col_offset=36, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=34,
                                arg='string',
                                value=Constant(lineno=11, col_offset=15, end_lineno=11, end_col_offset=34, value='Shopper Reference', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=36,
                                end_lineno=11,
                                end_col_offset=96,
                                arg='help',
                                value=Constant(lineno=11, col_offset=41, end_lineno=11, end_col_offset=96, value='The unique reference of the partner owning this token', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=21,
                                arg='readonly',
                                value=Constant(lineno=12, col_offset=17, end_lineno=12, end_col_offset=21, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=40,
                    end_col_offset=16,
                    name='_handle_deactivation_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=37, end_lineno=16, end_col_offset=41, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=22,
                            end_col_offset=11,
                            value=Constant(lineno=17, col_offset=8, end_lineno=22, end_col_offset=11, value=' Override of payment to request request Adyen to delete the token.\n\n        Note: self.ensure_one()\n\n        :return: None\n        ', kind=None),
                        ),
                        Expr(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=46,
                            value=Call(
                                lineno=23,
                                col_offset=8,
                                end_lineno=23,
                                end_col_offset=46,
                                func=Attribute(
                                    lineno=23,
                                    col_offset=8,
                                    end_lineno=23,
                                    end_col_offset=44,
                                    value=Call(
                                        lineno=23,
                                        col_offset=8,
                                        end_lineno=23,
                                        end_col_offset=15,
                                        func=Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=13, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_handle_deactivation_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            lineno=24,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=18,
                            test=Compare(
                                lineno=24,
                                col_offset=11,
                                end_lineno=24,
                                end_col_offset=35,
                                left=Attribute(
                                    lineno=24,
                                    col_offset=11,
                                    end_lineno=24,
                                    end_col_offset=24,
                                    value=Name(lineno=24, col_offset=11, end_lineno=24, end_col_offset=15, id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(lineno=24, col_offset=28, end_lineno=24, end_col_offset=35, value='adyen', kind=None)],
                            ),
                            body=[Return(lineno=25, col_offset=12, end_lineno=25, end_col_offset=18, value=None)],
                            orelse=[],
                        ),
                        Assign(
                            lineno=27,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=9,
                            targets=[Name(lineno=27, col_offset=8, end_lineno=27, end_col_offset=12, id='data', ctx=Store())],
                            value=Dict(
                                lineno=27,
                                col_offset=15,
                                end_lineno=31,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=28, col_offset=12, end_lineno=28, end_col_offset=29, value='merchantAccount', kind=None),
                                    Constant(lineno=29, col_offset=12, end_lineno=29, end_col_offset=30, value='shopperReference', kind=None),
                                    Constant(lineno=30, col_offset=12, end_lineno=30, end_col_offset=38, value='recurringDetailReference', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        lineno=28,
                                        col_offset=31,
                                        end_lineno=28,
                                        end_col_offset=70,
                                        value=Attribute(
                                            lineno=28,
                                            col_offset=31,
                                            end_lineno=28,
                                            end_col_offset=47,
                                            value=Name(lineno=28, col_offset=31, end_lineno=28, end_col_offset=35, id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='adyen_merchant_account',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=29,
                                        col_offset=32,
                                        end_lineno=29,
                                        end_col_offset=60,
                                        value=Name(lineno=29, col_offset=32, end_lineno=29, end_col_offset=36, id='self', ctx=Load()),
                                        attr='adyen_shopper_reference',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=30,
                                        col_offset=40,
                                        end_lineno=30,
                                        end_col_offset=57,
                                        value=Name(lineno=30, col_offset=40, end_lineno=30, end_col_offset=44, id='self', ctx=Load()),
                                        attr='acquirer_ref',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            lineno=32,
                            col_offset=8,
                            end_lineno=40,
                            end_col_offset=16,
                            body=[
                                Expr(
                                    lineno=33,
                                    col_offset=12,
                                    end_lineno=38,
                                    end_col_offset=13,
                                    value=Call(
                                        lineno=33,
                                        col_offset=12,
                                        end_lineno=38,
                                        end_col_offset=13,
                                        func=Attribute(
                                            lineno=33,
                                            col_offset=12,
                                            end_lineno=33,
                                            end_col_offset=48,
                                            value=Attribute(
                                                lineno=33,
                                                col_offset=12,
                                                end_lineno=33,
                                                end_col_offset=28,
                                                value=Name(lineno=33, col_offset=12, end_lineno=33, end_col_offset=16, id='self', ctx=Load()),
                                                attr='acquirer_id',
                                                ctx=Load(),
                                            ),
                                            attr='_adyen_make_request',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                lineno=34,
                                                col_offset=16,
                                                end_lineno=34,
                                                end_col_offset=56,
                                                arg='url_field_name',
                                                value=Constant(lineno=34, col_offset=31, end_lineno=34, end_col_offset=56, value='adyen_recurring_api_url', kind=None),
                                            ),
                                            keyword(
                                                lineno=35,
                                                col_offset=16,
                                                end_lineno=35,
                                                end_col_offset=35,
                                                arg='endpoint',
                                                value=Constant(lineno=35, col_offset=25, end_lineno=35, end_col_offset=35, value='/disable', kind=None),
                                            ),
                                            keyword(
                                                lineno=36,
                                                col_offset=16,
                                                end_lineno=36,
                                                end_col_offset=28,
                                                arg='payload',
                                                value=Name(lineno=36, col_offset=24, end_lineno=36, end_col_offset=28, id='data', ctx=Load()),
                                            ),
                                            keyword(
                                                lineno=37,
                                                col_offset=16,
                                                end_lineno=37,
                                                end_col_offset=29,
                                                arg='method',
                                                value=Constant(lineno=37, col_offset=23, end_lineno=37, end_col_offset=29, value='POST', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    lineno=39,
                                    col_offset=8,
                                    end_lineno=40,
                                    end_col_offset=16,
                                    type=Name(lineno=39, col_offset=15, end_lineno=39, end_col_offset=30, id='ValidationError', ctx=Load()),
                                    name=None,
                                    body=[Pass(lineno=40, col_offset=12, end_lineno=40, end_col_offset=16)],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=42,
                    col_offset=4,
                    end_lineno=54,
                    end_col_offset=99,
                    name='_handle_reactivation_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=42, col_offset=37, end_lineno=42, end_col_offset=41, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=43,
                            col_offset=8,
                            end_lineno=49,
                            end_col_offset=11,
                            value=Constant(lineno=43, col_offset=8, end_lineno=49, end_col_offset=11, value=' Override of payment to raise an error informing that Adyen tokens cannot be restored.\n\n        Note: self.ensure_one()\n\n        :return: None\n        :raise: UserError if the token is managed by Adyen\n        ', kind=None),
                        ),
                        Expr(
                            lineno=50,
                            col_offset=8,
                            end_lineno=50,
                            end_col_offset=46,
                            value=Call(
                                lineno=50,
                                col_offset=8,
                                end_lineno=50,
                                end_col_offset=46,
                                func=Attribute(
                                    lineno=50,
                                    col_offset=8,
                                    end_lineno=50,
                                    end_col_offset=44,
                                    value=Call(
                                        lineno=50,
                                        col_offset=8,
                                        end_lineno=50,
                                        end_col_offset=15,
                                        func=Name(lineno=50, col_offset=8, end_lineno=50, end_col_offset=13, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_handle_reactivation_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            lineno=51,
                            col_offset=8,
                            end_lineno=52,
                            end_col_offset=18,
                            test=Compare(
                                lineno=51,
                                col_offset=11,
                                end_lineno=51,
                                end_col_offset=35,
                                left=Attribute(
                                    lineno=51,
                                    col_offset=11,
                                    end_lineno=51,
                                    end_col_offset=24,
                                    value=Name(lineno=51, col_offset=11, end_lineno=51, end_col_offset=15, id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(lineno=51, col_offset=28, end_lineno=51, end_col_offset=35, value='adyen', kind=None)],
                            ),
                            body=[Return(lineno=52, col_offset=12, end_lineno=52, end_col_offset=18, value=None)],
                            orelse=[],
                        ),
                        Raise(
                            lineno=54,
                            col_offset=8,
                            end_lineno=54,
                            end_col_offset=99,
                            exc=Call(
                                lineno=54,
                                col_offset=14,
                                end_lineno=54,
                                end_col_offset=99,
                                func=Name(lineno=54, col_offset=14, end_lineno=54, end_col_offset=23, id='UserError', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=54,
                                        col_offset=24,
                                        end_lineno=54,
                                        end_col_offset=98,
                                        func=Name(lineno=54, col_offset=24, end_lineno=54, end_col_offset=25, id='_', ctx=Load()),
                                        args=[Constant(lineno=54, col_offset=26, end_lineno=54, end_col_offset=97, value='Saved payment methods cannot be restored once they have been deleted.', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
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