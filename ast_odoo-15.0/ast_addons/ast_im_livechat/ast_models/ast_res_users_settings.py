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
            end_lineno=10,
            end_col_offset=105,
            name='ResUsersSettings',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=23,
                    end_lineno=7,
                    end_col_offset=35,
                    value=Name(lineno=7, col_offset=23, end_lineno=7, end_col_offset=29, id='models', ctx=Load()),
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
                    end_col_offset=35,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=35, value='res.users.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=105,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=45, id='is_discuss_sidebar_category_livechat_open', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=48,
                        end_lineno=10,
                        end_col_offset=105,
                        func=Attribute(
                            lineno=10,
                            col_offset=48,
                            end_lineno=10,
                            end_col_offset=62,
                            value=Name(lineno=10, col_offset=48, end_lineno=10, end_col_offset=54, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=63, end_lineno=10, end_col_offset=90, value='Is category livechat open', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=92,
                                end_lineno=10,
                                end_col_offset=104,
                                arg='default',
                                value=Constant(lineno=10, col_offset=100, end_lineno=10, end_col_offset=104, value=True, kind=None),
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
