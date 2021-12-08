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
            end_lineno=14,
            end_col_offset=59,
            name='ResUsers',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=15,
                    end_lineno=7,
                    end_col_offset=27,
                    value=Name(lineno=7, col_offset=15, end_lineno=7, end_col_offset=21, id='models', ctx=Load()),
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
                    end_col_offset=26,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=26, value='res.users', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=52,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=16, id='resource_ids', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=19,
                        end_lineno=11,
                        end_col_offset=52,
                        func=Attribute(
                            lineno=10,
                            col_offset=19,
                            end_lineno=10,
                            end_col_offset=34,
                            value=Name(lineno=10, col_offset=19, end_lineno=10, end_col_offset=25, id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=11, col_offset=8, end_lineno=11, end_col_offset=27, value='resource.resource', kind=None),
                            Constant(lineno=11, col_offset=29, end_lineno=11, end_col_offset=38, value='user_id', kind=None),
                            Constant(lineno=11, col_offset=40, end_lineno=11, end_col_offset=51, value='Resources', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=59,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=24, id='resource_calendar_id', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=27,
                        end_lineno=14,
                        end_col_offset=59,
                        func=Attribute(
                            lineno=12,
                            col_offset=27,
                            end_lineno=12,
                            end_col_offset=42,
                            value=Name(lineno=12, col_offset=27, end_lineno=12, end_col_offset=33, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=13, col_offset=8, end_lineno=13, end_col_offset=27, value='resource.calendar', kind=None),
                            Constant(lineno=13, col_offset=29, end_lineno=13, end_col_offset=52, value='Default Working Hours', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=42,
                                arg='related',
                                value=Constant(lineno=14, col_offset=16, end_lineno=14, end_col_offset=42, value='resource_ids.calendar_id', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=44,
                                end_lineno=14,
                                end_col_offset=58,
                                arg='readonly',
                                value=Constant(lineno=14, col_offset=53, end_lineno=14, end_col_offset=58, value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)