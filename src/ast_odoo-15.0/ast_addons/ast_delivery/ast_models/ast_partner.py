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
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=10,
            end_col_offset=174,
            name='ResPartner',
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
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=28, value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=174,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=32, id='property_delivery_carrier_id', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=35,
                        end_lineno=10,
                        end_col_offset=174,
                        func=Attribute(
                            lineno=10,
                            col_offset=35,
                            end_lineno=10,
                            end_col_offset=50,
                            value=Name(lineno=10, col_offset=35, end_lineno=10, end_col_offset=41, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=51, end_lineno=10, end_col_offset=69, value='delivery.carrier', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=71,
                                end_lineno=10,
                                end_col_offset=93,
                                arg='company_dependent',
                                value=Constant(lineno=10, col_offset=89, end_lineno=10, end_col_offset=93, value=True, kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=95,
                                end_lineno=10,
                                end_col_offset=119,
                                arg='string',
                                value=Constant(lineno=10, col_offset=102, end_lineno=10, end_col_offset=119, value='Delivery Method', kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=121,
                                end_lineno=10,
                                end_col_offset=173,
                                arg='help',
                                value=Constant(lineno=10, col_offset=126, end_lineno=10, end_col_offset=173, value='Default delivery method used in sales orders.', kind=None),
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