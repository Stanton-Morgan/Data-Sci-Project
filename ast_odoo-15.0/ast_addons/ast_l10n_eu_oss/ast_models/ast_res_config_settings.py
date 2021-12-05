Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=19,
            end_col_offset=109,
            name='ResConfigSettings',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=24,
                    end_lineno=7,
                    end_col_offset=45,
                    value=Name(lineno=7, col_offset=24, end_lineno=7, end_col_offset=30, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=36,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=36, value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=116,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=26, id='l10n_eu_oss_eu_country', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=29,
                        end_lineno=10,
                        end_col_offset=116,
                        func=Attribute(
                            lineno=10,
                            col_offset=29,
                            end_lineno=10,
                            end_col_offset=43,
                            value=Name(lineno=10, col_offset=29, end_lineno=10, end_col_offset=35, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=44, end_lineno=10, end_col_offset=66, value='Is European country?', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=68,
                                end_lineno=10,
                                end_col_offset=115,
                                arg='compute',
                                value=Constant(lineno=10, col_offset=76, end_lineno=10, end_col_offset=115, value='_compute_l10n_eu_oss_european_country', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=42,
                    name='refresh_eu_tax_mapping',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=12, col_offset=31, end_lineno=12, end_col_offset=35, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=42,
                            value=Call(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=42,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=8,
                                    end_lineno=13,
                                    end_col_offset=40,
                                    value=Attribute(
                                        lineno=13,
                                        col_offset=8,
                                        end_lineno=13,
                                        end_col_offset=26,
                                        value=Attribute(
                                            lineno=13,
                                            col_offset=8,
                                            end_lineno=13,
                                            end_col_offset=16,
                                            value=Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='companies',
                                        ctx=Load(),
                                    ),
                                    attr='_map_eu_taxes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=109,
                    name='_compute_l10n_eu_oss_european_country',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=46, end_lineno=16, end_col_offset=50, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=68,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=26, id='european_countries', ctx=Store())],
                            value=Attribute(
                                lineno=17,
                                col_offset=29,
                                end_lineno=17,
                                end_col_offset=68,
                                value=Call(
                                    lineno=17,
                                    col_offset=29,
                                    end_lineno=17,
                                    end_col_offset=56,
                                    func=Attribute(
                                        lineno=17,
                                        col_offset=29,
                                        end_lineno=17,
                                        end_col_offset=41,
                                        value=Attribute(
                                            lineno=17,
                                            col_offset=29,
                                            end_lineno=17,
                                            end_col_offset=37,
                                            value=Name(lineno=17, col_offset=29, end_lineno=17, end_col_offset=33, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=17, col_offset=42, end_lineno=17, end_col_offset=55, value='base.europe', kind=None)],
                                    keywords=[],
                                ),
                                attr='country_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=18,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=109,
                            target=Name(lineno=18, col_offset=12, end_lineno=18, end_col_offset=18, id='record', ctx=Store()),
                            iter=Name(lineno=18, col_offset=22, end_lineno=18, end_col_offset=26, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=19,
                                    end_col_offset=109,
                                    targets=[
                                        Attribute(
                                            lineno=19,
                                            col_offset=12,
                                            end_lineno=19,
                                            end_col_offset=41,
                                            value=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=18, id='record', ctx=Load()),
                                            attr='l10n_eu_oss_eu_country',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        lineno=19,
                                        col_offset=44,
                                        end_lineno=19,
                                        end_col_offset=109,
                                        left=Attribute(
                                            lineno=19,
                                            col_offset=44,
                                            end_lineno=19,
                                            end_col_offset=87,
                                            value=Attribute(
                                                lineno=19,
                                                col_offset=44,
                                                end_lineno=19,
                                                end_col_offset=61,
                                                value=Name(lineno=19, col_offset=44, end_lineno=19, end_col_offset=50, id='record', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='account_fiscal_country_id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(lineno=19, col_offset=91, end_lineno=19, end_col_offset=109, id='european_countries', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=15,
                            col_offset=5,
                            end_lineno=15,
                            end_col_offset=30,
                            func=Attribute(
                                lineno=15,
                                col_offset=5,
                                end_lineno=15,
                                end_col_offset=16,
                                value=Name(lineno=15, col_offset=5, end_lineno=15, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=15, col_offset=17, end_lineno=15, end_col_offset=29, value='company_id', kind=None)],
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
