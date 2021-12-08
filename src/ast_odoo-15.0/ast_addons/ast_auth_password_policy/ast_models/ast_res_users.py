Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=37,
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=33,
            end_col_offset=52,
            name='ResUsers',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=15,
                    end_lineno=6,
                    end_col_offset=27,
                    value=Name(lineno=6, col_offset=15, end_lineno=6, end_col_offset=21, id='models', ctx=Load()),
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
                    end_col_offset=26,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=26, value='res.users', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=9,
                    name='get_password_policy',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=28, end_lineno=10, end_col_offset=32, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=55,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=14, id='params', ctx=Store())],
                            value=Call(
                                lineno=11,
                                col_offset=17,
                                end_lineno=11,
                                end_col_offset=55,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=17,
                                    end_lineno=11,
                                    end_col_offset=53,
                                    value=Subscript(
                                        lineno=11,
                                        col_offset=17,
                                        end_lineno=11,
                                        end_col_offset=48,
                                        value=Attribute(
                                            lineno=11,
                                            col_offset=17,
                                            end_lineno=11,
                                            end_col_offset=25,
                                            value=Name(lineno=11, col_offset=17, end_lineno=11, end_col_offset=21, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=11, col_offset=26, end_lineno=11, end_col_offset=47, value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=12,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=9,
                            value=Dict(
                                lineno=12,
                                col_offset=15,
                                end_lineno=14,
                                end_col_offset=9,
                                keys=[Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=23, value='minlength', kind=None)],
                                values=[
                                    Call(
                                        lineno=13,
                                        col_offset=25,
                                        end_lineno=13,
                                        end_col_offset=91,
                                        func=Name(lineno=13, col_offset=25, end_lineno=13, end_col_offset=28, id='int', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=13,
                                                col_offset=29,
                                                end_lineno=13,
                                                end_col_offset=90,
                                                func=Attribute(
                                                    lineno=13,
                                                    col_offset=29,
                                                    end_lineno=13,
                                                    end_col_offset=45,
                                                    value=Name(lineno=13, col_offset=29, end_lineno=13, end_col_offset=35, id='params', ctx=Load()),
                                                    attr='get_param',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(lineno=13, col_offset=46, end_lineno=13, end_col_offset=78, value='auth_password_policy.minlength', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        lineno=13,
                                                        col_offset=80,
                                                        end_lineno=13,
                                                        end_col_offset=89,
                                                        arg='default',
                                                        value=Constant(lineno=13, col_offset=88, end_lineno=13, end_col_offset=89, value=0, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=9,
                            col_offset=5,
                            end_lineno=9,
                            end_col_offset=14,
                            value=Name(lineno=9, col_offset=5, end_lineno=9, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=45,
                    name='_set_password',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=22, end_lineno=16, end_col_offset=26, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=60,
                            value=Call(
                                lineno=17,
                                col_offset=8,
                                end_lineno=17,
                                end_col_offset=60,
                                func=Attribute(
                                    lineno=17,
                                    col_offset=8,
                                    end_lineno=17,
                                    end_col_offset=35,
                                    value=Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=12, id='self', ctx=Load()),
                                    attr='_check_password_policy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=17,
                                        col_offset=36,
                                        end_lineno=17,
                                        end_col_offset=59,
                                        func=Attribute(
                                            lineno=17,
                                            col_offset=36,
                                            end_lineno=17,
                                            end_col_offset=47,
                                            value=Name(lineno=17, col_offset=36, end_lineno=17, end_col_offset=40, id='self', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=17, col_offset=48, end_lineno=17, end_col_offset=58, value='password', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=45,
                            value=Call(
                                lineno=19,
                                col_offset=8,
                                end_lineno=19,
                                end_col_offset=45,
                                func=Attribute(
                                    lineno=19,
                                    col_offset=8,
                                    end_lineno=19,
                                    end_col_offset=43,
                                    value=Call(
                                        lineno=19,
                                        col_offset=8,
                                        end_lineno=19,
                                        end_col_offset=29,
                                        func=Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=13, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=19, col_offset=14, end_lineno=19, end_col_offset=22, id='ResUsers', ctx=Load()),
                                            Name(lineno=19, col_offset=24, end_lineno=19, end_col_offset=28, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_set_password',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=33,
                    end_col_offset=52,
                    name='_check_password_policy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=21, col_offset=31, end_lineno=21, end_col_offset=35, arg='self', annotation=None, type_comment=None),
                            arg(lineno=21, col_offset=37, end_lineno=21, end_col_offset=46, arg='passwords', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=21,
                            targets=[Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=16, id='failures', ctx=Store())],
                            value=List(lineno=22, col_offset=19, end_lineno=22, end_col_offset=21, elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=55,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=14, id='params', ctx=Store())],
                            value=Call(
                                lineno=23,
                                col_offset=17,
                                end_lineno=23,
                                end_col_offset=55,
                                func=Attribute(
                                    lineno=23,
                                    col_offset=17,
                                    end_lineno=23,
                                    end_col_offset=53,
                                    value=Subscript(
                                        lineno=23,
                                        col_offset=17,
                                        end_lineno=23,
                                        end_col_offset=48,
                                        value=Attribute(
                                            lineno=23,
                                            col_offset=17,
                                            end_lineno=23,
                                            end_col_offset=25,
                                            value=Name(lineno=23, col_offset=17, end_lineno=23, end_col_offset=21, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=23, col_offset=26, end_lineno=23, end_col_offset=47, value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=86,
                            targets=[Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=17, id='minlength', ctx=Store())],
                            value=Call(
                                lineno=25,
                                col_offset=20,
                                end_lineno=25,
                                end_col_offset=86,
                                func=Name(lineno=25, col_offset=20, end_lineno=25, end_col_offset=23, id='int', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=25,
                                        col_offset=24,
                                        end_lineno=25,
                                        end_col_offset=85,
                                        func=Attribute(
                                            lineno=25,
                                            col_offset=24,
                                            end_lineno=25,
                                            end_col_offset=40,
                                            value=Name(lineno=25, col_offset=24, end_lineno=25, end_col_offset=30, id='params', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=25, col_offset=41, end_lineno=25, end_col_offset=73, value='auth_password_policy.minlength', kind=None)],
                                        keywords=[
                                            keyword(
                                                lineno=25,
                                                col_offset=75,
                                                end_lineno=25,
                                                end_col_offset=84,
                                                arg='default',
                                                value=Constant(lineno=25, col_offset=83, end_lineno=25, end_col_offset=84, value=0, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=26,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=119,
                            target=Name(lineno=26, col_offset=12, end_lineno=26, end_col_offset=20, id='password', ctx=Store()),
                            iter=Name(lineno=26, col_offset=24, end_lineno=26, end_col_offset=33, id='passwords', ctx=Load()),
                            body=[
                                If(
                                    lineno=27,
                                    col_offset=12,
                                    end_lineno=28,
                                    end_col_offset=24,
                                    test=UnaryOp(
                                        lineno=27,
                                        col_offset=15,
                                        end_lineno=27,
                                        end_col_offset=27,
                                        op=Not(),
                                        operand=Name(lineno=27, col_offset=19, end_lineno=27, end_col_offset=27, id='password', ctx=Load()),
                                    ),
                                    body=[Continue(lineno=28, col_offset=16, end_lineno=28, end_col_offset=24)],
                                    orelse=[],
                                ),
                                If(
                                    lineno=29,
                                    col_offset=12,
                                    end_lineno=30,
                                    end_col_offset=119,
                                    test=Compare(
                                        lineno=29,
                                        col_offset=15,
                                        end_lineno=29,
                                        end_col_offset=40,
                                        left=Call(
                                            lineno=29,
                                            col_offset=15,
                                            end_lineno=29,
                                            end_col_offset=28,
                                            func=Name(lineno=29, col_offset=15, end_lineno=29, end_col_offset=18, id='len', ctx=Load()),
                                            args=[Name(lineno=29, col_offset=19, end_lineno=29, end_col_offset=27, id='password', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Name(lineno=29, col_offset=31, end_lineno=29, end_col_offset=40, id='minlength', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            lineno=30,
                                            col_offset=16,
                                            end_lineno=30,
                                            end_col_offset=119,
                                            value=Call(
                                                lineno=30,
                                                col_offset=16,
                                                end_lineno=30,
                                                end_col_offset=119,
                                                func=Attribute(
                                                    lineno=30,
                                                    col_offset=16,
                                                    end_lineno=30,
                                                    end_col_offset=31,
                                                    value=Name(lineno=30, col_offset=16, end_lineno=30, end_col_offset=24, id='failures', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        lineno=30,
                                                        col_offset=32,
                                                        end_lineno=30,
                                                        end_col_offset=118,
                                                        left=Call(
                                                            lineno=30,
                                                            col_offset=32,
                                                            end_lineno=30,
                                                            end_col_offset=89,
                                                            func=Name(lineno=30, col_offset=32, end_lineno=30, end_col_offset=33, id='_', ctx=Load()),
                                                            args=[Constant(lineno=30, col_offset=34, end_lineno=30, end_col_offset=88, value='Passwords must have at least %d characters, got %d.', kind='u')],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            lineno=30,
                                                            col_offset=92,
                                                            end_lineno=30,
                                                            end_col_offset=118,
                                                            elts=[
                                                                Name(lineno=30, col_offset=93, end_lineno=30, end_col_offset=102, id='minlength', ctx=Load()),
                                                                Call(
                                                                    lineno=30,
                                                                    col_offset=104,
                                                                    end_lineno=30,
                                                                    end_col_offset=117,
                                                                    func=Name(lineno=30, col_offset=104, end_lineno=30, end_col_offset=107, id='len', ctx=Load()),
                                                                    args=[Name(lineno=30, col_offset=108, end_lineno=30, end_col_offset=116, id='password', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            lineno=32,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=52,
                            test=Name(lineno=32, col_offset=11, end_lineno=32, end_col_offset=19, id='failures', ctx=Load()),
                            body=[
                                Raise(
                                    lineno=33,
                                    col_offset=12,
                                    end_lineno=33,
                                    end_col_offset=52,
                                    exc=Call(
                                        lineno=33,
                                        col_offset=18,
                                        end_lineno=33,
                                        end_col_offset=52,
                                        func=Name(lineno=33, col_offset=18, end_lineno=33, end_col_offset=27, id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=33,
                                                col_offset=28,
                                                end_lineno=33,
                                                end_col_offset=51,
                                                func=Attribute(
                                                    lineno=33,
                                                    col_offset=28,
                                                    end_lineno=33,
                                                    end_col_offset=41,
                                                    value=Constant(lineno=33, col_offset=28, end_lineno=33, end_col_offset=36, value='\n\n ', kind='u'),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(lineno=33, col_offset=42, end_lineno=33, end_col_offset=50, id='failures', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
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