Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=45,
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=11,
            end_col_offset=152,
            name='TestUpdateNotification',
            bases=[Name(lineno=5, col_offset=29, end_lineno=5, end_col_offset=44, id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=6,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=152,
                    name='test_user_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=6, col_offset=24, end_lineno=6, end_col_offset=28, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=7,
                            col_offset=8,
                            end_lineno=7,
                            end_col_offset=105,
                            targets=[Name(lineno=7, col_offset=8, end_lineno=7, end_col_offset=16, id='ping_msg', ctx=Store())],
                            value=Call(
                                lineno=7,
                                col_offset=19,
                                end_lineno=7,
                                end_col_offset=105,
                                func=Attribute(
                                    lineno=7,
                                    col_offset=19,
                                    end_lineno=7,
                                    end_col_offset=103,
                                    value=Call(
                                        lineno=7,
                                        col_offset=19,
                                        end_lineno=7,
                                        end_col_offset=90,
                                        func=Attribute(
                                            lineno=7,
                                            col_offset=19,
                                            end_lineno=7,
                                            end_col_offset=71,
                                            value=Subscript(
                                                lineno=7,
                                                col_offset=19,
                                                end_lineno=7,
                                                end_col_offset=58,
                                                value=Attribute(
                                                    lineno=7,
                                                    col_offset=19,
                                                    end_lineno=7,
                                                    end_col_offset=27,
                                                    value=Name(lineno=7, col_offset=19, end_lineno=7, end_col_offset=23, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=7, col_offset=28, end_lineno=7, end_col_offset=57, value='publisher_warranty.contract', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                lineno=7,
                                                col_offset=72,
                                                end_lineno=7,
                                                end_col_offset=89,
                                                arg='active_test',
                                                value=Constant(lineno=7, col_offset=84, end_lineno=7, end_col_offset=89, value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='_get_message',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=8,
                            col_offset=8,
                            end_lineno=8,
                            end_col_offset=80,
                            targets=[Name(lineno=8, col_offset=8, end_lineno=8, end_col_offset=18, id='user_count', ctx=Store())],
                            value=Call(
                                lineno=8,
                                col_offset=21,
                                end_lineno=8,
                                end_col_offset=80,
                                func=Attribute(
                                    lineno=8,
                                    col_offset=21,
                                    end_lineno=8,
                                    end_col_offset=55,
                                    value=Subscript(
                                        lineno=8,
                                        col_offset=21,
                                        end_lineno=8,
                                        end_col_offset=42,
                                        value=Attribute(
                                            lineno=8,
                                            col_offset=21,
                                            end_lineno=8,
                                            end_col_offset=29,
                                            value=Name(lineno=8, col_offset=21, end_lineno=8, end_col_offset=25, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=8, col_offset=30, end_lineno=8, end_col_offset=41, value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=8,
                                        col_offset=56,
                                        end_lineno=8,
                                        end_col_offset=79,
                                        elts=[
                                            Tuple(
                                                lineno=8,
                                                col_offset=57,
                                                end_lineno=8,
                                                end_col_offset=78,
                                                elts=[
                                                    Constant(lineno=8, col_offset=58, end_lineno=8, end_col_offset=66, value='active', kind=None),
                                                    Constant(lineno=8, col_offset=68, end_lineno=8, end_col_offset=71, value='=', kind=None),
                                                    Constant(lineno=8, col_offset=73, end_lineno=8, end_col_offset=77, value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=9,
                            col_offset=8,
                            end_lineno=9,
                            end_col_offset=133,
                            value=Call(
                                lineno=9,
                                col_offset=8,
                                end_lineno=9,
                                end_col_offset=133,
                                func=Attribute(
                                    lineno=9,
                                    col_offset=8,
                                    end_lineno=9,
                                    end_col_offset=24,
                                    value=Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=9,
                                        col_offset=25,
                                        end_lineno=9,
                                        end_col_offset=50,
                                        func=Attribute(
                                            lineno=9,
                                            col_offset=25,
                                            end_lineno=9,
                                            end_col_offset=37,
                                            value=Name(lineno=9, col_offset=25, end_lineno=9, end_col_offset=33, id='ping_msg', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=9, col_offset=38, end_lineno=9, end_col_offset=49, value='nbr_users', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(lineno=9, col_offset=52, end_lineno=9, end_col_offset=62, id='user_count', ctx=Load()),
                                    Constant(lineno=9, col_offset=64, end_lineno=9, end_col_offset=132, value='Update Notification: Users count is badly computed in ping message', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=10,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=108,
                            targets=[Name(lineno=10, col_offset=8, end_lineno=10, end_col_offset=24, id='share_user_count', ctx=Store())],
                            value=Call(
                                lineno=10,
                                col_offset=27,
                                end_lineno=10,
                                end_col_offset=108,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=27,
                                    end_lineno=10,
                                    end_col_offset=61,
                                    value=Subscript(
                                        lineno=10,
                                        col_offset=27,
                                        end_lineno=10,
                                        end_col_offset=48,
                                        value=Attribute(
                                            lineno=10,
                                            col_offset=27,
                                            end_lineno=10,
                                            end_col_offset=35,
                                            value=Name(lineno=10, col_offset=27, end_lineno=10, end_col_offset=31, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=10, col_offset=36, end_lineno=10, end_col_offset=47, value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=10,
                                        col_offset=62,
                                        end_lineno=10,
                                        end_col_offset=107,
                                        elts=[
                                            Tuple(
                                                lineno=10,
                                                col_offset=63,
                                                end_lineno=10,
                                                end_col_offset=84,
                                                elts=[
                                                    Constant(lineno=10, col_offset=64, end_lineno=10, end_col_offset=72, value='active', kind=None),
                                                    Constant(lineno=10, col_offset=74, end_lineno=10, end_col_offset=77, value='=', kind=None),
                                                    Constant(lineno=10, col_offset=79, end_lineno=10, end_col_offset=83, value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=10,
                                                col_offset=86,
                                                end_lineno=10,
                                                end_col_offset=106,
                                                elts=[
                                                    Constant(lineno=10, col_offset=87, end_lineno=10, end_col_offset=94, value='share', kind=None),
                                                    Constant(lineno=10, col_offset=96, end_lineno=10, end_col_offset=99, value='=', kind=None),
                                                    Constant(lineno=10, col_offset=101, end_lineno=10, end_col_offset=105, value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=152,
                            value=Call(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=152,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=8,
                                    end_lineno=11,
                                    end_col_offset=24,
                                    value=Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=11,
                                        col_offset=25,
                                        end_lineno=11,
                                        end_col_offset=56,
                                        func=Attribute(
                                            lineno=11,
                                            col_offset=25,
                                            end_lineno=11,
                                            end_col_offset=37,
                                            value=Name(lineno=11, col_offset=25, end_lineno=11, end_col_offset=33, id='ping_msg', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=11, col_offset=38, end_lineno=11, end_col_offset=55, value='nbr_share_users', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(lineno=11, col_offset=58, end_lineno=11, end_col_offset=74, id='share_user_count', ctx=Load()),
                                    Constant(lineno=11, col_offset=76, end_lineno=11, end_col_offset=151, value='Update Notification: Portal Users count is badly computed in ping message', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
