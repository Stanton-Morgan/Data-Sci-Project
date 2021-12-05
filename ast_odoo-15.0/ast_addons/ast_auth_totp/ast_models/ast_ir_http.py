Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=13,
            end_col_offset=19,
            name='IrHttp',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=13,
                    end_lineno=5,
                    end_col_offset=33,
                    value=Name(lineno=5, col_offset=13, end_lineno=5, end_col_offset=19, id='models', ctx=Load()),
                    attr='AbstractModel',
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
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=6, col_offset=15, end_lineno=6, end_col_offset=24, value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=8,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=19,
                    name='session_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=8, col_offset=21, end_lineno=8, end_col_offset=25, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=9,
                            col_offset=8,
                            end_lineno=9,
                            end_col_offset=37,
                            targets=[Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=12, id='info', ctx=Store())],
                            value=Call(
                                lineno=9,
                                col_offset=15,
                                end_lineno=9,
                                end_col_offset=37,
                                func=Attribute(
                                    lineno=9,
                                    col_offset=15,
                                    end_lineno=9,
                                    end_col_offset=35,
                                    value=Call(
                                        lineno=9,
                                        col_offset=15,
                                        end_lineno=9,
                                        end_col_offset=22,
                                        func=Name(lineno=9, col_offset=15, end_lineno=9, end_col_offset=20, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='session_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=46,
                            targets=[
                                Subscript(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=23,
                                    value=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=12, id='info', ctx=Load()),
                                    slice=Constant(lineno=12, col_offset=13, end_lineno=12, end_col_offset=22, value='user_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                lineno=12,
                                col_offset=26,
                                end_lineno=12,
                                end_col_offset=46,
                                elts=[
                                    Attribute(
                                        lineno=12,
                                        col_offset=26,
                                        end_lineno=12,
                                        end_col_offset=45,
                                        value=Attribute(
                                            lineno=12,
                                            col_offset=26,
                                            end_lineno=12,
                                            end_col_offset=41,
                                            value=Name(lineno=12, col_offset=26, end_lineno=12, end_col_offset=33, id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=19,
                            value=Name(lineno=13, col_offset=15, end_lineno=13, end_col_offset=19, id='info', ctx=Load()),
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
