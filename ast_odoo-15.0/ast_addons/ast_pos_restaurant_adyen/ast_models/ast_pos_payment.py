Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=11,
            names=[alias(name='json', asname=None)],
        ),
        Import(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=15,
            names=[alias(name='requests', asname=None)],
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        Assign(
            lineno=9,
            col_offset=0,
            end_lineno=9,
            end_col_offset=12,
            targets=[Name(lineno=9, col_offset=0, end_lineno=9, end_col_offset=7, id='TIMEOUT', ctx=Store())],
            value=Constant(lineno=9, col_offset=10, end_lineno=9, end_col_offset=12, value=10, kind=None),
            type_comment=None,
        ),
        ClassDef(
            lineno=12,
            col_offset=0,
            end_lineno=32,
            end_col_offset=74,
            name='PosPayment',
            bases=[
                Attribute(
                    lineno=12,
                    col_offset=17,
                    end_lineno=12,
                    end_col_offset=29,
                    value=Name(lineno=12, col_offset=17, end_lineno=12, end_col_offset=23, id='models', ctx=Load()),
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
                    end_col_offset=28,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=13, col_offset=15, end_lineno=13, end_col_offset=28, value='pos.payment', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=18,
                    name='_update_payment_line_for_tip',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=15, col_offset=37, end_lineno=15, end_col_offset=41, arg='self', annotation=None, type_comment=None),
                            arg(lineno=15, col_offset=43, end_lineno=15, end_col_offset=53, arg='tip_amount', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=52,
                            value=Constant(lineno=16, col_offset=8, end_lineno=16, end_col_offset=52, value='Capture the payment when a tip is set.', kind=None),
                        ),
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=78,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=17,
                                col_offset=14,
                                end_lineno=17,
                                end_col_offset=78,
                                func=Attribute(
                                    lineno=17,
                                    col_offset=14,
                                    end_lineno=17,
                                    end_col_offset=66,
                                    value=Call(
                                        lineno=17,
                                        col_offset=14,
                                        end_lineno=17,
                                        end_col_offset=37,
                                        func=Name(lineno=17, col_offset=14, end_lineno=17, end_col_offset=19, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=17, col_offset=20, end_lineno=17, end_col_offset=30, id='PosPayment', ctx=Load()),
                                            Name(lineno=17, col_offset=32, end_lineno=17, end_col_offset=36, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_update_payment_line_for_tip',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=17, col_offset=67, end_lineno=17, end_col_offset=77, id='tip_amount', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=18,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=33,
                            test=Compare(
                                lineno=18,
                                col_offset=11,
                                end_lineno=18,
                                end_col_offset=65,
                                left=Attribute(
                                    lineno=18,
                                    col_offset=11,
                                    end_lineno=18,
                                    end_col_offset=54,
                                    value=Attribute(
                                        lineno=18,
                                        col_offset=11,
                                        end_lineno=18,
                                        end_col_offset=33,
                                        value=Name(lineno=18, col_offset=11, end_lineno=18, end_col_offset=15, id='self', ctx=Load()),
                                        attr='payment_method_id',
                                        ctx=Load(),
                                    ),
                                    attr='use_payment_terminal',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(lineno=18, col_offset=58, end_lineno=18, end_col_offset=65, value='adyen', kind=None)],
                            ),
                            body=[
                                Expr(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=19,
                                    end_col_offset=33,
                                    value=Call(
                                        lineno=19,
                                        col_offset=12,
                                        end_lineno=19,
                                        end_col_offset=33,
                                        func=Attribute(
                                            lineno=19,
                                            col_offset=12,
                                            end_lineno=19,
                                            end_col_offset=31,
                                            value=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=16, id='self', ctx=Load()),
                                            attr='_adyen_capture',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=18,
                            value=Name(lineno=20, col_offset=15, end_lineno=20, end_col_offset=18, id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=22,
                    col_offset=4,
                    end_lineno=32,
                    end_col_offset=74,
                    name='_adyen_capture',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=22, col_offset=23, end_lineno=22, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=30,
                            end_col_offset=9,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=12, id='data', ctx=Store())],
                            value=Dict(
                                lineno=23,
                                col_offset=15,
                                end_lineno=30,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=24, col_offset=12, end_lineno=24, end_col_offset=31, value='originalReference', kind=None),
                                    Constant(lineno=25, col_offset=12, end_lineno=25, end_col_offset=32, value='modificationAmount', kind=None),
                                    Constant(lineno=29, col_offset=12, end_lineno=29, end_col_offset=29, value='merchantAccount', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        lineno=24,
                                        col_offset=33,
                                        end_lineno=24,
                                        end_col_offset=52,
                                        value=Name(lineno=24, col_offset=33, end_lineno=24, end_col_offset=37, id='self', ctx=Load()),
                                        attr='transaction_id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        lineno=25,
                                        col_offset=34,
                                        end_lineno=28,
                                        end_col_offset=13,
                                        keys=[
                                            Constant(lineno=26, col_offset=16, end_lineno=26, end_col_offset=23, value='value', kind=None),
                                            Constant(lineno=27, col_offset=16, end_lineno=27, end_col_offset=26, value='currency', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                lineno=26,
                                                col_offset=25,
                                                end_lineno=26,
                                                end_col_offset=79,
                                                func=Name(lineno=26, col_offset=25, end_lineno=26, end_col_offset=28, id='int', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        lineno=26,
                                                        col_offset=29,
                                                        end_lineno=26,
                                                        end_col_offset=78,
                                                        left=Attribute(
                                                            lineno=26,
                                                            col_offset=29,
                                                            end_lineno=26,
                                                            end_col_offset=40,
                                                            value=Name(lineno=26, col_offset=29, end_lineno=26, end_col_offset=33, id='self', ctx=Load()),
                                                            attr='amount',
                                                            ctx=Load(),
                                                        ),
                                                        op=Mult(),
                                                        right=BinOp(
                                                            lineno=26,
                                                            col_offset=43,
                                                            end_lineno=26,
                                                            end_col_offset=78,
                                                            left=Constant(lineno=26, col_offset=43, end_lineno=26, end_col_offset=45, value=10, kind=None),
                                                            op=Pow(),
                                                            right=Attribute(
                                                                lineno=26,
                                                                col_offset=47,
                                                                end_lineno=26,
                                                                end_col_offset=78,
                                                                value=Attribute(
                                                                    lineno=26,
                                                                    col_offset=47,
                                                                    end_lineno=26,
                                                                    end_col_offset=63,
                                                                    value=Name(lineno=26, col_offset=47, end_lineno=26, end_col_offset=51, id='self', ctx=Load()),
                                                                    attr='currency_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='decimal_places',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                lineno=27,
                                                col_offset=28,
                                                end_lineno=27,
                                                end_col_offset=49,
                                                value=Attribute(
                                                    lineno=27,
                                                    col_offset=28,
                                                    end_lineno=27,
                                                    end_col_offset=44,
                                                    value=Name(lineno=27, col_offset=28, end_lineno=27, end_col_offset=32, id='self', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        lineno=29,
                                        col_offset=31,
                                        end_lineno=29,
                                        end_col_offset=76,
                                        value=Attribute(
                                            lineno=29,
                                            col_offset=31,
                                            end_lineno=29,
                                            end_col_offset=53,
                                            value=Name(lineno=29, col_offset=31, end_lineno=29, end_col_offset=35, id='self', ctx=Load()),
                                            attr='payment_method_id',
                                            ctx=Load(),
                                        ),
                                        attr='adyen_merchant_account',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=74,
                            value=Call(
                                lineno=32,
                                col_offset=15,
                                end_lineno=32,
                                end_col_offset=74,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=15,
                                    end_lineno=32,
                                    end_col_offset=57,
                                    value=Attribute(
                                        lineno=32,
                                        col_offset=15,
                                        end_lineno=32,
                                        end_col_offset=37,
                                        value=Name(lineno=32, col_offset=15, end_lineno=32, end_col_offset=19, id='self', ctx=Load()),
                                        attr='payment_method_id',
                                        ctx=Load(),
                                    ),
                                    attr='proxy_adyen_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=32, col_offset=58, end_lineno=32, end_col_offset=62, id='data', ctx=Load()),
                                    Constant(lineno=32, col_offset=64, end_lineno=32, end_col_offset=73, value='capture', kind=None),
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