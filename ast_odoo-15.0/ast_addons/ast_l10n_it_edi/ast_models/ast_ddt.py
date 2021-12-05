Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=18,
            end_col_offset=18,
            name='L10nItDdt',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=16,
                    end_lineno=6,
                    end_col_offset=28,
                    value=Name(lineno=6, col_offset=16, end_lineno=6, end_col_offset=22, id='models', ctx=Load()),
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
                    end_col_offset=25,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=7, col_offset=12, end_lineno=7, end_col_offset=25, value='l10n_it.ddt', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=39,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=8, col_offset=19, end_lineno=8, end_col_offset=39, value='Transport Document', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=94,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=14, id='invoice_id', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=17,
                        end_lineno=10,
                        end_col_offset=94,
                        func=Attribute(
                            lineno=10,
                            col_offset=17,
                            end_lineno=10,
                            end_col_offset=32,
                            value=Name(lineno=10, col_offset=17, end_lineno=10, end_col_offset=23, id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=10, col_offset=33, end_lineno=10, end_col_offset=47, value='account.move', kind=None),
                            Constant(lineno=10, col_offset=49, end_lineno=10, end_col_offset=65, value='l10n_it_ddt_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=67,
                                end_lineno=10,
                                end_col_offset=93,
                                arg='string',
                                value=Constant(lineno=10, col_offset=74, end_lineno=10, end_col_offset=93, value='Invoice Reference', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=101,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=11,
                        end_lineno=11,
                        end_col_offset=101,
                        func=Attribute(
                            lineno=11,
                            col_offset=11,
                            end_lineno=11,
                            end_col_offset=22,
                            value=Name(lineno=11, col_offset=11, end_lineno=11, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=23,
                                end_lineno=11,
                                end_col_offset=42,
                                arg='string',
                                value=Constant(lineno=11, col_offset=30, end_lineno=11, end_col_offset=42, value='Numero DDT', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=44,
                                end_lineno=11,
                                end_col_offset=51,
                                arg='size',
                                value=Constant(lineno=11, col_offset=49, end_lineno=11, end_col_offset=51, value=20, kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=53,
                                end_lineno=11,
                                end_col_offset=85,
                                arg='help',
                                value=Constant(lineno=11, col_offset=58, end_lineno=11, end_col_offset=85, value='Transport document number', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=87,
                                end_lineno=11,
                                end_col_offset=100,
                                arg='required',
                                value=Constant(lineno=11, col_offset=96, end_lineno=11, end_col_offset=100, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=88,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=8, id='date', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=11,
                        end_lineno=12,
                        end_col_offset=88,
                        func=Attribute(
                            lineno=12,
                            col_offset=11,
                            end_lineno=12,
                            end_col_offset=22,
                            value=Name(lineno=12, col_offset=11, end_lineno=12, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=23,
                                end_lineno=12,
                                end_col_offset=40,
                                arg='string',
                                value=Constant(lineno=12, col_offset=30, end_lineno=12, end_col_offset=40, value='Data DDT', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=42,
                                end_lineno=12,
                                end_col_offset=72,
                                arg='help',
                                value=Constant(lineno=12, col_offset=47, end_lineno=12, end_col_offset=72, value='Transport document date', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=74,
                                end_lineno=12,
                                end_col_offset=87,
                                arg='required',
                                value=Constant(lineno=12, col_offset=83, end_lineno=12, end_col_offset=87, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=18,
                    name='name_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=17, end_lineno=14, end_col_offset=21, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=16,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=11, id='res', ctx=Store())],
                            value=List(lineno=15, col_offset=14, end_lineno=15, end_col_offset=16, elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            lineno=16,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=68,
                            target=Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=15, id='ddt', ctx=Store()),
                            iter=Name(lineno=16, col_offset=19, end_lineno=16, end_col_offset=23, id='self', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=68,
                                    value=Call(
                                        lineno=17,
                                        col_offset=12,
                                        end_lineno=17,
                                        end_col_offset=68,
                                        func=Attribute(
                                            lineno=17,
                                            col_offset=12,
                                            end_lineno=17,
                                            end_col_offset=22,
                                            value=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=15, id='res', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                lineno=17,
                                                col_offset=23,
                                                end_lineno=17,
                                                end_col_offset=67,
                                                elts=[
                                                    Attribute(
                                                        lineno=17,
                                                        col_offset=24,
                                                        end_lineno=17,
                                                        end_col_offset=30,
                                                        value=Name(lineno=17, col_offset=24, end_lineno=17, end_col_offset=27, id='ddt', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        lineno=17,
                                                        col_offset=32,
                                                        end_lineno=17,
                                                        end_col_offset=66,
                                                        left=Constant(lineno=17, col_offset=33, end_lineno=17, end_col_offset=42, value='%s (%s)', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            lineno=17,
                                                            col_offset=46,
                                                            end_lineno=17,
                                                            end_col_offset=66,
                                                            elts=[
                                                                Attribute(
                                                                    lineno=17,
                                                                    col_offset=47,
                                                                    end_lineno=17,
                                                                    end_col_offset=55,
                                                                    value=Name(lineno=17, col_offset=47, end_lineno=17, end_col_offset=50, id='ddt', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    lineno=17,
                                                                    col_offset=57,
                                                                    end_lineno=17,
                                                                    end_col_offset=65,
                                                                    value=Name(lineno=17, col_offset=57, end_lineno=17, end_col_offset=60, id='ddt', ctx=Load()),
                                                                    attr='date',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=18,
                            value=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=18, id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
