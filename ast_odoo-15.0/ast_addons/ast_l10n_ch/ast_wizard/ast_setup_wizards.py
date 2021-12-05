Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=16,
            end_col_offset=71,
            name='SwissSetupBarBankConfigWizard',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=36,
                    end_lineno=6,
                    end_col_offset=57,
                    value=Name(lineno=6, col_offset=36, end_lineno=6, end_col_offset=42, id='models', ctx=Load()),
                    attr='TransientModel',
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
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=49, value='account.setup.bank.manual.config', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=71,
                    name='_onchange_recompute_qr_iban',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=36, end_lineno=10, end_col_offset=40, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=61,
                            targets=[
                                Attribute(
                                    lineno=14,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=43,
                                    value=Attribute(
                                        lineno=14,
                                        col_offset=8,
                                        end_lineno=14,
                                        end_col_offset=32,
                                        value=Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=12, id='self', ctx=Load()),
                                        attr='res_partner_bank_id',
                                        ctx=Load(),
                                    ),
                                    attr='acc_number',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                lineno=14,
                                col_offset=46,
                                end_lineno=14,
                                end_col_offset=61,
                                value=Name(lineno=14, col_offset=46, end_lineno=14, end_col_offset=50, id='self', ctx=Load()),
                                attr='acc_number',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=59,
                            value=Call(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=59,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=8,
                                    end_lineno=15,
                                    end_col_offset=57,
                                    value=Attribute(
                                        lineno=15,
                                        col_offset=8,
                                        end_lineno=15,
                                        end_col_offset=32,
                                        value=Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=12, id='self', ctx=Load()),
                                        attr='res_partner_bank_id',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_l10n_ch_qr_iban',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=71,
                            targets=[
                                Attribute(
                                    lineno=16,
                                    col_offset=8,
                                    end_lineno=16,
                                    end_col_offset=28,
                                    value=Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=12, id='self', ctx=Load()),
                                    attr='l10n_ch_qr_iban',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                lineno=16,
                                col_offset=31,
                                end_lineno=16,
                                end_col_offset=71,
                                value=Attribute(
                                    lineno=16,
                                    col_offset=31,
                                    end_lineno=16,
                                    end_col_offset=55,
                                    value=Name(lineno=16, col_offset=31, end_lineno=16, end_col_offset=35, id='self', ctx=Load()),
                                    attr='res_partner_bank_id',
                                    ctx=Load(),
                                ),
                                attr='l10n_ch_qr_iban',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=9,
                            col_offset=5,
                            end_lineno=9,
                            end_col_offset=31,
                            func=Attribute(
                                lineno=9,
                                col_offset=5,
                                end_lineno=9,
                                end_col_offset=17,
                                value=Name(lineno=9, col_offset=5, end_lineno=9, end_col_offset=8, id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=9, col_offset=18, end_lineno=9, end_col_offset=30, value='acc_number', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
