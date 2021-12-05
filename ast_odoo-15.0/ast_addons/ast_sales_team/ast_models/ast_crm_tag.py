Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=26,
            module='random',
            names=[alias(name='randint', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=21,
            end_col_offset=5,
            name='Tag',
            bases=[
                Attribute(
                    lineno=9,
                    col_offset=10,
                    end_lineno=9,
                    end_col_offset=22,
                    value=Name(lineno=9, col_offset=10, end_lineno=9, end_col_offset=16, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=21,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=21, value='crm.tag', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=28,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=11, col_offset=19, end_lineno=11, end_col_offset=28, value='CRM Tag', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=29,
                    name='_get_default_color',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=27, end_lineno=13, end_col_offset=31, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=29,
                            value=Call(
                                lineno=14,
                                col_offset=15,
                                end_lineno=14,
                                end_col_offset=29,
                                func=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=22, id='randint', ctx=Load()),
                                args=[
                                    Constant(lineno=14, col_offset=23, end_lineno=14, end_col_offset=24, value=1, kind=None),
                                    Constant(lineno=14, col_offset=26, end_lineno=14, end_col_offset=28, value=11, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=65,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=11,
                        end_lineno=16,
                        end_col_offset=65,
                        func=Attribute(
                            lineno=16,
                            col_offset=11,
                            end_lineno=16,
                            end_col_offset=22,
                            value=Name(lineno=16, col_offset=11, end_lineno=16, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=16, col_offset=23, end_lineno=16, end_col_offset=33, value='Tag Name', kind=None)],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=35,
                                end_lineno=16,
                                end_col_offset=48,
                                arg='required',
                                value=Constant(lineno=16, col_offset=44, end_lineno=16, end_col_offset=48, value=True, kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=50,
                                end_lineno=16,
                                end_col_offset=64,
                                arg='translate',
                                value=Constant(lineno=16, col_offset=60, end_lineno=16, end_col_offset=64, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=63,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=9, id='color', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=12,
                        end_lineno=17,
                        end_col_offset=63,
                        func=Attribute(
                            lineno=17,
                            col_offset=12,
                            end_lineno=17,
                            end_col_offset=26,
                            value=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=27, end_lineno=17, end_col_offset=34, value='Color', kind=None)],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=36,
                                end_lineno=17,
                                end_col_offset=62,
                                arg='default',
                                value=Name(lineno=17, col_offset=44, end_lineno=17, end_col_offset=62, id='_get_default_color', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=5,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=20, id='_sql_constraints', ctx=Store())],
                    value=List(
                        lineno=19,
                        col_offset=23,
                        end_lineno=21,
                        end_col_offset=5,
                        elts=[
                            Tuple(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=67,
                                elts=[
                                    Constant(lineno=20, col_offset=9, end_lineno=20, end_col_offset=20, value='name_uniq', kind=None),
                                    Constant(lineno=20, col_offset=22, end_lineno=20, end_col_offset=37, value='unique (name)', kind=None),
                                    Constant(lineno=20, col_offset=39, end_lineno=20, end_col_offset=66, value='Tag name already exists !', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
