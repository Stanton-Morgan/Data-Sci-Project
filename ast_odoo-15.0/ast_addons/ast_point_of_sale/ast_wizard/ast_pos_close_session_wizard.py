Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=20,
            end_col_offset=9,
            name='PosCloseSessionWizard',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=28,
                    end_lineno=7,
                    end_col_offset=49,
                    value=Name(lineno=7, col_offset=28, end_lineno=7, end_col_offset=34, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=38,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=38, value='pos.close.session.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=41,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=41, value='Close Session Wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=57,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=21, id='amount_to_balance', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=24,
                        end_lineno=11,
                        end_col_offset=57,
                        func=Attribute(
                            lineno=11,
                            col_offset=24,
                            end_lineno=11,
                            end_col_offset=36,
                            value=Name(lineno=11, col_offset=24, end_lineno=11, end_col_offset=30, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=37, end_lineno=11, end_col_offset=56, value='Amount to balance', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=74,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=14, id='account_id', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=17,
                        end_lineno=12,
                        end_col_offset=74,
                        func=Attribute(
                            lineno=12,
                            col_offset=17,
                            end_lineno=12,
                            end_col_offset=32,
                            value=Name(lineno=12, col_offset=17, end_lineno=12, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=12, col_offset=33, end_lineno=12, end_col_offset=50, value='account.account', kind=None),
                            Constant(lineno=12, col_offset=52, end_lineno=12, end_col_offset=73, value='Destination account', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=72,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=20, id='account_readonly', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=23,
                        end_lineno=13,
                        end_col_offset=72,
                        func=Attribute(
                            lineno=13,
                            col_offset=23,
                            end_lineno=13,
                            end_col_offset=37,
                            value=Name(lineno=13, col_offset=23, end_lineno=13, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=38, end_lineno=13, end_col_offset=71, value='Destination account is readonly', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=48,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=11, id='message', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=14,
                        end_lineno=14,
                        end_col_offset=48,
                        func=Attribute(
                            lineno=14,
                            col_offset=14,
                            end_lineno=14,
                            end_col_offset=25,
                            value=Name(lineno=14, col_offset=14, end_lineno=14, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=14, col_offset=26, end_lineno=14, end_col_offset=47, value='Information message', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=9,
                    name='close_session',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=22, end_lineno=16, end_col_offset=26, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=80,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=15, id='session', ctx=Store())],
                            value=Call(
                                lineno=17,
                                col_offset=18,
                                end_lineno=17,
                                end_col_offset=80,
                                func=Attribute(
                                    lineno=17,
                                    col_offset=18,
                                    end_lineno=17,
                                    end_col_offset=48,
                                    value=Subscript(
                                        lineno=17,
                                        col_offset=18,
                                        end_lineno=17,
                                        end_col_offset=41,
                                        value=Attribute(
                                            lineno=17,
                                            col_offset=18,
                                            end_lineno=17,
                                            end_col_offset=26,
                                            value=Name(lineno=17, col_offset=18, end_lineno=17, end_col_offset=22, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=17, col_offset=27, end_lineno=17, end_col_offset=40, value='pos.session', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        lineno=17,
                                        col_offset=49,
                                        end_lineno=17,
                                        end_col_offset=79,
                                        value=Attribute(
                                            lineno=17,
                                            col_offset=49,
                                            end_lineno=17,
                                            end_col_offset=65,
                                            value=Attribute(
                                                lineno=17,
                                                col_offset=49,
                                                end_lineno=17,
                                                end_col_offset=57,
                                                value=Name(lineno=17, col_offset=49, end_lineno=17, end_col_offset=53, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=17, col_offset=66, end_lineno=17, end_col_offset=78, value='active_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=18,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=9,
                            value=Call(
                                lineno=18,
                                col_offset=15,
                                end_lineno=20,
                                end_col_offset=9,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=15,
                                    end_lineno=18,
                                    end_col_offset=57,
                                    value=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=22, id='session', ctx=Load()),
                                    attr='action_pos_session_closing_control',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=19,
                                        col_offset=12,
                                        end_lineno=19,
                                        end_col_offset=27,
                                        value=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=16, id='self', ctx=Load()),
                                        attr='account_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=19,
                                        col_offset=29,
                                        end_lineno=19,
                                        end_col_offset=51,
                                        value=Name(lineno=19, col_offset=29, end_lineno=19, end_col_offset=33, id='self', ctx=Load()),
                                        attr='amount_to_balance',
                                        ctx=Load(),
                                    ),
                                ],
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
