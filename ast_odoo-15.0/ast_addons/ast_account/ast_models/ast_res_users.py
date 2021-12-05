Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='api', asname=None),
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
            end_lineno=27,
            end_col_offset=109,
            name='Users',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=12,
                    end_lineno=8,
                    end_col_offset=24,
                    value=Name(lineno=8, col_offset=12, end_lineno=8, end_col_offset=18, id='models', ctx=Load()),
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
                    end_col_offset=26,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=26, value='res.users', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=109,
                    name='_check_one_user_type',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=12, col_offset=29, end_lineno=12, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=49,
                            value=Call(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=49,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=8,
                                    end_lineno=13,
                                    end_col_offset=47,
                                    value=Call(
                                        lineno=13,
                                        col_offset=8,
                                        end_lineno=13,
                                        end_col_offset=26,
                                        func=Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=13, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=13, col_offset=14, end_lineno=13, end_col_offset=19, id='Users', ctx=Load()),
                                            Name(lineno=13, col_offset=21, end_lineno=13, end_col_offset=25, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_check_one_user_type',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=82,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=10, id='g1', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=13,
                                end_lineno=15,
                                end_col_offset=82,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=13,
                                    end_lineno=15,
                                    end_col_offset=25,
                                    value=Attribute(
                                        lineno=15,
                                        col_offset=13,
                                        end_lineno=15,
                                        end_col_offset=21,
                                        value=Name(lineno=15, col_offset=13, end_lineno=15, end_col_offset=17, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=15, col_offset=26, end_lineno=15, end_col_offset=74, value='account.group_show_line_subtotals_tax_included', kind=None),
                                    Constant(lineno=15, col_offset=76, end_lineno=15, end_col_offset=81, value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=82,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=10, id='g2', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=13,
                                end_lineno=16,
                                end_col_offset=82,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=13,
                                    end_lineno=16,
                                    end_col_offset=25,
                                    value=Attribute(
                                        lineno=16,
                                        col_offset=13,
                                        end_lineno=16,
                                        end_col_offset=21,
                                        value=Name(lineno=16, col_offset=13, end_lineno=16, end_col_offset=17, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=16, col_offset=26, end_lineno=16, end_col_offset=74, value='account.group_show_line_subtotals_tax_excluded', kind=None),
                                    Constant(lineno=16, col_offset=76, end_lineno=16, end_col_offset=81, value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=18,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=18,
                            test=BoolOp(
                                lineno=18,
                                col_offset=11,
                                end_lineno=18,
                                end_col_offset=27,
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        lineno=18,
                                        col_offset=11,
                                        end_lineno=18,
                                        end_col_offset=17,
                                        op=Not(),
                                        operand=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=17, id='g1', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        lineno=18,
                                        col_offset=21,
                                        end_lineno=18,
                                        end_col_offset=27,
                                        op=Not(),
                                        operand=Name(lineno=18, col_offset=25, end_lineno=18, end_col_offset=27, id='g2', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[Return(lineno=20, col_offset=12, end_lineno=20, end_col_offset=18, value=None)],
                            orelse=[],
                        ),
                        For(
                            lineno=22,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=109,
                            target=Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=16, id='user', ctx=Store()),
                            iter=Name(lineno=22, col_offset=20, end_lineno=22, end_col_offset=24, id='self', ctx=Load()),
                            body=[
                                If(
                                    lineno=23,
                                    col_offset=12,
                                    end_lineno=27,
                                    end_col_offset=109,
                                    test=Call(
                                        lineno=23,
                                        col_offset=15,
                                        end_lineno=23,
                                        end_col_offset=56,
                                        func=Attribute(
                                            lineno=23,
                                            col_offset=15,
                                            end_lineno=23,
                                            end_col_offset=40,
                                            value=Name(lineno=23, col_offset=15, end_lineno=23, end_col_offset=19, id='user', ctx=Load()),
                                            attr='_has_multiple_groups',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                lineno=23,
                                                col_offset=41,
                                                end_lineno=23,
                                                end_col_offset=55,
                                                elts=[
                                                    Attribute(
                                                        lineno=23,
                                                        col_offset=42,
                                                        end_lineno=23,
                                                        end_col_offset=47,
                                                        value=Name(lineno=23, col_offset=42, end_lineno=23, end_col_offset=44, id='g1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        lineno=23,
                                                        col_offset=49,
                                                        end_lineno=23,
                                                        end_col_offset=54,
                                                        value=Name(lineno=23, col_offset=49, end_lineno=23, end_col_offset=51, id='g2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Raise(
                                            lineno=24,
                                            col_offset=16,
                                            end_lineno=27,
                                            end_col_offset=109,
                                            exc=Call(
                                                lineno=24,
                                                col_offset=22,
                                                end_lineno=27,
                                                end_col_offset=109,
                                                func=Name(lineno=24, col_offset=22, end_lineno=24, end_col_offset=37, id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        lineno=24,
                                                        col_offset=38,
                                                        end_lineno=27,
                                                        end_col_offset=108,
                                                        func=Name(lineno=24, col_offset=38, end_lineno=24, end_col_offset=39, id='_', ctx=Load()),
                                                        args=[Constant(lineno=24, col_offset=40, end_lineno=27, end_col_offset=107, value="A user cannot have both Tax B2B and Tax B2C.\nYou should go in General Settings, and choose to display Product Prices\neither in 'Tax-Included' or in 'Tax-Excluded' mode\n(or switch twice the mode if you are already in the desired one).", kind=None)],
                                                        keywords=[],
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=11,
                            col_offset=5,
                            end_lineno=11,
                            end_col_offset=32,
                            func=Attribute(
                                lineno=11,
                                col_offset=5,
                                end_lineno=11,
                                end_col_offset=19,
                                value=Name(lineno=11, col_offset=5, end_lineno=11, end_col_offset=8, id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=11, col_offset=20, end_lineno=11, end_col_offset=31, value='groups_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            lineno=30,
            col_offset=0,
            end_lineno=43,
            end_col_offset=53,
            name='GroupsView',
            bases=[
                Attribute(
                    lineno=30,
                    col_offset=17,
                    end_lineno=30,
                    end_col_offset=29,
                    value=Name(lineno=30, col_offset=17, end_lineno=30, end_col_offset=23, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=31,
                    col_offset=4,
                    end_lineno=31,
                    end_col_offset=27,
                    targets=[Name(lineno=31, col_offset=4, end_lineno=31, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=31, col_offset=15, end_lineno=31, end_col_offset=27, value='res.groups', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=34,
                    col_offset=4,
                    end_lineno=43,
                    end_col_offset=53,
                    name='get_application_groups',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=34, col_offset=31, end_lineno=34, end_col_offset=35, arg='self', annotation=None, type_comment=None),
                            arg(lineno=34, col_offset=37, end_lineno=34, end_col_offset=43, arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=37,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=97,
                            targets=[Name(lineno=37, col_offset=8, end_lineno=37, end_col_offset=26, id='group_account_user', ctx=Store())],
                            value=Call(
                                lineno=37,
                                col_offset=29,
                                end_lineno=37,
                                end_col_offset=97,
                                func=Attribute(
                                    lineno=37,
                                    col_offset=29,
                                    end_lineno=37,
                                    end_col_offset=41,
                                    value=Attribute(
                                        lineno=37,
                                        col_offset=29,
                                        end_lineno=37,
                                        end_col_offset=37,
                                        value=Name(lineno=37, col_offset=29, end_lineno=37, end_col_offset=33, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=37, col_offset=42, end_lineno=37, end_col_offset=70, value='account.group_account_user', kind=None)],
                                keywords=[
                                    keyword(
                                        lineno=37,
                                        col_offset=72,
                                        end_lineno=37,
                                        end_col_offset=96,
                                        arg='raise_if_not_found',
                                        value=Constant(lineno=37, col_offset=91, end_lineno=37, end_col_offset=96, value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=38,
                            col_offset=8,
                            end_lineno=39,
                            end_col_offset=59,
                            test=BoolOp(
                                lineno=38,
                                col_offset=11,
                                end_lineno=38,
                                end_col_offset=104,
                                op=And(),
                                values=[
                                    Name(lineno=38, col_offset=11, end_lineno=38, end_col_offset=29, id='group_account_user', ctx=Load()),
                                    Compare(
                                        lineno=38,
                                        col_offset=34,
                                        end_lineno=38,
                                        end_col_offset=104,
                                        left=Attribute(
                                            lineno=38,
                                            col_offset=34,
                                            end_lineno=38,
                                            end_col_offset=71,
                                            value=Attribute(
                                                lineno=38,
                                                col_offset=34,
                                                end_lineno=38,
                                                end_col_offset=64,
                                                value=Name(lineno=38, col_offset=34, end_lineno=38, end_col_offset=52, id='group_account_user', ctx=Load()),
                                                attr='category_id',
                                                ctx=Load(),
                                            ),
                                            attr='xml_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(lineno=38, col_offset=75, end_lineno=38, end_col_offset=104, value='base.module_category_hidden', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    lineno=39,
                                    col_offset=12,
                                    end_lineno=39,
                                    end_col_offset=59,
                                    target=Name(lineno=39, col_offset=12, end_lineno=39, end_col_offset=18, id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        lineno=39,
                                        col_offset=22,
                                        end_lineno=39,
                                        end_col_offset=59,
                                        elts=[
                                            Tuple(
                                                lineno=39,
                                                col_offset=23,
                                                end_lineno=39,
                                                end_col_offset=58,
                                                elts=[
                                                    Constant(lineno=39, col_offset=24, end_lineno=39, end_col_offset=28, value='id', kind=None),
                                                    Constant(lineno=39, col_offset=30, end_lineno=39, end_col_offset=34, value='!=', kind=None),
                                                    Attribute(
                                                        lineno=39,
                                                        col_offset=36,
                                                        end_lineno=39,
                                                        end_col_offset=57,
                                                        value=Name(lineno=39, col_offset=36, end_lineno=39, end_col_offset=54, id='group_account_user', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=40,
                            col_offset=8,
                            end_lineno=40,
                            end_col_offset=105,
                            targets=[Name(lineno=40, col_offset=8, end_lineno=40, end_col_offset=30, id='group_account_readonly', ctx=Store())],
                            value=Call(
                                lineno=40,
                                col_offset=33,
                                end_lineno=40,
                                end_col_offset=105,
                                func=Attribute(
                                    lineno=40,
                                    col_offset=33,
                                    end_lineno=40,
                                    end_col_offset=45,
                                    value=Attribute(
                                        lineno=40,
                                        col_offset=33,
                                        end_lineno=40,
                                        end_col_offset=41,
                                        value=Name(lineno=40, col_offset=33, end_lineno=40, end_col_offset=37, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=40, col_offset=46, end_lineno=40, end_col_offset=78, value='account.group_account_readonly', kind=None)],
                                keywords=[
                                    keyword(
                                        lineno=40,
                                        col_offset=80,
                                        end_lineno=40,
                                        end_col_offset=104,
                                        arg='raise_if_not_found',
                                        value=Constant(lineno=40, col_offset=99, end_lineno=40, end_col_offset=104, value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=41,
                            col_offset=8,
                            end_lineno=42,
                            end_col_offset=63,
                            test=BoolOp(
                                lineno=41,
                                col_offset=11,
                                end_lineno=41,
                                end_col_offset=112,
                                op=And(),
                                values=[
                                    Name(lineno=41, col_offset=11, end_lineno=41, end_col_offset=33, id='group_account_readonly', ctx=Load()),
                                    Compare(
                                        lineno=41,
                                        col_offset=38,
                                        end_lineno=41,
                                        end_col_offset=112,
                                        left=Attribute(
                                            lineno=41,
                                            col_offset=38,
                                            end_lineno=41,
                                            end_col_offset=79,
                                            value=Attribute(
                                                lineno=41,
                                                col_offset=38,
                                                end_lineno=41,
                                                end_col_offset=72,
                                                value=Name(lineno=41, col_offset=38, end_lineno=41, end_col_offset=60, id='group_account_readonly', ctx=Load()),
                                                attr='category_id',
                                                ctx=Load(),
                                            ),
                                            attr='xml_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(lineno=41, col_offset=83, end_lineno=41, end_col_offset=112, value='base.module_category_hidden', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    lineno=42,
                                    col_offset=12,
                                    end_lineno=42,
                                    end_col_offset=63,
                                    target=Name(lineno=42, col_offset=12, end_lineno=42, end_col_offset=18, id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        lineno=42,
                                        col_offset=22,
                                        end_lineno=42,
                                        end_col_offset=63,
                                        elts=[
                                            Tuple(
                                                lineno=42,
                                                col_offset=23,
                                                end_lineno=42,
                                                end_col_offset=62,
                                                elts=[
                                                    Constant(lineno=42, col_offset=24, end_lineno=42, end_col_offset=28, value='id', kind=None),
                                                    Constant(lineno=42, col_offset=30, end_lineno=42, end_col_offset=34, value='!=', kind=None),
                                                    Attribute(
                                                        lineno=42,
                                                        col_offset=36,
                                                        end_lineno=42,
                                                        end_col_offset=61,
                                                        value=Name(lineno=42, col_offset=36, end_lineno=42, end_col_offset=58, id='group_account_readonly', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=43,
                            col_offset=8,
                            end_lineno=43,
                            end_col_offset=53,
                            value=Call(
                                lineno=43,
                                col_offset=15,
                                end_lineno=43,
                                end_col_offset=53,
                                func=Attribute(
                                    lineno=43,
                                    col_offset=15,
                                    end_lineno=43,
                                    end_col_offset=45,
                                    value=Call(
                                        lineno=43,
                                        col_offset=15,
                                        end_lineno=43,
                                        end_col_offset=22,
                                        func=Name(lineno=43, col_offset=15, end_lineno=43, end_col_offset=20, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_application_groups',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=43, col_offset=46, end_lineno=43, end_col_offset=52, id='domain', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=33,
                            col_offset=5,
                            end_lineno=33,
                            end_col_offset=14,
                            value=Name(lineno=33, col_offset=5, end_lineno=33, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
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