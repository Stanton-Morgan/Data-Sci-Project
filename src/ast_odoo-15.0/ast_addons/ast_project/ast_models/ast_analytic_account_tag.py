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
            lineno=6,
            col_offset=0,
            end_lineno=9,
            end_col_offset=63,
            name='AccountAnalyticTag',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=25,
                    end_lineno=6,
                    end_col_offset=37,
                    value=Name(lineno=6, col_offset=25, end_lineno=6, end_col_offset=31, id='models', ctx=Load()),
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
                    end_col_offset=37,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=37, value='account.analytic.tag', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=63,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='task_ids', ctx=Store())],
                    value=Call(
                        lineno=9,
                        col_offset=15,
                        end_lineno=9,
                        end_col_offset=63,
                        func=Attribute(
                            lineno=9,
                            col_offset=15,
                            end_lineno=9,
                            end_col_offset=31,
                            value=Name(lineno=9, col_offset=15, end_lineno=9, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=9, col_offset=32, end_lineno=9, end_col_offset=46, value='project.task', kind=None)],
                        keywords=[
                            keyword(
                                lineno=9,
                                col_offset=48,
                                end_lineno=9,
                                end_col_offset=62,
                                arg='string',
                                value=Constant(lineno=9, col_offset=55, end_lineno=9, end_col_offset=62, value='Tasks', kind=None),
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