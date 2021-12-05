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
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=46,
            module='odoo.addons.website.models',
            names=[alias(name='ir_http', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=20,
            end_col_offset=142,
            name='ProductProduct',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=21,
                    end_lineno=8,
                    end_col_offset=33,
                    value=Name(lineno=8, col_offset=21, end_lineno=8, end_col_offset=27, id='models', ctx=Load()),
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
                    end_col_offset=32,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=32, value='product.product', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=58,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=12, id='cart_qty', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=15,
                        end_lineno=11,
                        end_col_offset=58,
                        func=Attribute(
                            lineno=11,
                            col_offset=15,
                            end_lineno=11,
                            end_col_offset=29,
                            value=Name(lineno=11, col_offset=15, end_lineno=11, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=30,
                                end_lineno=11,
                                end_col_offset=57,
                                arg='compute',
                                value=Constant(lineno=11, col_offset=38, end_lineno=11, end_col_offset=57, value='_compute_cart_qty', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=142,
                    name='_compute_cart_qty',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=26, end_lineno=13, end_col_offset=30, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=47,
                            targets=[Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=15, id='website', ctx=Store())],
                            value=Call(
                                lineno=14,
                                col_offset=18,
                                end_lineno=14,
                                end_col_offset=47,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=18,
                                    end_lineno=14,
                                    end_col_offset=45,
                                    value=Name(lineno=14, col_offset=18, end_lineno=14, end_col_offset=25, id='ir_http', ctx=Load()),
                                    attr='get_request_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=15,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=18,
                            test=UnaryOp(
                                lineno=15,
                                col_offset=11,
                                end_lineno=15,
                                end_col_offset=22,
                                op=Not(),
                                operand=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=22, id='website', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=29,
                                    targets=[
                                        Attribute(
                                            lineno=16,
                                            col_offset=12,
                                            end_lineno=16,
                                            end_col_offset=25,
                                            value=Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=16, id='self', ctx=Load()),
                                            attr='cart_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(lineno=16, col_offset=28, end_lineno=16, end_col_offset=29, value=0, kind=None),
                                    type_comment=None,
                                ),
                                Return(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, value=None),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=39,
                            targets=[Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=12, id='cart', ctx=Store())],
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
                                    value=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=22, id='website', ctx=Load()),
                                    attr='sale_get_order',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=19,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=142,
                            target=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=19, id='product', ctx=Store()),
                            iter=Name(lineno=19, col_offset=23, end_lineno=19, end_col_offset=27, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=20,
                                    col_offset=12,
                                    end_lineno=20,
                                    end_col_offset=142,
                                    targets=[
                                        Attribute(
                                            lineno=20,
                                            col_offset=12,
                                            end_lineno=20,
                                            end_col_offset=28,
                                            value=Name(lineno=20, col_offset=12, end_lineno=20, end_col_offset=19, id='product', ctx=Load()),
                                            attr='cart_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        lineno=20,
                                        col_offset=31,
                                        end_lineno=20,
                                        end_col_offset=142,
                                        test=Name(lineno=20, col_offset=131, end_lineno=20, end_col_offset=135, id='cart', ctx=Load()),
                                        body=Call(
                                            lineno=20,
                                            col_offset=31,
                                            end_lineno=20,
                                            end_col_offset=127,
                                            func=Name(lineno=20, col_offset=31, end_lineno=20, end_col_offset=34, id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    lineno=20,
                                                    col_offset=35,
                                                    end_lineno=20,
                                                    end_col_offset=126,
                                                    func=Attribute(
                                                        lineno=20,
                                                        col_offset=35,
                                                        end_lineno=20,
                                                        end_col_offset=107,
                                                        value=Call(
                                                            lineno=20,
                                                            col_offset=35,
                                                            end_lineno=20,
                                                            end_col_offset=100,
                                                            func=Attribute(
                                                                lineno=20,
                                                                col_offset=35,
                                                                end_lineno=20,
                                                                end_col_offset=59,
                                                                value=Attribute(
                                                                    lineno=20,
                                                                    col_offset=35,
                                                                    end_lineno=20,
                                                                    end_col_offset=50,
                                                                    value=Name(lineno=20, col_offset=35, end_lineno=20, end_col_offset=39, id='cart', ctx=Load()),
                                                                    attr='order_line',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    lineno=20,
                                                                    col_offset=60,
                                                                    end_lineno=20,
                                                                    end_col_offset=99,
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(lineno=20, col_offset=67, end_lineno=20, end_col_offset=68, arg='p', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        lineno=20,
                                                                        col_offset=70,
                                                                        end_lineno=20,
                                                                        end_col_offset=99,
                                                                        left=Attribute(
                                                                            lineno=20,
                                                                            col_offset=70,
                                                                            end_lineno=20,
                                                                            end_col_offset=85,
                                                                            value=Attribute(
                                                                                lineno=20,
                                                                                col_offset=70,
                                                                                end_lineno=20,
                                                                                end_col_offset=82,
                                                                                value=Name(lineno=20, col_offset=70, end_lineno=20, end_col_offset=71, id='p', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                lineno=20,
                                                                                col_offset=89,
                                                                                end_lineno=20,
                                                                                end_col_offset=99,
                                                                                value=Name(lineno=20, col_offset=89, end_lineno=20, end_col_offset=96, id='product', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(lineno=20, col_offset=108, end_lineno=20, end_col_offset=125, value='product_uom_qty', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(lineno=20, col_offset=141, end_lineno=20, end_col_offset=142, value=0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
