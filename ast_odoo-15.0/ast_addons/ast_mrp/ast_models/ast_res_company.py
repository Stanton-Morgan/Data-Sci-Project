Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
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
            lineno=7,
            col_offset=0,
            end_lineno=38,
            end_col_offset=39,
            name='Company',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=14,
                    end_lineno=7,
                    end_col_offset=26,
                    value=Name(lineno=7, col_offset=14, end_lineno=7, end_col_offset=20, id='models', ctx=Load()),
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
                    end_col_offset=28,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=28, value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=63,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=22, id='manufacturing_lead', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=25,
                        end_lineno=12,
                        end_col_offset=63,
                        func=Attribute(
                            lineno=10,
                            col_offset=25,
                            end_lineno=10,
                            end_col_offset=37,
                            value=Name(lineno=10, col_offset=25, end_lineno=10, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=8, end_lineno=11, end_col_offset=33, value='Manufacturing Lead Time', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=35,
                                end_lineno=11,
                                end_col_offset=46,
                                arg='default',
                                value=Constant(lineno=11, col_offset=43, end_lineno=11, end_col_offset=46, value=0.0, kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=48,
                                end_lineno=11,
                                end_col_offset=61,
                                arg='required',
                                value=Constant(lineno=11, col_offset=57, end_lineno=11, end_col_offset=61, value=True, kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=62,
                                arg='help',
                                value=Constant(lineno=12, col_offset=13, end_lineno=12, end_col_offset=62, value='Security days for each manufacturing operation.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=56,
                    name='_create_unbuild_sequence',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=33, end_lineno=14, end_col_offset=37, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=25,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=20, id='unbuild_vals', ctx=Store())],
                            value=List(lineno=15, col_offset=23, end_lineno=15, end_col_offset=25, elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            lineno=16,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=14,
                            target=Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=19, id='company', ctx=Store()),
                            iter=Name(lineno=16, col_offset=23, end_lineno=16, end_col_offset=27, id='self', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=25,
                                    end_col_offset=14,
                                    value=Call(
                                        lineno=17,
                                        col_offset=12,
                                        end_lineno=25,
                                        end_col_offset=14,
                                        func=Attribute(
                                            lineno=17,
                                            col_offset=12,
                                            end_lineno=17,
                                            end_col_offset=31,
                                            value=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=24, id='unbuild_vals', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=17,
                                                col_offset=32,
                                                end_lineno=25,
                                                end_col_offset=13,
                                                keys=[
                                                    Constant(lineno=18, col_offset=16, end_lineno=18, end_col_offset=22, value='name', kind=None),
                                                    Constant(lineno=19, col_offset=16, end_lineno=19, end_col_offset=22, value='code', kind=None),
                                                    Constant(lineno=20, col_offset=16, end_lineno=20, end_col_offset=28, value='company_id', kind=None),
                                                    Constant(lineno=21, col_offset=16, end_lineno=21, end_col_offset=24, value='prefix', kind=None),
                                                    Constant(lineno=22, col_offset=16, end_lineno=22, end_col_offset=25, value='padding', kind=None),
                                                    Constant(lineno=23, col_offset=16, end_lineno=23, end_col_offset=29, value='number_next', kind=None),
                                                    Constant(lineno=24, col_offset=16, end_lineno=24, end_col_offset=34, value='number_increment', kind=None),
                                                ],
                                                values=[
                                                    Constant(lineno=18, col_offset=24, end_lineno=18, end_col_offset=33, value='Unbuild', kind=None),
                                                    Constant(lineno=19, col_offset=24, end_lineno=19, end_col_offset=37, value='mrp.unbuild', kind=None),
                                                    Attribute(
                                                        lineno=20,
                                                        col_offset=30,
                                                        end_lineno=20,
                                                        end_col_offset=40,
                                                        value=Name(lineno=20, col_offset=30, end_lineno=20, end_col_offset=37, id='company', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=21, col_offset=26, end_lineno=21, end_col_offset=31, value='UB/', kind=None),
                                                    Constant(lineno=22, col_offset=27, end_lineno=22, end_col_offset=28, value=5, kind=None),
                                                    Constant(lineno=23, col_offset=31, end_lineno=23, end_col_offset=32, value=1, kind=None),
                                                    Constant(lineno=24, col_offset=36, end_lineno=24, end_col_offset=37, value=1, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            lineno=26,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=56,
                            test=Name(lineno=26, col_offset=11, end_lineno=26, end_col_offset=23, id='unbuild_vals', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=27,
                                    col_offset=12,
                                    end_lineno=27,
                                    end_col_offset=56,
                                    value=Call(
                                        lineno=27,
                                        col_offset=12,
                                        end_lineno=27,
                                        end_col_offset=56,
                                        func=Attribute(
                                            lineno=27,
                                            col_offset=12,
                                            end_lineno=27,
                                            end_col_offset=42,
                                            value=Subscript(
                                                lineno=27,
                                                col_offset=12,
                                                end_lineno=27,
                                                end_col_offset=35,
                                                value=Attribute(
                                                    lineno=27,
                                                    col_offset=12,
                                                    end_lineno=27,
                                                    end_col_offset=20,
                                                    value=Name(lineno=27, col_offset=12, end_lineno=27, end_col_offset=16, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=27, col_offset=21, end_lineno=27, end_col_offset=34, value='ir.sequence', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=27, col_offset=43, end_lineno=27, end_col_offset=55, id='unbuild_vals', ctx=Load())],
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
                FunctionDef(
                    lineno=30,
                    col_offset=4,
                    end_lineno=34,
                    end_col_offset=56,
                    name='create_missing_unbuild_sequences',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=30, col_offset=41, end_lineno=30, end_col_offset=45, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=57,
                            targets=[Name(lineno=31, col_offset=8, end_lineno=31, end_col_offset=19, id='company_ids', ctx=Store())],
                            value=Call(
                                lineno=31,
                                col_offset=23,
                                end_lineno=31,
                                end_col_offset=57,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=23,
                                    end_lineno=31,
                                    end_col_offset=53,
                                    value=Subscript(
                                        lineno=31,
                                        col_offset=23,
                                        end_lineno=31,
                                        end_col_offset=46,
                                        value=Attribute(
                                            lineno=31,
                                            col_offset=23,
                                            end_lineno=31,
                                            end_col_offset=31,
                                            value=Name(lineno=31, col_offset=23, end_lineno=31, end_col_offset=27, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=31, col_offset=32, end_lineno=31, end_col_offset=45, value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(lineno=31, col_offset=54, end_lineno=31, end_col_offset=56, elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=117,
                            targets=[Name(lineno=32, col_offset=8, end_lineno=32, end_col_offset=31, id='company_has_unbuild_seq', ctx=Store())],
                            value=Call(
                                lineno=32,
                                col_offset=34,
                                end_lineno=32,
                                end_col_offset=117,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=34,
                                    end_lineno=32,
                                    end_col_offset=103,
                                    value=Call(
                                        lineno=32,
                                        col_offset=34,
                                        end_lineno=32,
                                        end_col_offset=96,
                                        func=Attribute(
                                            lineno=32,
                                            col_offset=34,
                                            end_lineno=32,
                                            end_col_offset=64,
                                            value=Subscript(
                                                lineno=32,
                                                col_offset=34,
                                                end_lineno=32,
                                                end_col_offset=57,
                                                value=Attribute(
                                                    lineno=32,
                                                    col_offset=34,
                                                    end_lineno=32,
                                                    end_col_offset=42,
                                                    value=Name(lineno=32, col_offset=34, end_lineno=32, end_col_offset=38, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=32, col_offset=43, end_lineno=32, end_col_offset=56, value='ir.sequence', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                lineno=32,
                                                col_offset=65,
                                                end_lineno=32,
                                                end_col_offset=95,
                                                elts=[
                                                    Tuple(
                                                        lineno=32,
                                                        col_offset=66,
                                                        end_lineno=32,
                                                        end_col_offset=94,
                                                        elts=[
                                                            Constant(lineno=32, col_offset=67, end_lineno=32, end_col_offset=73, value='code', kind=None),
                                                            Constant(lineno=32, col_offset=75, end_lineno=32, end_col_offset=78, value='=', kind=None),
                                                            Constant(lineno=32, col_offset=80, end_lineno=32, end_col_offset=93, value='mrp.unbuild', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=32, col_offset=104, end_lineno=32, end_col_offset=116, value='company_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=33,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=69,
                            targets=[Name(lineno=33, col_offset=8, end_lineno=33, end_col_offset=29, id='company_todo_sequence', ctx=Store())],
                            value=BinOp(
                                lineno=33,
                                col_offset=32,
                                end_lineno=33,
                                end_col_offset=69,
                                left=Name(lineno=33, col_offset=32, end_lineno=33, end_col_offset=43, id='company_ids', ctx=Load()),
                                op=Sub(),
                                right=Name(lineno=33, col_offset=46, end_lineno=33, end_col_offset=69, id='company_has_unbuild_seq', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=56,
                            value=Call(
                                lineno=34,
                                col_offset=8,
                                end_lineno=34,
                                end_col_offset=56,
                                func=Attribute(
                                    lineno=34,
                                    col_offset=8,
                                    end_lineno=34,
                                    end_col_offset=54,
                                    value=Name(lineno=34, col_offset=8, end_lineno=34, end_col_offset=29, id='company_todo_sequence', ctx=Load()),
                                    attr='_create_unbuild_sequence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=29,
                            col_offset=5,
                            end_lineno=29,
                            end_col_offset=14,
                            value=Name(lineno=29, col_offset=5, end_lineno=29, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=36,
                    col_offset=4,
                    end_lineno=38,
                    end_col_offset=39,
                    name='_create_per_company_sequences',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=36, col_offset=38, end_lineno=36, end_col_offset=42, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=37,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=60,
                            value=Call(
                                lineno=37,
                                col_offset=8,
                                end_lineno=37,
                                end_col_offset=60,
                                func=Attribute(
                                    lineno=37,
                                    col_offset=8,
                                    end_lineno=37,
                                    end_col_offset=58,
                                    value=Call(
                                        lineno=37,
                                        col_offset=8,
                                        end_lineno=37,
                                        end_col_offset=28,
                                        func=Name(lineno=37, col_offset=8, end_lineno=37, end_col_offset=13, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=37, col_offset=14, end_lineno=37, end_col_offset=21, id='Company', ctx=Load()),
                                            Name(lineno=37, col_offset=23, end_lineno=37, end_col_offset=27, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_create_per_company_sequences',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=38,
                            col_offset=8,
                            end_lineno=38,
                            end_col_offset=39,
                            value=Call(
                                lineno=38,
                                col_offset=8,
                                end_lineno=38,
                                end_col_offset=39,
                                func=Attribute(
                                    lineno=38,
                                    col_offset=8,
                                    end_lineno=38,
                                    end_col_offset=37,
                                    value=Name(lineno=38, col_offset=8, end_lineno=38, end_col_offset=12, id='self', ctx=Load()),
                                    attr='_create_unbuild_sequence',
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
