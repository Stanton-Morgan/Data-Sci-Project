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
            end_lineno=13,
            end_col_offset=6,
            name='UtmCampaign',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=18,
                    end_lineno=7,
                    end_col_offset=30,
                    value=Name(lineno=7, col_offset=18, end_lineno=7, end_col_offset=24, id='models', ctx=Load()),
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
                    end_col_offset=29,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=29, value='utm.campaign', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=6,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=31, id='ab_testing_winner_selection', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=34,
                        end_lineno=13,
                        end_col_offset=6,
                        func=Attribute(
                            lineno=10,
                            col_offset=34,
                            end_lineno=10,
                            end_col_offset=50,
                            value=Name(lineno=10, col_offset=34, end_lineno=10, end_col_offset=40, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=51,
                                end_lineno=13,
                                end_col_offset=5,
                                arg='selection_add',
                                value=List(
                                    lineno=10,
                                    col_offset=65,
                                    end_lineno=13,
                                    end_col_offset=5,
                                    elts=[
                                        Tuple(
                                            lineno=11,
                                            col_offset=8,
                                            end_lineno=11,
                                            end_col_offset=46,
                                            elts=[
                                                Constant(lineno=11, col_offset=9, end_lineno=11, end_col_offset=31, value='sale_quotation_count', kind=None),
                                                Constant(lineno=11, col_offset=33, end_lineno=11, end_col_offset=45, value='Quotations', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=12,
                                            col_offset=8,
                                            end_lineno=12,
                                            end_col_offset=44,
                                            elts=[
                                                Constant(lineno=12, col_offset=9, end_lineno=12, end_col_offset=31, value='sale_invoiced_amount', kind=None),
                                                Constant(lineno=12, col_offset=33, end_lineno=12, end_col_offset=43, value='Revenues', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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