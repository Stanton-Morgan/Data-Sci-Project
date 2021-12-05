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
            end_lineno=15,
            end_col_offset=64,
            name='company',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=14,
                    end_lineno=7,
                    end_col_offset=26,
                    value=Name(lineno=7, col_offset=14, end_lineno=7, end_col_offset=20, id='models', ctx=Load()),
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
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=64,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=17, id='security_lead', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=20,
                        end_lineno=15,
                        end_col_offset=64,
                        func=Attribute(
                            lineno=10,
                            col_offset=20,
                            end_lineno=10,
                            end_col_offset=32,
                            value=Name(lineno=10, col_offset=20, end_lineno=10, end_col_offset=26, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=8, end_lineno=11, end_col_offset=27, value='Sales Safety Days', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=29,
                                end_lineno=11,
                                end_col_offset=40,
                                arg='default',
                                value=Constant(lineno=11, col_offset=37, end_lineno=11, end_col_offset=40, value=0.0, kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=42,
                                end_lineno=11,
                                end_col_offset=55,
                                arg='required',
                                value=Constant(lineno=11, col_offset=51, end_lineno=11, end_col_offset=55, value=True, kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=63,
                                arg='help',
                                value=Constant(lineno=12, col_offset=13, end_lineno=15, end_col_offset=63, value='Margin of error for dates promised to customers. Products will be scheduled for procurement and delivery that many days earlier than the actual promised date, to cope with unexpected delays in the supply chain.', kind=None),
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
