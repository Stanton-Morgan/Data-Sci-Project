Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=14,
            end_col_offset=36,
            name='ResCountry',
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
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=28, value='res.country', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=37,
                    name='get_website_sale_countries',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=10, col_offset=35, end_lineno=10, end_col_offset=39, arg='self', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=41, end_lineno=10, end_col_offset=45, arg='mode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=10, col_offset=46, end_lineno=10, end_col_offset=55, value='billing', kind=None)],
                    ),
                    body=[
                        Return(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=37,
                            value=Call(
                                lineno=11,
                                col_offset=15,
                                end_lineno=11,
                                end_col_offset=37,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=15,
                                    end_lineno=11,
                                    end_col_offset=33,
                                    value=Call(
                                        lineno=11,
                                        col_offset=15,
                                        end_lineno=11,
                                        end_col_offset=26,
                                        func=Attribute(
                                            lineno=11,
                                            col_offset=15,
                                            end_lineno=11,
                                            end_col_offset=24,
                                            value=Name(lineno=11, col_offset=15, end_lineno=11, end_col_offset=19, id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(lineno=11, col_offset=34, end_lineno=11, end_col_offset=36, elts=[], ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=36,
                    name='get_website_sale_states',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=13, col_offset=32, end_lineno=13, end_col_offset=36, arg='self', annotation=None, type_comment=None),
                            arg(lineno=13, col_offset=38, end_lineno=13, end_col_offset=42, arg='mode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=13, col_offset=43, end_lineno=13, end_col_offset=52, value='billing', kind=None)],
                    ),
                    body=[
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=36,
                            value=Attribute(
                                lineno=14,
                                col_offset=15,
                                end_lineno=14,
                                end_col_offset=36,
                                value=Call(
                                    lineno=14,
                                    col_offset=15,
                                    end_lineno=14,
                                    end_col_offset=26,
                                    func=Attribute(
                                        lineno=14,
                                        col_offset=15,
                                        end_lineno=14,
                                        end_col_offset=24,
                                        value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=19, id='self', ctx=Load()),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='state_ids',
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
