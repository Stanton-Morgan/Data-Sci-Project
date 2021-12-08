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
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=18,
            end_col_offset=89,
            name='MailActivityMixin',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=24,
                    end_lineno=6,
                    end_col_offset=44,
                    value=Name(lineno=6, col_offset=24, end_lineno=6, end_col_offset=30, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=36,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=36, value='mail.activity.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=80,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=30, id='activity_calendar_event_id', ctx=Store())],
                    value=Call(
                        lineno=9,
                        col_offset=33,
                        end_lineno=11,
                        end_col_offset=80,
                        func=Attribute(
                            lineno=9,
                            col_offset=33,
                            end_lineno=9,
                            end_col_offset=48,
                            value=Name(lineno=9, col_offset=33, end_lineno=9, end_col_offset=39, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=8, end_lineno=10, end_col_offset=24, value='calendar.event', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=26,
                                end_lineno=10,
                                end_col_offset=63,
                                arg='string',
                                value=Constant(lineno=10, col_offset=33, end_lineno=10, end_col_offset=63, value='Next Activity Calendar Event', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=53,
                                arg='compute',
                                value=Constant(lineno=11, col_offset=16, end_lineno=11, end_col_offset=53, value='_compute_activity_calendar_event_id', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=55,
                                end_lineno=11,
                                end_col_offset=79,
                                arg='groups',
                                value=Constant(lineno=11, col_offset=62, end_lineno=11, end_col_offset=79, value='base.group_user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=89,
                    name='_compute_activity_calendar_event_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=44, end_lineno=14, end_col_offset=48, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=16,
                            end_col_offset=59,
                            value=Constant(lineno=15, col_offset=8, end_lineno=16, end_col_offset=59, value='This computes the calendar event of the next activity.\n        It evaluates to false if there is no such event.', kind=None),
                        ),
                        For(
                            lineno=17,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=89,
                            target=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, id='record', ctx=Store()),
                            iter=Name(lineno=17, col_offset=22, end_lineno=17, end_col_offset=26, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=18,
                                    end_col_offset=89,
                                    targets=[
                                        Attribute(
                                            lineno=18,
                                            col_offset=12,
                                            end_lineno=18,
                                            end_col_offset=45,
                                            value=Name(lineno=18, col_offset=12, end_lineno=18, end_col_offset=18, id='record', ctx=Load()),
                                            attr='activity_calendar_event_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        lineno=18,
                                        col_offset=48,
                                        end_lineno=18,
                                        end_col_offset=89,
                                        value=Subscript(
                                            lineno=18,
                                            col_offset=48,
                                            end_lineno=18,
                                            end_col_offset=71,
                                            value=Attribute(
                                                lineno=18,
                                                col_offset=48,
                                                end_lineno=18,
                                                end_col_offset=67,
                                                value=Name(lineno=18, col_offset=48, end_lineno=18, end_col_offset=54, id='record', ctx=Load()),
                                                attr='activity_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lineno=18,
                                                col_offset=68,
                                                end_lineno=18,
                                                end_col_offset=70,
                                                lower=None,
                                                upper=Constant(lineno=18, col_offset=69, end_lineno=18, end_col_offset=70, value=1, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='calendar_event_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
                            end_col_offset=50,
                            func=Attribute(
                                lineno=13,
                                col_offset=5,
                                end_lineno=13,
                                end_col_offset=16,
                                value=Name(lineno=13, col_offset=5, end_lineno=13, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=13, col_offset=17, end_lineno=13, end_col_offset=49, value='activity_ids.calendar_event_id', kind=None)],
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