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
            end_lineno=10,
            end_col_offset=57,
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
                    end_lineno=10,
                    end_col_offset=57,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=20, id='l10n_pe_district', ctx=Store())],
                    value=Call(
                        lineno=8,
                        col_offset=23,
                        end_lineno=10,
                        end_col_offset=57,
                        func=Attribute(
                            lineno=8,
                            col_offset=23,
                            end_lineno=8,
                            end_col_offset=38,
                            value=Name(lineno=8, col_offset=23, end_lineno=8, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=9, col_offset=8, end_lineno=9, end_col_offset=35, value='l10n_pe.res.city.district', kind=None)],
                        keywords=[
                            keyword(
                                lineno=9,
                                col_offset=37,
                                end_lineno=9,
                                end_col_offset=54,
                                arg='string',
                                value=Constant(lineno=9, col_offset=44, end_lineno=9, end_col_offset=54, value='District', kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=8,
                                end_lineno=10,
                                end_col_offset=56,
                                arg='help',
                                value=Constant(lineno=10, col_offset=13, end_lineno=10, end_col_offset=56, value='Districts are part of a province or city.', kind=None),
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
