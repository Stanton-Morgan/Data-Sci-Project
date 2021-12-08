Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=10,
            end_col_offset=71,
            name='AccountTax',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=17,
                    end_lineno=6,
                    end_col_offset=29,
                    value=Name(lineno=6, col_offset=17, end_lineno=6, end_col_offset=23, id='models', ctx=Load()),
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
                    value=Constant(lineno=7, col_offset=12, end_lineno=7, end_col_offset=25, value='account.tax', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=28,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=28, value='account.tax', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=71,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=20, id='l10n_cl_sii_code', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=23,
                        end_lineno=10,
                        end_col_offset=71,
                        func=Attribute(
                            lineno=10,
                            col_offset=23,
                            end_lineno=10,
                            end_col_offset=37,
                            value=Name(lineno=10, col_offset=23, end_lineno=10, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=38, end_lineno=10, end_col_offset=48, value='SII Code', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=50,
                                end_lineno=10,
                                end_col_offset=70,
                                arg='group_operator',
                                value=Constant(lineno=10, col_offset=65, end_lineno=10, end_col_offset=70, value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            lineno=13,
            col_offset=0,
            end_lineno=27,
            end_col_offset=19,
            name='AccountTaxTemplate',
            bases=[
                Attribute(
                    lineno=13,
                    col_offset=25,
                    end_lineno=13,
                    end_col_offset=37,
                    value=Name(lineno=13, col_offset=25, end_lineno=13, end_col_offset=31, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=34,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=14, col_offset=12, end_lineno=14, end_col_offset=34, value='account.tax.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=37,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=15, col_offset=15, end_lineno=15, end_col_offset=37, value='account.tax.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=49,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=20, id='l10n_cl_sii_code', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=23,
                        end_lineno=17,
                        end_col_offset=49,
                        func=Attribute(
                            lineno=17,
                            col_offset=23,
                            end_lineno=17,
                            end_col_offset=37,
                            value=Name(lineno=17, col_offset=23, end_lineno=17, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=38, end_lineno=17, end_col_offset=48, value='SII Code', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=19,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=19,
                    name='_get_tax_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=19, col_offset=22, end_lineno=19, end_col_offset=26, arg='self', annotation=None, type_comment=None),
                            arg(lineno=19, col_offset=28, end_lineno=19, end_col_offset=35, arg='company', annotation=None, type_comment=None),
                            arg(lineno=19, col_offset=37, end_lineno=19, end_col_offset=56, arg='tax_template_to_tax', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=25,
                            value=Call(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=23,
                                    value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=90,
                            targets=[Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=12, id='vals', ctx=Store())],
                            value=Call(
                                lineno=21,
                                col_offset=15,
                                end_lineno=21,
                                end_col_offset=90,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=15,
                                    end_lineno=21,
                                    end_col_offset=60,
                                    value=Call(
                                        lineno=21,
                                        col_offset=15,
                                        end_lineno=21,
                                        end_col_offset=46,
                                        func=Name(lineno=21, col_offset=15, end_lineno=21, end_col_offset=20, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=21, col_offset=21, end_lineno=21, end_col_offset=39, id='AccountTaxTemplate', ctx=Load()),
                                            Name(lineno=21, col_offset=41, end_lineno=21, end_col_offset=45, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_tax_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=21, col_offset=61, end_lineno=21, end_col_offset=68, id='company', ctx=Load()),
                                    Name(lineno=21, col_offset=70, end_lineno=21, end_col_offset=89, id='tax_template_to_tax', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=22,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=10,
                            value=Call(
                                lineno=22,
                                col_offset=8,
                                end_lineno=24,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=22,
                                    col_offset=8,
                                    end_lineno=22,
                                    end_col_offset=19,
                                    value=Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=12, id='vals', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=22,
                                        col_offset=20,
                                        end_lineno=24,
                                        end_col_offset=9,
                                        keys=[Constant(lineno=23, col_offset=12, end_lineno=23, end_col_offset=30, value='l10n_cl_sii_code', kind=None)],
                                        values=[
                                            Attribute(
                                                lineno=23,
                                                col_offset=32,
                                                end_lineno=23,
                                                end_col_offset=53,
                                                value=Name(lineno=23, col_offset=32, end_lineno=23, end_col_offset=36, id='self', ctx=Load()),
                                                attr='l10n_cl_sii_code',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            lineno=25,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=55,
                            test=Attribute(
                                lineno=25,
                                col_offset=11,
                                end_lineno=25,
                                end_col_offset=28,
                                value=Name(lineno=25, col_offset=11, end_lineno=25, end_col_offset=15, id='self', ctx=Load()),
                                attr='tax_group_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    lineno=26,
                                    col_offset=12,
                                    end_lineno=26,
                                    end_col_offset=55,
                                    targets=[
                                        Subscript(
                                            lineno=26,
                                            col_offset=12,
                                            end_lineno=26,
                                            end_col_offset=32,
                                            value=Name(lineno=26, col_offset=12, end_lineno=26, end_col_offset=16, id='vals', ctx=Load()),
                                            slice=Constant(lineno=26, col_offset=17, end_lineno=26, end_col_offset=31, value='tax_group_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        lineno=26,
                                        col_offset=35,
                                        end_lineno=26,
                                        end_col_offset=55,
                                        value=Attribute(
                                            lineno=26,
                                            col_offset=35,
                                            end_lineno=26,
                                            end_col_offset=52,
                                            value=Name(lineno=26, col_offset=35, end_lineno=26, end_col_offset=39, id='self', ctx=Load()),
                                            attr='tax_group_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=27,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=19,
                            value=Name(lineno=27, col_offset=15, end_lineno=27, end_col_offset=19, id='vals', ctx=Load()),
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