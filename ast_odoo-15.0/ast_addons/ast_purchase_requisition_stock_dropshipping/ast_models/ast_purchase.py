Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=16,
            end_col_offset=74,
            name='PurchaseOrder',
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
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=31, value='purchase.order', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=74,
                    name='_onchange_requisition_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=33, end_lineno=11, end_col_offset=37, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=42,
                            value=Call(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=42,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=40,
                                    value=Call(
                                        lineno=12,
                                        col_offset=8,
                                        end_lineno=12,
                                        end_col_offset=15,
                                        func=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=13, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_onchange_requisition_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            lineno=13,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=74,
                            test=BoolOp(
                                lineno=13,
                                col_offset=11,
                                end_lineno=13,
                                end_col_offset=75,
                                op=And(),
                                values=[
                                    Attribute(
                                        lineno=13,
                                        col_offset=11,
                                        end_lineno=13,
                                        end_col_offset=30,
                                        value=Name(lineno=13, col_offset=11, end_lineno=13, end_col_offset=15, id='self', ctx=Load()),
                                        attr='requisition_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=13,
                                        col_offset=35,
                                        end_lineno=13,
                                        end_col_offset=75,
                                        value=Attribute(
                                            lineno=13,
                                            col_offset=35,
                                            end_lineno=13,
                                            end_col_offset=54,
                                            value=Name(lineno=13, col_offset=35, end_lineno=13, end_col_offset=39, id='self', ctx=Load()),
                                            attr='requisition_id',
                                            ctx=Load(),
                                        ),
                                        attr='procurement_group_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=14,
                                    end_col_offset=71,
                                    targets=[
                                        Attribute(
                                            lineno=14,
                                            col_offset=12,
                                            end_lineno=14,
                                            end_col_offset=25,
                                            value=Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=16, id='self', ctx=Load()),
                                            attr='group_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        lineno=14,
                                        col_offset=28,
                                        end_lineno=14,
                                        end_col_offset=71,
                                        value=Attribute(
                                            lineno=14,
                                            col_offset=28,
                                            end_lineno=14,
                                            end_col_offset=68,
                                            value=Attribute(
                                                lineno=14,
                                                col_offset=28,
                                                end_lineno=14,
                                                end_col_offset=47,
                                                value=Name(lineno=14, col_offset=28, end_lineno=14, end_col_offset=32, id='self', ctx=Load()),
                                                attr='requisition_id',
                                                ctx=Load(),
                                            ),
                                            attr='procurement_group_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    lineno=15,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=74,
                                    test=Attribute(
                                        lineno=15,
                                        col_offset=15,
                                        end_lineno=15,
                                        end_col_offset=47,
                                        value=Attribute(
                                            lineno=15,
                                            col_offset=15,
                                            end_lineno=15,
                                            end_col_offset=36,
                                            value=Attribute(
                                                lineno=15,
                                                col_offset=15,
                                                end_lineno=15,
                                                end_col_offset=28,
                                                value=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=19, id='self', ctx=Load()),
                                                attr='group_id',
                                                ctx=Load(),
                                            ),
                                            attr='sale_id',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            lineno=16,
                                            col_offset=16,
                                            end_lineno=16,
                                            end_col_offset=74,
                                            targets=[
                                                Attribute(
                                                    lineno=16,
                                                    col_offset=16,
                                                    end_lineno=16,
                                                    end_col_offset=36,
                                                    value=Name(lineno=16, col_offset=16, end_lineno=16, end_col_offset=20, id='self', ctx=Load()),
                                                    attr='dest_address_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                lineno=16,
                                                col_offset=39,
                                                end_lineno=16,
                                                end_col_offset=74,
                                                value=Attribute(
                                                    lineno=16,
                                                    col_offset=39,
                                                    end_lineno=16,
                                                    end_col_offset=71,
                                                    value=Attribute(
                                                        lineno=16,
                                                        col_offset=39,
                                                        end_lineno=16,
                                                        end_col_offset=60,
                                                        value=Attribute(
                                                            lineno=16,
                                                            col_offset=39,
                                                            end_lineno=16,
                                                            end_col_offset=52,
                                                            value=Name(lineno=16, col_offset=39, end_lineno=16, end_col_offset=43, id='self', ctx=Load()),
                                                            attr='group_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='sale_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=10,
                            col_offset=5,
                            end_lineno=10,
                            end_col_offset=35,
                            func=Attribute(
                                lineno=10,
                                col_offset=5,
                                end_lineno=10,
                                end_col_offset=17,
                                value=Name(lineno=10, col_offset=5, end_lineno=10, end_col_offset=8, id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=10, col_offset=18, end_lineno=10, end_col_offset=34, value='requisition_id', kind=None)],
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
