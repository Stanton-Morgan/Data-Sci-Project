Module(
    body=[
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=19,
            end_col_offset=5,
            name='ResPartner',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=17,
                    end_lineno=8,
                    end_col_offset=29,
                    value=Name(lineno=8, col_offset=17, end_lineno=8, end_col_offset=23, id='models', ctx=Load()),
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
                    end_col_offset=28,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=28, value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=5,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=30, id='property_payment_method_id', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=33,
                        end_lineno=19,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=11,
                            col_offset=33,
                            end_lineno=11,
                            end_col_offset=48,
                            value=Name(lineno=11, col_offset=33, end_lineno=11, end_col_offset=39, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=45,
                                arg='comodel_name',
                                value=Constant(lineno=12, col_offset=21, end_lineno=12, end_col_offset=45, value='account.payment.method', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=31,
                                arg='string',
                                value=Constant(lineno=13, col_offset=15, end_lineno=13, end_col_offset=31, value='Payment Method', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=30,
                                arg='company_dependent',
                                value=Constant(lineno=14, col_offset=26, end_lineno=14, end_col_offset=30, value=True, kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=52,
                                arg='domain',
                                value=Constant(lineno=15, col_offset=15, end_lineno=15, end_col_offset=52, value="[('payment_type', '=', 'outbound')]", kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=8,
                                end_lineno=18,
                                end_col_offset=50,
                                arg='help',
                                value=Constant(lineno=16, col_offset=13, end_lineno=18, end_col_offset=50, value='Preferred payment method when paying this vendor. This is used to filter vendor bills by preferred payment method to register payments in mass. Use cases: create bank files for batch wires, check runs.', kind=None),
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
