Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=11,
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=21,
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=27,
            module='odoo.tools',
            names=[alias(name='misc', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=11,
            col_offset=0,
            end_lineno=23,
            end_col_offset=95,
            name='ImportController',
            bases=[
                Attribute(
                    lineno=11,
                    col_offset=23,
                    end_lineno=11,
                    end_col_offset=38,
                    value=Name(lineno=11, col_offset=23, end_lineno=11, end_col_offset=27, id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=95,
                    name='set_file',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=14, col_offset=17, end_lineno=14, end_col_offset=21, arg='self', annotation=None, type_comment=None),
                            arg(lineno=14, col_offset=23, end_lineno=14, end_col_offset=27, arg='file', annotation=None, type_comment=None),
                            arg(lineno=14, col_offset=29, end_lineno=14, end_col_offset=38, arg='import_id', annotation=None, type_comment=None),
                            arg(lineno=14, col_offset=40, end_lineno=14, end_col_offset=45, arg='jsonp', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=14, col_offset=46, end_lineno=14, end_col_offset=56, value='callback', kind=None)],
                    ),
                    body=[
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=34,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=17, id='import_id', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=20,
                                end_lineno=15,
                                end_col_offset=34,
                                func=Name(lineno=15, col_offset=20, end_lineno=15, end_col_offset=23, id='int', ctx=Load()),
                                args=[Name(lineno=15, col_offset=24, end_lineno=15, end_col_offset=33, id='import_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=10,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=15, id='written', ctx=Store())],
                            value=Call(
                                lineno=17,
                                col_offset=18,
                                end_lineno=21,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=17,
                                    col_offset=18,
                                    end_lineno=17,
                                    end_col_offset=75,
                                    value=Call(
                                        lineno=17,
                                        col_offset=18,
                                        end_lineno=17,
                                        end_col_offset=69,
                                        func=Attribute(
                                            lineno=17,
                                            col_offset=18,
                                            end_lineno=17,
                                            end_col_offset=58,
                                            value=Subscript(
                                                lineno=17,
                                                col_offset=18,
                                                end_lineno=17,
                                                end_col_offset=51,
                                                value=Attribute(
                                                    lineno=17,
                                                    col_offset=18,
                                                    end_lineno=17,
                                                    end_col_offset=29,
                                                    value=Name(lineno=17, col_offset=18, end_lineno=17, end_col_offset=25, id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=17, col_offset=30, end_lineno=17, end_col_offset=50, value='base_import.import', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=17, col_offset=59, end_lineno=17, end_col_offset=68, id='import_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=17,
                                        col_offset=76,
                                        end_lineno=21,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=18, col_offset=12, end_lineno=18, end_col_offset=18, value='file', kind=None),
                                            Constant(lineno=19, col_offset=12, end_lineno=19, end_col_offset=23, value='file_name', kind=None),
                                            Constant(lineno=20, col_offset=12, end_lineno=20, end_col_offset=23, value='file_type', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                lineno=18,
                                                col_offset=20,
                                                end_lineno=18,
                                                end_col_offset=31,
                                                func=Attribute(
                                                    lineno=18,
                                                    col_offset=20,
                                                    end_lineno=18,
                                                    end_col_offset=29,
                                                    value=Name(lineno=18, col_offset=20, end_lineno=18, end_col_offset=24, id='file', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                lineno=19,
                                                col_offset=25,
                                                end_lineno=19,
                                                end_col_offset=38,
                                                value=Name(lineno=19, col_offset=25, end_lineno=19, end_col_offset=29, id='file', ctx=Load()),
                                                attr='filename',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=20,
                                                col_offset=25,
                                                end_lineno=20,
                                                end_col_offset=42,
                                                value=Name(lineno=20, col_offset=25, end_lineno=20, end_col_offset=29, id='file', ctx=Load()),
                                                attr='content_type',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=95,
                            value=BinOp(
                                lineno=23,
                                col_offset=15,
                                end_lineno=23,
                                end_col_offset=95,
                                left=Constant(lineno=23, col_offset=15, end_lineno=23, end_col_offset=34, value='window.top.%s(%s)', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    lineno=23,
                                    col_offset=37,
                                    end_lineno=23,
                                    end_col_offset=95,
                                    elts=[
                                        Call(
                                            lineno=23,
                                            col_offset=38,
                                            end_lineno=23,
                                            end_col_offset=61,
                                            func=Attribute(
                                                lineno=23,
                                                col_offset=38,
                                                end_lineno=23,
                                                end_col_offset=54,
                                                value=Name(lineno=23, col_offset=38, end_lineno=23, end_col_offset=42, id='misc', ctx=Load()),
                                                attr='html_escape',
                                                ctx=Load(),
                                            ),
                                            args=[Name(lineno=23, col_offset=55, end_lineno=23, end_col_offset=60, id='jsonp', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Call(
                                            lineno=23,
                                            col_offset=63,
                                            end_lineno=23,
                                            end_col_offset=94,
                                            func=Attribute(
                                                lineno=23,
                                                col_offset=63,
                                                end_lineno=23,
                                                end_col_offset=73,
                                                value=Name(lineno=23, col_offset=63, end_lineno=23, end_col_offset=67, id='json', ctx=Load()),
                                                attr='dumps',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Dict(
                                                    lineno=23,
                                                    col_offset=74,
                                                    end_lineno=23,
                                                    end_col_offset=93,
                                                    keys=[Constant(lineno=23, col_offset=75, end_lineno=23, end_col_offset=83, value='result', kind=None)],
                                                    values=[Name(lineno=23, col_offset=85, end_lineno=23, end_col_offset=92, id='written', ctx=Load())],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=13,
                            col_offset=5,
                            end_lineno=13,
                            end_col_offset=58,
                            func=Attribute(
                                lineno=13,
                                col_offset=5,
                                end_lineno=13,
                                end_col_offset=15,
                                value=Name(lineno=13, col_offset=5, end_lineno=13, end_col_offset=9, id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=13, col_offset=16, end_lineno=13, end_col_offset=39, value='/base_import/set_file', kind=None)],
                            keywords=[
                                keyword(
                                    lineno=13,
                                    col_offset=41,
                                    end_lineno=13,
                                    end_col_offset=57,
                                    arg='methods',
                                    value=List(
                                        lineno=13,
                                        col_offset=49,
                                        end_lineno=13,
                                        end_col_offset=57,
                                        elts=[Constant(lineno=13, col_offset=50, end_lineno=13, end_col_offset=56, value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
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
