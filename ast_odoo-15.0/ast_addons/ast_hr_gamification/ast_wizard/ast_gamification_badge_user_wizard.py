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
            end_col_offset=50,
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='AccessError', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=31,
            end_col_offset=79,
            name='GamificationBadgeUserWizard',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=34,
                    end_lineno=8,
                    end_col_offset=55,
                    value=Name(lineno=8, col_offset=34, end_lineno=8, end_col_offset=40, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=47,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=47, value='gamification.badge.user.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=82,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=15, id='employee_id', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=18,
                        end_lineno=11,
                        end_col_offset=82,
                        func=Attribute(
                            lineno=11,
                            col_offset=18,
                            end_lineno=11,
                            end_col_offset=33,
                            value=Name(lineno=11, col_offset=18, end_lineno=11, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=34, end_lineno=11, end_col_offset=47, value='hr.employee', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=49,
                                end_lineno=11,
                                end_col_offset=66,
                                arg='string',
                                value=Constant(lineno=11, col_offset=56, end_lineno=11, end_col_offset=66, value='Employee', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=68,
                                end_lineno=11,
                                end_col_offset=81,
                                arg='required',
                                value=Constant(lineno=11, col_offset=77, end_lineno=11, end_col_offset=81, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=54,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=11, id='user_id', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=14,
                        end_lineno=13,
                        end_col_offset=54,
                        func=Attribute(
                            lineno=12,
                            col_offset=14,
                            end_lineno=12,
                            end_col_offset=29,
                            value=Name(lineno=12, col_offset=14, end_lineno=12, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=30, end_lineno=12, end_col_offset=41, value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=43,
                                end_lineno=12,
                                end_col_offset=56,
                                arg='string',
                                value=Constant(lineno=12, col_offset=50, end_lineno=12, end_col_offset=56, value='User', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=58,
                                end_lineno=12,
                                end_col_offset=87,
                                arg='related',
                                value=Constant(lineno=12, col_offset=66, end_lineno=12, end_col_offset=87, value='employee_id.user_id', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=19,
                                arg='store',
                                value=Constant(lineno=13, col_offset=14, end_lineno=13, end_col_offset=19, value=False, kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=21,
                                end_lineno=13,
                                end_col_offset=34,
                                arg='readonly',
                                value=Constant(lineno=13, col_offset=30, end_lineno=13, end_col_offset=34, value=True, kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=36,
                                end_lineno=13,
                                end_col_offset=53,
                                arg='compute_sudo',
                                value=Constant(lineno=13, col_offset=49, end_lineno=13, end_col_offset=53, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=31,
                    end_col_offset=79,
                    name='action_grant_badge',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=15, col_offset=27, end_lineno=15, end_col_offset=31, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=68,
                            value=Constant(lineno=16, col_offset=8, end_lineno=16, end_col_offset=68, value='Wizard action for sending a badge to a chosen employee', kind=None),
                        ),
                        If(
                            lineno=17,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=89,
                            test=UnaryOp(
                                lineno=17,
                                col_offset=11,
                                end_lineno=17,
                                end_col_offset=27,
                                op=Not(),
                                operand=Attribute(
                                    lineno=17,
                                    col_offset=15,
                                    end_lineno=17,
                                    end_col_offset=27,
                                    value=Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=19, id='self', ctx=Load()),
                                    attr='user_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Raise(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=18,
                                    end_col_offset=89,
                                    exc=Call(
                                        lineno=18,
                                        col_offset=18,
                                        end_lineno=18,
                                        end_col_offset=89,
                                        func=Name(lineno=18, col_offset=18, end_lineno=18, end_col_offset=27, id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=18,
                                                col_offset=28,
                                                end_lineno=18,
                                                end_col_offset=88,
                                                func=Name(lineno=18, col_offset=28, end_lineno=18, end_col_offset=29, id='_', ctx=Load()),
                                                args=[Constant(lineno=18, col_offset=30, end_lineno=18, end_col_offset=87, value='You can send badges only to employees linked to a user.', kind=None)],
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
                        If(
                            lineno=20,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=71,
                            test=Compare(
                                lineno=20,
                                col_offset=11,
                                end_lineno=20,
                                end_col_offset=42,
                                left=Attribute(
                                    lineno=20,
                                    col_offset=11,
                                    end_lineno=20,
                                    end_col_offset=23,
                                    value=Attribute(
                                        lineno=20,
                                        col_offset=11,
                                        end_lineno=20,
                                        end_col_offset=19,
                                        value=Name(lineno=20, col_offset=11, end_lineno=20, end_col_offset=15, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        lineno=20,
                                        col_offset=27,
                                        end_lineno=20,
                                        end_col_offset=42,
                                        value=Attribute(
                                            lineno=20,
                                            col_offset=27,
                                            end_lineno=20,
                                            end_col_offset=39,
                                            value=Name(lineno=20, col_offset=27, end_lineno=20, end_col_offset=31, id='self', ctx=Load()),
                                            attr='user_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    lineno=21,
                                    col_offset=12,
                                    end_lineno=21,
                                    end_col_offset=71,
                                    exc=Call(
                                        lineno=21,
                                        col_offset=18,
                                        end_lineno=21,
                                        end_col_offset=71,
                                        func=Name(lineno=21, col_offset=18, end_lineno=21, end_col_offset=27, id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=21,
                                                col_offset=28,
                                                end_lineno=21,
                                                end_col_offset=70,
                                                func=Name(lineno=21, col_offset=28, end_lineno=21, end_col_offset=29, id='_', ctx=Load()),
                                                args=[Constant(lineno=21, col_offset=30, end_lineno=21, end_col_offset=69, value='You can not send a badge to yourself.', kind=None)],
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
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=9,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=14, id='values', ctx=Store())],
                            value=Dict(
                                lineno=23,
                                col_offset=17,
                                end_lineno=29,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=24, col_offset=12, end_lineno=24, end_col_offset=21, value='user_id', kind=None),
                                    Constant(lineno=25, col_offset=12, end_lineno=25, end_col_offset=23, value='sender_id', kind=None),
                                    Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=22, value='badge_id', kind=None),
                                    Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=25, value='employee_id', kind=None),
                                    Constant(lineno=28, col_offset=12, end_lineno=28, end_col_offset=21, value='comment', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        lineno=24,
                                        col_offset=23,
                                        end_lineno=24,
                                        end_col_offset=38,
                                        value=Attribute(
                                            lineno=24,
                                            col_offset=23,
                                            end_lineno=24,
                                            end_col_offset=35,
                                            value=Name(lineno=24, col_offset=23, end_lineno=24, end_col_offset=27, id='self', ctx=Load()),
                                            attr='user_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=25,
                                        col_offset=25,
                                        end_lineno=25,
                                        end_col_offset=37,
                                        value=Attribute(
                                            lineno=25,
                                            col_offset=25,
                                            end_lineno=25,
                                            end_col_offset=33,
                                            value=Name(lineno=25, col_offset=25, end_lineno=25, end_col_offset=29, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=26,
                                        col_offset=24,
                                        end_lineno=26,
                                        end_col_offset=40,
                                        value=Attribute(
                                            lineno=26,
                                            col_offset=24,
                                            end_lineno=26,
                                            end_col_offset=37,
                                            value=Name(lineno=26, col_offset=24, end_lineno=26, end_col_offset=28, id='self', ctx=Load()),
                                            attr='badge_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=27,
                                        col_offset=27,
                                        end_lineno=27,
                                        end_col_offset=46,
                                        value=Attribute(
                                            lineno=27,
                                            col_offset=27,
                                            end_lineno=27,
                                            end_col_offset=43,
                                            value=Name(lineno=27, col_offset=27, end_lineno=27, end_col_offset=31, id='self', ctx=Load()),
                                            attr='employee_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=28,
                                        col_offset=23,
                                        end_lineno=28,
                                        end_col_offset=35,
                                        value=Name(lineno=28, col_offset=23, end_lineno=28, end_col_offset=27, id='self', ctx=Load()),
                                        attr='comment',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=79,
                            value=Call(
                                lineno=31,
                                col_offset=15,
                                end_lineno=31,
                                end_col_offset=79,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=15,
                                    end_lineno=31,
                                    end_col_offset=77,
                                    value=Call(
                                        lineno=31,
                                        col_offset=15,
                                        end_lineno=31,
                                        end_col_offset=65,
                                        func=Attribute(
                                            lineno=31,
                                            col_offset=15,
                                            end_lineno=31,
                                            end_col_offset=57,
                                            value=Subscript(
                                                lineno=31,
                                                col_offset=15,
                                                end_lineno=31,
                                                end_col_offset=50,
                                                value=Attribute(
                                                    lineno=31,
                                                    col_offset=15,
                                                    end_lineno=31,
                                                    end_col_offset=23,
                                                    value=Name(lineno=31, col_offset=15, end_lineno=31, end_col_offset=19, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=31, col_offset=24, end_lineno=31, end_col_offset=49, value='gamification.badge.user', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=31, col_offset=58, end_lineno=31, end_col_offset=64, id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_send_badge',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
