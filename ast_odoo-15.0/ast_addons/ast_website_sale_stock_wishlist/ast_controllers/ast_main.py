Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=21,
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=65,
            module='odoo.addons.website_sale.controllers.main',
            names=[alias(name='WebsiteSale', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=13,
            end_col_offset=41,
            name='WebsiteSaleStockWishlist',
            bases=[Name(lineno=8, col_offset=31, end_lineno=8, end_col_offset=42, id='WebsiteSale', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=41,
                    name='notify_stock',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=10, col_offset=21, end_lineno=10, end_col_offset=25, arg='self', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=27, end_lineno=10, end_col_offset=31, arg='wish', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=33, end_lineno=10, end_col_offset=39, arg='notify', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(lineno=10, col_offset=48, end_lineno=10, end_col_offset=50, arg='kw', annotation=None, type_comment=None),
                        defaults=[Constant(lineno=10, col_offset=40, end_lineno=10, end_col_offset=44, value=True, kind=None)],
                    ),
                    body=[
                        If(
                            lineno=11,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=47,
                            test=UnaryOp(
                                lineno=11,
                                col_offset=11,
                                end_lineno=11,
                                end_col_offset=47,
                                op=Not(),
                                operand=Call(
                                    lineno=11,
                                    col_offset=15,
                                    end_lineno=11,
                                    end_col_offset=47,
                                    func=Attribute(
                                        lineno=11,
                                        col_offset=15,
                                        end_lineno=11,
                                        end_col_offset=45,
                                        value=Attribute(
                                            lineno=11,
                                            col_offset=15,
                                            end_lineno=11,
                                            end_col_offset=30,
                                            value=Name(lineno=11, col_offset=15, end_lineno=11, end_col_offset=22, id='request', ctx=Load()),
                                            attr='website',
                                            ctx=Load(),
                                        ),
                                        attr='is_public_user',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    lineno=12,
                                    col_offset=12,
                                    end_lineno=12,
                                    end_col_offset=47,
                                    targets=[
                                        Subscript(
                                            lineno=12,
                                            col_offset=12,
                                            end_lineno=12,
                                            end_col_offset=38,
                                            value=Name(lineno=12, col_offset=12, end_lineno=12, end_col_offset=16, id='wish', ctx=Load()),
                                            slice=Constant(lineno=12, col_offset=17, end_lineno=12, end_col_offset=37, value='stock_notification', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(lineno=12, col_offset=41, end_lineno=12, end_col_offset=47, id='notify', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=41,
                            value=Subscript(
                                lineno=13,
                                col_offset=15,
                                end_lineno=13,
                                end_col_offset=41,
                                value=Name(lineno=13, col_offset=15, end_lineno=13, end_col_offset=19, id='wish', ctx=Load()),
                                slice=Constant(lineno=13, col_offset=20, end_lineno=13, end_col_offset=40, value='stock_notification', kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=9,
                            col_offset=5,
                            end_lineno=9,
                            end_col_offset=117,
                            func=Attribute(
                                lineno=9,
                                col_offset=5,
                                end_lineno=9,
                                end_col_offset=15,
                                value=Name(lineno=9, col_offset=5, end_lineno=9, end_col_offset=9, id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    lineno=9,
                                    col_offset=16,
                                    end_lineno=9,
                                    end_col_offset=74,
                                    elts=[Constant(lineno=9, col_offset=17, end_lineno=9, end_col_offset=73, value='/shop/wishlist/notify/<model("product.wishlist"):wish>', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    lineno=9,
                                    col_offset=76,
                                    end_lineno=9,
                                    end_col_offset=87,
                                    arg='type',
                                    value=Constant(lineno=9, col_offset=81, end_lineno=9, end_col_offset=87, value='json', kind=None),
                                ),
                                keyword(
                                    lineno=9,
                                    col_offset=89,
                                    end_lineno=9,
                                    end_col_offset=102,
                                    arg='auth',
                                    value=Constant(lineno=9, col_offset=94, end_lineno=9, end_col_offset=102, value='public', kind=None),
                                ),
                                keyword(
                                    lineno=9,
                                    col_offset=104,
                                    end_lineno=9,
                                    end_col_offset=116,
                                    arg='website',
                                    value=Constant(lineno=9, col_offset=112, end_lineno=9, end_col_offset=116, value=True, kind=None),
                                ),
                            ],
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
