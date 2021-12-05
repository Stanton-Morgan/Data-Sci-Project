Module(
    body=[
        ImportFrom(
            lineno=1,
            col_offset=0,
            end_lineno=1,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=4,
            col_offset=0,
            end_lineno=26,
            end_col_offset=9,
            name='ProductProduct',
            bases=[
                Attribute(
                    lineno=4,
                    col_offset=21,
                    end_lineno=4,
                    end_col_offset=33,
                    value=Name(lineno=4, col_offset=21, end_lineno=4, end_col_offset=27, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=5,
                    col_offset=4,
                    end_lineno=5,
                    end_col_offset=32,
                    targets=[Name(lineno=5, col_offset=4, end_lineno=5, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=5, col_offset=15, end_lineno=5, end_col_offset=32, value='product.product', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=7,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=18,
                    name='get_product_info_pos',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=7, col_offset=29, end_lineno=7, end_col_offset=33, arg='self', annotation=None, type_comment=None),
                            arg(lineno=7, col_offset=35, end_lineno=7, end_col_offset=40, arg='price', annotation=None, type_comment=None),
                            arg(lineno=7, col_offset=42, end_lineno=7, end_col_offset=50, arg='quantity', annotation=None, type_comment=None),
                            arg(lineno=7, col_offset=52, end_lineno=7, end_col_offset=65, arg='pos_config_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=8,
                            col_offset=8,
                            end_lineno=8,
                            end_col_offset=74,
                            targets=[Name(lineno=8, col_offset=8, end_lineno=8, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=8,
                                col_offset=14,
                                end_lineno=8,
                                end_col_offset=74,
                                func=Attribute(
                                    lineno=8,
                                    col_offset=14,
                                    end_lineno=8,
                                    end_col_offset=42,
                                    value=Call(
                                        lineno=8,
                                        col_offset=14,
                                        end_lineno=8,
                                        end_col_offset=21,
                                        func=Name(lineno=8, col_offset=14, end_lineno=8, end_col_offset=19, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_product_info_pos',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=8, col_offset=43, end_lineno=8, end_col_offset=48, id='price', ctx=Load()),
                                    Name(lineno=8, col_offset=50, end_lineno=8, end_col_offset=58, id='quantity', ctx=Load()),
                                    Name(lineno=8, col_offset=60, end_lineno=8, end_col_offset=73, id='pos_config_id', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=9,
                            targets=[
                                Subscript(
                                    lineno=11,
                                    col_offset=8,
                                    end_lineno=11,
                                    end_col_offset=32,
                                    value=Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=11, id='res', ctx=Load()),
                                    slice=Constant(lineno=11, col_offset=12, end_lineno=11, end_col_offset=31, value='optional_products', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                lineno=11,
                                col_offset=35,
                                end_lineno=14,
                                end_col_offset=9,
                                elt=Dict(
                                    lineno=12,
                                    col_offset=12,
                                    end_lineno=12,
                                    end_col_offset=85,
                                    keys=[
                                        Constant(lineno=12, col_offset=13, end_lineno=12, end_col_offset=19, value='name', kind=None),
                                        Constant(lineno=12, col_offset=29, end_lineno=12, end_col_offset=36, value='price', kind=None),
                                    ],
                                    values=[
                                        Attribute(
                                            lineno=12,
                                            col_offset=21,
                                            end_lineno=12,
                                            end_col_offset=27,
                                            value=Name(lineno=12, col_offset=21, end_lineno=12, end_col_offset=22, id='p', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        Call(
                                            lineno=12,
                                            col_offset=38,
                                            end_lineno=12,
                                            end_col_offset=84,
                                            func=Name(lineno=12, col_offset=38, end_lineno=12, end_col_offset=41, id='min', ctx=Load()),
                                            args=[
                                                Call(
                                                    lineno=12,
                                                    col_offset=42,
                                                    end_lineno=12,
                                                    end_col_offset=83,
                                                    func=Attribute(
                                                        lineno=12,
                                                        col_offset=42,
                                                        end_lineno=12,
                                                        end_col_offset=70,
                                                        value=Attribute(
                                                            lineno=12,
                                                            col_offset=42,
                                                            end_lineno=12,
                                                            end_col_offset=63,
                                                            value=Name(lineno=12, col_offset=42, end_lineno=12, end_col_offset=43, id='p', ctx=Load()),
                                                            attr='product_variant_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(lineno=12, col_offset=71, end_lineno=12, end_col_offset=82, value='lst_price', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(lineno=13, col_offset=16, end_lineno=13, end_col_offset=17, id='p', ctx=Store()),
                                        iter=Call(
                                            lineno=13,
                                            col_offset=21,
                                            end_lineno=13,
                                            end_col_offset=99,
                                            func=Attribute(
                                                lineno=13,
                                                col_offset=21,
                                                end_lineno=13,
                                                end_col_offset=62,
                                                value=Attribute(
                                                    lineno=13,
                                                    col_offset=21,
                                                    end_lineno=13,
                                                    end_col_offset=46,
                                                    value=Name(lineno=13, col_offset=21, end_lineno=13, end_col_offset=25, id='self', ctx=Load()),
                                                    attr='optional_product_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered_domain',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    lineno=13,
                                                    col_offset=63,
                                                    end_lineno=13,
                                                    end_col_offset=98,
                                                    func=Attribute(
                                                        lineno=13,
                                                        col_offset=63,
                                                        end_lineno=13,
                                                        end_col_offset=96,
                                                        value=Name(lineno=13, col_offset=63, end_lineno=13, end_col_offset=67, id='self', ctx=Load()),
                                                        attr='_optional_product_pos_domain',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=18,
                            value=Name(lineno=16, col_offset=15, end_lineno=16, end_col_offset=18, id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=18,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=99,
                    name='has_optional_product_in_pos',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=18, col_offset=36, end_lineno=18, end_col_offset=40, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=25,
                            value=Call(
                                lineno=19,
                                col_offset=8,
                                end_lineno=19,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=19,
                                    col_offset=8,
                                    end_lineno=19,
                                    end_col_offset=23,
                                    value=Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=99,
                            value=Call(
                                lineno=20,
                                col_offset=15,
                                end_lineno=20,
                                end_col_offset=99,
                                func=Name(lineno=20, col_offset=15, end_lineno=20, end_col_offset=19, id='bool', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=20,
                                        col_offset=20,
                                        end_lineno=20,
                                        end_col_offset=98,
                                        func=Attribute(
                                            lineno=20,
                                            col_offset=20,
                                            end_lineno=20,
                                            end_col_offset=61,
                                            value=Attribute(
                                                lineno=20,
                                                col_offset=20,
                                                end_lineno=20,
                                                end_col_offset=45,
                                                value=Name(lineno=20, col_offset=20, end_lineno=20, end_col_offset=24, id='self', ctx=Load()),
                                                attr='optional_product_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                lineno=20,
                                                col_offset=62,
                                                end_lineno=20,
                                                end_col_offset=97,
                                                func=Attribute(
                                                    lineno=20,
                                                    col_offset=62,
                                                    end_lineno=20,
                                                    end_col_offset=95,
                                                    value=Name(lineno=20, col_offset=62, end_lineno=20, end_col_offset=66, id='self', ctx=Load()),
                                                    attr='_optional_product_pos_domain',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=22,
                    col_offset=4,
                    end_lineno=26,
                    end_col_offset=9,
                    name='_optional_product_pos_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=22, col_offset=37, end_lineno=22, end_col_offset=41, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=23,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=9,
                            value=List(
                                lineno=23,
                                col_offset=15,
                                end_lineno=26,
                                end_col_offset=9,
                                elts=[
                                    Constant(lineno=24, col_offset=12, end_lineno=24, end_col_offset=15, value='&', kind=None),
                                    Constant(lineno=24, col_offset=17, end_lineno=24, end_col_offset=20, value='&', kind=None),
                                    List(
                                        lineno=24,
                                        col_offset=22,
                                        end_lineno=24,
                                        end_col_offset=44,
                                        elts=[
                                            Constant(lineno=24, col_offset=23, end_lineno=24, end_col_offset=32, value='sale_ok', kind=None),
                                            Constant(lineno=24, col_offset=34, end_lineno=24, end_col_offset=37, value='=', kind=None),
                                            Constant(lineno=24, col_offset=39, end_lineno=24, end_col_offset=43, value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=24,
                                        col_offset=46,
                                        end_lineno=24,
                                        end_col_offset=77,
                                        elts=[
                                            Constant(lineno=24, col_offset=47, end_lineno=24, end_col_offset=65, value='available_in_pos', kind=None),
                                            Constant(lineno=24, col_offset=67, end_lineno=24, end_col_offset=70, value='=', kind=None),
                                            Constant(lineno=24, col_offset=72, end_lineno=24, end_col_offset=76, value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=25, col_offset=12, end_lineno=25, end_col_offset=15, value='|', kind=None),
                                    List(
                                        lineno=25,
                                        col_offset=17,
                                        end_lineno=25,
                                        end_col_offset=54,
                                        elts=[
                                            Constant(lineno=25, col_offset=18, end_lineno=25, end_col_offset=30, value='company_id', kind=None),
                                            Constant(lineno=25, col_offset=32, end_lineno=25, end_col_offset=35, value='=', kind=None),
                                            Attribute(
                                                lineno=25,
                                                col_offset=37,
                                                end_lineno=25,
                                                end_col_offset=53,
                                                value=Attribute(
                                                    lineno=25,
                                                    col_offset=37,
                                                    end_lineno=25,
                                                    end_col_offset=45,
                                                    value=Name(lineno=25, col_offset=37, end_lineno=25, end_col_offset=41, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=25,
                                        col_offset=56,
                                        end_lineno=25,
                                        end_col_offset=82,
                                        elts=[
                                            Constant(lineno=25, col_offset=57, end_lineno=25, end_col_offset=69, value='company_id', kind=None),
                                            Constant(lineno=25, col_offset=71, end_lineno=25, end_col_offset=74, value='=', kind=None),
                                            Constant(lineno=25, col_offset=76, end_lineno=25, end_col_offset=81, value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
