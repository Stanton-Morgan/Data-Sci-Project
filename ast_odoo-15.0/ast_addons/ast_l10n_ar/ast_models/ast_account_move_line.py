Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=30,
            end_col_offset=9,
            name='AccountMoveLine',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=22,
                    end_lineno=5,
                    end_col_offset=34,
                    value=Name(lineno=5, col_offset=22, end_lineno=5, end_col_offset=28, id='models', ctx=Load()),
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
                    end_col_offset=34,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=34, value='account.move.line', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=9,
                    name='_l10n_ar_prices_and_taxes',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=34, end_lineno=9, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=10,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=25,
                            value=Call(
                                lineno=10,
                                col_offset=8,
                                end_lineno=10,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=8,
                                    end_lineno=10,
                                    end_col_offset=23,
                                    value=Name(lineno=10, col_offset=8, end_lineno=10, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=30,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=15, id='invoice', ctx=Store())],
                            value=Attribute(
                                lineno=11,
                                col_offset=18,
                                end_lineno=11,
                                end_col_offset=30,
                                value=Name(lineno=11, col_offset=18, end_lineno=11, end_col_offset=22, id='self', ctx=Load()),
                                attr='move_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=141,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=22, id='included_taxes', ctx=Store())],
                            value=IfExp(
                                lineno=12,
                                col_offset=25,
                                end_lineno=12,
                                end_col_offset=141,
                                test=Call(
                                    lineno=12,
                                    col_offset=88,
                                    end_lineno=12,
                                    end_col_offset=123,
                                    func=Attribute(
                                        lineno=12,
                                        col_offset=88,
                                        end_lineno=12,
                                        end_col_offset=121,
                                        value=Attribute(
                                            lineno=12,
                                            col_offset=88,
                                            end_lineno=12,
                                            end_col_offset=100,
                                            value=Name(lineno=12, col_offset=88, end_lineno=12, end_col_offset=92, id='self', ctx=Load()),
                                            attr='move_id',
                                            ctx=Load(),
                                        ),
                                        attr='_l10n_ar_include_vat',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                body=Call(
                                    lineno=12,
                                    col_offset=25,
                                    end_lineno=12,
                                    end_col_offset=84,
                                    func=Attribute(
                                        lineno=12,
                                        col_offset=25,
                                        end_lineno=12,
                                        end_col_offset=46,
                                        value=Attribute(
                                            lineno=12,
                                            col_offset=25,
                                            end_lineno=12,
                                            end_col_offset=37,
                                            value=Name(lineno=12, col_offset=25, end_lineno=12, end_col_offset=29, id='self', ctx=Load()),
                                            attr='tax_ids',
                                            ctx=Load(),
                                        ),
                                        attr='filtered',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=12, col_offset=47, end_lineno=12, end_col_offset=83, value='tax_group_id.l10n_ar_vat_afip_code', kind=None)],
                                    keywords=[],
                                ),
                                orelse=Attribute(
                                    lineno=12,
                                    col_offset=129,
                                    end_lineno=12,
                                    end_col_offset=141,
                                    value=Name(lineno=12, col_offset=129, end_lineno=12, end_col_offset=133, id='self', ctx=Load()),
                                    attr='tax_ids',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=13,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=113,
                            test=UnaryOp(
                                lineno=13,
                                col_offset=11,
                                end_lineno=13,
                                end_col_offset=29,
                                op=Not(),
                                operand=Name(lineno=13, col_offset=15, end_lineno=13, end_col_offset=29, id='included_taxes', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=15,
                                    end_col_offset=95,
                                    targets=[Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=22, id='price_unit', ctx=Store())],
                                    value=Call(
                                        lineno=14,
                                        col_offset=25,
                                        end_lineno=15,
                                        end_col_offset=95,
                                        func=Attribute(
                                            lineno=14,
                                            col_offset=25,
                                            end_lineno=14,
                                            end_col_offset=75,
                                            value=Call(
                                                lineno=14,
                                                col_offset=25,
                                                end_lineno=14,
                                                end_col_offset=63,
                                                func=Attribute(
                                                    lineno=14,
                                                    col_offset=25,
                                                    end_lineno=14,
                                                    end_col_offset=50,
                                                    value=Attribute(
                                                        lineno=14,
                                                        col_offset=25,
                                                        end_lineno=14,
                                                        end_col_offset=37,
                                                        value=Name(lineno=14, col_offset=25, end_lineno=14, end_col_offset=29, id='self', ctx=Load()),
                                                        attr='tax_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        lineno=14,
                                                        col_offset=51,
                                                        end_lineno=14,
                                                        end_col_offset=62,
                                                        arg='round',
                                                        value=Constant(lineno=14, col_offset=57, end_lineno=14, end_col_offset=62, value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=15,
                                                col_offset=16,
                                                end_lineno=15,
                                                end_col_offset=31,
                                                value=Name(lineno=15, col_offset=16, end_lineno=15, end_col_offset=20, id='self', ctx=Load()),
                                                attr='price_unit',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=15,
                                                col_offset=33,
                                                end_lineno=15,
                                                end_col_offset=52,
                                                value=Name(lineno=15, col_offset=33, end_lineno=15, end_col_offset=40, id='invoice', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            Constant(lineno=15, col_offset=54, end_lineno=15, end_col_offset=57, value=1.0, kind=None),
                                            Attribute(
                                                lineno=15,
                                                col_offset=59,
                                                end_lineno=15,
                                                end_col_offset=74,
                                                value=Name(lineno=15, col_offset=59, end_lineno=15, end_col_offset=63, id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=15,
                                                col_offset=76,
                                                end_lineno=15,
                                                end_col_offset=94,
                                                value=Name(lineno=15, col_offset=76, end_lineno=15, end_col_offset=83, id='invoice', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=53,
                                    targets=[Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=22, id='price_unit', ctx=Store())],
                                    value=Subscript(
                                        lineno=16,
                                        col_offset=25,
                                        end_lineno=16,
                                        end_col_offset=53,
                                        value=Name(lineno=16, col_offset=25, end_lineno=16, end_col_offset=35, id='price_unit', ctx=Load()),
                                        slice=Constant(lineno=16, col_offset=36, end_lineno=16, end_col_offset=52, value='total_excluded', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=48,
                                    targets=[Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=26, id='price_subtotal', ctx=Store())],
                                    value=Attribute(
                                        lineno=17,
                                        col_offset=29,
                                        end_lineno=17,
                                        end_col_offset=48,
                                        value=Name(lineno=17, col_offset=29, end_lineno=17, end_col_offset=33, id='self', ctx=Load()),
                                        attr='price_subtotal',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=20,
                                    end_col_offset=113,
                                    targets=[Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=22, id='price_unit', ctx=Store())],
                                    value=Subscript(
                                        lineno=19,
                                        col_offset=25,
                                        end_lineno=20,
                                        end_col_offset=113,
                                        value=Call(
                                            lineno=19,
                                            col_offset=25,
                                            end_lineno=20,
                                            end_col_offset=95,
                                            func=Attribute(
                                                lineno=19,
                                                col_offset=25,
                                                end_lineno=19,
                                                end_col_offset=51,
                                                value=Name(lineno=19, col_offset=25, end_lineno=19, end_col_offset=39, id='included_taxes', ctx=Load()),
                                                attr='compute_all',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    lineno=20,
                                                    col_offset=16,
                                                    end_lineno=20,
                                                    end_col_offset=31,
                                                    value=Name(lineno=20, col_offset=16, end_lineno=20, end_col_offset=20, id='self', ctx=Load()),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    lineno=20,
                                                    col_offset=33,
                                                    end_lineno=20,
                                                    end_col_offset=52,
                                                    value=Name(lineno=20, col_offset=33, end_lineno=20, end_col_offset=40, id='invoice', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                Constant(lineno=20, col_offset=54, end_lineno=20, end_col_offset=57, value=1.0, kind=None),
                                                Attribute(
                                                    lineno=20,
                                                    col_offset=59,
                                                    end_lineno=20,
                                                    end_col_offset=74,
                                                    value=Name(lineno=20, col_offset=59, end_lineno=20, end_col_offset=63, id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    lineno=20,
                                                    col_offset=76,
                                                    end_lineno=20,
                                                    end_col_offset=94,
                                                    value=Name(lineno=20, col_offset=76, end_lineno=20, end_col_offset=83, id='invoice', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(lineno=20, col_offset=96, end_lineno=20, end_col_offset=112, value='total_included', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=21,
                                    col_offset=12,
                                    end_lineno=21,
                                    end_col_offset=74,
                                    targets=[Name(lineno=21, col_offset=12, end_lineno=21, end_col_offset=17, id='price', ctx=Store())],
                                    value=BinOp(
                                        lineno=21,
                                        col_offset=20,
                                        end_lineno=21,
                                        end_col_offset=74,
                                        left=Attribute(
                                            lineno=21,
                                            col_offset=20,
                                            end_lineno=21,
                                            end_col_offset=35,
                                            value=Name(lineno=21, col_offset=20, end_lineno=21, end_col_offset=24, id='self', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=BinOp(
                                            lineno=21,
                                            col_offset=39,
                                            end_lineno=21,
                                            end_col_offset=73,
                                            left=Constant(lineno=21, col_offset=39, end_lineno=21, end_col_offset=40, value=1, kind=None),
                                            op=Sub(),
                                            right=BinOp(
                                                lineno=21,
                                                col_offset=43,
                                                end_lineno=21,
                                                end_col_offset=73,
                                                left=BoolOp(
                                                    lineno=21,
                                                    col_offset=44,
                                                    end_lineno=21,
                                                    end_col_offset=64,
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            lineno=21,
                                                            col_offset=44,
                                                            end_lineno=21,
                                                            end_col_offset=57,
                                                            value=Name(lineno=21, col_offset=44, end_lineno=21, end_col_offset=48, id='self', ctx=Load()),
                                                            attr='discount',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(lineno=21, col_offset=61, end_lineno=21, end_col_offset=64, value=0.0, kind=None),
                                                    ],
                                                ),
                                                op=Div(),
                                                right=Constant(lineno=21, col_offset=68, end_lineno=21, end_col_offset=73, value=100.0, kind=None),
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=113,
                                    targets=[Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=26, id='price_subtotal', ctx=Store())],
                                    value=Subscript(
                                        lineno=22,
                                        col_offset=29,
                                        end_lineno=23,
                                        end_col_offset=113,
                                        value=Call(
                                            lineno=22,
                                            col_offset=29,
                                            end_lineno=23,
                                            end_col_offset=95,
                                            func=Attribute(
                                                lineno=22,
                                                col_offset=29,
                                                end_lineno=22,
                                                end_col_offset=55,
                                                value=Name(lineno=22, col_offset=29, end_lineno=22, end_col_offset=43, id='included_taxes', ctx=Load()),
                                                attr='compute_all',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(lineno=23, col_offset=16, end_lineno=23, end_col_offset=21, id='price', ctx=Load()),
                                                Attribute(
                                                    lineno=23,
                                                    col_offset=23,
                                                    end_lineno=23,
                                                    end_col_offset=42,
                                                    value=Name(lineno=23, col_offset=23, end_lineno=23, end_col_offset=30, id='invoice', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    lineno=23,
                                                    col_offset=44,
                                                    end_lineno=23,
                                                    end_col_offset=57,
                                                    value=Name(lineno=23, col_offset=44, end_lineno=23, end_col_offset=48, id='self', ctx=Load()),
                                                    attr='quantity',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    lineno=23,
                                                    col_offset=59,
                                                    end_lineno=23,
                                                    end_col_offset=74,
                                                    value=Name(lineno=23, col_offset=59, end_lineno=23, end_col_offset=63, id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    lineno=23,
                                                    col_offset=76,
                                                    end_lineno=23,
                                                    end_col_offset=94,
                                                    value=Name(lineno=23, col_offset=76, end_lineno=23, end_col_offset=83, id='invoice', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(lineno=23, col_offset=96, end_lineno=23, end_col_offset=112, value='total_included', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=69,
                            targets=[Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=17, id='price_net', ctx=Store())],
                            value=BinOp(
                                lineno=24,
                                col_offset=20,
                                end_lineno=24,
                                end_col_offset=69,
                                left=Name(lineno=24, col_offset=20, end_lineno=24, end_col_offset=30, id='price_unit', ctx=Load()),
                                op=Mult(),
                                right=BinOp(
                                    lineno=24,
                                    col_offset=34,
                                    end_lineno=24,
                                    end_col_offset=68,
                                    left=Constant(lineno=24, col_offset=34, end_lineno=24, end_col_offset=35, value=1, kind=None),
                                    op=Sub(),
                                    right=BinOp(
                                        lineno=24,
                                        col_offset=38,
                                        end_lineno=24,
                                        end_col_offset=68,
                                        left=BoolOp(
                                            lineno=24,
                                            col_offset=39,
                                            end_lineno=24,
                                            end_col_offset=59,
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    lineno=24,
                                                    col_offset=39,
                                                    end_lineno=24,
                                                    end_col_offset=52,
                                                    value=Name(lineno=24, col_offset=39, end_lineno=24, end_col_offset=43, id='self', ctx=Load()),
                                                    attr='discount',
                                                    ctx=Load(),
                                                ),
                                                Constant(lineno=24, col_offset=56, end_lineno=24, end_col_offset=59, value=0.0, kind=None),
                                            ],
                                        ),
                                        op=Div(),
                                        right=Constant(lineno=24, col_offset=63, end_lineno=24, end_col_offset=68, value=100.0, kind=None),
                                    ),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=26,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=9,
                            value=Dict(
                                lineno=26,
                                col_offset=15,
                                end_lineno=30,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=24, value='price_unit', kind=None),
                                    Constant(lineno=28, col_offset=12, end_lineno=28, end_col_offset=28, value='price_subtotal', kind=None),
                                    Constant(lineno=29, col_offset=12, end_lineno=29, end_col_offset=23, value='price_net', kind=None),
                                ],
                                values=[
                                    Name(lineno=27, col_offset=26, end_lineno=27, end_col_offset=36, id='price_unit', ctx=Load()),
                                    Name(lineno=28, col_offset=30, end_lineno=28, end_col_offset=44, id='price_subtotal', ctx=Load()),
                                    Name(lineno=29, col_offset=25, end_lineno=29, end_col_offset=34, id='price_net', ctx=Load()),
                                ],
                            ),
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
