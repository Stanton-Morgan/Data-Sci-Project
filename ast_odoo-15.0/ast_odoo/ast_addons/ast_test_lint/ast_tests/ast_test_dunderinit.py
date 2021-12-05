Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=14,
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=24,
            module='pathlib',
            names=[alias(name='Path', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=53,
            module='odoo.modules',
            names=[
                alias(name='get_modules', asname=None),
                alias(name='get_module_path', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=23,
            module=None,
            names=[alias(name='lint_case', asname=None)],
            level=1,
        ),
        Assign(
            lineno=10,
            col_offset=0,
            end_lineno=10,
            end_col_offset=37,
            targets=[Name(lineno=10, col_offset=0, end_lineno=10, end_col_offset=7, id='_logger', ctx=Store())],
            value=Call(
                lineno=10,
                col_offset=10,
                end_lineno=10,
                end_col_offset=37,
                func=Attribute(
                    lineno=10,
                    col_offset=10,
                    end_lineno=10,
                    end_col_offset=27,
                    value=Name(lineno=10, col_offset=10, end_lineno=10, end_col_offset=17, id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(lineno=10, col_offset=28, end_lineno=10, end_col_offset=36, id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            lineno=13,
            col_offset=0,
            end_lineno=13,
            end_col_offset=34,
            targets=[Name(lineno=13, col_offset=0, end_lineno=13, end_col_offset=9, id='WHITELIST', ctx=Store())],
            value=List(
                lineno=13,
                col_offset=12,
                end_lineno=13,
                end_col_offset=34,
                elts=[Constant(lineno=13, col_offset=13, end_lineno=13, end_col_offset=31, value='test_data_module', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            lineno=15,
            col_offset=0,
            end_lineno=25,
            end_col_offset=61,
            name='TestDunderinit',
            bases=[
                Attribute(
                    lineno=15,
                    col_offset=21,
                    end_lineno=15,
                    end_col_offset=39,
                    value=Name(lineno=15, col_offset=21, end_lineno=15, end_col_offset=30, id='lint_case', ctx=Load()),
                    attr='LintCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=17,
                    col_offset=4,
                    end_lineno=25,
                    end_col_offset=61,
                    name='test_dunderinit',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=17, col_offset=24, end_lineno=17, end_col_offset=28, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=94,
                            value=Constant(lineno=18, col_offset=8, end_lineno=18, end_col_offset=94, value=" Test that __init__.py exists in Odoo modules, otherwise they won't get packaged", kind=None),
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=77,
                            targets=[Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=20, id='modules_list', ctx=Store())],
                            value=ListComp(
                                lineno=20,
                                col_offset=23,
                                end_lineno=20,
                                end_col_offset=77,
                                elt=Name(lineno=20, col_offset=24, end_lineno=20, end_col_offset=27, id='mod', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(lineno=20, col_offset=32, end_lineno=20, end_col_offset=35, id='mod', ctx=Store()),
                                        iter=Call(
                                            lineno=20,
                                            col_offset=39,
                                            end_lineno=20,
                                            end_col_offset=52,
                                            func=Name(lineno=20, col_offset=39, end_lineno=20, end_col_offset=50, id='get_modules', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                lineno=20,
                                                col_offset=56,
                                                end_lineno=20,
                                                end_col_offset=76,
                                                left=Name(lineno=20, col_offset=56, end_lineno=20, end_col_offset=59, id='mod', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(lineno=20, col_offset=67, end_lineno=20, end_col_offset=76, id='WHITELIST', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=21,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=99,
                            target=Name(lineno=21, col_offset=12, end_lineno=21, end_col_offset=15, id='mod', ctx=Store()),
                            iter=Name(lineno=21, col_offset=19, end_lineno=21, end_col_offset=31, id='modules_list', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=72,
                                    targets=[Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=27, id='dunderinit_path', ctx=Store())],
                                    value=BinOp(
                                        lineno=22,
                                        col_offset=30,
                                        end_lineno=22,
                                        end_col_offset=72,
                                        left=Call(
                                            lineno=22,
                                            col_offset=30,
                                            end_lineno=22,
                                            end_col_offset=56,
                                            func=Name(lineno=22, col_offset=30, end_lineno=22, end_col_offset=34, id='Path', ctx=Load()),
                                            args=[
                                                Call(
                                                    lineno=22,
                                                    col_offset=35,
                                                    end_lineno=22,
                                                    end_col_offset=55,
                                                    func=Name(lineno=22, col_offset=35, end_lineno=22, end_col_offset=50, id='get_module_path', ctx=Load()),
                                                    args=[Name(lineno=22, col_offset=51, end_lineno=22, end_col_offset=54, id='mod', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Div(),
                                        right=Constant(lineno=22, col_offset=59, end_lineno=22, end_col_offset=72, value='__init__.py', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    lineno=23,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=99,
                                    value=Call(
                                        lineno=23,
                                        col_offset=12,
                                        end_lineno=23,
                                        end_col_offset=99,
                                        func=Attribute(
                                            lineno=23,
                                            col_offset=12,
                                            end_lineno=23,
                                            end_col_offset=27,
                                            value=Name(lineno=23, col_offset=12, end_lineno=23, end_col_offset=16, id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                lineno=23,
                                                col_offset=28,
                                                end_lineno=23,
                                                end_col_offset=53,
                                                func=Attribute(
                                                    lineno=23,
                                                    col_offset=28,
                                                    end_lineno=23,
                                                    end_col_offset=51,
                                                    value=Name(lineno=23, col_offset=28, end_lineno=23, end_col_offset=43, id='dunderinit_path', ctx=Load()),
                                                    attr='is_file',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                lineno=23,
                                                col_offset=55,
                                                end_lineno=23,
                                                end_col_offset=98,
                                                left=Constant(lineno=23, col_offset=55, end_lineno=23, end_col_offset=92, value='Missing `__init__.py ` in module %s', kind=None),
                                                op=Mod(),
                                                right=Name(lineno=23, col_offset=95, end_lineno=23, end_col_offset=98, id='mod', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=61,
                            value=Call(
                                lineno=25,
                                col_offset=8,
                                end_lineno=25,
                                end_col_offset=61,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=8,
                                    end_lineno=25,
                                    end_col_offset=20,
                                    value=Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=15, id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=25, col_offset=21, end_lineno=25, end_col_offset=41, value='%s modules checked', kind=None),
                                    Call(
                                        lineno=25,
                                        col_offset=43,
                                        end_lineno=25,
                                        end_col_offset=60,
                                        func=Name(lineno=25, col_offset=43, end_lineno=25, end_col_offset=46, id='len', ctx=Load()),
                                        args=[Name(lineno=25, col_offset=47, end_lineno=25, end_col_offset=59, id='modules_list', ctx=Load())],
                                        keywords=[],
                                    ),
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
