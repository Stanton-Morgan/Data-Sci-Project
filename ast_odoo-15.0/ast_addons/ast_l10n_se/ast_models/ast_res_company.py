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
        Import(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=9,
            names=[alias(name='re', asname=None)],
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=22,
            end_col_offset=39,
            name='ResCompany',
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
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=28, value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=59,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=14, id='org_number', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=17,
                        end_lineno=11,
                        end_col_offset=59,
                        func=Attribute(
                            lineno=11,
                            col_offset=17,
                            end_lineno=11,
                            end_col_offset=28,
                            value=Name(lineno=11, col_offset=17, end_lineno=11, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=29,
                                end_lineno=11,
                                end_col_offset=58,
                                arg='compute',
                                value=Constant(lineno=11, col_offset=37, end_lineno=11, end_col_offset=58, value='_compute_org_number', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=39,
                    name='_compute_org_number',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=28, end_lineno=14, end_col_offset=32, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            lineno=15,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=39,
                            target=Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=19, id='company', ctx=Store()),
                            iter=Name(lineno=15, col_offset=23, end_lineno=15, end_col_offset=27, id='self', ctx=Load()),
                            body=[
                                If(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=39,
                                    test=BoolOp(
                                        lineno=16,
                                        col_offset=15,
                                        end_lineno=16,
                                        end_col_offset=77,
                                        op=And(),
                                        values=[
                                            Compare(
                                                lineno=16,
                                                col_offset=15,
                                                end_lineno=16,
                                                end_col_offset=61,
                                                left=Attribute(
                                                    lineno=16,
                                                    col_offset=15,
                                                    end_lineno=16,
                                                    end_col_offset=53,
                                                    value=Attribute(
                                                        lineno=16,
                                                        col_offset=15,
                                                        end_lineno=16,
                                                        end_col_offset=48,
                                                        value=Name(lineno=16, col_offset=15, end_lineno=16, end_col_offset=22, id='company', ctx=Load()),
                                                        attr='account_fiscal_country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(lineno=16, col_offset=57, end_lineno=16, end_col_offset=61, value='SE', kind=None)],
                                            ),
                                            Attribute(
                                                lineno=16,
                                                col_offset=66,
                                                end_lineno=16,
                                                end_col_offset=77,
                                                value=Name(lineno=16, col_offset=66, end_lineno=16, end_col_offset=73, id='company', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=17,
                                            col_offset=16,
                                            end_lineno=17,
                                            end_col_offset=64,
                                            targets=[Name(lineno=17, col_offset=16, end_lineno=17, end_col_offset=26, id='org_number', ctx=Store())],
                                            value=Subscript(
                                                lineno=17,
                                                col_offset=29,
                                                end_lineno=17,
                                                end_col_offset=64,
                                                value=Call(
                                                    lineno=17,
                                                    col_offset=29,
                                                    end_lineno=17,
                                                    end_col_offset=59,
                                                    func=Attribute(
                                                        lineno=17,
                                                        col_offset=29,
                                                        end_lineno=17,
                                                        end_col_offset=35,
                                                        value=Name(lineno=17, col_offset=29, end_lineno=17, end_col_offset=31, id='re', ctx=Load()),
                                                        attr='sub',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(lineno=17, col_offset=36, end_lineno=17, end_col_offset=41, value='\\D', kind=None),
                                                        Constant(lineno=17, col_offset=43, end_lineno=17, end_col_offset=45, value='', kind=None),
                                                        Attribute(
                                                            lineno=17,
                                                            col_offset=47,
                                                            end_lineno=17,
                                                            end_col_offset=58,
                                                            value=Name(lineno=17, col_offset=47, end_lineno=17, end_col_offset=54, id='company', ctx=Load()),
                                                            attr='vat',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Slice(
                                                    lineno=17,
                                                    col_offset=60,
                                                    end_lineno=17,
                                                    end_col_offset=63,
                                                    lower=None,
                                                    upper=UnaryOp(
                                                        lineno=17,
                                                        col_offset=61,
                                                        end_lineno=17,
                                                        end_col_offset=63,
                                                        op=USub(),
                                                        operand=Constant(lineno=17, col_offset=62, end_lineno=17, end_col_offset=63, value=2, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            lineno=18,
                                            col_offset=16,
                                            end_lineno=18,
                                            end_col_offset=66,
                                            targets=[Name(lineno=18, col_offset=16, end_lineno=18, end_col_offset=26, id='org_number', ctx=Store())],
                                            value=BinOp(
                                                lineno=18,
                                                col_offset=29,
                                                end_lineno=18,
                                                end_col_offset=66,
                                                left=BinOp(
                                                    lineno=18,
                                                    col_offset=29,
                                                    end_lineno=18,
                                                    end_col_offset=49,
                                                    left=Subscript(
                                                        lineno=18,
                                                        col_offset=29,
                                                        end_lineno=18,
                                                        end_col_offset=43,
                                                        value=Name(lineno=18, col_offset=29, end_lineno=18, end_col_offset=39, id='org_number', ctx=Load()),
                                                        slice=Slice(
                                                            lineno=18,
                                                            col_offset=40,
                                                            end_lineno=18,
                                                            end_col_offset=42,
                                                            lower=None,
                                                            upper=Constant(lineno=18, col_offset=41, end_lineno=18, end_col_offset=42, value=6, kind=None),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(lineno=18, col_offset=46, end_lineno=18, end_col_offset=49, value='-', kind=None),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    lineno=18,
                                                    col_offset=52,
                                                    end_lineno=18,
                                                    end_col_offset=66,
                                                    value=Name(lineno=18, col_offset=52, end_lineno=18, end_col_offset=62, id='org_number', ctx=Load()),
                                                    slice=Slice(
                                                        lineno=18,
                                                        col_offset=63,
                                                        end_lineno=18,
                                                        end_col_offset=65,
                                                        lower=Constant(lineno=18, col_offset=63, end_lineno=18, end_col_offset=64, value=6, kind=None),
                                                        upper=None,
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            lineno=20,
                                            col_offset=16,
                                            end_lineno=20,
                                            end_col_offset=47,
                                            targets=[
                                                Attribute(
                                                    lineno=20,
                                                    col_offset=16,
                                                    end_lineno=20,
                                                    end_col_offset=34,
                                                    value=Name(lineno=20, col_offset=16, end_lineno=20, end_col_offset=23, id='company', ctx=Load()),
                                                    attr='org_number',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(lineno=20, col_offset=37, end_lineno=20, end_col_offset=47, id='org_number', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            lineno=22,
                                            col_offset=16,
                                            end_lineno=22,
                                            end_col_offset=39,
                                            targets=[
                                                Attribute(
                                                    lineno=22,
                                                    col_offset=16,
                                                    end_lineno=22,
                                                    end_col_offset=34,
                                                    value=Name(lineno=22, col_offset=16, end_lineno=22, end_col_offset=23, id='company', ctx=Load()),
                                                    attr='org_number',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(lineno=22, col_offset=37, end_lineno=22, end_col_offset=39, value='', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=13,
                            col_offset=5,
                            end_lineno=13,
                            end_col_offset=23,
                            func=Attribute(
                                lineno=13,
                                col_offset=5,
                                end_lineno=13,
                                end_col_offset=16,
                                value=Name(lineno=13, col_offset=5, end_lineno=13, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=13, col_offset=17, end_lineno=13, end_col_offset=22, value='vat', kind=None)],
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
