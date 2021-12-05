Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
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
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=31,
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=37,
            end_col_offset=21,
            name='StockQuantityHistory',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=27,
                    end_lineno=8,
                    end_col_offset=48,
                    value=Name(lineno=8, col_offset=27, end_lineno=8, end_col_offset=33, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=36,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=9, col_offset=12, end_lineno=9, end_col_offset=36, value='stock.quantity.history', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=43,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=10, col_offset=19, end_lineno=10, end_col_offset=43, value='Stock Quantity History', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=36,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=22, id='inventory_datetime', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=25,
                        end_lineno=14,
                        end_col_offset=36,
                        func=Attribute(
                            lineno=12,
                            col_offset=25,
                            end_lineno=12,
                            end_col_offset=40,
                            value=Name(lineno=12, col_offset=25, end_lineno=12, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=41, end_lineno=12, end_col_offset=60, value='Inventory at Date', kind=None)],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=62,
                                arg='help',
                                value=Constant(lineno=13, col_offset=13, end_lineno=13, end_col_offset=62, value='Choose a date to get the inventory at that date', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=35,
                                arg='default',
                                value=Attribute(
                                    lineno=14,
                                    col_offset=16,
                                    end_lineno=14,
                                    end_col_offset=35,
                                    value=Attribute(
                                        lineno=14,
                                        col_offset=16,
                                        end_lineno=14,
                                        end_col_offset=31,
                                        value=Name(lineno=14, col_offset=16, end_lineno=14, end_col_offset=22, id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='now',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=37,
                    end_col_offset=21,
                    name='open_at_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=21, end_lineno=16, end_col_offset=25, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=71,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=20, id='tree_view_id', ctx=Store())],
                            value=Attribute(
                                lineno=17,
                                col_offset=23,
                                end_lineno=17,
                                end_col_offset=71,
                                value=Call(
                                    lineno=17,
                                    col_offset=23,
                                    end_lineno=17,
                                    end_col_offset=68,
                                    func=Attribute(
                                        lineno=17,
                                        col_offset=23,
                                        end_lineno=17,
                                        end_col_offset=35,
                                        value=Attribute(
                                            lineno=17,
                                            col_offset=23,
                                            end_lineno=17,
                                            end_col_offset=31,
                                            value=Name(lineno=17, col_offset=23, end_lineno=17, end_col_offset=27, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=17, col_offset=36, end_lineno=17, end_col_offset=67, value='stock.view_stock_product_tree', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=84,
                            targets=[Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=20, id='form_view_id', ctx=Store())],
                            value=Attribute(
                                lineno=18,
                                col_offset=23,
                                end_lineno=18,
                                end_col_offset=84,
                                value=Call(
                                    lineno=18,
                                    col_offset=23,
                                    end_lineno=18,
                                    end_col_offset=81,
                                    func=Attribute(
                                        lineno=18,
                                        col_offset=23,
                                        end_lineno=18,
                                        end_col_offset=35,
                                        value=Attribute(
                                            lineno=18,
                                            col_offset=23,
                                            end_lineno=18,
                                            end_col_offset=31,
                                            value=Name(lineno=18, col_offset=23, end_lineno=18, end_col_offset=27, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=18, col_offset=36, end_lineno=18, end_col_offset=80, value='stock.product_form_view_procurement_button', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=43,
                            targets=[Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=14, id='domain', ctx=Store())],
                            value=List(
                                lineno=19,
                                col_offset=17,
                                end_lineno=19,
                                end_col_offset=43,
                                elts=[
                                    Tuple(
                                        lineno=19,
                                        col_offset=18,
                                        end_lineno=19,
                                        end_col_offset=42,
                                        elts=[
                                            Constant(lineno=19, col_offset=19, end_lineno=19, end_col_offset=25, value='type', kind=None),
                                            Constant(lineno=19, col_offset=27, end_lineno=19, end_col_offset=30, value='=', kind=None),
                                            Constant(lineno=19, col_offset=32, end_lineno=19, end_col_offset=41, value='product', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=62,
                            targets=[Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=18, id='product_id', ctx=Store())],
                            value=Call(
                                lineno=20,
                                col_offset=21,
                                end_lineno=20,
                                end_col_offset=62,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=21,
                                    end_lineno=20,
                                    end_col_offset=41,
                                    value=Attribute(
                                        lineno=20,
                                        col_offset=21,
                                        end_lineno=20,
                                        end_col_offset=37,
                                        value=Attribute(
                                            lineno=20,
                                            col_offset=21,
                                            end_lineno=20,
                                            end_col_offset=29,
                                            value=Name(lineno=20, col_offset=21, end_lineno=20, end_col_offset=25, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=20, col_offset=42, end_lineno=20, end_col_offset=54, value='product_id', kind=None),
                                    Constant(lineno=20, col_offset=56, end_lineno=20, end_col_offset=61, value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=72,
                            targets=[Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=23, id='product_tmpl_id', ctx=Store())],
                            value=Call(
                                lineno=21,
                                col_offset=26,
                                end_lineno=21,
                                end_col_offset=72,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=26,
                                    end_lineno=21,
                                    end_col_offset=46,
                                    value=Attribute(
                                        lineno=21,
                                        col_offset=26,
                                        end_lineno=21,
                                        end_col_offset=42,
                                        value=Attribute(
                                            lineno=21,
                                            col_offset=26,
                                            end_lineno=21,
                                            end_col_offset=34,
                                            value=Name(lineno=21, col_offset=26, end_lineno=21, end_col_offset=30, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=21, col_offset=47, end_lineno=21, end_col_offset=64, value='product_tmpl_id', kind=None),
                                    Constant(lineno=21, col_offset=66, end_lineno=21, end_col_offset=71, value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=22,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=90,
                            test=Name(lineno=22, col_offset=11, end_lineno=22, end_col_offset=21, id='product_id', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=23,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=72,
                                    targets=[Name(lineno=23, col_offset=12, end_lineno=23, end_col_offset=18, id='domain', ctx=Store())],
                                    value=Call(
                                        lineno=23,
                                        col_offset=21,
                                        end_lineno=23,
                                        end_col_offset=72,
                                        func=Attribute(
                                            lineno=23,
                                            col_offset=21,
                                            end_lineno=23,
                                            end_col_offset=35,
                                            value=Name(lineno=23, col_offset=21, end_lineno=23, end_col_offset=31, id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                lineno=23,
                                                col_offset=36,
                                                end_lineno=23,
                                                end_col_offset=71,
                                                elts=[
                                                    Name(lineno=23, col_offset=37, end_lineno=23, end_col_offset=43, id='domain', ctx=Load()),
                                                    List(
                                                        lineno=23,
                                                        col_offset=45,
                                                        end_lineno=23,
                                                        end_col_offset=70,
                                                        elts=[
                                                            Tuple(
                                                                lineno=23,
                                                                col_offset=46,
                                                                end_lineno=23,
                                                                end_col_offset=69,
                                                                elts=[
                                                                    Constant(lineno=23, col_offset=47, end_lineno=23, end_col_offset=51, value='id', kind=None),
                                                                    Constant(lineno=23, col_offset=53, end_lineno=23, end_col_offset=56, value='=', kind=None),
                                                                    Name(lineno=23, col_offset=58, end_lineno=23, end_col_offset=68, id='product_id', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    lineno=24,
                                    col_offset=8,
                                    end_lineno=25,
                                    end_col_offset=90,
                                    test=Name(lineno=24, col_offset=13, end_lineno=24, end_col_offset=28, id='product_tmpl_id', ctx=Load()),
                                    body=[
                                        Assign(
                                            lineno=25,
                                            col_offset=12,
                                            end_lineno=25,
                                            end_col_offset=90,
                                            targets=[Name(lineno=25, col_offset=12, end_lineno=25, end_col_offset=18, id='domain', ctx=Store())],
                                            value=Call(
                                                lineno=25,
                                                col_offset=21,
                                                end_lineno=25,
                                                end_col_offset=90,
                                                func=Attribute(
                                                    lineno=25,
                                                    col_offset=21,
                                                    end_lineno=25,
                                                    end_col_offset=35,
                                                    value=Name(lineno=25, col_offset=21, end_lineno=25, end_col_offset=31, id='expression', ctx=Load()),
                                                    attr='AND',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        lineno=25,
                                                        col_offset=36,
                                                        end_lineno=25,
                                                        end_col_offset=89,
                                                        elts=[
                                                            Name(lineno=25, col_offset=37, end_lineno=25, end_col_offset=43, id='domain', ctx=Load()),
                                                            List(
                                                                lineno=25,
                                                                col_offset=45,
                                                                end_lineno=25,
                                                                end_col_offset=88,
                                                                elts=[
                                                                    Tuple(
                                                                        lineno=25,
                                                                        col_offset=46,
                                                                        end_lineno=25,
                                                                        end_col_offset=87,
                                                                        elts=[
                                                                            Constant(lineno=25, col_offset=47, end_lineno=25, end_col_offset=64, value='product_tmpl_id', kind=None),
                                                                            Constant(lineno=25, col_offset=66, end_lineno=25, end_col_offset=69, value='=', kind=None),
                                                                            Name(lineno=25, col_offset=71, end_lineno=25, end_col_offset=86, id='product_tmpl_id', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            lineno=28,
                            col_offset=8,
                            end_lineno=36,
                            end_col_offset=9,
                            targets=[Name(lineno=28, col_offset=8, end_lineno=28, end_col_offset=14, id='action', ctx=Store())],
                            value=Dict(
                                lineno=28,
                                col_offset=17,
                                end_lineno=36,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=29, col_offset=12, end_lineno=29, end_col_offset=18, value='type', kind=None),
                                    Constant(lineno=30, col_offset=12, end_lineno=30, end_col_offset=19, value='views', kind=None),
                                    Constant(lineno=31, col_offset=12, end_lineno=31, end_col_offset=23, value='view_mode', kind=None),
                                    Constant(lineno=32, col_offset=12, end_lineno=32, end_col_offset=18, value='name', kind=None),
                                    Constant(lineno=33, col_offset=12, end_lineno=33, end_col_offset=23, value='res_model', kind=None),
                                    Constant(lineno=34, col_offset=12, end_lineno=34, end_col_offset=20, value='domain', kind=None),
                                    Constant(lineno=35, col_offset=12, end_lineno=35, end_col_offset=21, value='context', kind=None),
                                ],
                                values=[
                                    Constant(lineno=29, col_offset=20, end_lineno=29, end_col_offset=43, value='ir.actions.act_window', kind=None),
                                    List(
                                        lineno=30,
                                        col_offset=21,
                                        end_lineno=30,
                                        end_col_offset=69,
                                        elts=[
                                            Tuple(
                                                lineno=30,
                                                col_offset=22,
                                                end_lineno=30,
                                                end_col_offset=44,
                                                elts=[
                                                    Name(lineno=30, col_offset=23, end_lineno=30, end_col_offset=35, id='tree_view_id', ctx=Load()),
                                                    Constant(lineno=30, col_offset=37, end_lineno=30, end_col_offset=43, value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=30,
                                                col_offset=46,
                                                end_lineno=30,
                                                end_col_offset=68,
                                                elts=[
                                                    Name(lineno=30, col_offset=47, end_lineno=30, end_col_offset=59, id='form_view_id', ctx=Load()),
                                                    Constant(lineno=30, col_offset=61, end_lineno=30, end_col_offset=67, value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=31, col_offset=25, end_lineno=31, end_col_offset=36, value='tree,form', kind=None),
                                    Call(
                                        lineno=32,
                                        col_offset=20,
                                        end_lineno=32,
                                        end_col_offset=33,
                                        func=Name(lineno=32, col_offset=20, end_lineno=32, end_col_offset=21, id='_', ctx=Load()),
                                        args=[Constant(lineno=32, col_offset=22, end_lineno=32, end_col_offset=32, value='Products', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(lineno=33, col_offset=25, end_lineno=33, end_col_offset=42, value='product.product', kind=None),
                                    Name(lineno=34, col_offset=22, end_lineno=34, end_col_offset=28, id='domain', ctx=Load()),
                                    Call(
                                        lineno=35,
                                        col_offset=23,
                                        end_lineno=35,
                                        end_col_offset=78,
                                        func=Name(lineno=35, col_offset=23, end_lineno=35, end_col_offset=27, id='dict', ctx=Load()),
                                        args=[
                                            Attribute(
                                                lineno=35,
                                                col_offset=28,
                                                end_lineno=35,
                                                end_col_offset=44,
                                                value=Attribute(
                                                    lineno=35,
                                                    col_offset=28,
                                                    end_lineno=35,
                                                    end_col_offset=36,
                                                    value=Name(lineno=35, col_offset=28, end_lineno=35, end_col_offset=32, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                lineno=35,
                                                col_offset=46,
                                                end_lineno=35,
                                                end_col_offset=77,
                                                arg='to_date',
                                                value=Attribute(
                                                    lineno=35,
                                                    col_offset=54,
                                                    end_lineno=35,
                                                    end_col_offset=77,
                                                    value=Name(lineno=35, col_offset=54, end_lineno=35, end_col_offset=58, id='self', ctx=Load()),
                                                    attr='inventory_datetime',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=37,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=21,
                            value=Name(lineno=37, col_offset=15, end_lineno=37, end_col_offset=21, id='action', ctx=Load()),
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
