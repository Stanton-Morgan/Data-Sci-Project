Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=11,
            names=[alias(name='time', asname=None)],
        ),
        Import(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=10,
            names=[alias(name='sys', asname=None)],
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=45,
            end_col_offset=19,
            name='m',
            bases=[
                Attribute(
                    lineno=9,
                    col_offset=8,
                    end_lineno=9,
                    end_col_offset=20,
                    value=Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=14, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    lineno=10,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=7,
                    value=Constant(lineno=10, col_offset=4, end_lineno=12, end_col_offset=7, value=" This model exposes a few methods that will consume between 'almost no\n        resource' and 'a lot of resource'.\n    ", kind=None),
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=31,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=31, value='test.limits.model', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=38,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=14, col_offset=19, end_lineno=14, end_col_offset=38, value='Test Limits Model', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=17,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=19,
                    name='consume_nothing',
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
                        Return(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=19,
                            value=Constant(lineno=18, col_offset=15, end_lineno=18, end_col_offset=19, value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=16,
                            col_offset=5,
                            end_lineno=16,
                            end_col_offset=14,
                            value=Name(lineno=16, col_offset=5, end_lineno=16, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=19,
                    name='consume_memory',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=21, col_offset=23, end_lineno=21, end_col_offset=27, arg='self', annotation=None, type_comment=None),
                            arg(lineno=21, col_offset=29, end_lineno=21, end_col_offset=33, arg='size', annotation=None, type_comment=None),
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
                            end_col_offset=22,
                            targets=[Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=9, id='l', ctx=Store())],
                            value=BinOp(
                                lineno=22,
                                col_offset=12,
                                end_lineno=22,
                                end_col_offset=22,
                                left=List(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=15,
                                    elts=[Constant(lineno=22, col_offset=13, end_lineno=22, end_col_offset=14, value=0, kind=None)],
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Name(lineno=22, col_offset=18, end_lineno=22, end_col_offset=22, id='size', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=19,
                            value=Constant(lineno=23, col_offset=15, end_lineno=23, end_col_offset=19, value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=20,
                            col_offset=5,
                            end_lineno=20,
                            end_col_offset=14,
                            value=Name(lineno=20, col_offset=5, end_lineno=20, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=26,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=19,
                    name='leak_memory',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=26, col_offset=20, end_lineno=26, end_col_offset=24, arg='self', annotation=None, type_comment=None),
                            arg(lineno=26, col_offset=26, end_lineno=26, end_col_offset=30, arg='size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            lineno=27,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=29,
                            test=UnaryOp(
                                lineno=27,
                                col_offset=11,
                                end_lineno=27,
                                end_col_offset=33,
                                op=Not(),
                                operand=Call(
                                    lineno=27,
                                    col_offset=15,
                                    end_lineno=27,
                                    end_col_offset=33,
                                    func=Name(lineno=27, col_offset=15, end_lineno=27, end_col_offset=22, id='hasattr', ctx=Load()),
                                    args=[
                                        Name(lineno=27, col_offset=23, end_lineno=27, end_col_offset=27, id='self', ctx=Load()),
                                        Constant(lineno=27, col_offset=29, end_lineno=27, end_col_offset=32, value='l', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    lineno=28,
                                    col_offset=12,
                                    end_lineno=28,
                                    end_col_offset=29,
                                    targets=[
                                        Attribute(
                                            lineno=28,
                                            col_offset=12,
                                            end_lineno=28,
                                            end_col_offset=24,
                                            value=Call(
                                                lineno=28,
                                                col_offset=12,
                                                end_lineno=28,
                                                end_col_offset=22,
                                                func=Name(lineno=28, col_offset=12, end_lineno=28, end_col_offset=16, id='type', ctx=Load()),
                                                args=[Name(lineno=28, col_offset=17, end_lineno=28, end_col_offset=21, id='self', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='l',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(lineno=28, col_offset=27, end_lineno=28, end_col_offset=29, elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=33,
                            value=Call(
                                lineno=29,
                                col_offset=8,
                                end_lineno=29,
                                end_col_offset=33,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=8,
                                    end_lineno=29,
                                    end_col_offset=21,
                                    value=Attribute(
                                        lineno=29,
                                        col_offset=8,
                                        end_lineno=29,
                                        end_col_offset=14,
                                        value=Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=12, id='self', ctx=Load()),
                                        attr='l',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        lineno=29,
                                        col_offset=22,
                                        end_lineno=29,
                                        end_col_offset=32,
                                        left=List(
                                            lineno=29,
                                            col_offset=22,
                                            end_lineno=29,
                                            end_col_offset=25,
                                            elts=[Constant(lineno=29, col_offset=23, end_lineno=29, end_col_offset=24, value=0, kind=None)],
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Name(lineno=29, col_offset=28, end_lineno=29, end_col_offset=32, id='size', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=19,
                            value=Constant(lineno=30, col_offset=15, end_lineno=30, end_col_offset=19, value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=25,
                            col_offset=5,
                            end_lineno=25,
                            end_col_offset=14,
                            value=Name(lineno=25, col_offset=5, end_lineno=25, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=33,
                    col_offset=4,
                    end_lineno=35,
                    end_col_offset=19,
                    name='consume_time',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=33, col_offset=21, end_lineno=33, end_col_offset=25, arg='self', annotation=None, type_comment=None),
                            arg(lineno=33, col_offset=27, end_lineno=33, end_col_offset=34, arg='seconds', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=27,
                            value=Call(
                                lineno=34,
                                col_offset=8,
                                end_lineno=34,
                                end_col_offset=27,
                                func=Attribute(
                                    lineno=34,
                                    col_offset=8,
                                    end_lineno=34,
                                    end_col_offset=18,
                                    value=Name(lineno=34, col_offset=8, end_lineno=34, end_col_offset=12, id='time', ctx=Load()),
                                    attr='sleep',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=34, col_offset=19, end_lineno=34, end_col_offset=26, id='seconds', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=35,
                            col_offset=8,
                            end_lineno=35,
                            end_col_offset=19,
                            value=Constant(lineno=35, col_offset=15, end_lineno=35, end_col_offset=19, value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=32,
                            col_offset=5,
                            end_lineno=32,
                            end_col_offset=14,
                            value=Name(lineno=32, col_offset=5, end_lineno=32, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=38,
                    col_offset=4,
                    end_lineno=45,
                    end_col_offset=19,
                    name='consume_cpu_time',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=38, col_offset=25, end_lineno=38, end_col_offset=29, arg='self', annotation=None, type_comment=None),
                            arg(lineno=38, col_offset=31, end_lineno=38, end_col_offset=38, arg='seconds', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=39,
                            col_offset=8,
                            end_lineno=39,
                            end_col_offset=32,
                            targets=[Name(lineno=39, col_offset=8, end_lineno=39, end_col_offset=10, id='t0', ctx=Store())],
                            value=Call(
                                lineno=39,
                                col_offset=13,
                                end_lineno=39,
                                end_col_offset=32,
                                func=Attribute(
                                    lineno=39,
                                    col_offset=13,
                                    end_lineno=39,
                                    end_col_offset=30,
                                    value=Name(lineno=39, col_offset=13, end_lineno=39, end_col_offset=17, id='time', ctx=Load()),
                                    attr='process_time',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=40,
                            col_offset=8,
                            end_lineno=40,
                            end_col_offset=32,
                            targets=[Name(lineno=40, col_offset=8, end_lineno=40, end_col_offset=10, id='t1', ctx=Store())],
                            value=Call(
                                lineno=40,
                                col_offset=13,
                                end_lineno=40,
                                end_col_offset=32,
                                func=Attribute(
                                    lineno=40,
                                    col_offset=13,
                                    end_lineno=40,
                                    end_col_offset=30,
                                    value=Name(lineno=40, col_offset=13, end_lineno=40, end_col_offset=17, id='time', ctx=Load()),
                                    attr='process_time',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            lineno=41,
                            col_offset=8,
                            end_lineno=44,
                            end_col_offset=36,
                            test=Compare(
                                lineno=41,
                                col_offset=14,
                                end_lineno=41,
                                end_col_offset=31,
                                left=BinOp(
                                    lineno=41,
                                    col_offset=14,
                                    end_lineno=41,
                                    end_col_offset=21,
                                    left=Name(lineno=41, col_offset=14, end_lineno=41, end_col_offset=16, id='t1', ctx=Load()),
                                    op=Sub(),
                                    right=Name(lineno=41, col_offset=19, end_lineno=41, end_col_offset=21, id='t0', ctx=Load()),
                                ),
                                ops=[Lt()],
                                comparators=[Name(lineno=41, col_offset=24, end_lineno=41, end_col_offset=31, id='seconds', ctx=Load())],
                            ),
                            body=[
                                For(
                                    lineno=42,
                                    col_offset=12,
                                    end_lineno=43,
                                    end_col_offset=25,
                                    target=Name(lineno=42, col_offset=16, end_lineno=42, end_col_offset=17, id='i', ctx=Store()),
                                    iter=Call(
                                        lineno=42,
                                        col_offset=21,
                                        end_lineno=42,
                                        end_col_offset=36,
                                        func=Name(lineno=42, col_offset=21, end_lineno=42, end_col_offset=26, id='range', ctx=Load()),
                                        args=[Constant(lineno=42, col_offset=27, end_lineno=42, end_col_offset=35, value=10000000, kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=43,
                                            col_offset=16,
                                            end_lineno=43,
                                            end_col_offset=25,
                                            targets=[Name(lineno=43, col_offset=16, end_lineno=43, end_col_offset=17, id='x', ctx=Store())],
                                            value=BinOp(
                                                lineno=43,
                                                col_offset=20,
                                                end_lineno=43,
                                                end_col_offset=25,
                                                left=Name(lineno=43, col_offset=20, end_lineno=43, end_col_offset=21, id='i', ctx=Load()),
                                                op=Mult(),
                                                right=Name(lineno=43, col_offset=24, end_lineno=43, end_col_offset=25, id='i', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=44,
                                    col_offset=12,
                                    end_lineno=44,
                                    end_col_offset=36,
                                    targets=[Name(lineno=44, col_offset=12, end_lineno=44, end_col_offset=14, id='t1', ctx=Store())],
                                    value=Call(
                                        lineno=44,
                                        col_offset=17,
                                        end_lineno=44,
                                        end_col_offset=36,
                                        func=Attribute(
                                            lineno=44,
                                            col_offset=17,
                                            end_lineno=44,
                                            end_col_offset=34,
                                            value=Name(lineno=44, col_offset=17, end_lineno=44, end_col_offset=21, id='time', ctx=Load()),
                                            attr='process_time',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=45,
                            col_offset=8,
                            end_lineno=45,
                            end_col_offset=19,
                            value=Constant(lineno=45, col_offset=15, end_lineno=45, end_col_offset=19, value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=37,
                            col_offset=5,
                            end_lineno=37,
                            end_col_offset=14,
                            value=Name(lineno=37, col_offset=5, end_lineno=37, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
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
