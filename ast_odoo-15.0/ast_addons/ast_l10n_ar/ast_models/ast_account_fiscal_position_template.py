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
            end_lineno=11,
            end_col_offset=43,
            name='AccountFiscalPositionTemplate',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=36,
                    end_lineno=5,
                    end_col_offset=48,
                    value=Name(lineno=5, col_offset=36, end_lineno=5, end_col_offset=42, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=49,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=49, value='account.fiscal.position.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=43,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=40, id='l10n_ar_afip_responsibility_type_ids', ctx=Store())],
                    value=Call(
                        lineno=9,
                        col_offset=43,
                        end_lineno=11,
                        end_col_offset=43,
                        func=Attribute(
                            lineno=9,
                            col_offset=43,
                            end_lineno=9,
                            end_col_offset=59,
                            value=Name(lineno=9, col_offset=43, end_lineno=9, end_col_offset=49, id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=10, col_offset=8, end_lineno=10, end_col_offset=42, value='l10n_ar.afip.responsibility.type', kind=None),
                            Constant(lineno=10, col_offset=44, end_lineno=10, end_col_offset=97, value='l10n_ar_afip_reponsibility_type_fiscal_pos_temp_rel', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=42,
                                arg='string',
                                value=Constant(lineno=11, col_offset=15, end_lineno=11, end_col_offset=42, value='AFIP Responsibility Types', kind=None),
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