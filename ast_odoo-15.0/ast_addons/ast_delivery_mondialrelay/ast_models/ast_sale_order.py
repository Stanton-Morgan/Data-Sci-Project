Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=26,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=37,
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=18,
            end_col_offset=39,
            name='SaleOrderMondialRelay',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=28,
                    end_lineno=8,
                    end_col_offset=40,
                    value=Name(lineno=8, col_offset=28, end_lineno=8, end_col_offset=34, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=27,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=27, value='sale.order', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=39,
                    name='action_confirm',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=23, end_lineno=11, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=115,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=15, id='unmatch', ctx=Store())],
                            value=Call(
                                lineno=12,
                                col_offset=18,
                                end_lineno=12,
                                end_col_offset=115,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=18,
                                    end_lineno=12,
                                    end_col_offset=31,
                                    value=Name(lineno=12, col_offset=18, end_lineno=12, end_col_offset=22, id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        lineno=12,
                                        col_offset=32,
                                        end_lineno=12,
                                        end_col_offset=114,
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(lineno=12, col_offset=39, end_lineno=12, end_col_offset=41, arg='so', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            lineno=12,
                                            col_offset=43,
                                            end_lineno=12,
                                            end_col_offset=114,
                                            left=Attribute(
                                                lineno=12,
                                                col_offset=43,
                                                end_lineno=12,
                                                end_col_offset=72,
                                                value=Attribute(
                                                    lineno=12,
                                                    col_offset=43,
                                                    end_lineno=12,
                                                    end_col_offset=56,
                                                    value=Name(lineno=12, col_offset=43, end_lineno=12, end_col_offset=45, id='so', ctx=Load()),
                                                    attr='carrier_id',
                                                    ctx=Load(),
                                                ),
                                                attr='is_mondialrelay',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[
                                                Attribute(
                                                    lineno=12,
                                                    col_offset=76,
                                                    end_lineno=12,
                                                    end_col_offset=114,
                                                    value=Attribute(
                                                        lineno=12,
                                                        col_offset=76,
                                                        end_lineno=12,
                                                        end_col_offset=98,
                                                        value=Name(lineno=12, col_offset=76, end_lineno=12, end_col_offset=78, id='so', ctx=Load()),
                                                        attr='partner_shipping_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='is_mondialrelay',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=13,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=34,
                            test=Name(lineno=13, col_offset=11, end_lineno=13, end_col_offset=18, id='unmatch', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=14,
                                    end_col_offset=96,
                                    targets=[Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=17, id='error', ctx=Store())],
                                    value=Call(
                                        lineno=14,
                                        col_offset=20,
                                        end_lineno=14,
                                        end_col_offset=96,
                                        func=Name(lineno=14, col_offset=20, end_lineno=14, end_col_offset=21, id='_', ctx=Load()),
                                        args=[Constant(lineno=14, col_offset=22, end_lineno=14, end_col_offset=95, value='Mondial Relay mismatching between delivery method and shipping address.', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    lineno=15,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=67,
                                    test=Compare(
                                        lineno=15,
                                        col_offset=15,
                                        end_lineno=15,
                                        end_col_offset=28,
                                        left=Call(
                                            lineno=15,
                                            col_offset=15,
                                            end_lineno=15,
                                            end_col_offset=24,
                                            func=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=18, id='len', ctx=Load()),
                                            args=[Name(lineno=15, col_offset=19, end_lineno=15, end_col_offset=23, id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(lineno=15, col_offset=27, end_lineno=15, end_col_offset=28, value=1, kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            lineno=16,
                                            col_offset=16,
                                            end_lineno=16,
                                            end_col_offset=67,
                                            target=Name(lineno=16, col_offset=16, end_lineno=16, end_col_offset=21, id='error', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                lineno=16,
                                                col_offset=25,
                                                end_lineno=16,
                                                end_col_offset=67,
                                                left=Constant(lineno=16, col_offset=25, end_lineno=16, end_col_offset=32, value=' (%s)', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    lineno=16,
                                                    col_offset=35,
                                                    end_lineno=16,
                                                    end_col_offset=67,
                                                    func=Attribute(
                                                        lineno=16,
                                                        col_offset=35,
                                                        end_lineno=16,
                                                        end_col_offset=43,
                                                        value=Constant(lineno=16, col_offset=35, end_lineno=16, end_col_offset=38, value=',', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            lineno=16,
                                                            col_offset=44,
                                                            end_lineno=16,
                                                            end_col_offset=66,
                                                            func=Attribute(
                                                                lineno=16,
                                                                col_offset=44,
                                                                end_lineno=16,
                                                                end_col_offset=58,
                                                                value=Name(lineno=16, col_offset=44, end_lineno=16, end_col_offset=51, id='unmatch', ctx=Load()),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(lineno=16, col_offset=59, end_lineno=16, end_col_offset=65, value='name', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Raise(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=34,
                                    exc=Call(
                                        lineno=17,
                                        col_offset=18,
                                        end_lineno=17,
                                        end_col_offset=34,
                                        func=Name(lineno=17, col_offset=18, end_lineno=17, end_col_offset=27, id='UserError', ctx=Load()),
                                        args=[Name(lineno=17, col_offset=28, end_lineno=17, end_col_offset=33, id='error', ctx=Load())],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=39,
                            value=Call(
                                lineno=18,
                                col_offset=15,
                                end_lineno=18,
                                end_col_offset=39,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=15,
                                    end_lineno=18,
                                    end_col_offset=37,
                                    value=Call(
                                        lineno=18,
                                        col_offset=15,
                                        end_lineno=18,
                                        end_col_offset=22,
                                        func=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=20, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
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
