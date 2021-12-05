Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=30,
            end_col_offset=53,
            name='ConfirmStockSms',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=22,
                    end_lineno=7,
                    end_col_offset=43,
                    value=Name(lineno=7, col_offset=22, end_lineno=7, end_col_offset=28, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=31,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=31, value='confirm.stock.sms', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=38,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=38, value='Confirm Stock SMS', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=73,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=12, id='pick_ids', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=15,
                        end_lineno=11,
                        end_col_offset=73,
                        func=Attribute(
                            lineno=11,
                            col_offset=15,
                            end_lineno=11,
                            end_col_offset=31,
                            value=Name(lineno=11, col_offset=15, end_lineno=11, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=11, col_offset=32, end_lineno=11, end_col_offset=47, value='stock.picking', kind=None),
                            Constant(lineno=11, col_offset=49, end_lineno=11, end_col_offset=72, value='stock_picking_sms_rel', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=53,
                    name='send_sms',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=17, end_lineno=13, end_col_offset=21, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=25,
                            value=Call(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=23,
                                    value=Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            lineno=15,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=78,
                            target=Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=19, id='company', ctx=Store()),
                            iter=Attribute(
                                lineno=15,
                                col_offset=23,
                                end_lineno=15,
                                end_col_offset=47,
                                value=Attribute(
                                    lineno=15,
                                    col_offset=23,
                                    end_lineno=15,
                                    end_col_offset=36,
                                    value=Name(lineno=15, col_offset=23, end_lineno=15, end_col_offset=27, id='self', ctx=Load()),
                                    attr='pick_ids',
                                    ctx=Load(),
                                ),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=78,
                                    test=UnaryOp(
                                        lineno=16,
                                        col_offset=15,
                                        end_lineno=16,
                                        end_col_offset=57,
                                        op=Not(),
                                        operand=Attribute(
                                            lineno=16,
                                            col_offset=19,
                                            end_lineno=16,
                                            end_col_offset=57,
                                            value=Name(lineno=16, col_offset=19, end_lineno=16, end_col_offset=26, id='company', ctx=Load()),
                                            attr='has_received_warning_stock_sms',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            lineno=17,
                                            col_offset=16,
                                            end_lineno=17,
                                            end_col_offset=78,
                                            value=Call(
                                                lineno=17,
                                                col_offset=16,
                                                end_lineno=17,
                                                end_col_offset=78,
                                                func=Attribute(
                                                    lineno=17,
                                                    col_offset=16,
                                                    end_lineno=17,
                                                    end_col_offset=36,
                                                    value=Call(
                                                        lineno=17,
                                                        col_offset=16,
                                                        end_lineno=17,
                                                        end_col_offset=30,
                                                        func=Attribute(
                                                            lineno=17,
                                                            col_offset=16,
                                                            end_lineno=17,
                                                            end_col_offset=28,
                                                            value=Name(lineno=17, col_offset=16, end_lineno=17, end_col_offset=23, id='company', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        lineno=17,
                                                        col_offset=37,
                                                        end_lineno=17,
                                                        end_col_offset=77,
                                                        keys=[Constant(lineno=17, col_offset=38, end_lineno=17, end_col_offset=70, value='has_received_warning_stock_sms', kind=None)],
                                                        values=[Constant(lineno=17, col_offset=72, end_lineno=17, end_col_offset=76, value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=116,
                            targets=[Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=28, id='pickings_to_validate', ctx=Store())],
                            value=Call(
                                lineno=18,
                                col_offset=31,
                                end_lineno=18,
                                end_col_offset=116,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=31,
                                    end_lineno=18,
                                    end_col_offset=63,
                                    value=Subscript(
                                        lineno=18,
                                        col_offset=31,
                                        end_lineno=18,
                                        end_col_offset=56,
                                        value=Attribute(
                                            lineno=18,
                                            col_offset=31,
                                            end_lineno=18,
                                            end_col_offset=39,
                                            value=Name(lineno=18, col_offset=31, end_lineno=18, end_col_offset=35, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=18, col_offset=40, end_lineno=18, end_col_offset=55, value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=18,
                                        col_offset=64,
                                        end_lineno=18,
                                        end_col_offset=115,
                                        func=Attribute(
                                            lineno=18,
                                            col_offset=64,
                                            end_lineno=18,
                                            end_col_offset=84,
                                            value=Attribute(
                                                lineno=18,
                                                col_offset=64,
                                                end_lineno=18,
                                                end_col_offset=80,
                                                value=Attribute(
                                                    lineno=18,
                                                    col_offset=64,
                                                    end_lineno=18,
                                                    end_col_offset=72,
                                                    value=Name(lineno=18, col_offset=64, end_lineno=18, end_col_offset=68, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=18, col_offset=85, end_lineno=18, end_col_offset=114, value='button_validate_picking_ids', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=53,
                            value=Call(
                                lineno=19,
                                col_offset=15,
                                end_lineno=19,
                                end_col_offset=53,
                                func=Attribute(
                                    lineno=19,
                                    col_offset=15,
                                    end_lineno=19,
                                    end_col_offset=51,
                                    value=Name(lineno=19, col_offset=15, end_lineno=19, end_col_offset=35, id='pickings_to_validate', ctx=Load()),
                                    attr='button_validate',
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
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=53,
                    name='dont_send_sms',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=21, col_offset=22, end_lineno=21, end_col_offset=26, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=25,
                            value=Call(
                                lineno=22,
                                col_offset=8,
                                end_lineno=22,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=22,
                                    col_offset=8,
                                    end_lineno=22,
                                    end_col_offset=23,
                                    value=Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            lineno=23,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=18,
                            target=Name(lineno=23, col_offset=12, end_lineno=23, end_col_offset=19, id='company', ctx=Store()),
                            iter=Attribute(
                                lineno=23,
                                col_offset=23,
                                end_lineno=23,
                                end_col_offset=47,
                                value=Attribute(
                                    lineno=23,
                                    col_offset=23,
                                    end_lineno=23,
                                    end_col_offset=36,
                                    value=Name(lineno=23, col_offset=23, end_lineno=23, end_col_offset=27, id='self', ctx=Load()),
                                    attr='pick_ids',
                                    ctx=Load(),
                                ),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    lineno=24,
                                    col_offset=12,
                                    end_lineno=28,
                                    end_col_offset=18,
                                    test=UnaryOp(
                                        lineno=24,
                                        col_offset=15,
                                        end_lineno=24,
                                        end_col_offset=57,
                                        op=Not(),
                                        operand=Attribute(
                                            lineno=24,
                                            col_offset=19,
                                            end_lineno=24,
                                            end_col_offset=57,
                                            value=Name(lineno=24, col_offset=19, end_lineno=24, end_col_offset=26, id='company', ctx=Load()),
                                            attr='has_received_warning_stock_sms',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            lineno=25,
                                            col_offset=16,
                                            end_lineno=28,
                                            end_col_offset=18,
                                            value=Call(
                                                lineno=25,
                                                col_offset=16,
                                                end_lineno=28,
                                                end_col_offset=18,
                                                func=Attribute(
                                                    lineno=25,
                                                    col_offset=16,
                                                    end_lineno=25,
                                                    end_col_offset=36,
                                                    value=Call(
                                                        lineno=25,
                                                        col_offset=16,
                                                        end_lineno=25,
                                                        end_col_offset=30,
                                                        func=Attribute(
                                                            lineno=25,
                                                            col_offset=16,
                                                            end_lineno=25,
                                                            end_col_offset=28,
                                                            value=Name(lineno=25, col_offset=16, end_lineno=25, end_col_offset=23, id='company', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        lineno=25,
                                                        col_offset=37,
                                                        end_lineno=28,
                                                        end_col_offset=17,
                                                        keys=[
                                                            Constant(lineno=26, col_offset=20, end_lineno=26, end_col_offset=52, value='has_received_warning_stock_sms', kind=None),
                                                            Constant(lineno=27, col_offset=20, end_lineno=27, end_col_offset=47, value='stock_move_sms_validation', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(lineno=26, col_offset=54, end_lineno=26, end_col_offset=58, value=True, kind=None),
                                                            Constant(lineno=27, col_offset=49, end_lineno=27, end_col_offset=54, value=False, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=116,
                            targets=[Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=28, id='pickings_to_validate', ctx=Store())],
                            value=Call(
                                lineno=29,
                                col_offset=31,
                                end_lineno=29,
                                end_col_offset=116,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=31,
                                    end_lineno=29,
                                    end_col_offset=63,
                                    value=Subscript(
                                        lineno=29,
                                        col_offset=31,
                                        end_lineno=29,
                                        end_col_offset=56,
                                        value=Attribute(
                                            lineno=29,
                                            col_offset=31,
                                            end_lineno=29,
                                            end_col_offset=39,
                                            value=Name(lineno=29, col_offset=31, end_lineno=29, end_col_offset=35, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=29, col_offset=40, end_lineno=29, end_col_offset=55, value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=29,
                                        col_offset=64,
                                        end_lineno=29,
                                        end_col_offset=115,
                                        func=Attribute(
                                            lineno=29,
                                            col_offset=64,
                                            end_lineno=29,
                                            end_col_offset=84,
                                            value=Attribute(
                                                lineno=29,
                                                col_offset=64,
                                                end_lineno=29,
                                                end_col_offset=80,
                                                value=Attribute(
                                                    lineno=29,
                                                    col_offset=64,
                                                    end_lineno=29,
                                                    end_col_offset=72,
                                                    value=Name(lineno=29, col_offset=64, end_lineno=29, end_col_offset=68, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=29, col_offset=85, end_lineno=29, end_col_offset=114, value='button_validate_picking_ids', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=53,
                            value=Call(
                                lineno=30,
                                col_offset=15,
                                end_lineno=30,
                                end_col_offset=53,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=15,
                                    end_lineno=30,
                                    end_col_offset=51,
                                    value=Name(lineno=30, col_offset=15, end_lineno=30, end_col_offset=35, id='pickings_to_validate', ctx=Load()),
                                    attr='button_validate',
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
