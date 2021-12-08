Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=111,
            module='odoo.addons.sale.tests.test_sale_product_attribute_value_config',
            names=[alias(name='TestSaleProductAttributeValueCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=52,
            end_col_offset=10,
            name='TestSaleGiftCardCommon',
            bases=[Name(lineno=7, col_offset=29, end_lineno=7, end_col_offset=64, id='TestSaleProductAttributeValueCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=52,
                    end_col_offset=10,
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=19, end_lineno=10, end_col_offset=22, arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=28,
                            value=Call(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=28,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=8,
                                    end_lineno=11,
                                    end_col_offset=26,
                                    value=Call(
                                        lineno=11,
                                        col_offset=8,
                                        end_lineno=11,
                                        end_col_offset=15,
                                        func=Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=13, id='super', ctx=Load()),
                                        args=[],
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
                            end_lineno=14,
                            end_col_offset=32,
                            targets=[
                                Attribute(
                                    lineno=14,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=26,
                                    value=Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='currency_ratio',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(lineno=14, col_offset=29, end_lineno=14, end_col_offset=32, value=1.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=48,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=17, id='pricelist', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=20,
                                end_lineno=15,
                                end_col_offset=48,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=20,
                                    end_lineno=15,
                                    end_col_offset=31,
                                    value=Attribute(
                                        lineno=15,
                                        col_offset=20,
                                        end_lineno=15,
                                        end_col_offset=27,
                                        value=Name(lineno=15, col_offset=20, end_lineno=15, end_col_offset=23, id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=15, col_offset=32, end_lineno=15, end_col_offset=47, value='product.list0', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=71,
                            targets=[
                                Attribute(
                                    lineno=16,
                                    col_offset=8,
                                    end_lineno=16,
                                    end_col_offset=29,
                                    value=Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=17, id='pricelist', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=16,
                                col_offset=32,
                                end_lineno=16,
                                end_col_offset=71,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=32,
                                    end_lineno=16,
                                    end_col_offset=51,
                                    value=Name(lineno=16, col_offset=32, end_lineno=16, end_col_offset=35, id='cls', ctx=Load()),
                                    attr='_setup_currency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=16,
                                        col_offset=52,
                                        end_lineno=16,
                                        end_col_offset=70,
                                        value=Name(lineno=16, col_offset=52, end_lineno=16, end_col_offset=55, id='cls', ctx=Load()),
                                        attr='currency_ratio',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=10,
                            targets=[
                                Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=18,
                                    value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='fatima',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=20,
                                col_offset=21,
                                end_lineno=23,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=21,
                                    end_lineno=20,
                                    end_col_offset=50,
                                    value=Subscript(
                                        lineno=20,
                                        col_offset=21,
                                        end_lineno=20,
                                        end_col_offset=43,
                                        value=Attribute(
                                            lineno=20,
                                            col_offset=21,
                                            end_lineno=20,
                                            end_col_offset=28,
                                            value=Name(lineno=20, col_offset=21, end_lineno=20, end_col_offset=24, id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=20, col_offset=29, end_lineno=20, end_col_offset=42, value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=20,
                                        col_offset=51,
                                        end_lineno=23,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=21, col_offset=12, end_lineno=21, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=22, col_offset=12, end_lineno=22, end_col_offset=19, value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=21, col_offset=20, end_lineno=21, end_col_offset=34, value='Fatima Kalai', kind=None),
                                            Constant(lineno=22, col_offset=21, end_lineno=22, end_col_offset=47, value='fatima.kalai@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=10,
                            targets=[
                                Attribute(
                                    lineno=25,
                                    col_offset=8,
                                    end_lineno=25,
                                    end_col_offset=23,
                                    value=Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='empty_order',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=25,
                                col_offset=26,
                                end_lineno=27,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=26,
                                    end_lineno=25,
                                    end_col_offset=54,
                                    value=Subscript(
                                        lineno=25,
                                        col_offset=26,
                                        end_lineno=25,
                                        end_col_offset=47,
                                        value=Attribute(
                                            lineno=25,
                                            col_offset=26,
                                            end_lineno=25,
                                            end_col_offset=33,
                                            value=Name(lineno=25, col_offset=26, end_lineno=25, end_col_offset=29, id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=25, col_offset=34, end_lineno=25, end_col_offset=46, value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=25,
                                        col_offset=55,
                                        end_lineno=27,
                                        end_col_offset=9,
                                        keys=[Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=24, value='partner_id', kind=None)],
                                        values=[
                                            Attribute(
                                                lineno=26,
                                                col_offset=26,
                                                end_lineno=26,
                                                end_col_offset=39,
                                                value=Attribute(
                                                    lineno=26,
                                                    col_offset=26,
                                                    end_lineno=26,
                                                    end_col_offset=36,
                                                    value=Name(lineno=26, col_offset=26, end_lineno=26, end_col_offset=29, id='cls', ctx=Load()),
                                                    attr='fatima',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=58,
                            targets=[
                                Attribute(
                                    lineno=29,
                                    col_offset=8,
                                    end_lineno=29,
                                    end_col_offset=20,
                                    value=Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='uom_unit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=29,
                                col_offset=23,
                                end_lineno=29,
                                end_col_offset=58,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=23,
                                    end_lineno=29,
                                    end_col_offset=34,
                                    value=Attribute(
                                        lineno=29,
                                        col_offset=23,
                                        end_lineno=29,
                                        end_col_offset=30,
                                        value=Name(lineno=29, col_offset=23, end_lineno=29, end_col_offset=26, id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=29, col_offset=35, end_lineno=29, end_col_offset=57, value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=32,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=10,
                            targets=[
                                Attribute(
                                    lineno=32,
                                    col_offset=8,
                                    end_lineno=32,
                                    end_col_offset=25,
                                    value=Name(lineno=32, col_offset=8, end_lineno=32, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='tax_15pc_excl',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=32,
                                col_offset=28,
                                end_lineno=37,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=28,
                                    end_lineno=32,
                                    end_col_offset=57,
                                    value=Subscript(
                                        lineno=32,
                                        col_offset=28,
                                        end_lineno=32,
                                        end_col_offset=50,
                                        value=Attribute(
                                            lineno=32,
                                            col_offset=28,
                                            end_lineno=32,
                                            end_col_offset=35,
                                            value=Name(lineno=32, col_offset=28, end_lineno=32, end_col_offset=31, id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=32, col_offset=36, end_lineno=32, end_col_offset=49, value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=32,
                                        col_offset=58,
                                        end_lineno=37,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=33, col_offset=12, end_lineno=33, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=34, col_offset=12, end_lineno=34, end_col_offset=25, value='amount_type', kind=None),
                                            Constant(lineno=35, col_offset=12, end_lineno=35, end_col_offset=20, value='amount', kind=None),
                                            Constant(lineno=36, col_offset=12, end_lineno=36, end_col_offset=26, value='type_tax_use', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=33, col_offset=20, end_lineno=33, end_col_offset=29, value='Tax 15%', kind=None),
                                            Constant(lineno=34, col_offset=27, end_lineno=34, end_col_offset=36, value='percent', kind=None),
                                            Constant(lineno=35, col_offset=22, end_lineno=35, end_col_offset=24, value=15, kind=None),
                                            Constant(lineno=36, col_offset=28, end_lineno=36, end_col_offset=34, value='sale', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=40,
                            col_offset=8,
                            end_lineno=45,
                            end_col_offset=10,
                            targets=[
                                Attribute(
                                    lineno=40,
                                    col_offset=8,
                                    end_lineno=40,
                                    end_col_offset=21,
                                    value=Name(lineno=40, col_offset=8, end_lineno=40, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='product_A',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=40,
                                col_offset=24,
                                end_lineno=45,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=40,
                                    col_offset=24,
                                    end_lineno=40,
                                    end_col_offset=57,
                                    value=Subscript(
                                        lineno=40,
                                        col_offset=24,
                                        end_lineno=40,
                                        end_col_offset=50,
                                        value=Attribute(
                                            lineno=40,
                                            col_offset=24,
                                            end_lineno=40,
                                            end_col_offset=31,
                                            value=Name(lineno=40, col_offset=24, end_lineno=40, end_col_offset=27, id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=40, col_offset=32, end_lineno=40, end_col_offset=49, value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=40,
                                        col_offset=58,
                                        end_lineno=45,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=41, col_offset=12, end_lineno=41, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=42, col_offset=12, end_lineno=42, end_col_offset=24, value='list_price', kind=None),
                                            Constant(lineno=43, col_offset=12, end_lineno=43, end_col_offset=21, value='sale_ok', kind=None),
                                            Constant(lineno=44, col_offset=12, end_lineno=44, end_col_offset=22, value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=41, col_offset=20, end_lineno=41, end_col_offset=31, value='Product A', kind=None),
                                            Constant(lineno=42, col_offset=26, end_lineno=42, end_col_offset=29, value=100, kind=None),
                                            Constant(lineno=43, col_offset=23, end_lineno=43, end_col_offset=27, value=True, kind=None),
                                            List(
                                                lineno=44,
                                                col_offset=24,
                                                end_lineno=44,
                                                end_col_offset=56,
                                                elts=[
                                                    Tuple(
                                                        lineno=44,
                                                        col_offset=25,
                                                        end_lineno=44,
                                                        end_col_offset=55,
                                                        elts=[
                                                            Constant(lineno=44, col_offset=26, end_lineno=44, end_col_offset=27, value=6, kind=None),
                                                            Constant(lineno=44, col_offset=29, end_lineno=44, end_col_offset=30, value=0, kind=None),
                                                            List(
                                                                lineno=44,
                                                                col_offset=32,
                                                                end_lineno=44,
                                                                end_col_offset=54,
                                                                elts=[
                                                                    Attribute(
                                                                        lineno=44,
                                                                        col_offset=33,
                                                                        end_lineno=44,
                                                                        end_col_offset=53,
                                                                        value=Attribute(
                                                                            lineno=44,
                                                                            col_offset=33,
                                                                            end_lineno=44,
                                                                            end_col_offset=50,
                                                                            value=Name(lineno=44, col_offset=33, end_lineno=44, end_col_offset=36, id='cls', ctx=Load()),
                                                                            attr='tax_15pc_excl',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=46,
                            col_offset=8,
                            end_lineno=52,
                            end_col_offset=10,
                            targets=[
                                Attribute(
                                    lineno=46,
                                    col_offset=8,
                                    end_lineno=46,
                                    end_col_offset=29,
                                    value=Name(lineno=46, col_offset=8, end_lineno=46, end_col_offset=11, id='cls', ctx=Load()),
                                    attr='product_gift_card',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=46,
                                col_offset=32,
                                end_lineno=52,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=46,
                                    col_offset=32,
                                    end_lineno=46,
                                    end_col_offset=65,
                                    value=Subscript(
                                        lineno=46,
                                        col_offset=32,
                                        end_lineno=46,
                                        end_col_offset=58,
                                        value=Attribute(
                                            lineno=46,
                                            col_offset=32,
                                            end_lineno=46,
                                            end_col_offset=39,
                                            value=Name(lineno=46, col_offset=32, end_lineno=46, end_col_offset=35, id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=46, col_offset=40, end_lineno=46, end_col_offset=57, value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=46,
                                        col_offset=66,
                                        end_lineno=52,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=47, col_offset=12, end_lineno=47, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=48, col_offset=12, end_lineno=48, end_col_offset=27, value='detailed_type', kind=None),
                                            Constant(lineno=49, col_offset=12, end_lineno=49, end_col_offset=24, value='list_price', kind=None),
                                            Constant(lineno=50, col_offset=12, end_lineno=50, end_col_offset=21, value='sale_ok', kind=None),
                                            Constant(lineno=51, col_offset=12, end_lineno=51, end_col_offset=22, value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=47, col_offset=20, end_lineno=47, end_col_offset=34, value='Gift Card 50', kind=None),
                                            Constant(lineno=48, col_offset=29, end_lineno=48, end_col_offset=35, value='gift', kind=None),
                                            Constant(lineno=49, col_offset=26, end_lineno=49, end_col_offset=28, value=50, kind=None),
                                            Constant(lineno=50, col_offset=23, end_lineno=50, end_col_offset=27, value=True, kind=None),
                                            Constant(lineno=51, col_offset=24, end_lineno=51, end_col_offset=29, value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(lineno=9, col_offset=5, end_lineno=9, end_col_offset=16, id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)