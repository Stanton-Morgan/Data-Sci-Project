Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=58,
            module='odoo.addons.event.tests.common',
            names=[alias(name='TestEventCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=63,
            module='odoo.addons.sales_team.tests.common',
            names=[alias(name='TestSalesCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=20,
            end_col_offset=10,
            name='TestEventSaleCommon',
            bases=[
                Name(lineno=8, col_offset=26, end_lineno=8, end_col_offset=41, id='TestEventCommon', ctx=Load()),
                Name(lineno=8, col_offset=43, end_lineno=8, end_col_offset=58, id='TestSalesCommon', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=10,
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=19, end_lineno=11, end_col_offset=22, arg='cls', annotation=None, type_comment=None)],
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
                            end_col_offset=52,
                            value=Call(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=52,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=50,
                                    value=Call(
                                        lineno=12,
                                        col_offset=8,
                                        end_lineno=12,
                                        end_col_offset=39,
                                        func=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=13, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=12, col_offset=14, end_lineno=12, end_col_offset=33, id='TestEventSaleCommon', ctx=Load()),
                                            Name(lineno=12, col_offset=35, end_lineno=12, end_col_offset=38, id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=10,
                            targets=[
                                Attribute(
                                    lineno=14,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=25,
                                    value=Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='event_product',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=14,
                                col_offset=28,
                                end_lineno=20,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=28,
                                    end_lineno=14,
                                    end_col_offset=61,
                                    value=Subscript(
                                        lineno=14,
                                        col_offset=28,
                                        end_lineno=14,
                                        end_col_offset=54,
                                        value=Attribute(
                                            lineno=14,
                                            col_offset=28,
                                            end_lineno=14,
                                            end_col_offset=35,
                                            value=Name(lineno=14, col_offset=28, end_lineno=14, end_col_offset=31, id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=14, col_offset=36, end_lineno=14, end_col_offset=53, value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=14,
                                        col_offset=62,
                                        end_lineno=20,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=15, col_offset=12, end_lineno=15, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=16, col_offset=12, end_lineno=16, end_col_offset=30, value='description_sale', kind=None),
                                            Constant(lineno=17, col_offset=12, end_lineno=17, end_col_offset=24, value='list_price', kind=None),
                                            Constant(lineno=18, col_offset=12, end_lineno=18, end_col_offset=28, value='standard_price', kind=None),
                                            Constant(lineno=19, col_offset=12, end_lineno=19, end_col_offset=27, value='detailed_type', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=15, col_offset=20, end_lineno=15, end_col_offset=47, value='Test Registration Product', kind=None),
                                            Constant(lineno=16, col_offset=32, end_lineno=16, end_col_offset=52, value='Mighty Description', kind=None),
                                            Constant(lineno=17, col_offset=26, end_lineno=17, end_col_offset=28, value=10, kind=None),
                                            Constant(lineno=18, col_offset=30, end_lineno=18, end_col_offset=34, value=30.0, kind=None),
                                            Constant(lineno=19, col_offset=29, end_lineno=19, end_col_offset=36, value='event', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(lineno=10, col_offset=5, end_lineno=10, end_col_offset=16, id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
