Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=32,
            end_col_offset=20,
            name='IrModelField',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=19,
                    end_lineno=7,
                    end_col_offset=31,
                    value=Name(lineno=7, col_offset=19, end_lineno=7, end_col_offset=25, id='models', ctx=Load()),
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
                    end_col_offset=32,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=32, value='ir.model.fields', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=5,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=12, id='tracking', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=15,
                        end_lineno=13,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=10,
                            col_offset=15,
                            end_lineno=10,
                            end_col_offset=29,
                            value=Name(lineno=10, col_offset=15, end_lineno=10, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=40,
                                arg='string',
                                value=Constant(lineno=11, col_offset=15, end_lineno=11, end_col_offset=40, value='Enable Ordered Tracking', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=126,
                                arg='help',
                                value=Constant(lineno=12, col_offset=13, end_lineno=12, end_col_offset=126, value='If set every modification done to this field is tracked in the chatter. Value is used to order tracking values.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=26,
                    end_col_offset=19,
                    name='_reflect_field_params',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=15, col_offset=30, end_lineno=15, end_col_offset=34, arg='self', annotation=None, type_comment=None),
                            arg(lineno=15, col_offset=36, end_lineno=15, end_col_offset=41, arg='field', annotation=None, type_comment=None),
                            arg(lineno=15, col_offset=43, end_lineno=15, end_col_offset=51, arg='model_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=16,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=23,
                            value=Constant(lineno=16, col_offset=8, end_lineno=18, end_col_offset=23, value=' Tracking value can be either a boolean enabling tracking mechanism\n        on field, either an integer giving the sequence. Default sequence is\n        set to 100. ', kind=None),
                        ),
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=79,
                            targets=[Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=12, id='vals', ctx=Store())],
                            value=Call(
                                lineno=19,
                                col_offset=15,
                                end_lineno=19,
                                end_col_offset=79,
                                func=Attribute(
                                    lineno=19,
                                    col_offset=15,
                                    end_lineno=19,
                                    end_col_offset=62,
                                    value=Call(
                                        lineno=19,
                                        col_offset=15,
                                        end_lineno=19,
                                        end_col_offset=40,
                                        func=Name(lineno=19, col_offset=15, end_lineno=19, end_col_offset=20, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=19, col_offset=21, end_lineno=19, end_col_offset=33, id='IrModelField', ctx=Load()),
                                            Name(lineno=19, col_offset=35, end_lineno=19, end_col_offset=39, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_reflect_field_params',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=19, col_offset=63, end_lineno=19, end_col_offset=68, id='field', ctx=Load()),
                                    Name(lineno=19, col_offset=70, end_lineno=19, end_col_offset=78, id='model_id', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=51,
                            targets=[Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=16, id='tracking', ctx=Store())],
                            value=Call(
                                lineno=20,
                                col_offset=19,
                                end_lineno=20,
                                end_col_offset=51,
                                func=Name(lineno=20, col_offset=19, end_lineno=20, end_col_offset=26, id='getattr', ctx=Load()),
                                args=[
                                    Name(lineno=20, col_offset=27, end_lineno=20, end_col_offset=32, id='field', ctx=Load()),
                                    Constant(lineno=20, col_offset=34, end_lineno=20, end_col_offset=44, value='tracking', kind=None),
                                    Constant(lineno=20, col_offset=46, end_lineno=20, end_col_offset=50, value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=21,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=27,
                            test=Compare(
                                lineno=21,
                                col_offset=11,
                                end_lineno=21,
                                end_col_offset=27,
                                left=Name(lineno=21, col_offset=11, end_lineno=21, end_col_offset=19, id='tracking', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(lineno=21, col_offset=23, end_lineno=21, end_col_offset=27, value=True, kind=None)],
                            ),
                            body=[
                                Assign(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=26,
                                    targets=[Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=20, id='tracking', ctx=Store())],
                                    value=Constant(lineno=22, col_offset=23, end_lineno=22, end_col_offset=26, value=100, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    lineno=23,
                                    col_offset=8,
                                    end_lineno=24,
                                    end_col_offset=27,
                                    test=Compare(
                                        lineno=23,
                                        col_offset=13,
                                        end_lineno=23,
                                        end_col_offset=30,
                                        left=Name(lineno=23, col_offset=13, end_lineno=23, end_col_offset=21, id='tracking', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(lineno=23, col_offset=25, end_lineno=23, end_col_offset=30, value=False, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=24,
                                            col_offset=12,
                                            end_lineno=24,
                                            end_col_offset=27,
                                            targets=[Name(lineno=24, col_offset=12, end_lineno=24, end_col_offset=20, id='tracking', ctx=Store())],
                                            value=Constant(lineno=24, col_offset=23, end_lineno=24, end_col_offset=27, value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=35,
                            targets=[
                                Subscript(
                                    lineno=25,
                                    col_offset=8,
                                    end_lineno=25,
                                    end_col_offset=24,
                                    value=Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=12, id='vals', ctx=Load()),
                                    slice=Constant(lineno=25, col_offset=13, end_lineno=25, end_col_offset=23, value='tracking', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(lineno=25, col_offset=27, end_lineno=25, end_col_offset=35, id='tracking', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=19,
                            value=Name(lineno=26, col_offset=15, end_lineno=26, end_col_offset=19, id='vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=28,
                    col_offset=4,
                    end_lineno=32,
                    end_col_offset=20,
                    name='_instanciate_attrs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=28, col_offset=27, end_lineno=28, end_col_offset=31, arg='self', annotation=None, type_comment=None),
                            arg(lineno=28, col_offset=33, end_lineno=28, end_col_offset=43, arg='field_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=72,
                            targets=[Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=13, id='attrs', ctx=Store())],
                            value=Call(
                                lineno=29,
                                col_offset=16,
                                end_lineno=29,
                                end_col_offset=72,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=16,
                                    end_lineno=29,
                                    end_col_offset=60,
                                    value=Call(
                                        lineno=29,
                                        col_offset=16,
                                        end_lineno=29,
                                        end_col_offset=41,
                                        func=Name(lineno=29, col_offset=16, end_lineno=29, end_col_offset=21, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=29, col_offset=22, end_lineno=29, end_col_offset=34, id='IrModelField', ctx=Load()),
                                            Name(lineno=29, col_offset=36, end_lineno=29, end_col_offset=40, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_instanciate_attrs',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=29, col_offset=61, end_lineno=29, end_col_offset=71, id='field_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=30,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=54,
                            test=BoolOp(
                                lineno=30,
                                col_offset=11,
                                end_lineno=30,
                                end_col_offset=47,
                                op=And(),
                                values=[
                                    Name(lineno=30, col_offset=11, end_lineno=30, end_col_offset=16, id='attrs', ctx=Load()),
                                    Call(
                                        lineno=30,
                                        col_offset=21,
                                        end_lineno=30,
                                        end_col_offset=47,
                                        func=Attribute(
                                            lineno=30,
                                            col_offset=21,
                                            end_lineno=30,
                                            end_col_offset=35,
                                            value=Name(lineno=30, col_offset=21, end_lineno=30, end_col_offset=31, id='field_data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=30, col_offset=36, end_lineno=30, end_col_offset=46, value='tracking', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    lineno=31,
                                    col_offset=12,
                                    end_lineno=31,
                                    end_col_offset=54,
                                    targets=[
                                        Subscript(
                                            lineno=31,
                                            col_offset=12,
                                            end_lineno=31,
                                            end_col_offset=29,
                                            value=Name(lineno=31, col_offset=12, end_lineno=31, end_col_offset=17, id='attrs', ctx=Load()),
                                            slice=Constant(lineno=31, col_offset=18, end_lineno=31, end_col_offset=28, value='tracking', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        lineno=31,
                                        col_offset=32,
                                        end_lineno=31,
                                        end_col_offset=54,
                                        value=Name(lineno=31, col_offset=32, end_lineno=31, end_col_offset=42, id='field_data', ctx=Load()),
                                        slice=Constant(lineno=31, col_offset=43, end_lineno=31, end_col_offset=53, value='tracking', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=20,
                            value=Name(lineno=32, col_offset=15, end_lineno=32, end_col_offset=20, id='attrs', ctx=Load()),
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