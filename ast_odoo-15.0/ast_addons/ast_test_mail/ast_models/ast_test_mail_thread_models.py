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
            lineno=7,
            col_offset=0,
            end_lineno=12,
            end_col_offset=24,
            name='MailTestCC',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=17,
                    end_lineno=7,
                    end_col_offset=29,
                    value=Name(lineno=7, col_offset=17, end_lineno=7, end_col_offset=23, id='models', ctx=Load()),
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
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=26, value='mail.test.cc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=41,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=41, value='Test Email CC Thread', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=33,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=List(
                        lineno=10,
                        col_offset=15,
                        end_lineno=10,
                        end_col_offset=33,
                        elts=[Constant(lineno=10, col_offset=16, end_lineno=10, end_col_offset=32, value='mail.thread.cc', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=24,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=11,
                        end_lineno=12,
                        end_col_offset=24,
                        func=Attribute(
                            lineno=12,
                            col_offset=11,
                            end_lineno=12,
                            end_col_offset=22,
                            value=Name(lineno=12, col_offset=11, end_lineno=12, end_col_offset=17, id='fields', ctx=Load()),
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
