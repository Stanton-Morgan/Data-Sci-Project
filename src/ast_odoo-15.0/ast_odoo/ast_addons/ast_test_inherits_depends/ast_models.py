Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
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
            end_lineno=10,
            end_col_offset=31,
            name='Unit',
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
                    end_col_offset=26,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=26, value='test.unit', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=31,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=15, id='second_name', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=18,
                        end_lineno=10,
                        end_col_offset=31,
                        func=Attribute(
                            lineno=10,
                            col_offset=18,
                            end_lineno=10,
                            end_col_offset=29,
                            value=Name(lineno=10, col_offset=18, end_lineno=10, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
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