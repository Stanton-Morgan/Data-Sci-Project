Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=26,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=18,
            end_col_offset=9,
            name='HrEmployee',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=17,
                    end_lineno=6,
                    end_col_offset=29,
                    value=Name(lineno=6, col_offset=17, end_lineno=6, end_col_offset=23, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=28,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=28, value='hr.employee', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=9,
                    name='action_open_work_entries',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=33, end_lineno=9, end_col_offset=37, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=10,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=25,
                            value=Call(
                                lineno=10,
                                col_offset=8,
                                end_lineno=10,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=8,
                                    end_lineno=10,
                                    end_col_offset=23,
                                    value=Name(lineno=10, col_offset=8, end_lineno=10, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=11,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=9,
                            value=Dict(
                                lineno=11,
                                col_offset=15,
                                end_lineno=18,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=12, col_offset=12, end_lineno=12, end_col_offset=18, value='type', kind=None),
                                    Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=18, value='name', kind=None),
                                    Constant(lineno=14, col_offset=12, end_lineno=14, end_col_offset=23, value='view_mode', kind=None),
                                    Constant(lineno=15, col_offset=12, end_lineno=15, end_col_offset=23, value='res_model', kind=None),
                                    Constant(lineno=16, col_offset=12, end_lineno=16, end_col_offset=21, value='context', kind=None),
                                    Constant(lineno=17, col_offset=12, end_lineno=17, end_col_offset=20, value='domain', kind=None),
                                ],
                                values=[
                                    Constant(lineno=12, col_offset=20, end_lineno=12, end_col_offset=43, value='ir.actions.act_window', kind=None),
                                    Call(
                                        lineno=13,
                                        col_offset=20,
                                        end_lineno=13,
                                        end_col_offset=59,
                                        func=Name(lineno=13, col_offset=20, end_lineno=13, end_col_offset=21, id='_', ctx=Load()),
                                        args=[
                                            Constant(lineno=13, col_offset=22, end_lineno=13, end_col_offset=39, value='%s work entries', kind=None),
                                            Attribute(
                                                lineno=13,
                                                col_offset=41,
                                                end_lineno=13,
                                                end_col_offset=58,
                                                value=Name(lineno=13, col_offset=41, end_lineno=13, end_col_offset=45, id='self', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(lineno=14, col_offset=25, end_lineno=14, end_col_offset=51, value='calendar,gantt,tree,form', kind=None),
                                    Constant(lineno=15, col_offset=25, end_lineno=15, end_col_offset=40, value='hr.work.entry', kind=None),
                                    Dict(
                                        lineno=16,
                                        col_offset=23,
                                        end_lineno=16,
                                        end_col_offset=55,
                                        keys=[Constant(lineno=16, col_offset=24, end_lineno=16, end_col_offset=45, value='default_employee_id', kind=None)],
                                        values=[
                                            Attribute(
                                                lineno=16,
                                                col_offset=47,
                                                end_lineno=16,
                                                end_col_offset=54,
                                                value=Name(lineno=16, col_offset=47, end_lineno=16, end_col_offset=51, id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    List(
                                        lineno=17,
                                        col_offset=22,
                                        end_lineno=17,
                                        end_col_offset=53,
                                        elts=[
                                            Tuple(
                                                lineno=17,
                                                col_offset=23,
                                                end_lineno=17,
                                                end_col_offset=52,
                                                elts=[
                                                    Constant(lineno=17, col_offset=24, end_lineno=17, end_col_offset=37, value='employee_id', kind=None),
                                                    Constant(lineno=17, col_offset=39, end_lineno=17, end_col_offset=42, value='=', kind=None),
                                                    Attribute(
                                                        lineno=17,
                                                        col_offset=44,
                                                        end_lineno=17,
                                                        end_col_offset=51,
                                                        value=Name(lineno=17, col_offset=44, end_lineno=17, end_col_offset=48, id='self', ctx=Load()),
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
