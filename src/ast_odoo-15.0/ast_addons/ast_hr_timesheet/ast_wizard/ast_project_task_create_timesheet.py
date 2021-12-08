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
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=29,
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=35,
            end_col_offset=43,
            name='ProjectTaskCreateTimesheet',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=33,
                    end_lineno=8,
                    end_col_offset=54,
                    value=Name(lineno=8, col_offset=33, end_lineno=8, end_col_offset=39, id='models', ctx=Load()),
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
                    end_col_offset=43,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=9, col_offset=12, end_lineno=9, end_col_offset=43, value='project.task.create.timesheet', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=47,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=10, col_offset=19, end_lineno=10, end_col_offset=47, value='Create Timesheet from task', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=110,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=20, id='_sql_constraints', ctx=Store())],
                    value=List(
                        lineno=12,
                        col_offset=23,
                        end_lineno=12,
                        end_col_offset=110,
                        elts=[
                            Tuple(
                                lineno=12,
                                col_offset=24,
                                end_lineno=12,
                                end_col_offset=109,
                                elts=[
                                    Constant(lineno=12, col_offset=25, end_lineno=12, end_col_offset=40, value='time_positive', kind=None),
                                    Constant(lineno=12, col_offset=42, end_lineno=12, end_col_offset=65, value='CHECK(time_spent > 0)', kind=None),
                                    Constant(lineno=12, col_offset=67, end_lineno=12, end_col_offset=107, value="The timesheet's time must be positive", kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=53,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=14, id='time_spent', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=17,
                        end_lineno=14,
                        end_col_offset=53,
                        func=Attribute(
                            lineno=14,
                            col_offset=17,
                            end_lineno=14,
                            end_col_offset=29,
                            value=Name(lineno=14, col_offset=17, end_lineno=14, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=14, col_offset=30, end_lineno=14, end_col_offset=36, value='Time', kind=None)],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=38,
                                end_lineno=14,
                                end_col_offset=52,
                                arg='digits',
                                value=Tuple(
                                    lineno=14,
                                    col_offset=45,
                                    end_lineno=14,
                                    end_col_offset=52,
                                    elts=[
                                        Constant(lineno=14, col_offset=46, end_lineno=14, end_col_offset=48, value=16, kind=None),
                                        Constant(lineno=14, col_offset=50, end_lineno=14, end_col_offset=51, value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=44,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=15, id='description', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=18,
                        end_lineno=15,
                        end_col_offset=44,
                        func=Attribute(
                            lineno=15,
                            col_offset=18,
                            end_lineno=15,
                            end_col_offset=29,
                            value=Name(lineno=15, col_offset=18, end_lineno=15, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=15, col_offset=30, end_lineno=15, end_col_offset=43, value='Description', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=5,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=11, id='task_id', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=14,
                        end_lineno=20,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=16,
                            col_offset=14,
                            end_lineno=16,
                            end_col_offset=29,
                            value=Name(lineno=16, col_offset=14, end_lineno=16, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=17, col_offset=8, end_lineno=17, end_col_offset=22, value='project.task', kind=None),
                            Constant(lineno=17, col_offset=24, end_lineno=17, end_col_offset=30, value='Task', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=32,
                                end_lineno=17,
                                end_col_offset=45,
                                arg='required',
                                value=Constant(lineno=17, col_offset=41, end_lineno=17, end_col_offset=45, value=True, kind=None),
                            ),
                            keyword(
                                lineno=18,
                                col_offset=8,
                                end_lineno=18,
                                end_col_offset=68,
                                arg='default',
                                value=Lambda(
                                    lineno=18,
                                    col_offset=16,
                                    end_lineno=18,
                                    end_col_offset=68,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=18, col_offset=23, end_lineno=18, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        lineno=18,
                                        col_offset=29,
                                        end_lineno=18,
                                        end_col_offset=68,
                                        func=Attribute(
                                            lineno=18,
                                            col_offset=29,
                                            end_lineno=18,
                                            end_col_offset=49,
                                            value=Attribute(
                                                lineno=18,
                                                col_offset=29,
                                                end_lineno=18,
                                                end_col_offset=45,
                                                value=Attribute(
                                                    lineno=18,
                                                    col_offset=29,
                                                    end_lineno=18,
                                                    end_col_offset=37,
                                                    value=Name(lineno=18, col_offset=29, end_lineno=18, end_col_offset=33, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(lineno=18, col_offset=50, end_lineno=18, end_col_offset=61, value='active_id', kind=None),
                                            Constant(lineno=18, col_offset=63, end_lineno=18, end_col_offset=67, value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=8,
                                end_lineno=19,
                                end_col_offset=59,
                                arg='help',
                                value=Constant(lineno=19, col_offset=13, end_lineno=19, end_col_offset=59, value='Task for which we are creating a sales order', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=22,
                    col_offset=4,
                    end_lineno=32,
                    end_col_offset=63,
                    name='save_timesheet',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=22, col_offset=23, end_lineno=22, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=9,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=14, id='values', ctx=Store())],
                            value=Dict(
                                lineno=23,
                                col_offset=17,
                                end_lineno=30,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=24, col_offset=12, end_lineno=24, end_col_offset=21, value='task_id', kind=None),
                                    Constant(lineno=25, col_offset=12, end_lineno=25, end_col_offset=24, value='project_id', kind=None),
                                    Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=18, value='date', kind=None),
                                    Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=18, value='name', kind=None),
                                    Constant(lineno=28, col_offset=12, end_lineno=28, end_col_offset=21, value='user_id', kind=None),
                                    Constant(lineno=29, col_offset=12, end_lineno=29, end_col_offset=25, value='unit_amount', kind=None),
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
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=25,
                                        col_offset=26,
                                        end_lineno=25,
                                        end_col_offset=52,
                                        value=Attribute(
                                            lineno=25,
                                            col_offset=26,
                                            end_lineno=25,
                                            end_col_offset=49,
                                            value=Attribute(
                                                lineno=25,
                                                col_offset=26,
                                                end_lineno=25,
                                                end_col_offset=38,
                                                value=Name(lineno=25, col_offset=26, end_lineno=25, end_col_offset=30, id='self', ctx=Load()),
                                                attr='task_id',
                                                ctx=Load(),
                                            ),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        lineno=26,
                                        col_offset=20,
                                        end_lineno=26,
                                        end_col_offset=51,
                                        func=Attribute(
                                            lineno=26,
                                            col_offset=20,
                                            end_lineno=26,
                                            end_col_offset=45,
                                            value=Attribute(
                                                lineno=26,
                                                col_offset=20,
                                                end_lineno=26,
                                                end_col_offset=31,
                                                value=Name(lineno=26, col_offset=20, end_lineno=26, end_col_offset=26, id='fields', ctx=Load()),
                                                attr='Date',
                                                ctx=Load(),
                                            ),
                                            attr='context_today',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=26, col_offset=46, end_lineno=26, end_col_offset=50, id='self', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        lineno=27,
                                        col_offset=20,
                                        end_lineno=27,
                                        end_col_offset=36,
                                        value=Name(lineno=27, col_offset=20, end_lineno=27, end_col_offset=24, id='self', ctx=Load()),
                                        attr='description',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=28,
                                        col_offset=23,
                                        end_lineno=28,
                                        end_col_offset=35,
                                        value=Attribute(
                                            lineno=28,
                                            col_offset=23,
                                            end_lineno=28,
                                            end_col_offset=31,
                                            value=Name(lineno=28, col_offset=23, end_lineno=28, end_col_offset=27, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=29,
                                        col_offset=27,
                                        end_lineno=29,
                                        end_col_offset=42,
                                        value=Name(lineno=29, col_offset=27, end_lineno=29, end_col_offset=31, id='self', ctx=Load()),
                                        attr='time_spent',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=43,
                            value=Call(
                                lineno=31,
                                col_offset=8,
                                end_lineno=31,
                                end_col_offset=43,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=8,
                                    end_lineno=31,
                                    end_col_offset=41,
                                    value=Attribute(
                                        lineno=31,
                                        col_offset=8,
                                        end_lineno=31,
                                        end_col_offset=34,
                                        value=Attribute(
                                            lineno=31,
                                            col_offset=8,
                                            end_lineno=31,
                                            end_col_offset=20,
                                            value=Name(lineno=31, col_offset=8, end_lineno=31, end_col_offset=12, id='self', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='user_timer_id',
                                        ctx=Load(),
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=63,
                            value=Call(
                                lineno=32,
                                col_offset=15,
                                end_lineno=32,
                                end_col_offset=63,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=15,
                                    end_lineno=32,
                                    end_col_offset=55,
                                    value=Subscript(
                                        lineno=32,
                                        col_offset=15,
                                        end_lineno=32,
                                        end_col_offset=48,
                                        value=Attribute(
                                            lineno=32,
                                            col_offset=15,
                                            end_lineno=32,
                                            end_col_offset=23,
                                            value=Name(lineno=32, col_offset=15, end_lineno=32, end_col_offset=19, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=32, col_offset=24, end_lineno=32, end_col_offset=47, value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=32, col_offset=56, end_lineno=32, end_col_offset=62, id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=34,
                    col_offset=4,
                    end_lineno=35,
                    end_col_offset=43,
                    name='action_delete_timesheet',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=34, col_offset=32, end_lineno=34, end_col_offset=36, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=35,
                            col_offset=8,
                            end_lineno=35,
                            end_col_offset=43,
                            value=Call(
                                lineno=35,
                                col_offset=8,
                                end_lineno=35,
                                end_col_offset=43,
                                func=Attribute(
                                    lineno=35,
                                    col_offset=8,
                                    end_lineno=35,
                                    end_col_offset=41,
                                    value=Attribute(
                                        lineno=35,
                                        col_offset=8,
                                        end_lineno=35,
                                        end_col_offset=34,
                                        value=Attribute(
                                            lineno=35,
                                            col_offset=8,
                                            end_lineno=35,
                                            end_col_offset=20,
                                            value=Name(lineno=35, col_offset=8, end_lineno=35, end_col_offset=12, id='self', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='user_timer_id',
                                        ctx=Load(),
                                    ),
                                    attr='unlink',
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