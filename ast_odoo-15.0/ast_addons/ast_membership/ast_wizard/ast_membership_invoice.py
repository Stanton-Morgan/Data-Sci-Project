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
            end_lineno=35,
            end_col_offset=9,
            name='MembershipInvoice',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=24,
                    end_lineno=7,
                    end_col_offset=45,
                    value=Name(lineno=7, col_offset=24, end_lineno=7, end_col_offset=30, id='models', ctx=Load()),
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
                    end_col_offset=32,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=32, value='membership.invoice', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=39,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=39, value='Membership Invoice', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=87,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=14, id='product_id', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=17,
                        end_lineno=11,
                        end_col_offset=87,
                        func=Attribute(
                            lineno=11,
                            col_offset=17,
                            end_lineno=11,
                            end_col_offset=32,
                            value=Name(lineno=11, col_offset=17, end_lineno=11, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=33, end_lineno=11, end_col_offset=50, value='product.product', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=52,
                                end_lineno=11,
                                end_col_offset=71,
                                arg='string',
                                value=Constant(lineno=11, col_offset=59, end_lineno=11, end_col_offset=71, value='Membership', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=73,
                                end_lineno=11,
                                end_col_offset=86,
                                arg='required',
                                value=Constant(lineno=11, col_offset=82, end_lineno=11, end_col_offset=86, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=93,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=16, id='member_price', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=19,
                        end_lineno=12,
                        end_col_offset=93,
                        func=Attribute(
                            lineno=12,
                            col_offset=19,
                            end_lineno=12,
                            end_col_offset=31,
                            value=Name(lineno=12, col_offset=19, end_lineno=12, end_col_offset=25, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=32,
                                end_lineno=12,
                                end_col_offset=53,
                                arg='string',
                                value=Constant(lineno=12, col_offset=39, end_lineno=12, end_col_offset=53, value='Member Price', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=55,
                                end_lineno=12,
                                end_col_offset=77,
                                arg='digits',
                                value=Constant(lineno=12, col_offset=62, end_lineno=12, end_col_offset=77, value='Product Price', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=79,
                                end_lineno=12,
                                end_col_offset=92,
                                arg='required',
                                value=Constant(lineno=12, col_offset=88, end_lineno=12, end_col_offset=92, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=71,
                    name='onchange_product',
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
                            end_lineno=17,
                            end_col_offset=11,
                            value=Constant(lineno=16, col_offset=8, end_lineno=17, end_col_offset=11, value="This function returns value of  product's member price based on product id.\n        ", kind=None),
                        ),
                        Assign(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=64,
                            targets=[Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=18, id='price_dict', ctx=Store())],
                            value=Call(
                                lineno=18,
                                col_offset=21,
                                end_lineno=18,
                                end_col_offset=64,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=21,
                                    end_lineno=18,
                                    end_col_offset=50,
                                    value=Attribute(
                                        lineno=18,
                                        col_offset=21,
                                        end_lineno=18,
                                        end_col_offset=36,
                                        value=Name(lineno=18, col_offset=21, end_lineno=18, end_col_offset=25, id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='price_compute',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=18, col_offset=51, end_lineno=18, end_col_offset=63, value='list_price', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=71,
                            targets=[
                                Attribute(
                                    lineno=19,
                                    col_offset=8,
                                    end_lineno=19,
                                    end_col_offset=25,
                                    value=Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=12, id='self', ctx=Load()),
                                    attr='member_price',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                lineno=19,
                                col_offset=28,
                                end_lineno=19,
                                end_col_offset=71,
                                op=Or(),
                                values=[
                                    Call(
                                        lineno=19,
                                        col_offset=28,
                                        end_lineno=19,
                                        end_col_offset=62,
                                        func=Attribute(
                                            lineno=19,
                                            col_offset=28,
                                            end_lineno=19,
                                            end_col_offset=42,
                                            value=Name(lineno=19, col_offset=28, end_lineno=19, end_col_offset=38, id='price_dict', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=19,
                                                col_offset=43,
                                                end_lineno=19,
                                                end_col_offset=61,
                                                value=Attribute(
                                                    lineno=19,
                                                    col_offset=43,
                                                    end_lineno=19,
                                                    end_col_offset=58,
                                                    value=Name(lineno=19, col_offset=43, end_lineno=19, end_col_offset=47, id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(lineno=19, col_offset=66, end_lineno=19, end_col_offset=71, value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=14,
                            col_offset=5,
                            end_lineno=14,
                            end_col_offset=31,
                            func=Attribute(
                                lineno=14,
                                col_offset=5,
                                end_lineno=14,
                                end_col_offset=17,
                                value=Name(lineno=14, col_offset=5, end_lineno=14, end_col_offset=8, id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=14, col_offset=18, end_lineno=14, end_col_offset=30, value='product_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=35,
                    end_col_offset=9,
                    name='membership_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=21, col_offset=27, end_lineno=21, end_col_offset=31, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=148,
                            targets=[Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=20, id='invoice_list', ctx=Store())],
                            value=Call(
                                lineno=22,
                                col_offset=23,
                                end_lineno=22,
                                end_col_offset=148,
                                func=Attribute(
                                    lineno=22,
                                    col_offset=23,
                                    end_lineno=22,
                                    end_col_offset=112,
                                    value=Call(
                                        lineno=22,
                                        col_offset=23,
                                        end_lineno=22,
                                        end_col_offset=86,
                                        func=Attribute(
                                            lineno=22,
                                            col_offset=23,
                                            end_lineno=22,
                                            end_col_offset=53,
                                            value=Subscript(
                                                lineno=22,
                                                col_offset=23,
                                                end_lineno=22,
                                                end_col_offset=46,
                                                value=Attribute(
                                                    lineno=22,
                                                    col_offset=23,
                                                    end_lineno=22,
                                                    end_col_offset=31,
                                                    value=Name(lineno=22, col_offset=23, end_lineno=22, end_col_offset=27, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=22, col_offset=32, end_lineno=22, end_col_offset=45, value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                lineno=22,
                                                col_offset=54,
                                                end_lineno=22,
                                                end_col_offset=85,
                                                func=Attribute(
                                                    lineno=22,
                                                    col_offset=54,
                                                    end_lineno=22,
                                                    end_col_offset=71,
                                                    value=Attribute(
                                                        lineno=22,
                                                        col_offset=54,
                                                        end_lineno=22,
                                                        end_col_offset=67,
                                                        value=Name(lineno=22, col_offset=54, end_lineno=22, end_col_offset=58, id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(lineno=22, col_offset=72, end_lineno=22, end_col_offset=84, value='active_ids', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create_membership_invoice',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=22,
                                        col_offset=113,
                                        end_lineno=22,
                                        end_col_offset=128,
                                        value=Name(lineno=22, col_offset=113, end_lineno=22, end_col_offset=117, id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=22,
                                        col_offset=130,
                                        end_lineno=22,
                                        end_col_offset=147,
                                        value=Name(lineno=22, col_offset=130, end_lineno=22, end_col_offset=134, id='self', ctx=Load()),
                                        attr='member_price',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=84,
                            targets=[Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=23, id='search_view_ref', ctx=Store())],
                            value=Call(
                                lineno=24,
                                col_offset=26,
                                end_lineno=24,
                                end_col_offset=84,
                                func=Attribute(
                                    lineno=24,
                                    col_offset=26,
                                    end_lineno=24,
                                    end_col_offset=38,
                                    value=Attribute(
                                        lineno=24,
                                        col_offset=26,
                                        end_lineno=24,
                                        end_col_offset=34,
                                        value=Name(lineno=24, col_offset=26, end_lineno=24, end_col_offset=30, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=24, col_offset=39, end_lineno=24, end_col_offset=76, value='account.view_account_invoice_filter', kind=None),
                                    Constant(lineno=24, col_offset=78, end_lineno=24, end_col_offset=83, value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=69,
                            targets=[Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=21, id='form_view_ref', ctx=Store())],
                            value=Call(
                                lineno=25,
                                col_offset=24,
                                end_lineno=25,
                                end_col_offset=69,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=24,
                                    end_lineno=25,
                                    end_col_offset=36,
                                    value=Attribute(
                                        lineno=25,
                                        col_offset=24,
                                        end_lineno=25,
                                        end_col_offset=32,
                                        value=Name(lineno=25, col_offset=24, end_lineno=25, end_col_offset=28, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=25, col_offset=37, end_lineno=25, end_col_offset=61, value='account.view_move_form', kind=None),
                                    Constant(lineno=25, col_offset=63, end_lineno=25, end_col_offset=68, value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=69,
                            targets=[Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=21, id='tree_view_ref', ctx=Store())],
                            value=Call(
                                lineno=26,
                                col_offset=24,
                                end_lineno=26,
                                end_col_offset=69,
                                func=Attribute(
                                    lineno=26,
                                    col_offset=24,
                                    end_lineno=26,
                                    end_col_offset=36,
                                    value=Attribute(
                                        lineno=26,
                                        col_offset=24,
                                        end_lineno=26,
                                        end_col_offset=32,
                                        value=Name(lineno=26, col_offset=24, end_lineno=26, end_col_offset=28, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=26, col_offset=37, end_lineno=26, end_col_offset=61, value='account.view_move_tree', kind=None),
                                    Constant(lineno=26, col_offset=63, end_lineno=26, end_col_offset=68, value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=28,
                            col_offset=8,
                            end_lineno=35,
                            end_col_offset=9,
                            value=Dict(
                                lineno=28,
                                col_offset=16,
                                end_lineno=35,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=29, col_offset=12, end_lineno=29, end_col_offset=20, value='domain', kind=None),
                                    Constant(lineno=30, col_offset=12, end_lineno=30, end_col_offset=18, value='name', kind=None),
                                    Constant(lineno=31, col_offset=12, end_lineno=31, end_col_offset=23, value='res_model', kind=None),
                                    Constant(lineno=32, col_offset=12, end_lineno=32, end_col_offset=18, value='type', kind=None),
                                    Constant(lineno=33, col_offset=12, end_lineno=33, end_col_offset=19, value='views', kind=None),
                                    Constant(lineno=34, col_offset=12, end_lineno=34, end_col_offset=28, value='search_view_id', kind=None),
                                ],
                                values=[
                                    List(
                                        lineno=29,
                                        col_offset=22,
                                        end_lineno=29,
                                        end_col_offset=54,
                                        elts=[
                                            Tuple(
                                                lineno=29,
                                                col_offset=23,
                                                end_lineno=29,
                                                end_col_offset=53,
                                                elts=[
                                                    Constant(lineno=29, col_offset=24, end_lineno=29, end_col_offset=28, value='id', kind=None),
                                                    Constant(lineno=29, col_offset=30, end_lineno=29, end_col_offset=34, value='in', kind=None),
                                                    Attribute(
                                                        lineno=29,
                                                        col_offset=36,
                                                        end_lineno=29,
                                                        end_col_offset=52,
                                                        value=Name(lineno=29, col_offset=36, end_lineno=29, end_col_offset=48, id='invoice_list', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=30, col_offset=20, end_lineno=30, end_col_offset=41, value='Membership Invoices', kind=None),
                                    Constant(lineno=31, col_offset=25, end_lineno=31, end_col_offset=39, value='account.move', kind=None),
                                    Constant(lineno=32, col_offset=20, end_lineno=32, end_col_offset=43, value='ir.actions.act_window', kind=None),
                                    List(
                                        lineno=33,
                                        col_offset=21,
                                        end_lineno=33,
                                        end_col_offset=77,
                                        elts=[
                                            Tuple(
                                                lineno=33,
                                                col_offset=22,
                                                end_lineno=33,
                                                end_col_offset=48,
                                                elts=[
                                                    Attribute(
                                                        lineno=33,
                                                        col_offset=23,
                                                        end_lineno=33,
                                                        end_col_offset=39,
                                                        value=Name(lineno=33, col_offset=23, end_lineno=33, end_col_offset=36, id='tree_view_ref', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=33, col_offset=41, end_lineno=33, end_col_offset=47, value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=33,
                                                col_offset=50,
                                                end_lineno=33,
                                                end_col_offset=76,
                                                elts=[
                                                    Attribute(
                                                        lineno=33,
                                                        col_offset=51,
                                                        end_lineno=33,
                                                        end_col_offset=67,
                                                        value=Name(lineno=33, col_offset=51, end_lineno=33, end_col_offset=64, id='form_view_ref', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=33, col_offset=69, end_lineno=33, end_col_offset=75, value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        lineno=34,
                                        col_offset=30,
                                        end_lineno=34,
                                        end_col_offset=70,
                                        op=And(),
                                        values=[
                                            Name(lineno=34, col_offset=30, end_lineno=34, end_col_offset=45, id='search_view_ref', ctx=Load()),
                                            List(
                                                lineno=34,
                                                col_offset=50,
                                                end_lineno=34,
                                                end_col_offset=70,
                                                elts=[
                                                    Attribute(
                                                        lineno=34,
                                                        col_offset=51,
                                                        end_lineno=34,
                                                        end_col_offset=69,
                                                        value=Name(lineno=34, col_offset=51, end_lineno=34, end_col_offset=66, id='search_view_ref', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
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
