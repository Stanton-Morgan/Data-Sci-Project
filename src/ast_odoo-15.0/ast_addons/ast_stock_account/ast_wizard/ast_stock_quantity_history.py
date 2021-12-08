Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=43,
            module='odoo.tools.misc',
            names=[alias(name='format_datetime', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=18,
            end_col_offset=63,
            name='StockQuantityHistory',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=27,
                    end_lineno=7,
                    end_col_offset=48,
                    value=Name(lineno=7, col_offset=27, end_lineno=7, end_col_offset=33, id='models', ctx=Load()),
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
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=39, value='stock.quantity.history', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=63,
                    name='open_at_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=21, end_lineno=10, end_col_offset=25, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=59,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=20, id='active_model', ctx=Store())],
                            value=Call(
                                lineno=11,
                                col_offset=23,
                                end_lineno=11,
                                end_col_offset=59,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=23,
                                    end_lineno=11,
                                    end_col_offset=43,
                                    value=Attribute(
                                        lineno=11,
                                        col_offset=23,
                                        end_lineno=11,
                                        end_col_offset=39,
                                        value=Attribute(
                                            lineno=11,
                                            col_offset=23,
                                            end_lineno=11,
                                            end_col_offset=31,
                                            value=Name(lineno=11, col_offset=23, end_lineno=11, end_col_offset=27, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=11, col_offset=44, end_lineno=11, end_col_offset=58, value='active_model', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=12,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=25,
                            test=Compare(
                                lineno=12,
                                col_offset=11,
                                end_lineno=12,
                                end_col_offset=50,
                                left=Name(lineno=12, col_offset=11, end_lineno=12, end_col_offset=23, id='active_model', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(lineno=12, col_offset=27, end_lineno=12, end_col_offset=50, value='stock.valuation.layer', kind=None)],
                            ),
                            body=[
                                Assign(
                                    lineno=13,
                                    col_offset=12,
                                    end_lineno=13,
                                    end_col_offset=109,
                                    targets=[Name(lineno=13, col_offset=12, end_lineno=13, end_col_offset=18, id='action', ctx=Store())],
                                    value=Call(
                                        lineno=13,
                                        col_offset=21,
                                        end_lineno=13,
                                        end_col_offset=109,
                                        func=Attribute(
                                            lineno=13,
                                            col_offset=21,
                                            end_lineno=13,
                                            end_col_offset=63,
                                            value=Subscript(
                                                lineno=13,
                                                col_offset=21,
                                                end_lineno=13,
                                                end_col_offset=51,
                                                value=Attribute(
                                                    lineno=13,
                                                    col_offset=21,
                                                    end_lineno=13,
                                                    end_col_offset=29,
                                                    value=Name(lineno=13, col_offset=21, end_lineno=13, end_col_offset=25, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=13, col_offset=30, end_lineno=13, end_col_offset=50, value='ir.actions.actions', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_for_xml_id',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=13, col_offset=64, end_lineno=13, end_col_offset=108, value='stock_account.stock_valuation_layer_action', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=14,
                                    end_col_offset=116,
                                    targets=[
                                        Subscript(
                                            lineno=14,
                                            col_offset=12,
                                            end_lineno=14,
                                            end_col_offset=28,
                                            value=Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=18, id='action', ctx=Load()),
                                            slice=Constant(lineno=14, col_offset=19, end_lineno=14, end_col_offset=27, value='domain', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        lineno=14,
                                        col_offset=31,
                                        end_lineno=14,
                                        end_col_offset=116,
                                        elts=[
                                            Tuple(
                                                lineno=14,
                                                col_offset=32,
                                                end_lineno=14,
                                                end_col_offset=78,
                                                elts=[
                                                    Constant(lineno=14, col_offset=33, end_lineno=14, end_col_offset=46, value='create_date', kind=None),
                                                    Constant(lineno=14, col_offset=48, end_lineno=14, end_col_offset=52, value='<=', kind=None),
                                                    Attribute(
                                                        lineno=14,
                                                        col_offset=54,
                                                        end_lineno=14,
                                                        end_col_offset=77,
                                                        value=Name(lineno=14, col_offset=54, end_lineno=14, end_col_offset=58, id='self', ctx=Load()),
                                                        attr='inventory_datetime',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=14,
                                                col_offset=80,
                                                end_lineno=14,
                                                end_col_offset=115,
                                                elts=[
                                                    Constant(lineno=14, col_offset=81, end_lineno=14, end_col_offset=98, value='product_id.type', kind=None),
                                                    Constant(lineno=14, col_offset=100, end_lineno=14, end_col_offset=103, value='=', kind=None),
                                                    Constant(lineno=14, col_offset=105, end_lineno=14, end_col_offset=114, value='product', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=15,
                                    col_offset=12,
                                    end_lineno=15,
                                    end_col_offset=87,
                                    targets=[
                                        Subscript(
                                            lineno=15,
                                            col_offset=12,
                                            end_lineno=15,
                                            end_col_offset=34,
                                            value=Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=18, id='action', ctx=Load()),
                                            slice=Constant(lineno=15, col_offset=19, end_lineno=15, end_col_offset=33, value='display_name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=15,
                                        col_offset=37,
                                        end_lineno=15,
                                        end_col_offset=87,
                                        func=Name(lineno=15, col_offset=37, end_lineno=15, end_col_offset=52, id='format_datetime', ctx=Load()),
                                        args=[
                                            Attribute(
                                                lineno=15,
                                                col_offset=53,
                                                end_lineno=15,
                                                end_col_offset=61,
                                                value=Name(lineno=15, col_offset=53, end_lineno=15, end_col_offset=57, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=15,
                                                col_offset=63,
                                                end_lineno=15,
                                                end_col_offset=86,
                                                value=Name(lineno=15, col_offset=63, end_lineno=15, end_col_offset=67, id='self', ctx=Load()),
                                                attr='inventory_datetime',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=25,
                                    value=Name(lineno=16, col_offset=19, end_lineno=16, end_col_offset=25, id='action', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=63,
                            value=Call(
                                lineno=18,
                                col_offset=15,
                                end_lineno=18,
                                end_col_offset=63,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=15,
                                    end_lineno=18,
                                    end_col_offset=61,
                                    value=Call(
                                        lineno=18,
                                        col_offset=15,
                                        end_lineno=18,
                                        end_col_offset=48,
                                        func=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=20, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=18, col_offset=21, end_lineno=18, end_col_offset=41, id='StockQuantityHistory', ctx=Load()),
                                            Name(lineno=18, col_offset=43, end_lineno=18, end_col_offset=47, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='open_at_date',
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