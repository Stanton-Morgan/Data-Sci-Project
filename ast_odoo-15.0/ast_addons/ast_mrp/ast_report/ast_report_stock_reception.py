Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=34,
            module='odoo.tools',
            names=[alias(name='format_date', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=14,
            end_col_offset=60,
            name='ReceptionReport',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=22,
                    end_lineno=8,
                    end_col_offset=42,
                    value=Name(lineno=8, col_offset=22, end_lineno=8, end_col_offset=28, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=46,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=46, value='report.stock.report_reception', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=60,
                    name='_get_formatted_scheduled_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=11, col_offset=38, end_lineno=11, end_col_offset=42, arg='self', annotation=None, type_comment=None),
                            arg(lineno=11, col_offset=44, end_lineno=11, end_col_offset=50, arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            lineno=12,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=67,
                            test=Compare(
                                lineno=12,
                                col_offset=11,
                                end_lineno=12,
                                end_col_offset=43,
                                left=Attribute(
                                    lineno=12,
                                    col_offset=11,
                                    end_lineno=12,
                                    end_col_offset=23,
                                    value=Name(lineno=12, col_offset=11, end_lineno=12, end_col_offset=17, id='source', ctx=Load()),
                                    attr='_name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(lineno=12, col_offset=27, end_lineno=12, end_col_offset=43, value='mrp.production', kind=None)],
                            ),
                            body=[
                                Return(
                                    lineno=13,
                                    col_offset=12,
                                    end_lineno=13,
                                    end_col_offset=67,
                                    value=Call(
                                        lineno=13,
                                        col_offset=19,
                                        end_lineno=13,
                                        end_col_offset=67,
                                        func=Name(lineno=13, col_offset=19, end_lineno=13, end_col_offset=30, id='format_date', ctx=Load()),
                                        args=[
                                            Attribute(
                                                lineno=13,
                                                col_offset=31,
                                                end_lineno=13,
                                                end_col_offset=39,
                                                value=Name(lineno=13, col_offset=31, end_lineno=13, end_col_offset=35, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=13,
                                                col_offset=41,
                                                end_lineno=13,
                                                end_col_offset=66,
                                                value=Name(lineno=13, col_offset=41, end_lineno=13, end_col_offset=47, id='source', ctx=Load()),
                                                attr='date_planned_start',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=60,
                            value=Call(
                                lineno=14,
                                col_offset=15,
                                end_lineno=14,
                                end_col_offset=60,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=15,
                                    end_lineno=14,
                                    end_col_offset=52,
                                    value=Call(
                                        lineno=14,
                                        col_offset=15,
                                        end_lineno=14,
                                        end_col_offset=22,
                                        func=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=20, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_formatted_scheduled_date',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=14, col_offset=53, end_lineno=14, end_col_offset=59, id='source', ctx=Load())],
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