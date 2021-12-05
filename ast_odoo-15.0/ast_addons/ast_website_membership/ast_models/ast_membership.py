Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=19,
            end_col_offset=71,
            name='MembershipLine',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=21,
                    end_lineno=6,
                    end_col_offset=33,
                    value=Name(lineno=6, col_offset=21, end_lineno=6, end_col_offset=27, id='models', ctx=Load()),
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
                    end_col_offset=43,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=43, value='membership.membership_line', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=71,
                    name='_get_published_companies',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=10, col_offset=33, end_lineno=10, end_col_offset=37, arg='self', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=39, end_lineno=10, end_col_offset=44, arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=10, col_offset=45, end_lineno=10, end_col_offset=49, value=None, kind=None)],
                    ),
                    body=[
                        If(
                            lineno=11,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=21,
                            test=UnaryOp(
                                lineno=11,
                                col_offset=11,
                                end_lineno=11,
                                end_col_offset=23,
                                op=Not(),
                                operand=Attribute(
                                    lineno=11,
                                    col_offset=15,
                                    end_lineno=11,
                                    end_col_offset=23,
                                    value=Name(lineno=11, col_offset=15, end_lineno=11, end_col_offset=19, id='self', ctx=Load()),
                                    attr='ids',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    lineno=12,
                                    col_offset=12,
                                    end_lineno=12,
                                    end_col_offset=21,
                                    value=List(lineno=12, col_offset=19, end_lineno=12, end_col_offset=21, elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=67,
                            targets=[Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=20, id='limit_clause', ctx=Store())],
                            value=IfExp(
                                lineno=13,
                                col_offset=23,
                                end_lineno=13,
                                end_col_offset=67,
                                test=Compare(
                                    lineno=13,
                                    col_offset=29,
                                    end_lineno=13,
                                    end_col_offset=42,
                                    left=Name(lineno=13, col_offset=29, end_lineno=13, end_col_offset=34, id='limit', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(lineno=13, col_offset=38, end_lineno=13, end_col_offset=42, value=None, kind=None)],
                                ),
                                body=Constant(lineno=13, col_offset=23, end_lineno=13, end_col_offset=25, value='', kind=None),
                                orelse=BinOp(
                                    lineno=13,
                                    col_offset=48,
                                    end_lineno=13,
                                    end_col_offset=67,
                                    left=Constant(lineno=13, col_offset=48, end_lineno=13, end_col_offset=59, value=' LIMIT %d', kind=None),
                                    op=Mod(),
                                    right=Name(lineno=13, col_offset=62, end_lineno=13, end_col_offset=67, id='limit', ctx=Load()),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=14,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=100,
                            value=Call(
                                lineno=14,
                                col_offset=8,
                                end_lineno=18,
                                end_col_offset=100,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=27,
                                    value=Attribute(
                                        lineno=14,
                                        col_offset=8,
                                        end_lineno=14,
                                        end_col_offset=19,
                                        value=Attribute(
                                            lineno=14,
                                            col_offset=8,
                                            end_lineno=14,
                                            end_col_offset=16,
                                            value=Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        lineno=14,
                                        col_offset=28,
                                        end_lineno=18,
                                        end_col_offset=79,
                                        left=Constant(lineno=14, col_offset=28, end_lineno=18, end_col_offset=64, value='\n            SELECT DISTINCT p.id\n            FROM res_partner p INNER JOIN membership_membership_line m\n            ON  p.id = m.partner\n            WHERE is_published AND is_company AND m.id IN %s ', kind=None),
                                        op=Add(),
                                        right=Name(lineno=18, col_offset=67, end_lineno=18, end_col_offset=79, id='limit_clause', ctx=Load()),
                                    ),
                                    Tuple(
                                        lineno=18,
                                        col_offset=81,
                                        end_lineno=18,
                                        end_col_offset=99,
                                        elts=[
                                            Call(
                                                lineno=18,
                                                col_offset=82,
                                                end_lineno=18,
                                                end_col_offset=97,
                                                func=Name(lineno=18, col_offset=82, end_lineno=18, end_col_offset=87, id='tuple', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        lineno=18,
                                                        col_offset=88,
                                                        end_lineno=18,
                                                        end_col_offset=96,
                                                        value=Name(lineno=18, col_offset=88, end_lineno=18, end_col_offset=92, id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=71,
                            value=ListComp(
                                lineno=19,
                                col_offset=15,
                                end_lineno=19,
                                end_col_offset=71,
                                elt=Subscript(
                                    lineno=19,
                                    col_offset=16,
                                    end_lineno=19,
                                    end_col_offset=29,
                                    value=Name(lineno=19, col_offset=16, end_lineno=19, end_col_offset=26, id='partner_id', ctx=Load()),
                                    slice=Constant(lineno=19, col_offset=27, end_lineno=19, end_col_offset=28, value=0, kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(lineno=19, col_offset=34, end_lineno=19, end_col_offset=44, id='partner_id', ctx=Store()),
                                        iter=Call(
                                            lineno=19,
                                            col_offset=48,
                                            end_lineno=19,
                                            end_col_offset=70,
                                            func=Attribute(
                                                lineno=19,
                                                col_offset=48,
                                                end_lineno=19,
                                                end_col_offset=68,
                                                value=Attribute(
                                                    lineno=19,
                                                    col_offset=48,
                                                    end_lineno=19,
                                                    end_col_offset=59,
                                                    value=Attribute(
                                                        lineno=19,
                                                        col_offset=48,
                                                        end_lineno=19,
                                                        end_col_offset=56,
                                                        value=Name(lineno=19, col_offset=48, end_lineno=19, end_col_offset=52, id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='fetchall',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
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
