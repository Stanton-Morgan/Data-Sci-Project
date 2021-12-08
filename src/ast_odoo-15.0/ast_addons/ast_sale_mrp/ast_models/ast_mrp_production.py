Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=39,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=38,
            end_col_offset=21,
            name='MrpProduction',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=20,
                    end_lineno=7,
                    end_col_offset=32,
                    value=Name(lineno=7, col_offset=20, end_lineno=7, end_col_offset=26, id='models', ctx=Load()),
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
                    end_col_offset=31,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=31, value='mrp.production', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=48,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=20, id='sale_order_count', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=23,
                        end_lineno=13,
                        end_col_offset=48,
                        func=Attribute(
                            lineno=10,
                            col_offset=23,
                            end_lineno=10,
                            end_col_offset=37,
                            value=Name(lineno=10, col_offset=23, end_lineno=10, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=8, end_lineno=11, end_col_offset=28, value='Count of Source SO', kind=None)],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=43,
                                arg='compute',
                                value=Constant(lineno=12, col_offset=16, end_lineno=12, end_col_offset=43, value='_compute_sale_order_count', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=47,
                                arg='groups',
                                value=Constant(lineno=13, col_offset=15, end_lineno=13, end_col_offset=47, value='sales_team.group_sale_salesman', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=128,
                    name='_compute_sale_order_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=34, end_lineno=16, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            lineno=17,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=128,
                            target=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=22, id='production', ctx=Store()),
                            iter=Name(lineno=17, col_offset=26, end_lineno=17, end_col_offset=30, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=18,
                                    end_col_offset=128,
                                    targets=[
                                        Attribute(
                                            lineno=18,
                                            col_offset=12,
                                            end_lineno=18,
                                            end_col_offset=39,
                                            value=Name(lineno=18, col_offset=12, end_lineno=18, end_col_offset=22, id='production', ctx=Load()),
                                            attr='sale_order_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=18,
                                        col_offset=42,
                                        end_lineno=18,
                                        end_col_offset=128,
                                        func=Name(lineno=18, col_offset=42, end_lineno=18, end_col_offset=45, id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                lineno=18,
                                                col_offset=46,
                                                end_lineno=18,
                                                end_col_offset=127,
                                                value=Attribute(
                                                    lineno=18,
                                                    col_offset=46,
                                                    end_lineno=18,
                                                    end_col_offset=119,
                                                    value=Attribute(
                                                        lineno=18,
                                                        col_offset=46,
                                                        end_lineno=18,
                                                        end_col_offset=110,
                                                        value=Attribute(
                                                            lineno=18,
                                                            col_offset=46,
                                                            end_lineno=18,
                                                            end_col_offset=96,
                                                            value=Attribute(
                                                                lineno=18,
                                                                col_offset=46,
                                                                end_lineno=18,
                                                                end_col_offset=77,
                                                                value=Name(lineno=18, col_offset=46, end_lineno=18, end_col_offset=56, id='production', ctx=Load()),
                                                                attr='procurement_group_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='mrp_production_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='move_dest_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='group_id',
                                                    ctx=Load(),
                                                ),
                                                attr='sale_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=15,
                            col_offset=5,
                            end_lineno=15,
                            end_col_offset=90,
                            func=Attribute(
                                lineno=15,
                                col_offset=5,
                                end_lineno=15,
                                end_col_offset=16,
                                value=Name(lineno=15, col_offset=5, end_lineno=15, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=15, col_offset=17, end_lineno=15, end_col_offset=89, value='procurement_group_id.mrp_production_ids.move_dest_ids.group_id.sale_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=20,
                    col_offset=4,
                    end_lineno=38,
                    end_col_offset=21,
                    name='action_view_sale_orders',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=20, col_offset=32, end_lineno=20, end_col_offset=36, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=25,
                            value=Call(
                                lineno=21,
                                col_offset=8,
                                end_lineno=21,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=8,
                                    end_lineno=21,
                                    end_col_offset=23,
                                    value=Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=104,
                            targets=[Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=22, id='sale_order_ids', ctx=Store())],
                            value=Attribute(
                                lineno=22,
                                col_offset=25,
                                end_lineno=22,
                                end_col_offset=104,
                                value=Attribute(
                                    lineno=22,
                                    col_offset=25,
                                    end_lineno=22,
                                    end_col_offset=100,
                                    value=Attribute(
                                        lineno=22,
                                        col_offset=25,
                                        end_lineno=22,
                                        end_col_offset=92,
                                        value=Attribute(
                                            lineno=22,
                                            col_offset=25,
                                            end_lineno=22,
                                            end_col_offset=83,
                                            value=Attribute(
                                                lineno=22,
                                                col_offset=25,
                                                end_lineno=22,
                                                end_col_offset=69,
                                                value=Attribute(
                                                    lineno=22,
                                                    col_offset=25,
                                                    end_lineno=22,
                                                    end_col_offset=50,
                                                    value=Name(lineno=22, col_offset=25, end_lineno=22, end_col_offset=29, id='self', ctx=Load()),
                                                    attr='procurement_group_id',
                                                    ctx=Load(),
                                                ),
                                                attr='mrp_production_ids',
                                                ctx=Load(),
                                            ),
                                            attr='move_dest_ids',
                                            ctx=Load(),
                                        ),
                                        attr='group_id',
                                        ctx=Load(),
                                    ),
                                    attr='sale_id',
                                    ctx=Load(),
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=9,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=14, id='action', ctx=Store())],
                            value=Dict(
                                lineno=23,
                                col_offset=17,
                                end_lineno=26,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=24, col_offset=12, end_lineno=24, end_col_offset=23, value='res_model', kind=None),
                                    Constant(lineno=25, col_offset=12, end_lineno=25, end_col_offset=18, value='type', kind=None),
                                ],
                                values=[
                                    Constant(lineno=24, col_offset=25, end_lineno=24, end_col_offset=37, value='sale.order', kind=None),
                                    Constant(lineno=25, col_offset=20, end_lineno=25, end_col_offset=43, value='ir.actions.act_window', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=27,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=14,
                            test=Compare(
                                lineno=27,
                                col_offset=11,
                                end_lineno=27,
                                end_col_offset=35,
                                left=Call(
                                    lineno=27,
                                    col_offset=11,
                                    end_lineno=27,
                                    end_col_offset=30,
                                    func=Name(lineno=27, col_offset=11, end_lineno=27, end_col_offset=14, id='len', ctx=Load()),
                                    args=[Name(lineno=27, col_offset=15, end_lineno=27, end_col_offset=29, id='sale_order_ids', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(lineno=27, col_offset=34, end_lineno=27, end_col_offset=35, value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    lineno=28,
                                    col_offset=12,
                                    end_lineno=31,
                                    end_col_offset=14,
                                    value=Call(
                                        lineno=28,
                                        col_offset=12,
                                        end_lineno=31,
                                        end_col_offset=14,
                                        func=Attribute(
                                            lineno=28,
                                            col_offset=12,
                                            end_lineno=28,
                                            end_col_offset=25,
                                            value=Name(lineno=28, col_offset=12, end_lineno=28, end_col_offset=18, id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=28,
                                                col_offset=26,
                                                end_lineno=31,
                                                end_col_offset=13,
                                                keys=[
                                                    Constant(lineno=29, col_offset=16, end_lineno=29, end_col_offset=27, value='view_mode', kind=None),
                                                    Constant(lineno=30, col_offset=16, end_lineno=30, end_col_offset=24, value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(lineno=29, col_offset=29, end_lineno=29, end_col_offset=35, value='form', kind=None),
                                                    Subscript(
                                                        lineno=30,
                                                        col_offset=26,
                                                        end_lineno=30,
                                                        end_col_offset=43,
                                                        value=Name(lineno=30, col_offset=26, end_lineno=30, end_col_offset=40, id='sale_order_ids', ctx=Load()),
                                                        slice=Constant(lineno=30, col_offset=41, end_lineno=30, end_col_offset=42, value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    lineno=33,
                                    col_offset=12,
                                    end_lineno=37,
                                    end_col_offset=14,
                                    value=Call(
                                        lineno=33,
                                        col_offset=12,
                                        end_lineno=37,
                                        end_col_offset=14,
                                        func=Attribute(
                                            lineno=33,
                                            col_offset=12,
                                            end_lineno=33,
                                            end_col_offset=25,
                                            value=Name(lineno=33, col_offset=12, end_lineno=33, end_col_offset=18, id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=33,
                                                col_offset=26,
                                                end_lineno=37,
                                                end_col_offset=13,
                                                keys=[
                                                    Constant(lineno=34, col_offset=16, end_lineno=34, end_col_offset=22, value='name', kind=None),
                                                    Constant(lineno=35, col_offset=16, end_lineno=35, end_col_offset=24, value='domain', kind=None),
                                                    Constant(lineno=36, col_offset=16, end_lineno=36, end_col_offset=27, value='view_mode', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        lineno=34,
                                                        col_offset=24,
                                                        end_lineno=34,
                                                        end_col_offset=65,
                                                        func=Name(lineno=34, col_offset=24, end_lineno=34, end_col_offset=25, id='_', ctx=Load()),
                                                        args=[
                                                            Constant(lineno=34, col_offset=26, end_lineno=34, end_col_offset=53, value='Sources Sale Orders of %s', kind=None),
                                                            Attribute(
                                                                lineno=34,
                                                                col_offset=55,
                                                                end_lineno=34,
                                                                end_col_offset=64,
                                                                value=Name(lineno=34, col_offset=55, end_lineno=34, end_col_offset=59, id='self', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        lineno=35,
                                                        col_offset=26,
                                                        end_lineno=35,
                                                        end_col_offset=56,
                                                        elts=[
                                                            Tuple(
                                                                lineno=35,
                                                                col_offset=27,
                                                                end_lineno=35,
                                                                end_col_offset=55,
                                                                elts=[
                                                                    Constant(lineno=35, col_offset=28, end_lineno=35, end_col_offset=32, value='id', kind=None),
                                                                    Constant(lineno=35, col_offset=34, end_lineno=35, end_col_offset=38, value='in', kind=None),
                                                                    Name(lineno=35, col_offset=40, end_lineno=35, end_col_offset=54, id='sale_order_ids', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=36, col_offset=29, end_lineno=36, end_col_offset=40, value='tree,form', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            lineno=38,
                            col_offset=8,
                            end_lineno=38,
                            end_col_offset=21,
                            value=Name(lineno=38, col_offset=15, end_lineno=38, end_col_offset=21, id='action', ctx=Load()),
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