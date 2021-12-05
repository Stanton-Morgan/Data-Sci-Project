Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=23,
            end_col_offset=18,
            name='AccountChartTemplate',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=27,
                    end_lineno=5,
                    end_col_offset=39,
                    value=Name(lineno=5, col_offset=27, end_lineno=5, end_col_offset=33, id='models', ctx=Load()),
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
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=6, col_offset=15, end_lineno=6, end_col_offset=39, value='account.chart.template', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=18,
                    name='_prepare_transfer_account_for_direct_creation',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=9, col_offset=54, end_lineno=9, end_col_offset=58, arg='self', annotation=None, type_comment=None),
                            arg(lineno=9, col_offset=60, end_lineno=9, end_col_offset=64, arg='name', annotation=None, type_comment=None),
                            arg(lineno=9, col_offset=66, end_lineno=9, end_col_offset=73, arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=10,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=108,
                            targets=[Name(lineno=10, col_offset=8, end_lineno=10, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=10,
                                col_offset=14,
                                end_lineno=10,
                                end_col_offset=108,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=14,
                                    end_lineno=10,
                                    end_col_offset=93,
                                    value=Call(
                                        lineno=10,
                                        col_offset=14,
                                        end_lineno=10,
                                        end_col_offset=47,
                                        func=Name(lineno=10, col_offset=14, end_lineno=10, end_col_offset=19, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=10, col_offset=20, end_lineno=10, end_col_offset=40, id='AccountChartTemplate', ctx=Load()),
                                            Name(lineno=10, col_offset=42, end_lineno=10, end_col_offset=46, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_transfer_account_for_direct_creation',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=10, col_offset=94, end_lineno=10, end_col_offset=98, id='name', ctx=Load()),
                                    Name(lineno=10, col_offset=100, end_lineno=10, end_col_offset=107, id='company', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=11,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=46,
                            test=Compare(
                                lineno=11,
                                col_offset=11,
                                end_lineno=11,
                                end_col_offset=57,
                                left=Attribute(
                                    lineno=11,
                                    col_offset=11,
                                    end_lineno=11,
                                    end_col_offset=49,
                                    value=Attribute(
                                        lineno=11,
                                        col_offset=11,
                                        end_lineno=11,
                                        end_col_offset=44,
                                        value=Name(lineno=11, col_offset=11, end_lineno=11, end_col_offset=18, id='company', ctx=Load()),
                                        attr='account_fiscal_country_id',
                                        ctx=Load(),
                                    ),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(lineno=11, col_offset=53, end_lineno=11, end_col_offset=57, value='DE', kind=None)],
                            ),
                            body=[
                                Assign(
                                    lineno=12,
                                    col_offset=12,
                                    end_lineno=12,
                                    end_col_offset=71,
                                    targets=[Name(lineno=12, col_offset=12, end_lineno=12, end_col_offset=18, id='xml_id', ctx=Store())],
                                    value=Attribute(
                                        lineno=12,
                                        col_offset=21,
                                        end_lineno=12,
                                        end_col_offset=71,
                                        value=Call(
                                            lineno=12,
                                            col_offset=21,
                                            end_lineno=12,
                                            end_col_offset=68,
                                            func=Attribute(
                                                lineno=12,
                                                col_offset=21,
                                                end_lineno=12,
                                                end_col_offset=33,
                                                value=Attribute(
                                                    lineno=12,
                                                    col_offset=21,
                                                    end_lineno=12,
                                                    end_col_offset=29,
                                                    value=Name(lineno=12, col_offset=21, end_lineno=12, end_col_offset=25, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='ref',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(lineno=12, col_offset=34, end_lineno=12, end_col_offset=67, value='l10n_de.tag_de_asset_bs_B_III_2', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    lineno=13,
                                    col_offset=12,
                                    end_lineno=13,
                                    end_col_offset=41,
                                    value=Call(
                                        lineno=13,
                                        col_offset=12,
                                        end_lineno=13,
                                        end_col_offset=41,
                                        func=Attribute(
                                            lineno=13,
                                            col_offset=12,
                                            end_lineno=13,
                                            end_col_offset=26,
                                            value=Name(lineno=13, col_offset=12, end_lineno=13, end_col_offset=15, id='res', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(lineno=13, col_offset=27, end_lineno=13, end_col_offset=36, value='tag_ids', kind=None),
                                            List(lineno=13, col_offset=38, end_lineno=13, end_col_offset=40, elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=14,
                                    end_col_offset=46,
                                    value=Call(
                                        lineno=14,
                                        col_offset=12,
                                        end_lineno=14,
                                        end_col_offset=46,
                                        func=Attribute(
                                            lineno=14,
                                            col_offset=12,
                                            end_lineno=14,
                                            end_col_offset=33,
                                            value=Subscript(
                                                lineno=14,
                                                col_offset=12,
                                                end_lineno=14,
                                                end_col_offset=26,
                                                value=Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=15, id='res', ctx=Load()),
                                                slice=Constant(lineno=14, col_offset=16, end_lineno=14, end_col_offset=25, value='tag_ids', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                lineno=14,
                                                col_offset=34,
                                                end_lineno=14,
                                                end_col_offset=45,
                                                elts=[
                                                    Constant(lineno=14, col_offset=35, end_lineno=14, end_col_offset=36, value=4, kind=None),
                                                    Name(lineno=14, col_offset=38, end_lineno=14, end_col_offset=44, id='xml_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=18,
                            value=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=18, id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=8,
                            col_offset=5,
                            end_lineno=8,
                            end_col_offset=14,
                            value=Name(lineno=8, col_offset=5, end_lineno=8, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=18,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=18,
                    name='_load',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=18, col_offset=14, end_lineno=18, end_col_offset=18, arg='self', annotation=None, type_comment=None),
                            arg(lineno=18, col_offset=20, end_lineno=18, end_col_offset=33, arg='sale_tax_rate', annotation=None, type_comment=None),
                            arg(lineno=18, col_offset=35, end_lineno=18, end_col_offset=52, arg='purchase_tax_rate', annotation=None, type_comment=None),
                            arg(lineno=18, col_offset=54, end_lineno=18, end_col_offset=61, arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=96,
                            targets=[Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=19,
                                col_offset=14,
                                end_lineno=19,
                                end_col_offset=96,
                                func=Attribute(
                                    lineno=19,
                                    col_offset=14,
                                    end_lineno=19,
                                    end_col_offset=53,
                                    value=Call(
                                        lineno=19,
                                        col_offset=14,
                                        end_lineno=19,
                                        end_col_offset=47,
                                        func=Name(lineno=19, col_offset=14, end_lineno=19, end_col_offset=19, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=19, col_offset=20, end_lineno=19, end_col_offset=40, id='AccountChartTemplate', ctx=Load()),
                                            Name(lineno=19, col_offset=42, end_lineno=19, end_col_offset=46, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_load',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=19, col_offset=54, end_lineno=19, end_col_offset=67, id='sale_tax_rate', ctx=Load()),
                                    Name(lineno=19, col_offset=69, end_lineno=19, end_col_offset=86, id='purchase_tax_rate', ctx=Load()),
                                    Name(lineno=19, col_offset=88, end_lineno=19, end_col_offset=95, id='company', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=20,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=79,
                            test=Compare(
                                lineno=20,
                                col_offset=11,
                                end_lineno=20,
                                end_col_offset=57,
                                left=Attribute(
                                    lineno=20,
                                    col_offset=11,
                                    end_lineno=20,
                                    end_col_offset=49,
                                    value=Attribute(
                                        lineno=20,
                                        col_offset=11,
                                        end_lineno=20,
                                        end_col_offset=44,
                                        value=Name(lineno=20, col_offset=11, end_lineno=20, end_col_offset=18, id='company', ctx=Load()),
                                        attr='account_fiscal_country_id',
                                        ctx=Load(),
                                    ),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(lineno=20, col_offset=53, end_lineno=20, end_col_offset=57, value='DE', kind=None)],
                            ),
                            body=[
                                Expr(
                                    lineno=21,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=79,
                                    value=Call(
                                        lineno=21,
                                        col_offset=12,
                                        end_lineno=22,
                                        end_col_offset=79,
                                        func=Attribute(
                                            lineno=21,
                                            col_offset=12,
                                            end_lineno=21,
                                            end_col_offset=25,
                                            value=Name(lineno=21, col_offset=12, end_lineno=21, end_col_offset=19, id='company', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=21,
                                                col_offset=26,
                                                end_lineno=22,
                                                end_col_offset=78,
                                                keys=[
                                                    Constant(lineno=21, col_offset=27, end_lineno=21, end_col_offset=54, value='external_report_layout_id', kind=None),
                                                    Constant(lineno=22, col_offset=12, end_lineno=22, end_col_offset=28, value='paperformat_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        lineno=21,
                                                        col_offset=56,
                                                        end_lineno=21,
                                                        end_col_offset=106,
                                                        value=Call(
                                                            lineno=21,
                                                            col_offset=56,
                                                            end_lineno=21,
                                                            end_col_offset=103,
                                                            func=Attribute(
                                                                lineno=21,
                                                                col_offset=56,
                                                                end_lineno=21,
                                                                end_col_offset=68,
                                                                value=Attribute(
                                                                    lineno=21,
                                                                    col_offset=56,
                                                                    end_lineno=21,
                                                                    end_col_offset=64,
                                                                    value=Name(lineno=21, col_offset=56, end_lineno=21, end_col_offset=60, id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(lineno=21, col_offset=69, end_lineno=21, end_col_offset=102, value='l10n_de.external_layout_din5008', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        lineno=22,
                                                        col_offset=30,
                                                        end_lineno=22,
                                                        end_col_offset=77,
                                                        value=Call(
                                                            lineno=22,
                                                            col_offset=30,
                                                            end_lineno=22,
                                                            end_col_offset=74,
                                                            func=Attribute(
                                                                lineno=22,
                                                                col_offset=30,
                                                                end_lineno=22,
                                                                end_col_offset=42,
                                                                value=Attribute(
                                                                    lineno=22,
                                                                    col_offset=30,
                                                                    end_lineno=22,
                                                                    end_col_offset=38,
                                                                    value=Name(lineno=22, col_offset=30, end_lineno=22, end_col_offset=34, id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(lineno=22, col_offset=43, end_lineno=22, end_col_offset=73, value='l10n_de.paperformat_euro_din', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
    ],
    type_ignores=[],
)
