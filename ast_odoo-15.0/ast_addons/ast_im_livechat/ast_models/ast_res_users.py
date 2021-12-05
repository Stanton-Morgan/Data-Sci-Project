Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=21,
            end_col_offset=68,
            name='Users',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=12,
                    end_lineno=7,
                    end_col_offset=24,
                    value=Name(lineno=7, col_offset=12, end_lineno=7, end_col_offset=18, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    lineno=8,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=7,
                    value=Constant(lineno=8, col_offset=4, end_lineno=10, end_col_offset=7, value=' Update of res.users class\n        - add a preference about username for livechat purpose\n    ', kind=None),
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=26,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=11, col_offset=15, end_lineno=11, end_col_offset=26, value='res.users', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=130,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=21, id='livechat_username', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=24,
                        end_lineno=13,
                        end_col_offset=130,
                        func=Attribute(
                            lineno=13,
                            col_offset=24,
                            end_lineno=13,
                            end_col_offset=35,
                            value=Name(lineno=13, col_offset=24, end_lineno=13, end_col_offset=30, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=36, end_lineno=13, end_col_offset=55, value='Livechat Username', kind=None)],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=57,
                                end_lineno=13,
                                end_col_offset=129,
                                arg='help',
                                value=Constant(lineno=13, col_offset=62, end_lineno=13, end_col_offset=129, value='This username will be used as your name in the livechat channels.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=67,
                    name='SELF_READABLE_FIELDS',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=29, end_lineno=16, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=67,
                            value=BinOp(
                                lineno=17,
                                col_offset=15,
                                end_lineno=17,
                                end_col_offset=67,
                                left=Attribute(
                                    lineno=17,
                                    col_offset=15,
                                    end_lineno=17,
                                    end_col_offset=43,
                                    value=Call(
                                        lineno=17,
                                        col_offset=15,
                                        end_lineno=17,
                                        end_col_offset=22,
                                        func=Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=20, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='SELF_READABLE_FIELDS',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=List(
                                    lineno=17,
                                    col_offset=46,
                                    end_lineno=17,
                                    end_col_offset=67,
                                    elts=[Constant(lineno=17, col_offset=47, end_lineno=17, end_col_offset=66, value='livechat_username', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(lineno=15, col_offset=5, end_lineno=15, end_col_offset=13, id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=20,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=68,
                    name='SELF_WRITEABLE_FIELDS',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=20, col_offset=30, end_lineno=20, end_col_offset=34, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=68,
                            value=BinOp(
                                lineno=21,
                                col_offset=15,
                                end_lineno=21,
                                end_col_offset=68,
                                left=Attribute(
                                    lineno=21,
                                    col_offset=15,
                                    end_lineno=21,
                                    end_col_offset=44,
                                    value=Call(
                                        lineno=21,
                                        col_offset=15,
                                        end_lineno=21,
                                        end_col_offset=22,
                                        func=Name(lineno=21, col_offset=15, end_lineno=21, end_col_offset=20, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='SELF_WRITEABLE_FIELDS',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=List(
                                    lineno=21,
                                    col_offset=47,
                                    end_lineno=21,
                                    end_col_offset=68,
                                    elts=[Constant(lineno=21, col_offset=48, end_lineno=21, end_col_offset=67, value='livechat_username', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(lineno=19, col_offset=5, end_lineno=19, end_col_offset=13, id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
