Module(
    body=[
        ImportFrom(
            lineno=1,
            col_offset=0,
            end_lineno=1,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=4,
            col_offset=0,
            end_lineno=24,
            end_col_offset=5,
            name='AccountJournal',
            bases=[
                Attribute(
                    lineno=4,
                    col_offset=21,
                    end_lineno=4,
                    end_col_offset=33,
                    value=Name(lineno=4, col_offset=21, end_lineno=4, end_col_offset=27, id='models', ctx=Load()),
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
                    end_col_offset=32,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=6, col_offset=15, end_lineno=6, end_col_offset=32, value='account.journal', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=81,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=18, id='l10n_ec_entity', ctx=Store())],
                    value=Call(
                        lineno=8,
                        col_offset=21,
                        end_lineno=8,
                        end_col_offset=81,
                        func=Attribute(
                            lineno=8,
                            col_offset=21,
                            end_lineno=8,
                            end_col_offset=32,
                            value=Name(lineno=8, col_offset=21, end_lineno=8, end_col_offset=27, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=8,
                                col_offset=33,
                                end_lineno=8,
                                end_col_offset=57,
                                arg='string',
                                value=Constant(lineno=8, col_offset=40, end_lineno=8, end_col_offset=57, value='Emission Entity', kind=None),
                            ),
                            keyword(
                                lineno=8,
                                col_offset=59,
                                end_lineno=8,
                                end_col_offset=65,
                                arg='size',
                                value=Constant(lineno=8, col_offset=64, end_lineno=8, end_col_offset=65, value=3, kind=None),
                            ),
                            keyword(
                                lineno=8,
                                col_offset=67,
                                end_lineno=8,
                                end_col_offset=80,
                                arg='default',
                                value=Constant(lineno=8, col_offset=75, end_lineno=8, end_col_offset=80, value='001', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=82,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=20, id='l10n_ec_emission', ctx=Store())],
                    value=Call(
                        lineno=9,
                        col_offset=23,
                        end_lineno=9,
                        end_col_offset=82,
                        func=Attribute(
                            lineno=9,
                            col_offset=23,
                            end_lineno=9,
                            end_col_offset=34,
                            value=Name(lineno=9, col_offset=23, end_lineno=9, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=9,
                                col_offset=35,
                                end_lineno=9,
                                end_col_offset=58,
                                arg='string',
                                value=Constant(lineno=9, col_offset=42, end_lineno=9, end_col_offset=58, value='Emission Point', kind=None),
                            ),
                            keyword(
                                lineno=9,
                                col_offset=60,
                                end_lineno=9,
                                end_col_offset=66,
                                arg='size',
                                value=Constant(lineno=9, col_offset=65, end_lineno=9, end_col_offset=66, value=3, kind=None),
                            ),
                            keyword(
                                lineno=9,
                                col_offset=68,
                                end_lineno=9,
                                end_col_offset=81,
                                arg='default',
                                value=Constant(lineno=9, col_offset=76, end_lineno=9, end_col_offset=81, value='001', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=5,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=31, id='l10n_ec_emission_address_id', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=34,
                        end_lineno=14,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=10,
                            col_offset=34,
                            end_lineno=10,
                            end_col_offset=49,
                            value=Name(lineno=10, col_offset=34, end_lineno=10, end_col_offset=40, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=34,
                                arg='comodel_name',
                                value=Constant(lineno=11, col_offset=21, end_lineno=11, end_col_offset=34, value='res.partner', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=33,
                                arg='string',
                                value=Constant(lineno=12, col_offset=15, end_lineno=12, end_col_offset=33, value='Emission address', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=127,
                                arg='domain',
                                value=Constant(lineno=13, col_offset=15, end_lineno=13, end_col_offset=127, value="['|', ('id', '=', company_partner_id), '&', ('id', 'child_of', company_partner_id), ('type', '!=', 'contact')]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=5,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=25, id='l10n_ec_emission_type', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=28,
                        end_lineno=24,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=16,
                            col_offset=28,
                            end_lineno=16,
                            end_col_offset=44,
                            value=Name(lineno=16, col_offset=28, end_lineno=16, end_col_offset=34, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=8,
                                end_lineno=17,
                                end_col_offset=30,
                                arg='string',
                                value=Constant(lineno=17, col_offset=15, end_lineno=17, end_col_offset=30, value='Emission type', kind=None),
                            ),
                            keyword(
                                lineno=18,
                                col_offset=8,
                                end_lineno=22,
                                end_col_offset=9,
                                arg='selection',
                                value=List(
                                    lineno=18,
                                    col_offset=18,
                                    end_lineno=22,
                                    end_col_offset=9,
                                    elts=[
                                        Tuple(
                                            lineno=19,
                                            col_offset=12,
                                            end_lineno=19,
                                            end_col_offset=42,
                                            elts=[
                                                Constant(lineno=19, col_offset=13, end_lineno=19, end_col_offset=26, value='pre_printed', kind=None),
                                                Constant(lineno=19, col_offset=28, end_lineno=19, end_col_offset=41, value='Pre Printed', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=20,
                                            col_offset=12,
                                            end_lineno=20,
                                            end_col_offset=44,
                                            elts=[
                                                Constant(lineno=20, col_offset=13, end_lineno=20, end_col_offset=27, value='auto_printer', kind=None),
                                                Constant(lineno=20, col_offset=29, end_lineno=20, end_col_offset=43, value='Auto Printer', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=21,
                                            col_offset=12,
                                            end_lineno=21,
                                            end_col_offset=40,
                                            elts=[
                                                Constant(lineno=21, col_offset=13, end_lineno=21, end_col_offset=25, value='electronic', kind=None),
                                                Constant(lineno=21, col_offset=27, end_lineno=21, end_col_offset=39, value='Electronic', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                lineno=23,
                                col_offset=8,
                                end_lineno=23,
                                end_col_offset=28,
                                arg='default',
                                value=Constant(lineno=23, col_offset=16, end_lineno=23, end_col_offset=28, value='electronic', kind=None),
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
