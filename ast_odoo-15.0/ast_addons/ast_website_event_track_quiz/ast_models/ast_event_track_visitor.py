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
            end_lineno=12,
            end_col_offset=58,
            name='TrackVisitor',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=19,
                    end_lineno=7,
                    end_col_offset=31,
                    value=Name(lineno=7, col_offset=19, end_lineno=7, end_col_offset=25, id='models', ctx=Load()),
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
                    end_col_offset=33,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=33, value='event.track.visitor', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=38,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=List(
                        lineno=9,
                        col_offset=15,
                        end_lineno=9,
                        end_col_offset=38,
                        elts=[Constant(lineno=9, col_offset=16, end_lineno=9, end_col_offset=37, value='event.track.visitor', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=48,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=18, id='quiz_completed', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=21,
                        end_lineno=11,
                        end_col_offset=48,
                        func=Attribute(
                            lineno=11,
                            col_offset=21,
                            end_lineno=11,
                            end_col_offset=35,
                            value=Name(lineno=11, col_offset=21, end_lineno=11, end_col_offset=27, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=36, end_lineno=11, end_col_offset=47, value='Completed', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=58,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=15, id='quiz_points', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=18,
                        end_lineno=12,
                        end_col_offset=58,
                        func=Attribute(
                            lineno=12,
                            col_offset=18,
                            end_lineno=12,
                            end_col_offset=32,
                            value=Name(lineno=12, col_offset=18, end_lineno=12, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=33, end_lineno=12, end_col_offset=46, value='Quiz Points', kind=None)],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=48,
                                end_lineno=12,
                                end_col_offset=57,
                                arg='default',
                                value=Constant(lineno=12, col_offset=56, end_lineno=12, end_col_offset=57, value=0, kind=None),
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
