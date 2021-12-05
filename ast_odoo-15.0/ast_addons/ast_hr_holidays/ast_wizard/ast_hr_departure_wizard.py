Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=40,
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=27,
            end_col_offset=49,
            name='HrDepartureWizard',
            bases=[
                Attribute(
                    lineno=9,
                    col_offset=24,
                    end_lineno=9,
                    end_col_offset=45,
                    value=Name(lineno=9, col_offset=24, end_lineno=9, end_col_offset=30, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=36,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=10, col_offset=15, end_lineno=10, end_col_offset=36, value='hr.departure.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=52,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=17, id='cancel_leaves', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=20,
                        end_lineno=13,
                        end_col_offset=52,
                        func=Attribute(
                            lineno=12,
                            col_offset=20,
                            end_lineno=12,
                            end_col_offset=34,
                            value=Name(lineno=12, col_offset=20, end_lineno=12, end_col_offset=26, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=35, end_lineno=12, end_col_offset=57, value='Cancel Future Leaves', kind=None)],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=59,
                                end_lineno=12,
                                end_col_offset=71,
                                arg='default',
                                value=Constant(lineno=12, col_offset=67, end_lineno=12, end_col_offset=71, value=True, kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=51,
                                arg='help',
                                value=Constant(lineno=13, col_offset=13, end_lineno=13, end_col_offset=51, value='Cancel all time off after this date.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=60,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=22, id='archive_allocation', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=25,
                        end_lineno=15,
                        end_col_offset=60,
                        func=Attribute(
                            lineno=14,
                            col_offset=25,
                            end_lineno=14,
                            end_col_offset=39,
                            value=Name(lineno=14, col_offset=25, end_lineno=14, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=14, col_offset=40, end_lineno=14, end_col_offset=70, value='Archive Employee Allocations', kind=None)],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=72,
                                end_lineno=14,
                                end_col_offset=84,
                                arg='default',
                                value=Constant(lineno=14, col_offset=80, end_lineno=14, end_col_offset=84, value=True, kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=59,
                                arg='help',
                                value=Constant(lineno=15, col_offset=13, end_lineno=15, end_col_offset=59, value='Remove employee from existing accrual plans.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=17,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=49,
                    name='action_register_departure',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=17, col_offset=34, end_lineno=17, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=66,
                            value=Call(
                                lineno=18,
                                col_offset=8,
                                end_lineno=18,
                                end_col_offset=66,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=8,
                                    end_lineno=18,
                                    end_col_offset=64,
                                    value=Call(
                                        lineno=18,
                                        col_offset=8,
                                        end_lineno=18,
                                        end_col_offset=38,
                                        func=Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=13, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=18, col_offset=14, end_lineno=18, end_col_offset=31, id='HrDepartureWizard', ctx=Load()),
                                            Name(lineno=18, col_offset=33, end_lineno=18, end_col_offset=37, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='action_register_departure',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            lineno=19,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=52,
                            test=Attribute(
                                lineno=19,
                                col_offset=11,
                                end_lineno=19,
                                end_col_offset=29,
                                value=Name(lineno=19, col_offset=11, end_lineno=19, end_col_offset=15, id='self', ctx=Load()),
                                attr='cancel_leaves',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    lineno=20,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=84,
                                    targets=[Name(lineno=20, col_offset=12, end_lineno=20, end_col_offset=25, id='future_leaves', ctx=Store())],
                                    value=Call(
                                        lineno=20,
                                        col_offset=28,
                                        end_lineno=22,
                                        end_col_offset=84,
                                        func=Attribute(
                                            lineno=20,
                                            col_offset=28,
                                            end_lineno=20,
                                            end_col_offset=55,
                                            value=Subscript(
                                                lineno=20,
                                                col_offset=28,
                                                end_lineno=20,
                                                end_col_offset=48,
                                                value=Attribute(
                                                    lineno=20,
                                                    col_offset=28,
                                                    end_lineno=20,
                                                    end_col_offset=36,
                                                    value=Name(lineno=20, col_offset=28, end_lineno=20, end_col_offset=32, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=20, col_offset=37, end_lineno=20, end_col_offset=47, value='hr.leave', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                lineno=20,
                                                col_offset=56,
                                                end_lineno=22,
                                                end_col_offset=83,
                                                elts=[
                                                    Tuple(
                                                        lineno=20,
                                                        col_offset=57,
                                                        end_lineno=20,
                                                        end_col_offset=98,
                                                        elts=[
                                                            Constant(lineno=20, col_offset=58, end_lineno=20, end_col_offset=71, value='employee_id', kind=None),
                                                            Constant(lineno=20, col_offset=73, end_lineno=20, end_col_offset=76, value='=', kind=None),
                                                            Attribute(
                                                                lineno=20,
                                                                col_offset=78,
                                                                end_lineno=20,
                                                                end_col_offset=97,
                                                                value=Attribute(
                                                                    lineno=20,
                                                                    col_offset=78,
                                                                    end_lineno=20,
                                                                    end_col_offset=94,
                                                                    value=Name(lineno=20, col_offset=78, end_lineno=20, end_col_offset=82, id='self', ctx=Load()),
                                                                    attr='employee_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        lineno=21,
                                                        col_offset=57,
                                                        end_lineno=21,
                                                        end_col_offset=94,
                                                        elts=[
                                                            Constant(lineno=21, col_offset=58, end_lineno=21, end_col_offset=67, value='date_to', kind=None),
                                                            Constant(lineno=21, col_offset=69, end_lineno=21, end_col_offset=72, value='>', kind=None),
                                                            Attribute(
                                                                lineno=21,
                                                                col_offset=74,
                                                                end_lineno=21,
                                                                end_col_offset=93,
                                                                value=Name(lineno=21, col_offset=74, end_lineno=21, end_col_offset=78, id='self', ctx=Load()),
                                                                attr='departure_date',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        lineno=22,
                                                        col_offset=57,
                                                        end_lineno=22,
                                                        end_col_offset=82,
                                                        elts=[
                                                            Constant(lineno=22, col_offset=58, end_lineno=22, end_col_offset=65, value='state', kind=None),
                                                            Constant(lineno=22, col_offset=67, end_lineno=22, end_col_offset=71, value='!=', kind=None),
                                                            Constant(lineno=22, col_offset=73, end_lineno=22, end_col_offset=81, value='refuse', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    lineno=23,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=52,
                                    value=Call(
                                        lineno=23,
                                        col_offset=12,
                                        end_lineno=23,
                                        end_col_offset=52,
                                        func=Attribute(
                                            lineno=23,
                                            col_offset=12,
                                            end_lineno=23,
                                            end_col_offset=31,
                                            value=Name(lineno=23, col_offset=12, end_lineno=23, end_col_offset=25, id='future_leaves', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=23,
                                                col_offset=32,
                                                end_lineno=23,
                                                end_col_offset=51,
                                                keys=[Constant(lineno=23, col_offset=33, end_lineno=23, end_col_offset=40, value='state', kind=None)],
                                                values=[Constant(lineno=23, col_offset=42, end_lineno=23, end_col_offset=50, value='refuse', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            lineno=25,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=49,
                            test=Attribute(
                                lineno=25,
                                col_offset=11,
                                end_lineno=25,
                                end_col_offset=34,
                                value=Name(lineno=25, col_offset=11, end_lineno=25, end_col_offset=15, id='self', ctx=Load()),
                                attr='archive_allocation',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    lineno=26,
                                    col_offset=12,
                                    end_lineno=26,
                                    end_col_offset=118,
                                    targets=[Name(lineno=26, col_offset=12, end_lineno=26, end_col_offset=32, id='employee_allocations', ctx=Store())],
                                    value=Call(
                                        lineno=26,
                                        col_offset=35,
                                        end_lineno=26,
                                        end_col_offset=118,
                                        func=Attribute(
                                            lineno=26,
                                            col_offset=35,
                                            end_lineno=26,
                                            end_col_offset=73,
                                            value=Subscript(
                                                lineno=26,
                                                col_offset=35,
                                                end_lineno=26,
                                                end_col_offset=66,
                                                value=Attribute(
                                                    lineno=26,
                                                    col_offset=35,
                                                    end_lineno=26,
                                                    end_col_offset=43,
                                                    value=Name(lineno=26, col_offset=35, end_lineno=26, end_col_offset=39, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=26, col_offset=44, end_lineno=26, end_col_offset=65, value='hr.leave.allocation', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                lineno=26,
                                                col_offset=74,
                                                end_lineno=26,
                                                end_col_offset=117,
                                                elts=[
                                                    Tuple(
                                                        lineno=26,
                                                        col_offset=75,
                                                        end_lineno=26,
                                                        end_col_offset=116,
                                                        elts=[
                                                            Constant(lineno=26, col_offset=76, end_lineno=26, end_col_offset=89, value='employee_id', kind=None),
                                                            Constant(lineno=26, col_offset=91, end_lineno=26, end_col_offset=94, value='=', kind=None),
                                                            Attribute(
                                                                lineno=26,
                                                                col_offset=96,
                                                                end_lineno=26,
                                                                end_col_offset=115,
                                                                value=Attribute(
                                                                    lineno=26,
                                                                    col_offset=96,
                                                                    end_lineno=26,
                                                                    end_col_offset=112,
                                                                    value=Name(lineno=26, col_offset=96, end_lineno=26, end_col_offset=100, id='self', ctx=Load()),
                                                                    attr='employee_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    lineno=27,
                                    col_offset=12,
                                    end_lineno=27,
                                    end_col_offset=49,
                                    value=Call(
                                        lineno=27,
                                        col_offset=12,
                                        end_lineno=27,
                                        end_col_offset=49,
                                        func=Attribute(
                                            lineno=27,
                                            col_offset=12,
                                            end_lineno=27,
                                            end_col_offset=47,
                                            value=Name(lineno=27, col_offset=12, end_lineno=27, end_col_offset=32, id='employee_allocations', ctx=Load()),
                                            attr='action_archive',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
