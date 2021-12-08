Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=24,
            end_col_offset=63,
            name='AlarmManager',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=19,
                    end_lineno=7,
                    end_col_offset=39,
                    value=Name(lineno=7, col_offset=19, end_lineno=7, end_col_offset=25, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=39,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=39, value='calendar.alarm_manager', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=63,
                    name='_send_reminder',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=23, end_lineno=11, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=11,
                            value=Constant(lineno=12, col_offset=8, end_lineno=13, end_col_offset=11, value=' Cron method, overridden here to send SMS reminders as well\n        ', kind=None),
                        ),
                        Expr(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=32,
                            value=Call(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=32,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=30,
                                    value=Call(
                                        lineno=14,
                                        col_offset=8,
                                        end_lineno=14,
                                        end_col_offset=15,
                                        func=Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=13, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_send_reminder',
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
                            end_col_offset=68,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=23, id='alarms_by_event', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=26,
                                end_lineno=15,
                                end_col_offset=68,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=26,
                                    end_lineno=15,
                                    end_col_offset=61,
                                    value=Name(lineno=15, col_offset=26, end_lineno=15, end_col_offset=30, id='self', ctx=Load()),
                                    attr='_get_events_by_alarm_to_notify',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=15, col_offset=62, end_lineno=15, end_col_offset=67, value='sms', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=16,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=18,
                            test=UnaryOp(
                                lineno=16,
                                col_offset=11,
                                end_lineno=16,
                                end_col_offset=30,
                                op=Not(),
                                operand=Name(lineno=16, col_offset=15, end_lineno=16, end_col_offset=30, id='alarms_by_event', ctx=Load()),
                            ),
                            body=[Return(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, value=None)],
                            orelse=[],
                        ),
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=80,
                            targets=[Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=14, id='events', ctx=Store())],
                            value=Call(
                                lineno=19,
                                col_offset=17,
                                end_lineno=19,
                                end_col_offset=80,
                                func=Attribute(
                                    lineno=19,
                                    col_offset=17,
                                    end_lineno=19,
                                    end_col_offset=50,
                                    value=Subscript(
                                        lineno=19,
                                        col_offset=17,
                                        end_lineno=19,
                                        end_col_offset=43,
                                        value=Attribute(
                                            lineno=19,
                                            col_offset=17,
                                            end_lineno=19,
                                            end_col_offset=25,
                                            value=Name(lineno=19, col_offset=17, end_lineno=19, end_col_offset=21, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=19, col_offset=26, end_lineno=19, end_col_offset=42, value='calendar.event', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=19,
                                        col_offset=51,
                                        end_lineno=19,
                                        end_col_offset=79,
                                        func=Name(lineno=19, col_offset=51, end_lineno=19, end_col_offset=55, id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=19,
                                                col_offset=56,
                                                end_lineno=19,
                                                end_col_offset=78,
                                                func=Attribute(
                                                    lineno=19,
                                                    col_offset=56,
                                                    end_lineno=19,
                                                    end_col_offset=76,
                                                    value=Name(lineno=19, col_offset=56, end_lineno=19, end_col_offset=71, id='alarms_by_event', ctx=Load()),
                                                    attr='keys',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=81,
                            targets=[Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=17, id='attendees', ctx=Store())],
                            value=Call(
                                lineno=20,
                                col_offset=20,
                                end_lineno=20,
                                end_col_offset=81,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=20,
                                    end_lineno=20,
                                    end_col_offset=48,
                                    value=Attribute(
                                        lineno=20,
                                        col_offset=20,
                                        end_lineno=20,
                                        end_col_offset=39,
                                        value=Name(lineno=20, col_offset=20, end_lineno=20, end_col_offset=26, id='events', ctx=Load()),
                                        attr='attendee_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        lineno=20,
                                        col_offset=49,
                                        end_lineno=20,
                                        end_col_offset=80,
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(lineno=20, col_offset=56, end_lineno=20, end_col_offset=57, arg='a', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            lineno=20,
                                            col_offset=59,
                                            end_lineno=20,
                                            end_col_offset=80,
                                            left=Attribute(
                                                lineno=20,
                                                col_offset=59,
                                                end_lineno=20,
                                                end_col_offset=66,
                                                value=Name(lineno=20, col_offset=59, end_lineno=20, end_col_offset=60, id='a', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(lineno=20, col_offset=70, end_lineno=20, end_col_offset=80, value='declined', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=21,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=63,
                            target=Name(lineno=21, col_offset=12, end_lineno=21, end_col_offset=20, id='event_id', ctx=Store()),
                            iter=Call(
                                lineno=21,
                                col_offset=24,
                                end_lineno=21,
                                end_col_offset=46,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=24,
                                    end_lineno=21,
                                    end_col_offset=44,
                                    value=Name(lineno=21, col_offset=24, end_lineno=21, end_col_offset=39, id='alarms_by_event', ctx=Load()),
                                    attr='keys',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=125,
                                    targets=[Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=24, id='event_alarms', ctx=Store())],
                                    value=Call(
                                        lineno=22,
                                        col_offset=27,
                                        end_lineno=22,
                                        end_col_offset=125,
                                        func=Attribute(
                                            lineno=22,
                                            col_offset=27,
                                            end_lineno=22,
                                            end_col_offset=64,
                                            value=Attribute(
                                                lineno=22,
                                                col_offset=27,
                                                end_lineno=22,
                                                end_col_offset=55,
                                                value=Attribute(
                                                    lineno=22,
                                                    col_offset=27,
                                                    end_lineno=22,
                                                    end_col_offset=45,
                                                    value=Name(lineno=22, col_offset=27, end_lineno=22, end_col_offset=36, id='attendees', ctx=Load()),
                                                    attr='event_id',
                                                    ctx=Load(),
                                                ),
                                                attr='alarm_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                lineno=22,
                                                col_offset=65,
                                                end_lineno=22,
                                                end_col_offset=124,
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(lineno=22, col_offset=72, end_lineno=22, end_col_offset=77, arg='alarm', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    lineno=22,
                                                    col_offset=79,
                                                    end_lineno=22,
                                                    end_col_offset=124,
                                                    left=Attribute(
                                                        lineno=22,
                                                        col_offset=79,
                                                        end_lineno=22,
                                                        end_col_offset=87,
                                                        value=Name(lineno=22, col_offset=79, end_lineno=22, end_col_offset=84, id='alarm', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Call(
                                                            lineno=22,
                                                            col_offset=91,
                                                            end_lineno=22,
                                                            end_col_offset=124,
                                                            func=Attribute(
                                                                lineno=22,
                                                                col_offset=91,
                                                                end_lineno=22,
                                                                end_col_offset=110,
                                                                value=Name(lineno=22, col_offset=91, end_lineno=22, end_col_offset=106, id='alarms_by_event', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(lineno=22, col_offset=111, end_lineno=22, end_col_offset=119, id='event_id', ctx=Load()),
                                                                List(lineno=22, col_offset=121, end_lineno=22, end_col_offset=123, elts=[], ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    lineno=23,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=63,
                                    target=Name(lineno=23, col_offset=16, end_lineno=23, end_col_offset=21, id='alarm', ctx=Store()),
                                    iter=Name(lineno=23, col_offset=25, end_lineno=23, end_col_offset=37, id='event_alarms', ctx=Load()),
                                    body=[
                                        Expr(
                                            lineno=24,
                                            col_offset=16,
                                            end_lineno=24,
                                            end_col_offset=63,
                                            value=Call(
                                                lineno=24,
                                                col_offset=16,
                                                end_lineno=24,
                                                end_col_offset=63,
                                                func=Attribute(
                                                    lineno=24,
                                                    col_offset=16,
                                                    end_lineno=24,
                                                    end_col_offset=56,
                                                    value=Call(
                                                        lineno=24,
                                                        col_offset=16,
                                                        end_lineno=24,
                                                        end_col_offset=39,
                                                        func=Attribute(
                                                            lineno=24,
                                                            col_offset=16,
                                                            end_lineno=24,
                                                            end_col_offset=29,
                                                            value=Name(lineno=24, col_offset=16, end_lineno=24, end_col_offset=22, id='events', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(lineno=24, col_offset=30, end_lineno=24, end_col_offset=38, id='event_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='_do_sms_reminder',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(lineno=24, col_offset=57, end_lineno=24, end_col_offset=62, id='alarm', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=10,
                            col_offset=5,
                            end_lineno=10,
                            end_col_offset=14,
                            value=Name(lineno=10, col_offset=5, end_lineno=10, end_col_offset=8, id='api', ctx=Load()),
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