Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=20,
            end_col_offset=59,
            name='User',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=11,
                    end_lineno=7,
                    end_col_offset=23,
                    value=Name(lineno=7, col_offset=11, end_lineno=7, end_col_offset=17, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=28,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=List(
                        lineno=8,
                        col_offset=15,
                        end_lineno=8,
                        end_col_offset=28,
                        elts=[Constant(lineno=8, col_offset=16, end_lineno=8, end_col_offset=27, value='res.users', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=83,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=23, id='employee_cars_count', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=26,
                        end_lineno=10,
                        end_col_offset=83,
                        func=Attribute(
                            lineno=10,
                            col_offset=26,
                            end_lineno=10,
                            end_col_offset=40,
                            value=Name(lineno=10, col_offset=26, end_lineno=10, end_col_offset=32, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=41,
                                end_lineno=10,
                                end_col_offset=82,
                                arg='related',
                                value=Constant(lineno=10, col_offset=49, end_lineno=10, end_col_offset=82, value='employee_id.employee_cars_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=69,
                    name='SELF_READABLE_FIELDS',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=29, end_lineno=13, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=69,
                            value=BinOp(
                                lineno=14,
                                col_offset=15,
                                end_lineno=14,
                                end_col_offset=69,
                                left=Attribute(
                                    lineno=14,
                                    col_offset=15,
                                    end_lineno=14,
                                    end_col_offset=43,
                                    value=Call(
                                        lineno=14,
                                        col_offset=15,
                                        end_lineno=14,
                                        end_col_offset=22,
                                        func=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=20, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='SELF_READABLE_FIELDS',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=List(
                                    lineno=14,
                                    col_offset=46,
                                    end_lineno=14,
                                    end_col_offset=69,
                                    elts=[Constant(lineno=14, col_offset=47, end_lineno=14, end_col_offset=68, value='employee_cars_count', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(lineno=12, col_offset=5, end_lineno=12, end_col_offset=13, id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=57,
                    name='action_get_claim_report',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=32, end_lineno=16, end_col_offset=36, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=57,
                            value=Call(
                                lineno=17,
                                col_offset=15,
                                end_lineno=17,
                                end_col_offset=57,
                                func=Attribute(
                                    lineno=17,
                                    col_offset=15,
                                    end_lineno=17,
                                    end_col_offset=55,
                                    value=Attribute(
                                        lineno=17,
                                        col_offset=15,
                                        end_lineno=17,
                                        end_col_offset=31,
                                        value=Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=19, id='self', ctx=Load()),
                                        attr='employee_id',
                                        ctx=Load(),
                                    ),
                                    attr='action_get_claim_report',
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
                FunctionDef(
                    lineno=19,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=59,
                    name='action_open_employee_cars',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=19, col_offset=34, end_lineno=19, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=59,
                            value=Call(
                                lineno=20,
                                col_offset=15,
                                end_lineno=20,
                                end_col_offset=59,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=15,
                                    end_lineno=20,
                                    end_col_offset=57,
                                    value=Attribute(
                                        lineno=20,
                                        col_offset=15,
                                        end_lineno=20,
                                        end_col_offset=31,
                                        value=Name(lineno=20, col_offset=15, end_lineno=20, end_col_offset=19, id='self', ctx=Load()),
                                        attr='employee_id',
                                        ctx=Load(),
                                    ),
                                    attr='action_open_employee_cars',
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