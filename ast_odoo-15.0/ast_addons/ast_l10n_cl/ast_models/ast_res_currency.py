Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=39,
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=10,
            end_col_offset=50,
            name='ResCurrency',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=18,
                    end_lineno=5,
                    end_col_offset=30,
                    value=Name(lineno=5, col_offset=18, end_lineno=5, end_col_offset=24, id='models', ctx=Load()),
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
                    end_col_offset=26,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=6, col_offset=12, end_lineno=6, end_col_offset=26, value='res.currency', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=29,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=29, value='res.currency', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=56,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=25, id='l10n_cl_currency_code', ctx=Store())],
                    value=Call(
                        lineno=9,
                        col_offset=28,
                        end_lineno=9,
                        end_col_offset=56,
                        func=Attribute(
                            lineno=9,
                            col_offset=28,
                            end_lineno=9,
                            end_col_offset=39,
                            value=Name(lineno=9, col_offset=28, end_lineno=9, end_col_offset=34, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=9, col_offset=40, end_lineno=9, end_col_offset=55, value='Currency Code', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=50,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=22, id='l10n_cl_short_name', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=25,
                        end_lineno=10,
                        end_col_offset=50,
                        func=Attribute(
                            lineno=10,
                            col_offset=25,
                            end_lineno=10,
                            end_col_offset=36,
                            value=Name(lineno=10, col_offset=25, end_lineno=10, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=37, end_lineno=10, end_col_offset=49, value='Short Name', kind=None)],
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
