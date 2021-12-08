Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=17,
            end_col_offset=87,
            name='ResCompany',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=17,
                    end_lineno=7,
                    end_col_offset=29,
                    value=Name(lineno=7, col_offset=17, end_lineno=7, end_col_offset=23, id='models', ctx=Load()),
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
                    end_col_offset=28,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=28, value='res.company', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=87,
                    name='_set_default_sale_order_template_id_if_empty',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=53, end_lineno=11, end_col_offset=57, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=111,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=16, id='template', ctx=Store())],
                            value=Call(
                                lineno=12,
                                col_offset=19,
                                end_lineno=12,
                                end_col_offset=111,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=19,
                                    end_lineno=12,
                                    end_col_offset=31,
                                    value=Attribute(
                                        lineno=12,
                                        col_offset=19,
                                        end_lineno=12,
                                        end_col_offset=27,
                                        value=Name(lineno=12, col_offset=19, end_lineno=12, end_col_offset=23, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=12, col_offset=32, end_lineno=12, end_col_offset=84, value='sale_quotation_builder.sale_order_template_default', kind=None)],
                                keywords=[
                                    keyword(
                                        lineno=12,
                                        col_offset=86,
                                        end_lineno=12,
                                        end_col_offset=110,
                                        arg='raise_if_not_found',
                                        value=Constant(lineno=12, col_offset=105, end_lineno=12, end_col_offset=110, value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=13,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=18,
                            test=UnaryOp(
                                lineno=13,
                                col_offset=11,
                                end_lineno=13,
                                end_col_offset=23,
                                op=Not(),
                                operand=Name(lineno=13, col_offset=15, end_lineno=13, end_col_offset=23, id='template', ctx=Load()),
                            ),
                            body=[Return(lineno=14, col_offset=12, end_lineno=14, end_col_offset=18, value=None)],
                            orelse=[],
                        ),
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=42,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=17, id='companies', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=20,
                                end_lineno=15,
                                end_col_offset=42,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=20,
                                    end_lineno=15,
                                    end_col_offset=38,
                                    value=Call(
                                        lineno=15,
                                        col_offset=20,
                                        end_lineno=15,
                                        end_col_offset=31,
                                        func=Attribute(
                                            lineno=15,
                                            col_offset=20,
                                            end_lineno=15,
                                            end_col_offset=29,
                                            value=Name(lineno=15, col_offset=20, end_lineno=15, end_col_offset=24, id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(lineno=15, col_offset=39, end_lineno=15, end_col_offset=41, elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=16,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=87,
                            target=Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=19, id='company', ctx=Store()),
                            iter=Name(lineno=16, col_offset=23, end_lineno=16, end_col_offset=32, id='companies', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=87,
                                    targets=[
                                        Attribute(
                                            lineno=17,
                                            col_offset=12,
                                            end_lineno=17,
                                            end_col_offset=42,
                                            value=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=19, id='company', ctx=Load()),
                                            attr='sale_order_template_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        lineno=17,
                                        col_offset=45,
                                        end_lineno=17,
                                        end_col_offset=87,
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                lineno=17,
                                                col_offset=45,
                                                end_lineno=17,
                                                end_col_offset=75,
                                                value=Name(lineno=17, col_offset=45, end_lineno=17, end_col_offset=52, id='company', ctx=Load()),
                                                attr='sale_order_template_id',
                                                ctx=Load(),
                                            ),
                                            Name(lineno=17, col_offset=79, end_lineno=17, end_col_offset=87, id='template', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=10,
                            col_offset=5,
                            end_lineno=10,
                            end_col_offset=14,
                            value=Name(lineno=10, col_offset=5, end_lineno=10, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
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