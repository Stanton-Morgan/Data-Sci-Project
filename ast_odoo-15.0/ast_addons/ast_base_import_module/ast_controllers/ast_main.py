Module(
    body=[
        Import(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=16,
            names=[alias(name='functools', asname=None)],
        ),
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=18,
            module='odoo',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=39,
            module='odoo.exceptions',
            names=[alias(name='AccessError', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=58,
            module='odoo.http',
            names=[
                alias(name='Controller', asname=None),
                alias(name='route', asname=None),
                alias(name='request', asname=None),
                alias(name='Response', asname=None),
            ],
            level=0,
        ),
        FunctionDef(
            lineno=8,
            col_offset=0,
            end_lineno=15,
            end_col_offset=15,
            name='webservice',
            args=arguments(
                posonlyargs=[],
                args=[arg(lineno=8, col_offset=15, end_lineno=8, end_col_offset=16, arg='f', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=56,
                    name='wrap',
                    args=arguments(
                        posonlyargs=[],
                        args=[],
                        vararg=arg(lineno=10, col_offset=14, end_lineno=10, end_col_offset=18, arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(lineno=10, col_offset=22, end_lineno=10, end_col_offset=24, arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Try(
                            lineno=11,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=56,
                            body=[
                                Return(
                                    lineno=12,
                                    col_offset=12,
                                    end_lineno=12,
                                    end_col_offset=33,
                                    value=Call(
                                        lineno=12,
                                        col_offset=19,
                                        end_lineno=12,
                                        end_col_offset=33,
                                        func=Name(lineno=12, col_offset=19, end_lineno=12, end_col_offset=20, id='f', ctx=Load()),
                                        args=[
                                            Starred(
                                                lineno=12,
                                                col_offset=21,
                                                end_lineno=12,
                                                end_col_offset=26,
                                                value=Name(lineno=12, col_offset=22, end_lineno=12, end_col_offset=26, id='args', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                lineno=12,
                                                col_offset=28,
                                                end_lineno=12,
                                                end_col_offset=32,
                                                arg=None,
                                                value=Name(lineno=12, col_offset=30, end_lineno=12, end_col_offset=32, id='kw', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    lineno=13,
                                    col_offset=8,
                                    end_lineno=14,
                                    end_col_offset=56,
                                    type=Name(lineno=13, col_offset=15, end_lineno=13, end_col_offset=24, id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Return(
                                            lineno=14,
                                            col_offset=12,
                                            end_lineno=14,
                                            end_col_offset=56,
                                            value=Call(
                                                lineno=14,
                                                col_offset=19,
                                                end_lineno=14,
                                                end_col_offset=56,
                                                func=Name(lineno=14, col_offset=19, end_lineno=14, end_col_offset=27, id='Response', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        lineno=14,
                                                        col_offset=28,
                                                        end_lineno=14,
                                                        end_col_offset=43,
                                                        arg='response',
                                                        value=Call(
                                                            lineno=14,
                                                            col_offset=37,
                                                            end_lineno=14,
                                                            end_col_offset=43,
                                                            func=Name(lineno=14, col_offset=37, end_lineno=14, end_col_offset=40, id='str', ctx=Load()),
                                                            args=[Name(lineno=14, col_offset=41, end_lineno=14, end_col_offset=42, id='e', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        lineno=14,
                                                        col_offset=45,
                                                        end_lineno=14,
                                                        end_col_offset=55,
                                                        arg='status',
                                                        value=Constant(lineno=14, col_offset=52, end_lineno=14, end_col_offset=55, value=500, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=9,
                            col_offset=5,
                            end_lineno=9,
                            end_col_offset=23,
                            func=Attribute(
                                lineno=9,
                                col_offset=5,
                                end_lineno=9,
                                end_col_offset=20,
                                value=Name(lineno=9, col_offset=5, end_lineno=9, end_col_offset=14, id='functools', ctx=Load()),
                                attr='wraps',
                                ctx=Load(),
                            ),
                            args=[Name(lineno=9, col_offset=21, end_lineno=9, end_col_offset=22, id='f', ctx=Load())],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=15,
                    value=Name(lineno=15, col_offset=11, end_lineno=15, end_col_offset=15, id='wrap', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            lineno=18,
            col_offset=0,
            end_lineno=37,
            end_col_offset=87,
            name='ImportModule',
            bases=[Name(lineno=18, col_offset=19, end_lineno=18, end_col_offset=29, id='Controller', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=20,
                    col_offset=4,
                    end_lineno=25,
                    end_col_offset=75,
                    name='check_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=20, col_offset=19, end_lineno=20, end_col_offset=23, arg='self', annotation=None, type_comment=None),
                            arg(lineno=20, col_offset=25, end_lineno=20, end_col_offset=28, arg='uid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=20, col_offset=29, end_lineno=20, end_col_offset=33, value=None, kind=None)],
                    ),
                    body=[
                        If(
                            lineno=21,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=29,
                            test=Compare(
                                lineno=21,
                                col_offset=11,
                                end_lineno=21,
                                end_col_offset=22,
                                left=Name(lineno=21, col_offset=11, end_lineno=21, end_col_offset=14, id='uid', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(lineno=21, col_offset=18, end_lineno=21, end_col_offset=22, value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=29,
                                    targets=[Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=15, id='uid', ctx=Store())],
                                    value=Attribute(
                                        lineno=22,
                                        col_offset=18,
                                        end_lineno=22,
                                        end_col_offset=29,
                                        value=Name(lineno=22, col_offset=18, end_lineno=22, end_col_offset=25, id='request', ctx=Load()),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=67,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=16, id='is_admin', ctx=Store())],
                            value=Call(
                                lineno=23,
                                col_offset=19,
                                end_lineno=23,
                                end_col_offset=67,
                                func=Attribute(
                                    lineno=23,
                                    col_offset=19,
                                    end_lineno=23,
                                    end_col_offset=65,
                                    value=Call(
                                        lineno=23,
                                        col_offset=19,
                                        end_lineno=23,
                                        end_col_offset=55,
                                        func=Attribute(
                                            lineno=23,
                                            col_offset=19,
                                            end_lineno=23,
                                            end_col_offset=50,
                                            value=Subscript(
                                                lineno=23,
                                                col_offset=19,
                                                end_lineno=23,
                                                end_col_offset=43,
                                                value=Attribute(
                                                    lineno=23,
                                                    col_offset=19,
                                                    end_lineno=23,
                                                    end_col_offset=30,
                                                    value=Name(lineno=23, col_offset=19, end_lineno=23, end_col_offset=26, id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=23, col_offset=31, end_lineno=23, end_col_offset=42, value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=23, col_offset=51, end_lineno=23, end_col_offset=54, id='uid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_is_admin',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=24,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=75,
                            test=UnaryOp(
                                lineno=24,
                                col_offset=11,
                                end_lineno=24,
                                end_col_offset=23,
                                op=Not(),
                                operand=Name(lineno=24, col_offset=15, end_lineno=24, end_col_offset=23, id='is_admin', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    lineno=25,
                                    col_offset=12,
                                    end_lineno=25,
                                    end_col_offset=75,
                                    exc=Call(
                                        lineno=25,
                                        col_offset=18,
                                        end_lineno=25,
                                        end_col_offset=75,
                                        func=Name(lineno=25, col_offset=18, end_lineno=25, end_col_offset=29, id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=25,
                                                col_offset=30,
                                                end_lineno=25,
                                                end_col_offset=74,
                                                func=Name(lineno=25, col_offset=30, end_lineno=25, end_col_offset=31, id='_', ctx=Load()),
                                                args=[Constant(lineno=25, col_offset=32, end_lineno=25, end_col_offset=73, value='Only administrators can upload a module', kind=None)],
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
                FunctionDef(
                    lineno=31,
                    col_offset=4,
                    end_lineno=37,
                    end_col_offset=87,
                    name='login_upload',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=31, col_offset=21, end_lineno=31, end_col_offset=25, arg='self', annotation=None, type_comment=None),
                            arg(lineno=31, col_offset=27, end_lineno=31, end_col_offset=32, arg='login', annotation=None, type_comment=None),
                            arg(lineno=31, col_offset=34, end_lineno=31, end_col_offset=42, arg='password', annotation=None, type_comment=None),
                            arg(lineno=31, col_offset=44, end_lineno=31, end_col_offset=46, arg='db', annotation=None, type_comment=None),
                            arg(lineno=31, col_offset=53, end_lineno=31, end_col_offset=58, arg='force', annotation=None, type_comment=None),
                            arg(lineno=31, col_offset=63, end_lineno=31, end_col_offset=71, arg='mod_file', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(lineno=31, col_offset=80, end_lineno=31, end_col_offset=82, arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(lineno=31, col_offset=47, end_lineno=31, end_col_offset=51, value=None, kind=None),
                            Constant(lineno=31, col_offset=59, end_lineno=31, end_col_offset=61, value='', kind=None),
                            Constant(lineno=31, col_offset=72, end_lineno=31, end_col_offset=76, value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            lineno=32,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=68,
                            test=BoolOp(
                                lineno=32,
                                col_offset=11,
                                end_lineno=32,
                                end_col_offset=34,
                                op=And(),
                                values=[
                                    Name(lineno=32, col_offset=11, end_lineno=32, end_col_offset=13, id='db', ctx=Load()),
                                    Compare(
                                        lineno=32,
                                        col_offset=18,
                                        end_lineno=32,
                                        end_col_offset=34,
                                        left=Name(lineno=32, col_offset=18, end_lineno=32, end_col_offset=20, id='db', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                lineno=32,
                                                col_offset=24,
                                                end_lineno=32,
                                                end_col_offset=34,
                                                value=Name(lineno=32, col_offset=24, end_lineno=32, end_col_offset=31, id='request', ctx=Load()),
                                                attr='db',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    lineno=33,
                                    col_offset=12,
                                    end_lineno=33,
                                    end_col_offset=68,
                                    exc=Call(
                                        lineno=33,
                                        col_offset=18,
                                        end_lineno=33,
                                        end_col_offset=68,
                                        func=Name(lineno=33, col_offset=18, end_lineno=33, end_col_offset=27, id='Exception', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=33,
                                                col_offset=28,
                                                end_lineno=33,
                                                end_col_offset=67,
                                                func=Name(lineno=33, col_offset=28, end_lineno=33, end_col_offset=29, id='_', ctx=Load()),
                                                args=[
                                                    Constant(lineno=33, col_offset=30, end_lineno=33, end_col_offset=62, value="Could not select database '%s'", kind=None),
                                                    Name(lineno=33, col_offset=64, end_lineno=33, end_col_offset=66, id='db', ctx=Load()),
                                                ],
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
                        Assign(
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=71,
                            targets=[Name(lineno=34, col_offset=8, end_lineno=34, end_col_offset=11, id='uid', ctx=Store())],
                            value=Call(
                                lineno=34,
                                col_offset=14,
                                end_lineno=34,
                                end_col_offset=71,
                                func=Attribute(
                                    lineno=34,
                                    col_offset=14,
                                    end_lineno=34,
                                    end_col_offset=42,
                                    value=Attribute(
                                        lineno=34,
                                        col_offset=14,
                                        end_lineno=34,
                                        end_col_offset=29,
                                        value=Name(lineno=34, col_offset=14, end_lineno=34, end_col_offset=21, id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=34,
                                        col_offset=43,
                                        end_lineno=34,
                                        end_col_offset=53,
                                        value=Name(lineno=34, col_offset=43, end_lineno=34, end_col_offset=50, id='request', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    Name(lineno=34, col_offset=55, end_lineno=34, end_col_offset=60, id='login', ctx=Load()),
                                    Name(lineno=34, col_offset=62, end_lineno=34, end_col_offset=70, id='password', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=35,
                            col_offset=8,
                            end_lineno=35,
                            end_col_offset=28,
                            value=Call(
                                lineno=35,
                                col_offset=8,
                                end_lineno=35,
                                end_col_offset=28,
                                func=Attribute(
                                    lineno=35,
                                    col_offset=8,
                                    end_lineno=35,
                                    end_col_offset=23,
                                    value=Name(lineno=35, col_offset=8, end_lineno=35, end_col_offset=12, id='self', ctx=Load()),
                                    attr='check_user',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=35, col_offset=24, end_lineno=35, end_col_offset=27, id='uid', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=36,
                            col_offset=8,
                            end_lineno=36,
                            end_col_offset=47,
                            targets=[Name(lineno=36, col_offset=8, end_lineno=36, end_col_offset=13, id='force', ctx=Store())],
                            value=IfExp(
                                lineno=36,
                                col_offset=16,
                                end_lineno=36,
                                end_col_offset=47,
                                test=Compare(
                                    lineno=36,
                                    col_offset=24,
                                    end_lineno=36,
                                    end_col_offset=36,
                                    left=Name(lineno=36, col_offset=24, end_lineno=36, end_col_offset=29, id='force', ctx=Load()),
                                    ops=[Eq()],
                                    comparators=[Constant(lineno=36, col_offset=33, end_lineno=36, end_col_offset=36, value='1', kind=None)],
                                ),
                                body=Constant(lineno=36, col_offset=16, end_lineno=36, end_col_offset=20, value=True, kind=None),
                                orelse=Constant(lineno=36, col_offset=42, end_lineno=36, end_col_offset=47, value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=37,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=87,
                            value=Subscript(
                                lineno=37,
                                col_offset=15,
                                end_lineno=37,
                                end_col_offset=87,
                                value=Call(
                                    lineno=37,
                                    col_offset=15,
                                    end_lineno=37,
                                    end_col_offset=84,
                                    func=Attribute(
                                        lineno=37,
                                        col_offset=15,
                                        end_lineno=37,
                                        end_col_offset=61,
                                        value=Subscript(
                                            lineno=37,
                                            col_offset=15,
                                            end_lineno=37,
                                            end_col_offset=46,
                                            value=Attribute(
                                                lineno=37,
                                                col_offset=15,
                                                end_lineno=37,
                                                end_col_offset=26,
                                                value=Name(lineno=37, col_offset=15, end_lineno=37, end_col_offset=22, id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(lineno=37, col_offset=27, end_lineno=37, end_col_offset=45, value='ir.module.module', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='import_zipfile',
                                        ctx=Load(),
                                    ),
                                    args=[Name(lineno=37, col_offset=62, end_lineno=37, end_col_offset=70, id='mod_file', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            lineno=37,
                                            col_offset=72,
                                            end_lineno=37,
                                            end_col_offset=83,
                                            arg='force',
                                            value=Name(lineno=37, col_offset=78, end_lineno=37, end_col_offset=83, id='force', ctx=Load()),
                                        ),
                                    ],
                                ),
                                slice=Constant(lineno=37, col_offset=85, end_lineno=37, end_col_offset=86, value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=27,
                            col_offset=5,
                            end_lineno=29,
                            end_col_offset=83,
                            func=Name(lineno=27, col_offset=5, end_lineno=27, end_col_offset=10, id='route', ctx=Load()),
                            args=[Constant(lineno=28, col_offset=8, end_lineno=28, end_col_offset=42, value='/base_import_module/login_upload', kind=None)],
                            keywords=[
                                keyword(
                                    lineno=29,
                                    col_offset=8,
                                    end_lineno=29,
                                    end_col_offset=19,
                                    arg='type',
                                    value=Constant(lineno=29, col_offset=13, end_lineno=29, end_col_offset=19, value='http', kind=None),
                                ),
                                keyword(
                                    lineno=29,
                                    col_offset=21,
                                    end_lineno=29,
                                    end_col_offset=32,
                                    arg='auth',
                                    value=Constant(lineno=29, col_offset=26, end_lineno=29, end_col_offset=32, value='none', kind=None),
                                ),
                                keyword(
                                    lineno=29,
                                    col_offset=34,
                                    end_lineno=29,
                                    end_col_offset=50,
                                    arg='methods',
                                    value=List(
                                        lineno=29,
                                        col_offset=42,
                                        end_lineno=29,
                                        end_col_offset=50,
                                        elts=[Constant(lineno=29, col_offset=43, end_lineno=29, end_col_offset=49, value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    lineno=29,
                                    col_offset=52,
                                    end_lineno=29,
                                    end_col_offset=62,
                                    arg='csrf',
                                    value=Constant(lineno=29, col_offset=57, end_lineno=29, end_col_offset=62, value=False, kind=None),
                                ),
                                keyword(
                                    lineno=29,
                                    col_offset=64,
                                    end_lineno=29,
                                    end_col_offset=82,
                                    arg='save_session',
                                    value=Constant(lineno=29, col_offset=77, end_lineno=29, end_col_offset=82, value=False, kind=None),
                                ),
                            ],
                        ),
                        Name(lineno=30, col_offset=5, end_lineno=30, end_col_offset=15, id='webservice', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)