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
            end_lineno=14,
            end_col_offset=19,
            name='L10nPeResCityDistrict',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=28,
                    end_lineno=5,
                    end_col_offset=40,
                    value=Name(lineno=5, col_offset=28, end_lineno=5, end_col_offset=34, id='models', ctx=Load()),
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
                    end_col_offset=39,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=6, col_offset=12, end_lineno=6, end_col_offset=39, value='l10n_pe.res.city.district', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=29,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=7, col_offset=19, end_lineno=7, end_col_offset=29, value='District', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=19,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=8, col_offset=13, end_lineno=8, end_col_offset=19, value='name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=38,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=11,
                        end_lineno=10,
                        end_col_offset=38,
                        func=Attribute(
                            lineno=10,
                            col_offset=11,
                            end_lineno=10,
                            end_col_offset=22,
                            value=Name(lineno=10, col_offset=11, end_lineno=10, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=23,
                                end_lineno=10,
                                end_col_offset=37,
                                arg='translate',
                                value=Constant(lineno=10, col_offset=33, end_lineno=10, end_col_offset=37, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=49,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=11, id='city_id', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=14,
                        end_lineno=11,
                        end_col_offset=49,
                        func=Attribute(
                            lineno=11,
                            col_offset=14,
                            end_lineno=11,
                            end_col_offset=29,
                            value=Name(lineno=11, col_offset=14, end_lineno=11, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=11, col_offset=30, end_lineno=11, end_col_offset=40, value='res.city', kind=None),
                            Constant(lineno=11, col_offset=42, end_lineno=11, end_col_offset=48, value='City', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=19,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=8, id='code', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=11,
                        end_lineno=14,
                        end_col_offset=19,
                        func=Attribute(
                            lineno=12,
                            col_offset=11,
                            end_lineno=12,
                            end_col_offset=22,
                            value=Name(lineno=12, col_offset=11, end_lineno=12, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=18,
                                arg='help',
                                value=Constant(lineno=13, col_offset=13, end_lineno=14, end_col_offset=18, value='This code will help with the identification of each district in Peru.', kind=None),
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
