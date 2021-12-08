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
            end_lineno=12,
            end_col_offset=42,
            name='Challenge',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=16,
                    end_lineno=7,
                    end_col_offset=28,
                    value=Name(lineno=7, col_offset=16, end_lineno=7, end_col_offset=22, id='models', ctx=Load()),
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
                    end_col_offset=39,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=39, value='gamification.challenge', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=42,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=22, id='challenge_category', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=25,
                        end_lineno=12,
                        end_col_offset=42,
                        func=Attribute(
                            lineno=10,
                            col_offset=25,
                            end_lineno=10,
                            end_col_offset=41,
                            value=Name(lineno=10, col_offset=25, end_lineno=10, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=42,
                                end_lineno=12,
                                end_col_offset=5,
                                arg='selection_add',
                                value=List(
                                    lineno=10,
                                    col_offset=56,
                                    end_lineno=12,
                                    end_col_offset=5,
                                    elts=[
                                        Tuple(
                                            lineno=11,
                                            col_offset=8,
                                            end_lineno=11,
                                            end_col_offset=38,
                                            elts=[
                                                Constant(lineno=11, col_offset=9, end_lineno=11, end_col_offset=17, value='slides', kind=None),
                                                Constant(lineno=11, col_offset=19, end_lineno=11, end_col_offset=37, value='Website / Slides', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=7,
                                end_lineno=12,
                                end_col_offset=41,
                                arg='ondelete',
                                value=Dict(
                                    lineno=12,
                                    col_offset=16,
                                    end_lineno=12,
                                    end_col_offset=41,
                                    keys=[Constant(lineno=12, col_offset=17, end_lineno=12, end_col_offset=25, value='slides', kind=None)],
                                    values=[Constant(lineno=12, col_offset=27, end_lineno=12, end_col_offset=40, value='set default', kind=None)],
                                ),
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