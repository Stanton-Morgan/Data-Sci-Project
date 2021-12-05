Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=69,
            module='odoo.addons.website_slides.controllers.main',
            names=[alias(name='WebsiteSlides', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=17,
            end_col_offset=21,
            name='WebsiteSaleSlides',
            bases=[Name(lineno=8, col_offset=24, end_lineno=8, end_col_offset=37, id='WebsiteSlides', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=21,
                    name='_prepare_additional_channel_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=10, col_offset=43, end_lineno=10, end_col_offset=47, arg='self', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=49, end_lineno=10, end_col_offset=55, arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(lineno=10, col_offset=59, end_lineno=10, end_col_offset=65, arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=100,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=14, id='values', ctx=Store())],
                            value=Call(
                                lineno=11,
                                col_offset=17,
                                end_lineno=11,
                                end_col_offset=100,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=17,
                                    end_lineno=11,
                                    end_col_offset=82,
                                    value=Call(
                                        lineno=11,
                                        col_offset=17,
                                        end_lineno=11,
                                        end_col_offset=47,
                                        func=Name(lineno=11, col_offset=17, end_lineno=11, end_col_offset=22, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=11, col_offset=23, end_lineno=11, end_col_offset=40, id='WebsiteSaleSlides', ctx=Load()),
                                            Name(lineno=11, col_offset=42, end_lineno=11, end_col_offset=46, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_additional_channel_values',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=11, col_offset=83, end_lineno=11, end_col_offset=89, id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        lineno=11,
                                        col_offset=91,
                                        end_lineno=11,
                                        end_col_offset=99,
                                        arg=None,
                                        value=Name(lineno=11, col_offset=93, end_lineno=11, end_col_offset=99, id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=35,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=15, id='channel', ctx=Store())],
                            value=Subscript(
                                lineno=12,
                                col_offset=18,
                                end_lineno=12,
                                end_col_offset=35,
                                value=Name(lineno=12, col_offset=18, end_lineno=12, end_col_offset=24, id='values', ctx=Load()),
                                slice=Constant(lineno=12, col_offset=25, end_lineno=12, end_col_offset=34, value='channel', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=13,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=79,
                            test=BoolOp(
                                lineno=13,
                                col_offset=11,
                                end_lineno=13,
                                end_col_offset=61,
                                op=And(),
                                values=[
                                    Compare(
                                        lineno=13,
                                        col_offset=11,
                                        end_lineno=13,
                                        end_col_offset=38,
                                        left=Attribute(
                                            lineno=13,
                                            col_offset=11,
                                            end_lineno=13,
                                            end_col_offset=25,
                                            value=Name(lineno=13, col_offset=11, end_lineno=13, end_col_offset=18, id='channel', ctx=Load()),
                                            attr='enroll',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(lineno=13, col_offset=29, end_lineno=13, end_col_offset=38, value='payment', kind=None)],
                                    ),
                                    Attribute(
                                        lineno=13,
                                        col_offset=43,
                                        end_lineno=13,
                                        end_col_offset=61,
                                        value=Name(lineno=13, col_offset=43, end_lineno=13, end_col_offset=50, id='channel', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=14,
                                    end_col_offset=63,
                                    targets=[Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=21, id='pricelist', ctx=Store())],
                                    value=Call(
                                        lineno=14,
                                        col_offset=24,
                                        end_lineno=14,
                                        end_col_offset=63,
                                        func=Attribute(
                                            lineno=14,
                                            col_offset=24,
                                            end_lineno=14,
                                            end_col_offset=61,
                                            value=Attribute(
                                                lineno=14,
                                                col_offset=24,
                                                end_lineno=14,
                                                end_col_offset=39,
                                                value=Name(lineno=14, col_offset=24, end_lineno=14, end_col_offset=31, id='request', ctx=Load()),
                                                attr='website',
                                                ctx=Load(),
                                            ),
                                            attr='get_current_pricelist',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=15,
                                    col_offset=12,
                                    end_lineno=15,
                                    end_col_offset=148,
                                    targets=[
                                        Subscript(
                                            lineno=15,
                                            col_offset=12,
                                            end_lineno=15,
                                            end_col_offset=34,
                                            value=Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=18, id='values', ctx=Load()),
                                            slice=Constant(lineno=15, col_offset=19, end_lineno=15, end_col_offset=33, value='product_info', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=15,
                                        col_offset=37,
                                        end_lineno=15,
                                        end_col_offset=148,
                                        func=Attribute(
                                            lineno=15,
                                            col_offset=37,
                                            end_lineno=15,
                                            end_col_offset=93,
                                            value=Attribute(
                                                lineno=15,
                                                col_offset=37,
                                                end_lineno=15,
                                                end_col_offset=71,
                                                value=Attribute(
                                                    lineno=15,
                                                    col_offset=37,
                                                    end_lineno=15,
                                                    end_col_offset=55,
                                                    value=Name(lineno=15, col_offset=37, end_lineno=15, end_col_offset=44, id='channel', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='product_tmpl_id',
                                                ctx=Load(),
                                            ),
                                            attr='_get_combination_info',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                lineno=15,
                                                col_offset=94,
                                                end_lineno=15,
                                                end_col_offset=126,
                                                arg='product_id',
                                                value=Attribute(
                                                    lineno=15,
                                                    col_offset=105,
                                                    end_lineno=15,
                                                    end_col_offset=126,
                                                    value=Attribute(
                                                        lineno=15,
                                                        col_offset=105,
                                                        end_lineno=15,
                                                        end_col_offset=123,
                                                        value=Name(lineno=15, col_offset=105, end_lineno=15, end_col_offset=112, id='channel', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                lineno=15,
                                                col_offset=128,
                                                end_lineno=15,
                                                end_col_offset=147,
                                                arg='pricelist',
                                                value=Name(lineno=15, col_offset=138, end_lineno=15, end_col_offset=147, id='pricelist', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=79,
                                    targets=[
                                        Subscript(
                                            lineno=16,
                                            col_offset=12,
                                            end_lineno=16,
                                            end_col_offset=49,
                                            value=Subscript(
                                                lineno=16,
                                                col_offset=12,
                                                end_lineno=16,
                                                end_col_offset=34,
                                                value=Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=18, id='values', ctx=Load()),
                                                slice=Constant(lineno=16, col_offset=19, end_lineno=16, end_col_offset=33, value='product_info', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(lineno=16, col_offset=35, end_lineno=16, end_col_offset=48, value='currency_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        lineno=16,
                                        col_offset=52,
                                        end_lineno=16,
                                        end_col_offset=79,
                                        value=Attribute(
                                            lineno=16,
                                            col_offset=52,
                                            end_lineno=16,
                                            end_col_offset=67,
                                            value=Name(lineno=16, col_offset=52, end_lineno=16, end_col_offset=59, id='request', ctx=Load()),
                                            attr='website',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=21,
                            value=Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=21, id='values', ctx=Load()),
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
