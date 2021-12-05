Module(
    body=[
        ImportFrom(
            lineno=1,
            col_offset=0,
            end_lineno=1,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=4,
            col_offset=0,
            end_lineno=7,
            end_col_offset=181,
            name='PosConfig',
            bases=[
                Attribute(
                    lineno=4,
                    col_offset=16,
                    end_lineno=4,
                    end_col_offset=28,
                    value=Name(lineno=4, col_offset=16, end_lineno=4, end_col_offset=22, id='models', ctx=Load()),
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
                    end_col_offset=27,
                    targets=[Name(lineno=5, col_offset=4, end_lineno=5, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=5, col_offset=15, end_lineno=5, end_col_offset=27, value='pos.config', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=181,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=27, id='iface_open_product_info', ctx=Store())],
                    value=Call(
                        lineno=7,
                        col_offset=30,
                        end_lineno=7,
                        end_col_offset=181,
                        func=Attribute(
                            lineno=7,
                            col_offset=30,
                            end_lineno=7,
                            end_col_offset=44,
                            value=Name(lineno=7, col_offset=30, end_lineno=7, end_col_offset=36, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=7,
                                col_offset=45,
                                end_lineno=7,
                                end_col_offset=71,
                                arg='string',
                                value=Constant(lineno=7, col_offset=52, end_lineno=7, end_col_offset=71, value='Open Product Info', kind=None),
                            ),
                            keyword(
                                lineno=7,
                                col_offset=73,
                                end_lineno=7,
                                end_col_offset=180,
                                arg='help',
                                value=Constant(lineno=7, col_offset=78, end_lineno=7, end_col_offset=180, value="Display the 'Product Info' page when a product with optional products are added in the customer cart", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)