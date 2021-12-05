Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=31,
            end_col_offset=26,
            name='IrConfigParameter',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=24,
                    end_lineno=7,
                    end_col_offset=36,
                    value=Name(lineno=7, col_offset=24, end_lineno=7, end_col_offset=30, id='models', ctx=Load()),
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
                    end_col_offset=36,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=36, value='ir.config_parameter', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=21,
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=10, col_offset=14, end_lineno=10, end_col_offset=18, arg='self', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=20, end_lineno=10, end_col_offset=24, arg='vals', annotation=None, type_comment=None),
                        ],
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
                            end_col_offset=59,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=14, id='result', ctx=Store())],
                            value=Call(
                                lineno=11,
                                col_offset=17,
                                end_lineno=11,
                                end_col_offset=59,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=17,
                                    end_lineno=11,
                                    end_col_offset=53,
                                    value=Call(
                                        lineno=11,
                                        col_offset=17,
                                        end_lineno=11,
                                        end_col_offset=47,
                                        func=Name(lineno=11, col_offset=17, end_lineno=11, end_col_offset=22, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=11, col_offset=23, end_lineno=11, end_col_offset=40, id='IrConfigParameter', ctx=Load()),
                                            Name(lineno=11, col_offset=42, end_lineno=11, end_col_offset=46, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=11, col_offset=54, end_lineno=11, end_col_offset=58, id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=12,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=55,
                            test=Call(
                                lineno=12,
                                col_offset=11,
                                end_lineno=12,
                                end_col_offset=65,
                                func=Name(lineno=12, col_offset=11, end_lineno=12, end_col_offset=14, id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        lineno=12,
                                        col_offset=14,
                                        end_lineno=12,
                                        end_col_offset=65,
                                        elt=Compare(
                                            lineno=12,
                                            col_offset=15,
                                            end_lineno=12,
                                            end_col_offset=45,
                                            left=Attribute(
                                                lineno=12,
                                                col_offset=15,
                                                end_lineno=12,
                                                end_col_offset=25,
                                                value=Name(lineno=12, col_offset=15, end_lineno=12, end_col_offset=21, id='record', ctx=Load()),
                                                attr='key',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(lineno=12, col_offset=29, end_lineno=12, end_col_offset=45, value='crm.pls_fields', kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(lineno=12, col_offset=50, end_lineno=12, end_col_offset=56, id='record', ctx=Store()),
                                                iter=Name(lineno=12, col_offset=60, end_lineno=12, end_col_offset=64, id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    lineno=13,
                                    col_offset=12,
                                    end_lineno=13,
                                    end_col_offset=24,
                                    value=Call(
                                        lineno=13,
                                        col_offset=12,
                                        end_lineno=13,
                                        end_col_offset=24,
                                        func=Attribute(
                                            lineno=13,
                                            col_offset=12,
                                            end_lineno=13,
                                            end_col_offset=22,
                                            value=Name(lineno=13, col_offset=12, end_lineno=13, end_col_offset=16, id='self', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=14,
                                    end_col_offset=55,
                                    value=Call(
                                        lineno=14,
                                        col_offset=12,
                                        end_lineno=14,
                                        end_col_offset=55,
                                        func=Attribute(
                                            lineno=14,
                                            col_offset=12,
                                            end_lineno=14,
                                            end_col_offset=42,
                                            value=Attribute(
                                                lineno=14,
                                                col_offset=12,
                                                end_lineno=14,
                                                end_col_offset=29,
                                                value=Attribute(
                                                    lineno=14,
                                                    col_offset=12,
                                                    end_lineno=14,
                                                    end_col_offset=20,
                                                    value=Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=16, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='registry',
                                                ctx=Load(),
                                            ),
                                            attr='setup_models',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=14,
                                                col_offset=43,
                                                end_lineno=14,
                                                end_col_offset=54,
                                                value=Attribute(
                                                    lineno=14,
                                                    col_offset=43,
                                                    end_lineno=14,
                                                    end_col_offset=51,
                                                    value=Name(lineno=14, col_offset=43, end_lineno=14, end_col_offset=47, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=21,
                            value=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=21, id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=18,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=22,
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=18, col_offset=15, end_lineno=18, end_col_offset=19, arg='self', annotation=None, type_comment=None),
                            arg(lineno=18, col_offset=21, end_lineno=18, end_col_offset=30, arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=66,
                            targets=[Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=15, id='records', ctx=Store())],
                            value=Call(
                                lineno=19,
                                col_offset=18,
                                end_lineno=19,
                                end_col_offset=66,
                                func=Attribute(
                                    lineno=19,
                                    col_offset=18,
                                    end_lineno=19,
                                    end_col_offset=55,
                                    value=Call(
                                        lineno=19,
                                        col_offset=18,
                                        end_lineno=19,
                                        end_col_offset=48,
                                        func=Name(lineno=19, col_offset=18, end_lineno=19, end_col_offset=23, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=19, col_offset=24, end_lineno=19, end_col_offset=41, id='IrConfigParameter', ctx=Load()),
                                            Name(lineno=19, col_offset=43, end_lineno=19, end_col_offset=47, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=19, col_offset=56, end_lineno=19, end_col_offset=65, id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=20,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=55,
                            test=Call(
                                lineno=20,
                                col_offset=11,
                                end_lineno=20,
                                end_col_offset=68,
                                func=Name(lineno=20, col_offset=11, end_lineno=20, end_col_offset=14, id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        lineno=20,
                                        col_offset=14,
                                        end_lineno=20,
                                        end_col_offset=68,
                                        elt=Compare(
                                            lineno=20,
                                            col_offset=15,
                                            end_lineno=20,
                                            end_col_offset=45,
                                            left=Attribute(
                                                lineno=20,
                                                col_offset=15,
                                                end_lineno=20,
                                                end_col_offset=25,
                                                value=Name(lineno=20, col_offset=15, end_lineno=20, end_col_offset=21, id='record', ctx=Load()),
                                                attr='key',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(lineno=20, col_offset=29, end_lineno=20, end_col_offset=45, value='crm.pls_fields', kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(lineno=20, col_offset=50, end_lineno=20, end_col_offset=56, id='record', ctx=Store()),
                                                iter=Name(lineno=20, col_offset=60, end_lineno=20, end_col_offset=67, id='records', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    lineno=21,
                                    col_offset=12,
                                    end_lineno=21,
                                    end_col_offset=24,
                                    value=Call(
                                        lineno=21,
                                        col_offset=12,
                                        end_lineno=21,
                                        end_col_offset=24,
                                        func=Attribute(
                                            lineno=21,
                                            col_offset=12,
                                            end_lineno=21,
                                            end_col_offset=22,
                                            value=Name(lineno=21, col_offset=12, end_lineno=21, end_col_offset=16, id='self', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=55,
                                    value=Call(
                                        lineno=22,
                                        col_offset=12,
                                        end_lineno=22,
                                        end_col_offset=55,
                                        func=Attribute(
                                            lineno=22,
                                            col_offset=12,
                                            end_lineno=22,
                                            end_col_offset=42,
                                            value=Attribute(
                                                lineno=22,
                                                col_offset=12,
                                                end_lineno=22,
                                                end_col_offset=29,
                                                value=Attribute(
                                                    lineno=22,
                                                    col_offset=12,
                                                    end_lineno=22,
                                                    end_col_offset=20,
                                                    value=Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=16, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='registry',
                                                ctx=Load(),
                                            ),
                                            attr='setup_models',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=22,
                                                col_offset=43,
                                                end_lineno=22,
                                                end_col_offset=54,
                                                value=Attribute(
                                                    lineno=22,
                                                    col_offset=43,
                                                    end_lineno=22,
                                                    end_col_offset=51,
                                                    value=Name(lineno=22, col_offset=43, end_lineno=22, end_col_offset=47, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=22,
                            value=Name(lineno=23, col_offset=15, end_lineno=23, end_col_offset=22, id='records', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=17,
                            col_offset=5,
                            end_lineno=17,
                            end_col_offset=27,
                            value=Name(lineno=17, col_offset=5, end_lineno=17, end_col_offset=8, id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=25,
                    col_offset=4,
                    end_lineno=31,
                    end_col_offset=26,
                    name='unlink',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=25, col_offset=15, end_lineno=25, end_col_offset=19, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=76,
                            targets=[Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=19, id='pls_emptied', ctx=Store())],
                            value=Call(
                                lineno=26,
                                col_offset=22,
                                end_lineno=26,
                                end_col_offset=76,
                                func=Name(lineno=26, col_offset=22, end_lineno=26, end_col_offset=25, id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        lineno=26,
                                        col_offset=25,
                                        end_lineno=26,
                                        end_col_offset=76,
                                        elt=Compare(
                                            lineno=26,
                                            col_offset=26,
                                            end_lineno=26,
                                            end_col_offset=56,
                                            left=Attribute(
                                                lineno=26,
                                                col_offset=26,
                                                end_lineno=26,
                                                end_col_offset=36,
                                                value=Name(lineno=26, col_offset=26, end_lineno=26, end_col_offset=32, id='record', ctx=Load()),
                                                attr='key',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(lineno=26, col_offset=40, end_lineno=26, end_col_offset=56, value='crm.pls_fields', kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(lineno=26, col_offset=61, end_lineno=26, end_col_offset=67, id='record', ctx=Store()),
                                                iter=Name(lineno=26, col_offset=71, end_lineno=26, end_col_offset=75, id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=27,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=56,
                            targets=[Name(lineno=27, col_offset=8, end_lineno=27, end_col_offset=14, id='result', ctx=Store())],
                            value=Call(
                                lineno=27,
                                col_offset=17,
                                end_lineno=27,
                                end_col_offset=56,
                                func=Attribute(
                                    lineno=27,
                                    col_offset=17,
                                    end_lineno=27,
                                    end_col_offset=54,
                                    value=Call(
                                        lineno=27,
                                        col_offset=17,
                                        end_lineno=27,
                                        end_col_offset=47,
                                        func=Name(lineno=27, col_offset=17, end_lineno=27, end_col_offset=22, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=27, col_offset=23, end_lineno=27, end_col_offset=40, id='IrConfigParameter', ctx=Load()),
                                            Name(lineno=27, col_offset=42, end_lineno=27, end_col_offset=46, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=28,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=55,
                            test=Name(lineno=28, col_offset=11, end_lineno=28, end_col_offset=22, id='pls_emptied', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=29,
                                    col_offset=12,
                                    end_lineno=29,
                                    end_col_offset=24,
                                    value=Call(
                                        lineno=29,
                                        col_offset=12,
                                        end_lineno=29,
                                        end_col_offset=24,
                                        func=Attribute(
                                            lineno=29,
                                            col_offset=12,
                                            end_lineno=29,
                                            end_col_offset=22,
                                            value=Name(lineno=29, col_offset=12, end_lineno=29, end_col_offset=16, id='self', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    lineno=30,
                                    col_offset=12,
                                    end_lineno=30,
                                    end_col_offset=55,
                                    value=Call(
                                        lineno=30,
                                        col_offset=12,
                                        end_lineno=30,
                                        end_col_offset=55,
                                        func=Attribute(
                                            lineno=30,
                                            col_offset=12,
                                            end_lineno=30,
                                            end_col_offset=42,
                                            value=Attribute(
                                                lineno=30,
                                                col_offset=12,
                                                end_lineno=30,
                                                end_col_offset=29,
                                                value=Attribute(
                                                    lineno=30,
                                                    col_offset=12,
                                                    end_lineno=30,
                                                    end_col_offset=20,
                                                    value=Name(lineno=30, col_offset=12, end_lineno=30, end_col_offset=16, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='registry',
                                                ctx=Load(),
                                            ),
                                            attr='setup_models',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=30,
                                                col_offset=43,
                                                end_lineno=30,
                                                end_col_offset=54,
                                                value=Attribute(
                                                    lineno=30,
                                                    col_offset=43,
                                                    end_lineno=30,
                                                    end_col_offset=51,
                                                    value=Name(lineno=30, col_offset=43, end_lineno=30, end_col_offset=47, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=26,
                            value=Name(lineno=31, col_offset=15, end_lineno=31, end_col_offset=26, id='pls_emptied', ctx=Load()),
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
