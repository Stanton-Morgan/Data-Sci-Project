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
            end_lineno=36,
            end_col_offset=47,
            name='AccountMove',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=18,
                    end_lineno=7,
                    end_col_offset=30,
                    value=Name(lineno=7, col_offset=18, end_lineno=7, end_col_offset=24, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=29,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=29, value='account.move', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=5,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=27, id='l10n_es_edi_is_required', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=30,
                        end_lineno=13,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=10,
                            col_offset=30,
                            end_lineno=10,
                            end_col_offset=44,
                            value=Name(lineno=10, col_offset=30, end_lineno=10, end_col_offset=36, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=42,
                                arg='string',
                                value=Constant(lineno=11, col_offset=15, end_lineno=11, end_col_offset=42, value='Is the Spanish EDI needed', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=50,
                                arg='compute',
                                value=Constant(lineno=12, col_offset=16, end_lineno=12, end_col_offset=50, value='_compute_l10n_es_edi_is_required', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=71,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=19, id='l10n_es_edi_csv', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=22,
                        end_lineno=14,
                        end_col_offset=71,
                        func=Attribute(
                            lineno=14,
                            col_offset=22,
                            end_lineno=14,
                            end_col_offset=33,
                            value=Name(lineno=14, col_offset=22, end_lineno=14, end_col_offset=28, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=34,
                                end_lineno=14,
                                end_col_offset=58,
                                arg='string',
                                value=Constant(lineno=14, col_offset=41, end_lineno=14, end_col_offset=58, value='CSV return code', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=60,
                                end_lineno=14,
                                end_col_offset=70,
                                arg='copy',
                                value=Constant(lineno=14, col_offset=65, end_lineno=14, end_col_offset=70, value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=5,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=29, id='l10n_es_registration_date', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=32,
                        end_lineno=19,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=15,
                            col_offset=32,
                            end_lineno=15,
                            end_col_offset=43,
                            value=Name(lineno=15, col_offset=32, end_lineno=15, end_col_offset=38, id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=8,
                                end_lineno=16,
                                end_col_offset=34,
                                arg='string',
                                value=Constant(lineno=16, col_offset=15, end_lineno=16, end_col_offset=34, value='Registration Date', kind=None),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=8,
                                end_lineno=18,
                                end_col_offset=42,
                                arg='help',
                                value=Constant(lineno=17, col_offset=13, end_lineno=18, end_col_offset=42, value='Technical field to keep the date the invoice was sent the first time as the date the invoice was registered into the system.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=26,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=85,
                    name='_compute_l10n_es_edi_is_required',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=26, col_offset=41, end_lineno=26, end_col_offset=45, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            lineno=27,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=85,
                            target=Name(lineno=27, col_offset=12, end_lineno=27, end_col_offset=16, id='move', ctx=Store()),
                            iter=Name(lineno=27, col_offset=20, end_lineno=27, end_col_offset=24, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=28,
                                    col_offset=12,
                                    end_lineno=30,
                                    end_col_offset=85,
                                    targets=[
                                        Attribute(
                                            lineno=28,
                                            col_offset=12,
                                            end_lineno=28,
                                            end_col_offset=40,
                                            value=Name(lineno=28, col_offset=12, end_lineno=28, end_col_offset=16, id='move', ctx=Load()),
                                            attr='l10n_es_edi_is_required',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        lineno=28,
                                        col_offset=43,
                                        end_lineno=30,
                                        end_col_offset=85,
                                        op=And(),
                                        values=[
                                            Call(
                                                lineno=28,
                                                col_offset=43,
                                                end_lineno=28,
                                                end_col_offset=60,
                                                func=Attribute(
                                                    lineno=28,
                                                    col_offset=43,
                                                    end_lineno=28,
                                                    end_col_offset=58,
                                                    value=Name(lineno=28, col_offset=43, end_lineno=28, end_col_offset=47, id='move', ctx=Load()),
                                                    attr='is_invoice',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Compare(
                                                lineno=29,
                                                col_offset=47,
                                                end_lineno=29,
                                                end_col_offset=72,
                                                left=Attribute(
                                                    lineno=29,
                                                    col_offset=47,
                                                    end_lineno=29,
                                                    end_col_offset=64,
                                                    value=Name(lineno=29, col_offset=47, end_lineno=29, end_col_offset=51, id='move', ctx=Load()),
                                                    attr='country_code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(lineno=29, col_offset=68, end_lineno=29, end_col_offset=72, value='ES', kind=None)],
                                            ),
                                            Attribute(
                                                lineno=30,
                                                col_offset=47,
                                                end_lineno=30,
                                                end_col_offset=85,
                                                value=Attribute(
                                                    lineno=30,
                                                    col_offset=47,
                                                    end_lineno=30,
                                                    end_col_offset=62,
                                                    value=Name(lineno=30, col_offset=47, end_lineno=30, end_col_offset=51, id='move', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='l10n_es_edi_tax_agency',
                                                ctx=Load(),
                                            ),
                                        ],
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
                            lineno=25,
                            col_offset=5,
                            end_lineno=25,
                            end_col_offset=43,
                            func=Attribute(
                                lineno=25,
                                col_offset=5,
                                end_lineno=25,
                                end_col_offset=16,
                                value=Name(lineno=25, col_offset=5, end_lineno=25, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(lineno=25, col_offset=17, end_lineno=25, end_col_offset=28, value='move_type', kind=None),
                                Constant(lineno=25, col_offset=30, end_lineno=25, end_col_offset=42, value='company_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=33,
                    col_offset=4,
                    end_lineno=36,
                    end_col_offset=47,
                    name='_compute_edi_show_cancel_button',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=33, col_offset=40, end_lineno=33, end_col_offset=44, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=49,
                            value=Call(
                                lineno=34,
                                col_offset=8,
                                end_lineno=34,
                                end_col_offset=49,
                                func=Attribute(
                                    lineno=34,
                                    col_offset=8,
                                    end_lineno=34,
                                    end_col_offset=47,
                                    value=Call(
                                        lineno=34,
                                        col_offset=8,
                                        end_lineno=34,
                                        end_col_offset=15,
                                        func=Name(lineno=34, col_offset=8, end_lineno=34, end_col_offset=13, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compute_edi_show_cancel_button',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            lineno=35,
                            col_offset=8,
                            end_lineno=36,
                            end_col_offset=47,
                            target=Name(lineno=35, col_offset=12, end_lineno=35, end_col_offset=16, id='move', ctx=Store()),
                            iter=Call(
                                lineno=35,
                                col_offset=20,
                                end_lineno=35,
                                end_col_offset=60,
                                func=Attribute(
                                    lineno=35,
                                    col_offset=20,
                                    end_lineno=35,
                                    end_col_offset=33,
                                    value=Name(lineno=35, col_offset=20, end_lineno=35, end_col_offset=24, id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=35, col_offset=34, end_lineno=35, end_col_offset=59, value='l10n_es_edi_is_required', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    lineno=36,
                                    col_offset=12,
                                    end_lineno=36,
                                    end_col_offset=47,
                                    targets=[
                                        Attribute(
                                            lineno=36,
                                            col_offset=12,
                                            end_lineno=36,
                                            end_col_offset=39,
                                            value=Name(lineno=36, col_offset=12, end_lineno=36, end_col_offset=16, id='move', ctx=Load()),
                                            attr='edi_show_cancel_button',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(lineno=36, col_offset=42, end_lineno=36, end_col_offset=47, value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=32,
                            col_offset=5,
                            end_lineno=32,
                            end_col_offset=43,
                            func=Attribute(
                                lineno=32,
                                col_offset=5,
                                end_lineno=32,
                                end_col_offset=16,
                                value=Name(lineno=32, col_offset=5, end_lineno=32, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=32, col_offset=17, end_lineno=32, end_col_offset=42, value='l10n_es_edi_is_required', kind=None)],
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
