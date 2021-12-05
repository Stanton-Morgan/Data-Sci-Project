Module(
    body=[
        Import(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=11,
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
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
            lineno=8,
            col_offset=0,
            end_lineno=31,
            end_col_offset=109,
            name='HolidaysSummaryEmployee',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=30,
                    end_lineno=8,
                    end_col_offset=51,
                    value=Name(lineno=8, col_offset=30, end_lineno=8, end_col_offset=36, id='models', ctx=Load()),
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
                    end_col_offset=42,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=42, value='hr.holidays.summary.employee', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=59,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=11, col_offset=19, end_lineno=11, end_col_offset=59, value='HR Time Off Summary Report By Employee', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=103,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=13, id='date_from', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=16,
                        end_lineno=13,
                        end_col_offset=103,
                        func=Attribute(
                            lineno=13,
                            col_offset=16,
                            end_lineno=13,
                            end_col_offset=27,
                            value=Name(lineno=13, col_offset=16, end_lineno=13, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=28,
                                end_lineno=13,
                                end_col_offset=41,
                                arg='string',
                                value=Constant(lineno=13, col_offset=35, end_lineno=13, end_col_offset=41, value='From', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=43,
                                end_lineno=13,
                                end_col_offset=56,
                                arg='required',
                                value=Constant(lineno=13, col_offset=52, end_lineno=13, end_col_offset=56, value=True, kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=58,
                                end_lineno=13,
                                end_col_offset=102,
                                arg='default',
                                value=Lambda(
                                    lineno=13,
                                    col_offset=66,
                                    end_lineno=13,
                                    end_col_offset=102,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[],
                                        vararg=arg(lineno=13, col_offset=74, end_lineno=13, end_col_offset=75, arg='a', annotation=None, type_comment=None),
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        lineno=13,
                                        col_offset=77,
                                        end_lineno=13,
                                        end_col_offset=102,
                                        func=Attribute(
                                            lineno=13,
                                            col_offset=77,
                                            end_lineno=13,
                                            end_col_offset=90,
                                            value=Name(lineno=13, col_offset=77, end_lineno=13, end_col_offset=81, id='time', ctx=Load()),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=13, col_offset=91, end_lineno=13, end_col_offset=101, value='%Y-%m-01', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=102,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=7, id='emp', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=10,
                        end_lineno=14,
                        end_col_offset=102,
                        func=Attribute(
                            lineno=14,
                            col_offset=10,
                            end_lineno=14,
                            end_col_offset=26,
                            value=Name(lineno=14, col_offset=10, end_lineno=14, end_col_offset=16, id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=14, col_offset=27, end_lineno=14, end_col_offset=40, value='hr.employee', kind=None),
                            Constant(lineno=14, col_offset=42, end_lineno=14, end_col_offset=59, value='summary_emp_rel', kind=None),
                            Constant(lineno=14, col_offset=61, end_lineno=14, end_col_offset=69, value='sum_id', kind=None),
                            Constant(lineno=14, col_offset=71, end_lineno=14, end_col_offset=79, value='emp_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=81,
                                end_lineno=14,
                                end_col_offset=101,
                                arg='string',
                                value=Constant(lineno=14, col_offset=88, end_lineno=14, end_col_offset=101, value='Employee(s)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=72,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=16, id='holiday_type', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=19,
                        end_lineno=19,
                        end_col_offset=72,
                        func=Attribute(
                            lineno=15,
                            col_offset=19,
                            end_lineno=15,
                            end_col_offset=35,
                            value=Name(lineno=15, col_offset=19, end_lineno=15, end_col_offset=25, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                lineno=15,
                                col_offset=36,
                                end_lineno=19,
                                end_col_offset=5,
                                elts=[
                                    Tuple(
                                        lineno=16,
                                        col_offset=8,
                                        end_lineno=16,
                                        end_col_offset=32,
                                        elts=[
                                            Constant(lineno=16, col_offset=9, end_lineno=16, end_col_offset=19, value='Approved', kind=None),
                                            Constant(lineno=16, col_offset=21, end_lineno=16, end_col_offset=31, value='Approved', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=17,
                                        col_offset=8,
                                        end_lineno=17,
                                        end_col_offset=34,
                                        elts=[
                                            Constant(lineno=17, col_offset=9, end_lineno=17, end_col_offset=20, value='Confirmed', kind=None),
                                            Constant(lineno=17, col_offset=22, end_lineno=17, end_col_offset=33, value='Confirmed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=18,
                                        col_offset=8,
                                        end_lineno=18,
                                        end_col_offset=47,
                                        elts=[
                                            Constant(lineno=18, col_offset=9, end_lineno=18, end_col_offset=15, value='both', kind=None),
                                            Constant(lineno=18, col_offset=17, end_lineno=18, end_col_offset=46, value='Both Approved and Confirmed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                lineno=19,
                                col_offset=7,
                                end_lineno=19,
                                end_col_offset=36,
                                arg='string',
                                value=Constant(lineno=19, col_offset=14, end_lineno=19, end_col_offset=36, value='Select Time Off Type', kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=38,
                                end_lineno=19,
                                end_col_offset=51,
                                arg='required',
                                value=Constant(lineno=19, col_offset=47, end_lineno=19, end_col_offset=51, value=True, kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=53,
                                end_lineno=19,
                                end_col_offset=71,
                                arg='default',
                                value=Constant(lineno=19, col_offset=61, end_lineno=19, end_col_offset=71, value='Approved', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=31,
                    end_col_offset=109,
                    name='print_report',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=21, col_offset=21, end_lineno=21, end_col_offset=25, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=25,
                            value=Call(
                                lineno=22,
                                col_offset=8,
                                end_lineno=22,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=22,
                                    col_offset=8,
                                    end_lineno=22,
                                    end_col_offset=23,
                                    value=Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=28,
                            targets=[
                                List(
                                    lineno=23,
                                    col_offset=8,
                                    end_lineno=23,
                                    end_col_offset=14,
                                    elts=[Name(lineno=23, col_offset=9, end_lineno=23, end_col_offset=13, id='data', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=23,
                                col_offset=17,
                                end_lineno=23,
                                end_col_offset=28,
                                func=Attribute(
                                    lineno=23,
                                    col_offset=17,
                                    end_lineno=23,
                                    end_col_offset=26,
                                    value=Name(lineno=23, col_offset=17, end_lineno=23, end_col_offset=21, id='self', ctx=Load()),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=60,
                            targets=[
                                Subscript(
                                    lineno=24,
                                    col_offset=8,
                                    end_lineno=24,
                                    end_col_offset=19,
                                    value=Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=12, id='data', ctx=Load()),
                                    slice=Constant(lineno=24, col_offset=13, end_lineno=24, end_col_offset=18, value='emp', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=24,
                                col_offset=22,
                                end_lineno=24,
                                end_col_offset=60,
                                func=Attribute(
                                    lineno=24,
                                    col_offset=22,
                                    end_lineno=24,
                                    end_col_offset=42,
                                    value=Attribute(
                                        lineno=24,
                                        col_offset=22,
                                        end_lineno=24,
                                        end_col_offset=38,
                                        value=Attribute(
                                            lineno=24,
                                            col_offset=22,
                                            end_lineno=24,
                                            end_col_offset=30,
                                            value=Name(lineno=24, col_offset=22, end_lineno=24, end_col_offset=26, id='self', ctx=Load()),
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
                                    Constant(lineno=24, col_offset=43, end_lineno=24, end_col_offset=55, value='active_ids', kind=None),
                                    List(lineno=24, col_offset=57, end_lineno=24, end_col_offset=59, elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=63,
                            targets=[Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=17, id='employees', ctx=Store())],
                            value=Call(
                                lineno=25,
                                col_offset=20,
                                end_lineno=25,
                                end_col_offset=63,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=20,
                                    end_lineno=25,
                                    end_col_offset=50,
                                    value=Subscript(
                                        lineno=25,
                                        col_offset=20,
                                        end_lineno=25,
                                        end_col_offset=43,
                                        value=Attribute(
                                            lineno=25,
                                            col_offset=20,
                                            end_lineno=25,
                                            end_col_offset=28,
                                            value=Name(lineno=25, col_offset=20, end_lineno=25, end_col_offset=24, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=25, col_offset=29, end_lineno=25, end_col_offset=42, value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        lineno=25,
                                        col_offset=51,
                                        end_lineno=25,
                                        end_col_offset=62,
                                        value=Name(lineno=25, col_offset=51, end_lineno=25, end_col_offset=55, id='data', ctx=Load()),
                                        slice=Constant(lineno=25, col_offset=56, end_lineno=25, end_col_offset=61, value='emp', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=26,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=9,
                            targets=[Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=13, id='datas', ctx=Store())],
                            value=Dict(
                                lineno=26,
                                col_offset=16,
                                end_lineno=30,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=17, value='ids', kind=None),
                                    Constant(lineno=28, col_offset=12, end_lineno=28, end_col_offset=19, value='model', kind=None),
                                    Constant(lineno=29, col_offset=12, end_lineno=29, end_col_offset=18, value='form', kind=None),
                                ],
                                values=[
                                    List(lineno=27, col_offset=19, end_lineno=27, end_col_offset=21, elts=[], ctx=Load()),
                                    Constant(lineno=28, col_offset=21, end_lineno=28, end_col_offset=34, value='hr.employee', kind=None),
                                    Name(lineno=29, col_offset=20, end_lineno=29, end_col_offset=24, id='data', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=109,
                            value=Call(
                                lineno=31,
                                col_offset=15,
                                end_lineno=31,
                                end_col_offset=109,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=15,
                                    end_lineno=31,
                                    end_col_offset=86,
                                    value=Call(
                                        lineno=31,
                                        col_offset=15,
                                        end_lineno=31,
                                        end_col_offset=72,
                                        func=Attribute(
                                            lineno=31,
                                            col_offset=15,
                                            end_lineno=31,
                                            end_col_offset=27,
                                            value=Attribute(
                                                lineno=31,
                                                col_offset=15,
                                                end_lineno=31,
                                                end_col_offset=23,
                                                value=Name(lineno=31, col_offset=15, end_lineno=31, end_col_offset=19, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=31, col_offset=28, end_lineno=31, end_col_offset=71, value='hr_holidays.action_report_holidayssummary', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='report_action',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=31, col_offset=87, end_lineno=31, end_col_offset=96, id='employees', ctx=Load())],
                                keywords=[
                                    keyword(
                                        lineno=31,
                                        col_offset=98,
                                        end_lineno=31,
                                        end_col_offset=108,
                                        arg='data',
                                        value=Name(lineno=31, col_offset=103, end_lineno=31, end_col_offset=108, id='datas', ctx=Load()),
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
