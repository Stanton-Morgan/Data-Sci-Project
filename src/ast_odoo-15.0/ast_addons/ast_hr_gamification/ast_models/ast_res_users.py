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
            end_lineno=11,
            end_col_offset=69,
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
                    end_lineno=10,
                    end_col_offset=62,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=12, id='goal_ids', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=15,
                        end_lineno=10,
                        end_col_offset=62,
                        func=Attribute(
                            lineno=10,
                            col_offset=15,
                            end_lineno=10,
                            end_col_offset=30,
                            value=Name(lineno=10, col_offset=15, end_lineno=10, end_col_offset=21, id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=10, col_offset=31, end_lineno=10, end_col_offset=50, value='gamification.goal', kind=None),
                            Constant(lineno=10, col_offset=52, end_lineno=10, end_col_offset=61, value='user_id', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=69,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=13, id='badge_ids', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=16,
                        end_lineno=11,
                        end_col_offset=69,
                        func=Attribute(
                            lineno=11,
                            col_offset=16,
                            end_lineno=11,
                            end_col_offset=31,
                            value=Name(lineno=11, col_offset=16, end_lineno=11, end_col_offset=22, id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=11, col_offset=32, end_lineno=11, end_col_offset=57, value='gamification.badge.user', kind=None),
                            Constant(lineno=11, col_offset=59, end_lineno=11, end_col_offset=68, value='user_id', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)