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
            end_lineno=34,
            end_col_offset=9,
            name='MakeInvoice',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=18,
                    end_lineno=7,
                    end_col_offset=39,
                    value=Name(lineno=7, col_offset=18, end_lineno=7, end_col_offset=24, id='models', ctx=Load()),
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
                    end_col_offset=39,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=39, value='repair.order.make_invoice', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=49,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=49, value='Create Mass Invoice (repair)', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=62,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=9, id='group', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=12,
                        end_lineno=11,
                        end_col_offset=62,
                        func=Attribute(
                            lineno=11,
                            col_offset=12,
                            end_lineno=11,
                            end_col_offset=26,
                            value=Name(lineno=11, col_offset=12, end_lineno=11, end_col_offset=18, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=27, end_lineno=11, end_col_offset=61, value='Group by partner invoice address', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=34,
                    end_col_offset=9,
                    name='make_invoices',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=22, end_lineno=13, end_col_offset=26, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            lineno=14,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=58,
                            test=UnaryOp(
                                lineno=14,
                                col_offset=11,
                                end_lineno=14,
                                end_col_offset=46,
                                op=Not(),
                                operand=Call(
                                    lineno=14,
                                    col_offset=15,
                                    end_lineno=14,
                                    end_col_offset=46,
                                    func=Attribute(
                                        lineno=14,
                                        col_offset=15,
                                        end_lineno=14,
                                        end_col_offset=32,
                                        value=Attribute(
                                            lineno=14,
                                            col_offset=15,
                                            end_lineno=14,
                                            end_col_offset=28,
                                            value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=19, id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=14, col_offset=33, end_lineno=14, end_col_offset=45, value='active_ids', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    lineno=15,
                                    col_offset=12,
                                    end_lineno=15,
                                    end_col_offset=58,
                                    value=Dict(
                                        lineno=15,
                                        col_offset=19,
                                        end_lineno=15,
                                        end_col_offset=58,
                                        keys=[Constant(lineno=15, col_offset=20, end_lineno=15, end_col_offset=26, value='type', kind=None)],
                                        values=[Constant(lineno=15, col_offset=28, end_lineno=15, end_col_offset=57, value='ir.actions.act_window_close', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=24,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=19, id='new_invoice', ctx=Store())],
                            value=Dict(lineno=16, col_offset=22, end_lineno=16, end_col_offset=24, keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            lineno=17,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=50,
                            target=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, id='wizard', ctx=Store()),
                            iter=Name(lineno=17, col_offset=22, end_lineno=17, end_col_offset=26, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=18,
                                    end_col_offset=82,
                                    targets=[Name(lineno=18, col_offset=12, end_lineno=18, end_col_offset=19, id='repairs', ctx=Store())],
                                    value=Call(
                                        lineno=18,
                                        col_offset=22,
                                        end_lineno=18,
                                        end_col_offset=82,
                                        func=Attribute(
                                            lineno=18,
                                            col_offset=22,
                                            end_lineno=18,
                                            end_col_offset=53,
                                            value=Subscript(
                                                lineno=18,
                                                col_offset=22,
                                                end_lineno=18,
                                                end_col_offset=46,
                                                value=Attribute(
                                                    lineno=18,
                                                    col_offset=22,
                                                    end_lineno=18,
                                                    end_col_offset=30,
                                                    value=Name(lineno=18, col_offset=22, end_lineno=18, end_col_offset=26, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=18, col_offset=31, end_lineno=18, end_col_offset=45, value='repair.order', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                lineno=18,
                                                col_offset=54,
                                                end_lineno=18,
                                                end_col_offset=81,
                                                value=Attribute(
                                                    lineno=18,
                                                    col_offset=54,
                                                    end_lineno=18,
                                                    end_col_offset=67,
                                                    value=Name(lineno=18, col_offset=54, end_lineno=18, end_col_offset=58, id='self', ctx=Load()),
                                                    attr='_context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=18, col_offset=68, end_lineno=18, end_col_offset=80, value='active_ids', kind=None),
                                                ctx=Load(),
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
                                    end_col_offset=70,
                                    targets=[Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=23, id='new_invoice', ctx=Store())],
                                    value=Call(
                                        lineno=19,
                                        col_offset=26,
                                        end_lineno=19,
                                        end_col_offset=70,
                                        func=Attribute(
                                            lineno=19,
                                            col_offset=26,
                                            end_lineno=19,
                                            end_col_offset=50,
                                            value=Name(lineno=19, col_offset=26, end_lineno=19, end_col_offset=33, id='repairs', ctx=Load()),
                                            attr='_create_invoices',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                lineno=19,
                                                col_offset=51,
                                                end_lineno=19,
                                                end_col_offset=69,
                                                arg='group',
                                                value=Attribute(
                                                    lineno=19,
                                                    col_offset=57,
                                                    end_lineno=19,
                                                    end_col_offset=69,
                                                    value=Name(lineno=19, col_offset=57, end_lineno=19, end_col_offset=63, id='wizard', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    lineno=24,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=50,
                                    value=Call(
                                        lineno=24,
                                        col_offset=12,
                                        end_lineno=24,
                                        end_col_offset=50,
                                        func=Attribute(
                                            lineno=24,
                                            col_offset=12,
                                            end_lineno=24,
                                            end_col_offset=48,
                                            value=Name(lineno=24, col_offset=12, end_lineno=24, end_col_offset=19, id='repairs', ctx=Load()),
                                            attr='action_repair_invoice_create',
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
                            lineno=25,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=9,
                            value=Dict(
                                lineno=25,
                                col_offset=15,
                                end_lineno=34,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=20, value='domain', kind=None),
                                    Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=18, value='name', kind=None),
                                    Constant(lineno=28, col_offset=12, end_lineno=28, end_col_offset=23, value='view_mode', kind=None),
                                    Constant(lineno=29, col_offset=12, end_lineno=29, end_col_offset=23, value='res_model', kind=None),
                                    Constant(lineno=30, col_offset=12, end_lineno=30, end_col_offset=21, value='view_id', kind=None),
                                    Constant(lineno=31, col_offset=12, end_lineno=31, end_col_offset=19, value='views', kind=None),
                                    Constant(lineno=32, col_offset=12, end_lineno=32, end_col_offset=21, value='context', kind=None),
                                    Constant(lineno=33, col_offset=12, end_lineno=33, end_col_offset=18, value='type', kind=None),
                                ],
                                values=[
                                    List(
                                        lineno=26,
                                        col_offset=22,
                                        end_lineno=26,
                                        end_col_offset=64,
                                        elts=[
                                            Tuple(
                                                lineno=26,
                                                col_offset=23,
                                                end_lineno=26,
                                                end_col_offset=63,
                                                elts=[
                                                    Constant(lineno=26, col_offset=24, end_lineno=26, end_col_offset=28, value='id', kind=None),
                                                    Constant(lineno=26, col_offset=30, end_lineno=26, end_col_offset=34, value='in', kind=None),
                                                    Call(
                                                        lineno=26,
                                                        col_offset=36,
                                                        end_lineno=26,
                                                        end_col_offset=62,
                                                        func=Name(lineno=26, col_offset=36, end_lineno=26, end_col_offset=40, id='list', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                lineno=26,
                                                                col_offset=41,
                                                                end_lineno=26,
                                                                end_col_offset=61,
                                                                func=Attribute(
                                                                    lineno=26,
                                                                    col_offset=41,
                                                                    end_lineno=26,
                                                                    end_col_offset=59,
                                                                    value=Name(lineno=26, col_offset=41, end_lineno=26, end_col_offset=52, id='new_invoice', ctx=Load()),
                                                                    attr='values',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=27, col_offset=20, end_lineno=27, end_col_offset=30, value='Invoices', kind=None),
                                    Constant(lineno=28, col_offset=25, end_lineno=28, end_col_offset=36, value='tree,form', kind=None),
                                    Constant(lineno=29, col_offset=25, end_lineno=29, end_col_offset=39, value='account.move', kind=None),
                                    Constant(lineno=30, col_offset=23, end_lineno=30, end_col_offset=28, value=False, kind=None),
                                    List(
                                        lineno=31,
                                        col_offset=21,
                                        end_lineno=31,
                                        end_col_offset=127,
                                        elts=[
                                            Tuple(
                                                lineno=31,
                                                col_offset=22,
                                                end_lineno=31,
                                                end_col_offset=73,
                                                elts=[
                                                    Attribute(
                                                        lineno=31,
                                                        col_offset=23,
                                                        end_lineno=31,
                                                        end_col_offset=64,
                                                        value=Call(
                                                            lineno=31,
                                                            col_offset=23,
                                                            end_lineno=31,
                                                            end_col_offset=61,
                                                            func=Attribute(
                                                                lineno=31,
                                                                col_offset=23,
                                                                end_lineno=31,
                                                                end_col_offset=35,
                                                                value=Attribute(
                                                                    lineno=31,
                                                                    col_offset=23,
                                                                    end_lineno=31,
                                                                    end_col_offset=31,
                                                                    value=Name(lineno=31, col_offset=23, end_lineno=31, end_col_offset=27, id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(lineno=31, col_offset=36, end_lineno=31, end_col_offset=60, value='account.view_move_tree', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=31, col_offset=66, end_lineno=31, end_col_offset=72, value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=31,
                                                col_offset=75,
                                                end_lineno=31,
                                                end_col_offset=126,
                                                elts=[
                                                    Attribute(
                                                        lineno=31,
                                                        col_offset=76,
                                                        end_lineno=31,
                                                        end_col_offset=117,
                                                        value=Call(
                                                            lineno=31,
                                                            col_offset=76,
                                                            end_lineno=31,
                                                            end_col_offset=114,
                                                            func=Attribute(
                                                                lineno=31,
                                                                col_offset=76,
                                                                end_lineno=31,
                                                                end_col_offset=88,
                                                                value=Attribute(
                                                                    lineno=31,
                                                                    col_offset=76,
                                                                    end_lineno=31,
                                                                    end_col_offset=84,
                                                                    value=Name(lineno=31, col_offset=76, end_lineno=31, end_col_offset=80, id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(lineno=31, col_offset=89, end_lineno=31, end_col_offset=113, value='account.view_move_form', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=31, col_offset=119, end_lineno=31, end_col_offset=125, value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=32, col_offset=23, end_lineno=32, end_col_offset=52, value="{'move_type':'out_invoice'}", kind=None),
                                    Constant(lineno=33, col_offset=20, end_lineno=33, end_col_offset=43, value='ir.actions.act_window', kind=None),
                                ],
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
