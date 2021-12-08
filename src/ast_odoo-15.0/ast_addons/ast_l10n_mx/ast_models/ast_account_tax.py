Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=23,
            end_col_offset=18,
            name='AccountTaxTemplate',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=25,
                    end_lineno=5,
                    end_col_offset=37,
                    value=Name(lineno=5, col_offset=25, end_lineno=5, end_col_offset=31, id='models', ctx=Load()),
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
                    end_col_offset=37,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=6, col_offset=15, end_lineno=6, end_col_offset=37, value='account.tax.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=60,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=20, id='l10n_mx_tax_type', ctx=Store())],
                    value=Call(
                        lineno=8,
                        col_offset=23,
                        end_lineno=17,
                        end_col_offset=60,
                        func=Attribute(
                            lineno=8,
                            col_offset=23,
                            end_lineno=8,
                            end_col_offset=39,
                            value=Name(lineno=8, col_offset=23, end_lineno=8, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=9,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=9,
                                arg='selection',
                                value=List(
                                    lineno=9,
                                    col_offset=18,
                                    end_lineno=13,
                                    end_col_offset=9,
                                    elts=[
                                        Tuple(
                                            lineno=10,
                                            col_offset=12,
                                            end_lineno=10,
                                            end_col_offset=28,
                                            elts=[
                                                Constant(lineno=10, col_offset=13, end_lineno=10, end_col_offset=19, value='Tasa', kind=None),
                                                Constant(lineno=10, col_offset=21, end_lineno=10, end_col_offset=27, value='Tasa', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=11,
                                            col_offset=12,
                                            end_lineno=11,
                                            end_col_offset=30,
                                            elts=[
                                                Constant(lineno=11, col_offset=13, end_lineno=11, end_col_offset=20, value='Cuota', kind=None),
                                                Constant(lineno=11, col_offset=22, end_lineno=11, end_col_offset=29, value='Cuota', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=12,
                                            col_offset=12,
                                            end_lineno=12,
                                            end_col_offset=32,
                                            elts=[
                                                Constant(lineno=12, col_offset=13, end_lineno=12, end_col_offset=21, value='Exento', kind=None),
                                                Constant(lineno=12, col_offset=23, end_lineno=12, end_col_offset=31, value='Exento', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=28,
                                arg='string',
                                value=Constant(lineno=14, col_offset=15, end_lineno=14, end_col_offset=28, value='Factor Type', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=22,
                                arg='default',
                                value=Constant(lineno=15, col_offset=16, end_lineno=15, end_col_offset=22, value='Tasa', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=8,
                                end_lineno=17,
                                end_col_offset=59,
                                arg='help',
                                value=Constant(lineno=16, col_offset=13, end_lineno=17, end_col_offset=59, value="The CFDI version 3.3 have the attribute 'TipoFactor' in the tax lines. In it is indicated the factor type that is applied to the base of the tax.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=19,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=18,
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
                        Assign(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=65,
                            targets=[Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=21,
                                col_offset=14,
                                end_lineno=21,
                                end_col_offset=65,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=14,
                                    end_lineno=21,
                                    end_col_offset=35,
                                    value=Call(
                                        lineno=21,
                                        col_offset=14,
                                        end_lineno=21,
                                        end_col_offset=21,
                                        func=Name(lineno=21, col_offset=14, end_lineno=21, end_col_offset=19, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_tax_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=21, col_offset=36, end_lineno=21, end_col_offset=43, id='company', ctx=Load()),
                                    Name(lineno=21, col_offset=45, end_lineno=21, end_col_offset=64, id='tax_template_to_tax', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=55,
                            targets=[
                                Subscript(
                                    lineno=22,
                                    col_offset=8,
                                    end_lineno=22,
                                    end_col_offset=31,
                                    value=Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=11, id='res', ctx=Load()),
                                    slice=Constant(lineno=22, col_offset=12, end_lineno=22, end_col_offset=30, value='l10n_mx_tax_type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                lineno=22,
                                col_offset=34,
                                end_lineno=22,
                                end_col_offset=55,
                                value=Name(lineno=22, col_offset=34, end_lineno=22, end_col_offset=38, id='self', ctx=Load()),
                                attr='l10n_mx_tax_type',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=18,
                            value=Name(lineno=23, col_offset=15, end_lineno=23, end_col_offset=18, id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            lineno=26,
            col_offset=0,
            end_lineno=38,
            end_col_offset=60,
            name='AccountTax',
            bases=[
                Attribute(
                    lineno=26,
                    col_offset=17,
                    end_lineno=26,
                    end_col_offset=29,
                    value=Name(lineno=26, col_offset=17, end_lineno=26, end_col_offset=23, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=27,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=28,
                    targets=[Name(lineno=27, col_offset=4, end_lineno=27, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=27, col_offset=15, end_lineno=27, end_col_offset=28, value='account.tax', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=29,
                    col_offset=4,
                    end_lineno=38,
                    end_col_offset=60,
                    targets=[Name(lineno=29, col_offset=4, end_lineno=29, end_col_offset=20, id='l10n_mx_tax_type', ctx=Store())],
                    value=Call(
                        lineno=29,
                        col_offset=23,
                        end_lineno=38,
                        end_col_offset=60,
                        func=Attribute(
                            lineno=29,
                            col_offset=23,
                            end_lineno=29,
                            end_col_offset=39,
                            value=Name(lineno=29, col_offset=23, end_lineno=29, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=30,
                                col_offset=8,
                                end_lineno=34,
                                end_col_offset=9,
                                arg='selection',
                                value=List(
                                    lineno=30,
                                    col_offset=18,
                                    end_lineno=34,
                                    end_col_offset=9,
                                    elts=[
                                        Tuple(
                                            lineno=31,
                                            col_offset=12,
                                            end_lineno=31,
                                            end_col_offset=28,
                                            elts=[
                                                Constant(lineno=31, col_offset=13, end_lineno=31, end_col_offset=19, value='Tasa', kind=None),
                                                Constant(lineno=31, col_offset=21, end_lineno=31, end_col_offset=27, value='Tasa', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=32,
                                            col_offset=12,
                                            end_lineno=32,
                                            end_col_offset=30,
                                            elts=[
                                                Constant(lineno=32, col_offset=13, end_lineno=32, end_col_offset=20, value='Cuota', kind=None),
                                                Constant(lineno=32, col_offset=22, end_lineno=32, end_col_offset=29, value='Cuota', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=33,
                                            col_offset=12,
                                            end_lineno=33,
                                            end_col_offset=32,
                                            elts=[
                                                Constant(lineno=33, col_offset=13, end_lineno=33, end_col_offset=21, value='Exento', kind=None),
                                                Constant(lineno=33, col_offset=23, end_lineno=33, end_col_offset=31, value='Exento', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                lineno=35,
                                col_offset=8,
                                end_lineno=35,
                                end_col_offset=28,
                                arg='string',
                                value=Constant(lineno=35, col_offset=15, end_lineno=35, end_col_offset=28, value='Factor Type', kind=None),
                            ),
                            keyword(
                                lineno=36,
                                col_offset=8,
                                end_lineno=36,
                                end_col_offset=22,
                                arg='default',
                                value=Constant(lineno=36, col_offset=16, end_lineno=36, end_col_offset=22, value='Tasa', kind=None),
                            ),
                            keyword(
                                lineno=37,
                                col_offset=8,
                                end_lineno=38,
                                end_col_offset=59,
                                arg='help',
                                value=Constant(lineno=37, col_offset=13, end_lineno=38, end_col_offset=59, value="The CFDI version 3.3 have the attribute 'TipoFactor' in the tax lines. In it is indicated the factor type that is applied to the base of the tax.", kind=None),
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