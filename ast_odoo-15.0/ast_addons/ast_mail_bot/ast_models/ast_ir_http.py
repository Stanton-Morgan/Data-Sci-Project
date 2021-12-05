Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=14,
            end_col_offset=18,
            name='Http',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=11,
                    end_lineno=7,
                    end_col_offset=31,
                    value=Name(lineno=7, col_offset=11, end_lineno=7, end_col_offset=17, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=24,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=24, value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=18,
                    name='session_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=21, end_lineno=10, end_col_offset=25, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=46,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=11,
                                col_offset=14,
                                end_lineno=11,
                                end_col_offset=46,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=14,
                                    end_lineno=11,
                                    end_col_offset=44,
                                    value=Call(
                                        lineno=11,
                                        col_offset=14,
                                        end_lineno=11,
                                        end_col_offset=31,
                                        func=Name(lineno=11, col_offset=14, end_lineno=11, end_col_offset=19, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=11, col_offset=20, end_lineno=11, end_col_offset=24, id='Http', ctx=Load()),
                                            Name(lineno=11, col_offset=26, end_lineno=11, end_col_offset=30, id='self', ctx=Load()),
                                        ],
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
                        If(
                            lineno=12,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=102,
                            test=Call(
                                lineno=12,
                                col_offset=11,
                                end_lineno=12,
                                end_col_offset=53,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=11,
                                    end_lineno=12,
                                    end_col_offset=34,
                                    value=Attribute(
                                        lineno=12,
                                        col_offset=11,
                                        end_lineno=12,
                                        end_col_offset=24,
                                        value=Attribute(
                                            lineno=12,
                                            col_offset=11,
                                            end_lineno=12,
                                            end_col_offset=19,
                                            value=Name(lineno=12, col_offset=11, end_lineno=12, end_col_offset=15, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=12, col_offset=35, end_lineno=12, end_col_offset=52, value='base.group_user', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    lineno=13,
                                    col_offset=12,
                                    end_lineno=13,
                                    end_col_offset=102,
                                    targets=[
                                        Subscript(
                                            lineno=13,
                                            col_offset=12,
                                            end_lineno=13,
                                            end_col_offset=38,
                                            value=Name(lineno=13, col_offset=12, end_lineno=13, end_col_offset=15, id='res', ctx=Load()),
                                            slice=Constant(lineno=13, col_offset=16, end_lineno=13, end_col_offset=37, value='odoobot_initialized', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        lineno=13,
                                        col_offset=41,
                                        end_lineno=13,
                                        end_col_offset=102,
                                        left=Attribute(
                                            lineno=13,
                                            col_offset=41,
                                            end_lineno=13,
                                            end_col_offset=68,
                                            value=Attribute(
                                                lineno=13,
                                                col_offset=41,
                                                end_lineno=13,
                                                end_col_offset=54,
                                                value=Attribute(
                                                    lineno=13,
                                                    col_offset=41,
                                                    end_lineno=13,
                                                    end_col_offset=49,
                                                    value=Name(lineno=13, col_offset=41, end_lineno=13, end_col_offset=45, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='odoobot_state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            List(
                                                lineno=13,
                                                col_offset=76,
                                                end_lineno=13,
                                                end_col_offset=102,
                                                elts=[
                                                    Constant(lineno=13, col_offset=77, end_lineno=13, end_col_offset=82, value=False, kind=None),
                                                    Constant(lineno=13, col_offset=84, end_lineno=13, end_col_offset=101, value='not_initialized', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=18,
                            value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=18, id='res', ctx=Load()),
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
