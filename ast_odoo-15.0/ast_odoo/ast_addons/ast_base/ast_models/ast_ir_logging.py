Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=43,
            end_col_offset=96,
            name='IrLogging',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=16,
                    end_lineno=5,
                    end_col_offset=28,
                    value=Name(lineno=5, col_offset=16, end_lineno=5, end_col_offset=22, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=6,
                    col_offset=4,
                    end_lineno=6,
                    end_col_offset=24,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=6, col_offset=12, end_lineno=6, end_col_offset=24, value='ir.logging', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=28,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=7, col_offset=19, end_lineno=7, end_col_offset=28, value='Logging', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=22,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=8, col_offset=13, end_lineno=8, end_col_offset=22, value='id DESC', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=21,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=67,
                    targets=[Name(lineno=21, col_offset=4, end_lineno=21, end_col_offset=14, id='create_uid', ctx=Store())],
                    value=Call(
                        lineno=21,
                        col_offset=17,
                        end_lineno=21,
                        end_col_offset=67,
                        func=Attribute(
                            lineno=21,
                            col_offset=17,
                            end_lineno=21,
                            end_col_offset=31,
                            value=Name(lineno=21, col_offset=17, end_lineno=21, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=21,
                                col_offset=32,
                                end_lineno=21,
                                end_col_offset=51,
                                arg='string',
                                value=Constant(lineno=21, col_offset=39, end_lineno=21, end_col_offset=51, value='Created by', kind=None),
                            ),
                            keyword(
                                lineno=21,
                                col_offset=53,
                                end_lineno=21,
                                end_col_offset=66,
                                arg='readonly',
                                value=Constant(lineno=21, col_offset=62, end_lineno=21, end_col_offset=66, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=22,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=69,
                    targets=[Name(lineno=22, col_offset=4, end_lineno=22, end_col_offset=15, id='create_date', ctx=Store())],
                    value=Call(
                        lineno=22,
                        col_offset=18,
                        end_lineno=22,
                        end_col_offset=69,
                        func=Attribute(
                            lineno=22,
                            col_offset=18,
                            end_lineno=22,
                            end_col_offset=33,
                            value=Name(lineno=22, col_offset=18, end_lineno=22, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=22,
                                col_offset=34,
                                end_lineno=22,
                                end_col_offset=53,
                                arg='string',
                                value=Constant(lineno=22, col_offset=41, end_lineno=22, end_col_offset=53, value='Created on', kind=None),
                            ),
                            keyword(
                                lineno=22,
                                col_offset=55,
                                end_lineno=22,
                                end_col_offset=68,
                                arg='readonly',
                                value=Constant(lineno=22, col_offset=64, end_lineno=22, end_col_offset=68, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=23,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=71,
                    targets=[Name(lineno=23, col_offset=4, end_lineno=23, end_col_offset=13, id='write_uid', ctx=Store())],
                    value=Call(
                        lineno=23,
                        col_offset=16,
                        end_lineno=23,
                        end_col_offset=71,
                        func=Attribute(
                            lineno=23,
                            col_offset=16,
                            end_lineno=23,
                            end_col_offset=30,
                            value=Name(lineno=23, col_offset=16, end_lineno=23, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=23,
                                col_offset=31,
                                end_lineno=23,
                                end_col_offset=55,
                                arg='string',
                                value=Constant(lineno=23, col_offset=38, end_lineno=23, end_col_offset=55, value='Last Updated by', kind=None),
                            ),
                            keyword(
                                lineno=23,
                                col_offset=57,
                                end_lineno=23,
                                end_col_offset=70,
                                arg='readonly',
                                value=Constant(lineno=23, col_offset=66, end_lineno=23, end_col_offset=70, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=24,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=73,
                    targets=[Name(lineno=24, col_offset=4, end_lineno=24, end_col_offset=14, id='write_date', ctx=Store())],
                    value=Call(
                        lineno=24,
                        col_offset=17,
                        end_lineno=24,
                        end_col_offset=73,
                        func=Attribute(
                            lineno=24,
                            col_offset=17,
                            end_lineno=24,
                            end_col_offset=32,
                            value=Name(lineno=24, col_offset=17, end_lineno=24, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=24,
                                col_offset=33,
                                end_lineno=24,
                                end_col_offset=57,
                                arg='string',
                                value=Constant(lineno=24, col_offset=40, end_lineno=24, end_col_offset=57, value='Last Updated on', kind=None),
                            ),
                            keyword(
                                lineno=24,
                                col_offset=59,
                                end_lineno=24,
                                end_col_offset=72,
                                arg='readonly',
                                value=Constant(lineno=24, col_offset=68, end_lineno=24, end_col_offset=72, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=26,
                    col_offset=4,
                    end_lineno=26,
                    end_col_offset=37,
                    targets=[Name(lineno=26, col_offset=4, end_lineno=26, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=26,
                        col_offset=11,
                        end_lineno=26,
                        end_col_offset=37,
                        func=Attribute(
                            lineno=26,
                            col_offset=11,
                            end_lineno=26,
                            end_col_offset=22,
                            value=Name(lineno=26, col_offset=11, end_lineno=26, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=26,
                                col_offset=23,
                                end_lineno=26,
                                end_col_offset=36,
                                arg='required',
                                value=Constant(lineno=26, col_offset=32, end_lineno=26, end_col_offset=36, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=27,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=100,
                    targets=[Name(lineno=27, col_offset=4, end_lineno=27, end_col_offset=8, id='type', ctx=Store())],
                    value=Call(
                        lineno=27,
                        col_offset=11,
                        end_lineno=27,
                        end_col_offset=100,
                        func=Attribute(
                            lineno=27,
                            col_offset=11,
                            end_lineno=27,
                            end_col_offset=27,
                            value=Name(lineno=27, col_offset=11, end_lineno=27, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                lineno=27,
                                col_offset=28,
                                end_lineno=27,
                                end_col_offset=72,
                                elts=[
                                    Tuple(
                                        lineno=27,
                                        col_offset=29,
                                        end_lineno=27,
                                        end_col_offset=49,
                                        elts=[
                                            Constant(lineno=27, col_offset=30, end_lineno=27, end_col_offset=38, value='client', kind=None),
                                            Constant(lineno=27, col_offset=40, end_lineno=27, end_col_offset=48, value='Client', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=27,
                                        col_offset=51,
                                        end_lineno=27,
                                        end_col_offset=71,
                                        elts=[
                                            Constant(lineno=27, col_offset=52, end_lineno=27, end_col_offset=60, value='server', kind=None),
                                            Constant(lineno=27, col_offset=62, end_lineno=27, end_col_offset=70, value='Server', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                lineno=27,
                                col_offset=74,
                                end_lineno=27,
                                end_col_offset=87,
                                arg='required',
                                value=Constant(lineno=27, col_offset=83, end_lineno=27, end_col_offset=87, value=True, kind=None),
                            ),
                            keyword(
                                lineno=27,
                                col_offset=89,
                                end_lineno=27,
                                end_col_offset=99,
                                arg='index',
                                value=Constant(lineno=27, col_offset=95, end_lineno=27, end_col_offset=99, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=28,
                    col_offset=4,
                    end_lineno=28,
                    end_col_offset=60,
                    targets=[Name(lineno=28, col_offset=4, end_lineno=28, end_col_offset=10, id='dbname', ctx=Store())],
                    value=Call(
                        lineno=28,
                        col_offset=13,
                        end_lineno=28,
                        end_col_offset=60,
                        func=Attribute(
                            lineno=28,
                            col_offset=13,
                            end_lineno=28,
                            end_col_offset=24,
                            value=Name(lineno=28, col_offset=13, end_lineno=28, end_col_offset=19, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=28,
                                col_offset=25,
                                end_lineno=28,
                                end_col_offset=47,
                                arg='string',
                                value=Constant(lineno=28, col_offset=32, end_lineno=28, end_col_offset=47, value='Database Name', kind=None),
                            ),
                            keyword(
                                lineno=28,
                                col_offset=49,
                                end_lineno=28,
                                end_col_offset=59,
                                arg='index',
                                value=Constant(lineno=28, col_offset=55, end_lineno=28, end_col_offset=59, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=29,
                    col_offset=4,
                    end_lineno=29,
                    end_col_offset=35,
                    targets=[Name(lineno=29, col_offset=4, end_lineno=29, end_col_offset=9, id='level', ctx=Store())],
                    value=Call(
                        lineno=29,
                        col_offset=12,
                        end_lineno=29,
                        end_col_offset=35,
                        func=Attribute(
                            lineno=29,
                            col_offset=12,
                            end_lineno=29,
                            end_col_offset=23,
                            value=Name(lineno=29, col_offset=12, end_lineno=29, end_col_offset=18, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=29,
                                col_offset=24,
                                end_lineno=29,
                                end_col_offset=34,
                                arg='index',
                                value=Constant(lineno=29, col_offset=30, end_lineno=29, end_col_offset=34, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=30,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=40,
                    targets=[Name(lineno=30, col_offset=4, end_lineno=30, end_col_offset=11, id='message', ctx=Store())],
                    value=Call(
                        lineno=30,
                        col_offset=14,
                        end_lineno=30,
                        end_col_offset=40,
                        func=Attribute(
                            lineno=30,
                            col_offset=14,
                            end_lineno=30,
                            end_col_offset=25,
                            value=Name(lineno=30, col_offset=14, end_lineno=30, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=30,
                                col_offset=26,
                                end_lineno=30,
                                end_col_offset=39,
                                arg='required',
                                value=Constant(lineno=30, col_offset=35, end_lineno=30, end_col_offset=39, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=31,
                    col_offset=4,
                    end_lineno=31,
                    end_col_offset=37,
                    targets=[Name(lineno=31, col_offset=4, end_lineno=31, end_col_offset=8, id='path', ctx=Store())],
                    value=Call(
                        lineno=31,
                        col_offset=11,
                        end_lineno=31,
                        end_col_offset=37,
                        func=Attribute(
                            lineno=31,
                            col_offset=11,
                            end_lineno=31,
                            end_col_offset=22,
                            value=Name(lineno=31, col_offset=11, end_lineno=31, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=31,
                                col_offset=23,
                                end_lineno=31,
                                end_col_offset=36,
                                arg='required',
                                value=Constant(lineno=31, col_offset=32, end_lineno=31, end_col_offset=36, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=32,
                    col_offset=4,
                    end_lineno=32,
                    end_col_offset=56,
                    targets=[Name(lineno=32, col_offset=4, end_lineno=32, end_col_offset=8, id='func', ctx=Store())],
                    value=Call(
                        lineno=32,
                        col_offset=11,
                        end_lineno=32,
                        end_col_offset=56,
                        func=Attribute(
                            lineno=32,
                            col_offset=11,
                            end_lineno=32,
                            end_col_offset=22,
                            value=Name(lineno=32, col_offset=11, end_lineno=32, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=32,
                                col_offset=23,
                                end_lineno=32,
                                end_col_offset=40,
                                arg='string',
                                value=Constant(lineno=32, col_offset=30, end_lineno=32, end_col_offset=40, value='Function', kind=None),
                            ),
                            keyword(
                                lineno=32,
                                col_offset=42,
                                end_lineno=32,
                                end_col_offset=55,
                                arg='required',
                                value=Constant(lineno=32, col_offset=51, end_lineno=32, end_col_offset=55, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=33,
                    col_offset=4,
                    end_lineno=33,
                    end_col_offset=37,
                    targets=[Name(lineno=33, col_offset=4, end_lineno=33, end_col_offset=8, id='line', ctx=Store())],
                    value=Call(
                        lineno=33,
                        col_offset=11,
                        end_lineno=33,
                        end_col_offset=37,
                        func=Attribute(
                            lineno=33,
                            col_offset=11,
                            end_lineno=33,
                            end_col_offset=22,
                            value=Name(lineno=33, col_offset=11, end_lineno=33, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=33,
                                col_offset=23,
                                end_lineno=33,
                                end_col_offset=36,
                                arg='required',
                                value=Constant(lineno=33, col_offset=32, end_lineno=33, end_col_offset=36, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=35,
                    col_offset=4,
                    end_lineno=43,
                    end_col_offset=96,
                    name='init',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=35, col_offset=13, end_lineno=35, end_col_offset=17, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=36,
                            col_offset=8,
                            end_lineno=36,
                            end_col_offset=37,
                            value=Call(
                                lineno=36,
                                col_offset=8,
                                end_lineno=36,
                                end_col_offset=37,
                                func=Attribute(
                                    lineno=36,
                                    col_offset=8,
                                    end_lineno=36,
                                    end_col_offset=35,
                                    value=Call(
                                        lineno=36,
                                        col_offset=8,
                                        end_lineno=36,
                                        end_col_offset=30,
                                        func=Name(lineno=36, col_offset=8, end_lineno=36, end_col_offset=13, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=36, col_offset=14, end_lineno=36, end_col_offset=23, id='IrLogging', ctx=Load()),
                                            Name(lineno=36, col_offset=25, end_lineno=36, end_col_offset=29, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='init',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=37,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=166,
                            value=Call(
                                lineno=37,
                                col_offset=8,
                                end_lineno=37,
                                end_col_offset=166,
                                func=Attribute(
                                    lineno=37,
                                    col_offset=8,
                                    end_lineno=37,
                                    end_col_offset=24,
                                    value=Attribute(
                                        lineno=37,
                                        col_offset=8,
                                        end_lineno=37,
                                        end_col_offset=16,
                                        value=Name(lineno=37, col_offset=8, end_lineno=37, end_col_offset=12, id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=37, col_offset=25, end_lineno=37, end_col_offset=165, value="select 1 from information_schema.constraint_column_usage where table_name = 'ir_logging' and constraint_name = 'ir_logging_write_uid_fkey'", kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            lineno=38,
                            col_offset=8,
                            end_lineno=43,
                            end_col_offset=96,
                            test=Attribute(
                                lineno=38,
                                col_offset=11,
                                end_lineno=38,
                                end_col_offset=28,
                                value=Attribute(
                                    lineno=38,
                                    col_offset=11,
                                    end_lineno=38,
                                    end_col_offset=19,
                                    value=Name(lineno=38, col_offset=11, end_lineno=38, end_col_offset=15, id='self', ctx=Load()),
                                    attr='_cr',
                                    ctx=Load(),
                                ),
                                attr='rowcount',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    lineno=43,
                                    col_offset=12,
                                    end_lineno=43,
                                    end_col_offset=96,
                                    value=Call(
                                        lineno=43,
                                        col_offset=12,
                                        end_lineno=43,
                                        end_col_offset=96,
                                        func=Attribute(
                                            lineno=43,
                                            col_offset=12,
                                            end_lineno=43,
                                            end_col_offset=28,
                                            value=Attribute(
                                                lineno=43,
                                                col_offset=12,
                                                end_lineno=43,
                                                end_col_offset=20,
                                                value=Name(lineno=43, col_offset=12, end_lineno=43, end_col_offset=16, id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=43, col_offset=29, end_lineno=43, end_col_offset=95, value='ALTER TABLE ir_logging DROP CONSTRAINT ir_logging_write_uid_fkey', kind=None)],
                                        keywords=[],
                                    ),
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