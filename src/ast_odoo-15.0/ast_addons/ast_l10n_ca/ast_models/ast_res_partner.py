Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=39,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=8,
            end_col_offset=36,
            name='ResPartner',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=17,
                    end_lineno=5,
                    end_col_offset=29,
                    value=Name(lineno=5, col_offset=17, end_lineno=5, end_col_offset=23, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=6,
                    col_offset=4,
                    end_lineno=6,
                    end_col_offset=28,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=6, col_offset=15, end_lineno=6, end_col_offset=28, value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=36,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=15, id='l10n_ca_pst', ctx=Store())],
                    value=Call(
                        lineno=8,
                        col_offset=18,
                        end_lineno=8,
                        end_col_offset=36,
                        func=Attribute(
                            lineno=8,
                            col_offset=18,
                            end_lineno=8,
                            end_col_offset=29,
                            value=Name(lineno=8, col_offset=18, end_lineno=8, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=8, col_offset=30, end_lineno=8, end_col_offset=35, value='PST', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)