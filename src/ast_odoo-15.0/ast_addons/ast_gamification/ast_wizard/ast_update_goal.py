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
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=24,
            end_col_offset=20,
            name='goal_manual_wizard',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=25,
                    end_lineno=6,
                    end_col_offset=46,
                    value=Name(lineno=6, col_offset=25, end_lineno=6, end_col_offset=31, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=40,
                    value=Constant(lineno=7, col_offset=4, end_lineno=7, end_col_offset=40, value='Wizard to update a manual goal', kind=None),
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=38,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=38, value='gamification.goal.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=45,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=45, value='Gamification Goal Wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=80,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=11, id='goal_id', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=14,
                        end_lineno=11,
                        end_col_offset=80,
                        func=Attribute(
                            lineno=11,
                            col_offset=14,
                            end_lineno=11,
                            end_col_offset=29,
                            value=Name(lineno=11, col_offset=14, end_lineno=11, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=30, end_lineno=11, end_col_offset=49, value='gamification.goal', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=51,
                                end_lineno=11,
                                end_col_offset=64,
                                arg='string',
                                value=Constant(lineno=11, col_offset=58, end_lineno=11, end_col_offset=64, value='Goal', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=66,
                                end_lineno=11,
                                end_col_offset=79,
                                arg='required',
                                value=Constant(lineno=11, col_offset=75, end_lineno=11, end_col_offset=79, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=37,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=11, id='current', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=14,
                        end_lineno=12,
                        end_col_offset=37,
                        func=Attribute(
                            lineno=12,
                            col_offset=14,
                            end_lineno=12,
                            end_col_offset=26,
                            value=Name(lineno=12, col_offset=14, end_lineno=12, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=27, end_lineno=12, end_col_offset=36, value='Current', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=20,
                    name='action_update_current',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=30, end_lineno=14, end_col_offset=34, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=58,
                            value=Constant(lineno=15, col_offset=8, end_lineno=15, end_col_offset=58, value='Wizard action for updating the current value', kind=None),
                        ),
                        For(
                            lineno=16,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=37,
                            target=Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=15, id='wiz', ctx=Store()),
                            iter=Name(lineno=16, col_offset=19, end_lineno=16, end_col_offset=23, id='self', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=21,
                                    end_col_offset=14,
                                    value=Call(
                                        lineno=17,
                                        col_offset=12,
                                        end_lineno=21,
                                        end_col_offset=14,
                                        func=Attribute(
                                            lineno=17,
                                            col_offset=12,
                                            end_lineno=17,
                                            end_col_offset=29,
                                            value=Attribute(
                                                lineno=17,
                                                col_offset=12,
                                                end_lineno=17,
                                                end_col_offset=23,
                                                value=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=15, id='wiz', ctx=Load()),
                                                attr='goal_id',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=17,
                                                col_offset=30,
                                                end_lineno=21,
                                                end_col_offset=13,
                                                keys=[
                                                    Constant(lineno=18, col_offset=16, end_lineno=18, end_col_offset=25, value='current', kind=None),
                                                    Constant(lineno=19, col_offset=16, end_lineno=19, end_col_offset=25, value='goal_id', kind=None),
                                                    Constant(lineno=20, col_offset=16, end_lineno=20, end_col_offset=27, value='to_update', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        lineno=18,
                                                        col_offset=27,
                                                        end_lineno=18,
                                                        end_col_offset=38,
                                                        value=Name(lineno=18, col_offset=27, end_lineno=18, end_col_offset=30, id='wiz', ctx=Load()),
                                                        attr='current',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        lineno=19,
                                                        col_offset=27,
                                                        end_lineno=19,
                                                        end_col_offset=41,
                                                        value=Attribute(
                                                            lineno=19,
                                                            col_offset=27,
                                                            end_lineno=19,
                                                            end_col_offset=38,
                                                            value=Name(lineno=19, col_offset=27, end_lineno=19, end_col_offset=30, id='wiz', ctx=Load()),
                                                            attr='goal_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=20, col_offset=29, end_lineno=20, end_col_offset=34, value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=37,
                                    value=Call(
                                        lineno=22,
                                        col_offset=12,
                                        end_lineno=22,
                                        end_col_offset=37,
                                        func=Attribute(
                                            lineno=22,
                                            col_offset=12,
                                            end_lineno=22,
                                            end_col_offset=35,
                                            value=Attribute(
                                                lineno=22,
                                                col_offset=12,
                                                end_lineno=22,
                                                end_col_offset=23,
                                                value=Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=15, id='wiz', ctx=Load()),
                                                attr='goal_id',
                                                ctx=Load(),
                                            ),
                                            attr='update_goal',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=20,
                            value=Constant(lineno=24, col_offset=15, end_lineno=24, end_col_offset=20, value=False, kind=None),
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