Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=9,
            end_col_offset=57,
            name='ResBank',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=14,
                    end_lineno=5,
                    end_col_offset=26,
                    value=Name(lineno=5, col_offset=14, end_lineno=5, end_col_offset=20, id='models', ctx=Load()),
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
                    end_col_offset=22,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=6, col_offset=12, end_lineno=6, end_col_offset=22, value='res.bank', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=25,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=25, value='res.bank', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=57,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=21, id='l10n_cl_sbif_code', ctx=Store())],
                    value=Call(
                        lineno=9,
                        col_offset=24,
                        end_lineno=9,
                        end_col_offset=57,
                        func=Attribute(
                            lineno=9,
                            col_offset=24,
                            end_lineno=9,
                            end_col_offset=35,
                            value=Name(lineno=9, col_offset=24, end_lineno=9, end_col_offset=30, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=9, col_offset=36, end_lineno=9, end_col_offset=47, value='Cod. SBIF', kind=None)],
                        keywords=[
                            keyword(
                                lineno=9,
                                col_offset=49,
                                end_lineno=9,
                                end_col_offset=56,
                                arg='size',
                                value=Constant(lineno=9, col_offset=54, end_lineno=9, end_col_offset=56, value=10, kind=None),
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