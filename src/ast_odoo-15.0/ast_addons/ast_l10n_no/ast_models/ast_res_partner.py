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
            end_lineno=8,
            end_col_offset=121,
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
                    end_col_offset=121,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=30, id='l10n_no_bronnoysund_number', ctx=Store())],
                    value=Call(
                        lineno=8,
                        col_offset=33,
                        end_lineno=8,
                        end_col_offset=121,
                        func=Attribute(
                            lineno=8,
                            col_offset=33,
                            end_lineno=8,
                            end_col_offset=44,
                            value=Name(lineno=8, col_offset=33, end_lineno=8, end_col_offset=39, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=8,
                                col_offset=45,
                                end_lineno=8,
                                end_col_offset=112,
                                arg='string',
                                value=Constant(lineno=8, col_offset=52, end_lineno=8, end_col_offset=112, value='Register of Legal Entities (Brønnøysund Register Center)', kind=None),
                            ),
                            keyword(
                                lineno=8,
                                col_offset=114,
                                end_lineno=8,
                                end_col_offset=120,
                                arg='size',
                                value=Constant(lineno=8, col_offset=119, end_lineno=8, end_col_offset=120, value=9, kind=None),
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