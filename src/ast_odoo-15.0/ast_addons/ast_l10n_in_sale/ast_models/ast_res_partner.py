Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=39,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=43,
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=18,
            end_col_offset=172,
            name='ResPartner',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=17,
                    end_lineno=8,
                    end_col_offset=29,
                    value=Name(lineno=8, col_offset=17, end_lineno=8, end_col_offset=23, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=28,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=28, value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=58,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=26, id='l10n_in_shipping_gstin', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=29,
                        end_lineno=11,
                        end_col_offset=58,
                        func=Attribute(
                            lineno=11,
                            col_offset=29,
                            end_lineno=11,
                            end_col_offset=40,
                            value=Name(lineno=11, col_offset=29, end_lineno=11, end_col_offset=35, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=41, end_lineno=11, end_col_offset=57, value='Shipping GSTIN', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=172,
                    name='_check_l10n_in_shipping_gstin',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=38, end_lineno=14, end_col_offset=42, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=59,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=20, id='check_vat_in', ctx=Store())],
                            value=Attribute(
                                lineno=15,
                                col_offset=23,
                                end_lineno=15,
                                end_col_offset=59,
                                value=Subscript(
                                    lineno=15,
                                    col_offset=23,
                                    end_lineno=15,
                                    end_col_offset=46,
                                    value=Attribute(
                                        lineno=15,
                                        col_offset=23,
                                        end_lineno=15,
                                        end_col_offset=31,
                                        value=Name(lineno=15, col_offset=23, end_lineno=15, end_col_offset=27, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(lineno=15, col_offset=32, end_lineno=15, end_col_offset=45, value='res.partner', kind=None),
                                    ctx=Load(),
                                ),
                                attr='check_vat_in',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=135,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=36, id='wrong_shipping_gstin_partner', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=39,
                                end_lineno=16,
                                end_col_offset=135,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=39,
                                    end_lineno=16,
                                    end_col_offset=52,
                                    value=Name(lineno=16, col_offset=39, end_lineno=16, end_col_offset=43, id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        lineno=16,
                                        col_offset=53,
                                        end_lineno=16,
                                        end_col_offset=134,
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(lineno=16, col_offset=60, end_lineno=16, end_col_offset=61, arg='p', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            lineno=16,
                                            col_offset=63,
                                            end_lineno=16,
                                            end_col_offset=134,
                                            op=And(),
                                            values=[
                                                Attribute(
                                                    lineno=16,
                                                    col_offset=63,
                                                    end_lineno=16,
                                                    end_col_offset=87,
                                                    value=Name(lineno=16, col_offset=63, end_lineno=16, end_col_offset=64, id='p', ctx=Load()),
                                                    attr='l10n_in_shipping_gstin',
                                                    ctx=Load(),
                                                ),
                                                UnaryOp(
                                                    lineno=16,
                                                    col_offset=92,
                                                    end_lineno=16,
                                                    end_col_offset=134,
                                                    op=Not(),
                                                    operand=Call(
                                                        lineno=16,
                                                        col_offset=96,
                                                        end_lineno=16,
                                                        end_col_offset=134,
                                                        func=Name(lineno=16, col_offset=96, end_lineno=16, end_col_offset=108, id='check_vat_in', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                lineno=16,
                                                                col_offset=109,
                                                                end_lineno=16,
                                                                end_col_offset=133,
                                                                value=Name(lineno=16, col_offset=109, end_lineno=16, end_col_offset=110, id='p', ctx=Load()),
                                                                attr='l10n_in_shipping_gstin',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=17,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=172,
                            test=Name(lineno=17, col_offset=11, end_lineno=17, end_col_offset=39, id='wrong_shipping_gstin_partner', ctx=Load()),
                            body=[
                                Raise(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=18,
                                    end_col_offset=172,
                                    exc=Call(
                                        lineno=18,
                                        col_offset=18,
                                        end_lineno=18,
                                        end_col_offset=172,
                                        func=Name(lineno=18, col_offset=18, end_lineno=18, end_col_offset=33, id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                lineno=18,
                                                col_offset=34,
                                                end_lineno=18,
                                                end_col_offset=171,
                                                left=Call(
                                                    lineno=18,
                                                    col_offset=34,
                                                    end_lineno=18,
                                                    end_col_offset=95,
                                                    func=Name(lineno=18, col_offset=34, end_lineno=18, end_col_offset=35, id='_', ctx=Load()),
                                                    args=[Constant(lineno=18, col_offset=36, end_lineno=18, end_col_offset=94, value='The shipping GSTIN number [%s] does not seem to be valid', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Call(
                                                    lineno=18,
                                                    col_offset=98,
                                                    end_lineno=18,
                                                    end_col_offset=170,
                                                    func=Attribute(
                                                        lineno=18,
                                                        col_offset=98,
                                                        end_lineno=18,
                                                        end_col_offset=106,
                                                        value=Constant(lineno=18, col_offset=98, end_lineno=18, end_col_offset=101, value=',', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        GeneratorExp(
                                                            lineno=18,
                                                            col_offset=106,
                                                            end_lineno=18,
                                                            end_col_offset=170,
                                                            elt=Attribute(
                                                                lineno=18,
                                                                col_offset=107,
                                                                end_lineno=18,
                                                                end_col_offset=131,
                                                                value=Name(lineno=18, col_offset=107, end_lineno=18, end_col_offset=108, id='p', ctx=Load()),
                                                                attr='l10n_in_shipping_gstin',
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(lineno=18, col_offset=136, end_lineno=18, end_col_offset=137, id='p', ctx=Store()),
                                                                    iter=Name(lineno=18, col_offset=141, end_lineno=18, end_col_offset=169, id='wrong_shipping_gstin_partner', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=13,
                            col_offset=5,
                            end_lineno=13,
                            end_col_offset=45,
                            func=Attribute(
                                lineno=13,
                                col_offset=5,
                                end_lineno=13,
                                end_col_offset=19,
                                value=Name(lineno=13, col_offset=5, end_lineno=13, end_col_offset=8, id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=13, col_offset=20, end_lineno=13, end_col_offset=44, value='l10n_in_shipping_gstin', kind=None)],
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