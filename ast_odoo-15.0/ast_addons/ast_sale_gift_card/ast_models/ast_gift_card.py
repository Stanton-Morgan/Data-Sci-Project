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
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=24,
            end_col_offset=36,
            name='GiftCard',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=15,
                    end_lineno=7,
                    end_col_offset=27,
                    value=Name(lineno=7, col_offset=15, end_lineno=7, end_col_offset=21, id='models', ctx=Load()),
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
                    end_col_offset=26,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=26, value='gift.card', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=95,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=15, id='buy_line_id', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=18,
                        end_lineno=11,
                        end_col_offset=95,
                        func=Attribute(
                            lineno=10,
                            col_offset=18,
                            end_lineno=10,
                            end_col_offset=33,
                            value=Name(lineno=10, col_offset=18, end_lineno=10, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=34, end_lineno=10, end_col_offset=51, value='sale.order.line', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=53,
                                end_lineno=10,
                                end_col_offset=63,
                                arg='copy',
                                value=Constant(lineno=10, col_offset=58, end_lineno=10, end_col_offset=63, value=False, kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=65,
                                end_lineno=10,
                                end_col_offset=78,
                                arg='readonly',
                                value=Constant(lineno=10, col_offset=74, end_lineno=10, end_col_offset=78, value=True, kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=34,
                                end_lineno=11,
                                end_col_offset=94,
                                arg='help',
                                value=Constant(lineno=11, col_offset=39, end_lineno=11, end_col_offset=94, value='Sale Order line where this gift card has been bought.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=90,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=19, id='redeem_line_ids', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=22,
                        end_lineno=12,
                        end_col_offset=90,
                        func=Attribute(
                            lineno=12,
                            col_offset=22,
                            end_lineno=12,
                            end_col_offset=37,
                            value=Name(lineno=12, col_offset=22, end_lineno=12, end_col_offset=28, id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=12, col_offset=38, end_lineno=12, end_col_offset=55, value='sale.order.line', kind=None),
                            Constant(lineno=12, col_offset=57, end_lineno=12, end_col_offset=71, value='gift_card_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=73,
                                end_lineno=12,
                                end_col_offset=89,
                                arg='string',
                                value=Constant(lineno=12, col_offset=80, end_lineno=12, end_col_offset=89, value='Redeems', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=36,
                    name='_compute_balance',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=15, col_offset=25, end_lineno=15, end_col_offset=29, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=34,
                            value=Call(
                                lineno=16,
                                col_offset=8,
                                end_lineno=16,
                                end_col_offset=34,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=8,
                                    end_lineno=16,
                                    end_col_offset=32,
                                    value=Call(
                                        lineno=16,
                                        col_offset=8,
                                        end_lineno=16,
                                        end_col_offset=15,
                                        func=Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=13, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compute_balance',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            lineno=17,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=36,
                            target=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, id='record', ctx=Store()),
                            iter=Name(lineno=17, col_offset=22, end_lineno=17, end_col_offset=26, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=18,
                                    end_col_offset=89,
                                    targets=[Name(lineno=18, col_offset=12, end_lineno=18, end_col_offset=26, id='confirmed_line', ctx=Store())],
                                    value=Call(
                                        lineno=18,
                                        col_offset=29,
                                        end_lineno=18,
                                        end_col_offset=89,
                                        func=Attribute(
                                            lineno=18,
                                            col_offset=29,
                                            end_lineno=18,
                                            end_col_offset=60,
                                            value=Attribute(
                                                lineno=18,
                                                col_offset=29,
                                                end_lineno=18,
                                                end_col_offset=51,
                                                value=Name(lineno=18, col_offset=29, end_lineno=18, end_col_offset=35, id='record', ctx=Load()),
                                                attr='redeem_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                lineno=18,
                                                col_offset=61,
                                                end_lineno=18,
                                                end_col_offset=88,
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(lineno=18, col_offset=68, end_lineno=18, end_col_offset=69, arg='l', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    lineno=18,
                                                    col_offset=71,
                                                    end_lineno=18,
                                                    end_col_offset=88,
                                                    left=Attribute(
                                                        lineno=18,
                                                        col_offset=71,
                                                        end_lineno=18,
                                                        end_col_offset=78,
                                                        value=Name(lineno=18, col_offset=71, end_lineno=18, end_col_offset=72, id='l', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(lineno=18, col_offset=82, end_lineno=18, end_col_offset=88, value='sale', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=19,
                                    end_col_offset=36,
                                    targets=[Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=19, id='balance', ctx=Store())],
                                    value=Attribute(
                                        lineno=19,
                                        col_offset=22,
                                        end_lineno=19,
                                        end_col_offset=36,
                                        value=Name(lineno=19, col_offset=22, end_lineno=19, end_col_offset=28, id='record', ctx=Load()),
                                        attr='balance',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    lineno=20,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=18,
                                    test=Name(lineno=20, col_offset=15, end_lineno=20, end_col_offset=29, id='confirmed_line', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            lineno=21,
                                            col_offset=16,
                                            end_lineno=23,
                                            end_col_offset=18,
                                            target=Name(lineno=21, col_offset=16, end_lineno=21, end_col_offset=23, id='balance', ctx=Store()),
                                            op=Sub(),
                                            value=Call(
                                                lineno=21,
                                                col_offset=27,
                                                end_lineno=23,
                                                end_col_offset=18,
                                                func=Name(lineno=21, col_offset=27, end_lineno=21, end_col_offset=30, id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        lineno=21,
                                                        col_offset=31,
                                                        end_lineno=23,
                                                        end_col_offset=17,
                                                        func=Attribute(
                                                            lineno=21,
                                                            col_offset=31,
                                                            end_lineno=21,
                                                            end_col_offset=52,
                                                            value=Name(lineno=21, col_offset=31, end_lineno=21, end_col_offset=45, id='confirmed_line', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                lineno=22,
                                                                col_offset=20,
                                                                end_lineno=22,
                                                                end_col_offset=138,
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(lineno=22, col_offset=27, end_lineno=22, end_col_offset=31, arg='line', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=BinOp(
                                                                    lineno=22,
                                                                    col_offset=33,
                                                                    end_lineno=22,
                                                                    end_col_offset=138,
                                                                    left=Call(
                                                                        lineno=22,
                                                                        col_offset=33,
                                                                        end_lineno=22,
                                                                        end_col_offset=133,
                                                                        func=Attribute(
                                                                            lineno=22,
                                                                            col_offset=33,
                                                                            end_lineno=22,
                                                                            end_col_offset=58,
                                                                            value=Attribute(
                                                                                lineno=22,
                                                                                col_offset=33,
                                                                                end_lineno=22,
                                                                                end_col_offset=49,
                                                                                value=Name(lineno=22, col_offset=33, end_lineno=22, end_col_offset=37, id='line', ctx=Load()),
                                                                                attr='currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='_convert',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                lineno=22,
                                                                                col_offset=59,
                                                                                end_lineno=22,
                                                                                end_col_offset=74,
                                                                                value=Name(lineno=22, col_offset=59, end_lineno=22, end_col_offset=63, id='line', ctx=Load()),
                                                                                attr='price_unit',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                lineno=22,
                                                                                col_offset=76,
                                                                                end_lineno=22,
                                                                                end_col_offset=94,
                                                                                value=Name(lineno=22, col_offset=76, end_lineno=22, end_col_offset=82, id='record', ctx=Load()),
                                                                                attr='currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                lineno=22,
                                                                                col_offset=96,
                                                                                end_lineno=22,
                                                                                end_col_offset=114,
                                                                                value=Attribute(
                                                                                    lineno=22,
                                                                                    col_offset=96,
                                                                                    end_lineno=22,
                                                                                    end_col_offset=106,
                                                                                    value=Name(lineno=22, col_offset=96, end_lineno=22, end_col_offset=102, id='record', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='company',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                lineno=22,
                                                                                col_offset=116,
                                                                                end_lineno=22,
                                                                                end_col_offset=132,
                                                                                value=Name(lineno=22, col_offset=116, end_lineno=22, end_col_offset=120, id='line', ctx=Load()),
                                                                                attr='create_date',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    op=Mult(),
                                                                    right=UnaryOp(
                                                                        lineno=22,
                                                                        col_offset=136,
                                                                        end_lineno=22,
                                                                        end_col_offset=138,
                                                                        op=USub(),
                                                                        operand=Constant(lineno=22, col_offset=137, end_lineno=22, end_col_offset=138, value=1, kind=None),
                                                                    ),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    lineno=24,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=36,
                                    targets=[
                                        Attribute(
                                            lineno=24,
                                            col_offset=12,
                                            end_lineno=24,
                                            end_col_offset=26,
                                            value=Name(lineno=24, col_offset=12, end_lineno=24, end_col_offset=18, id='record', ctx=Load()),
                                            attr='balance',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(lineno=24, col_offset=29, end_lineno=24, end_col_offset=36, id='balance', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=14,
                            col_offset=5,
                            end_lineno=14,
                            end_col_offset=35,
                            func=Attribute(
                                lineno=14,
                                col_offset=5,
                                end_lineno=14,
                                end_col_offset=16,
                                value=Name(lineno=14, col_offset=5, end_lineno=14, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=14, col_offset=17, end_lineno=14, end_col_offset=34, value='redeem_line_ids', kind=None)],
                            keywords=[],
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