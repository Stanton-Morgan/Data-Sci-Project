Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
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
            lineno=6,
            col_offset=0,
            end_lineno=14,
            end_col_offset=54,
            name='WebsiteRobots',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=20,
                    end_lineno=6,
                    end_col_offset=41,
                    value=Name(lineno=6, col_offset=20, end_lineno=6, end_col_offset=26, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=28,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=7, col_offset=12, end_lineno=7, end_col_offset=28, value='website.robots', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=38,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=8, col_offset=19, end_lineno=8, end_col_offset=38, value='Robots.txt Editor', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=94,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=11, id='content', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=14,
                        end_lineno=10,
                        end_col_offset=94,
                        func=Attribute(
                            lineno=10,
                            col_offset=14,
                            end_lineno=10,
                            end_col_offset=25,
                            value=Name(lineno=10, col_offset=14, end_lineno=10, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=26,
                                end_lineno=10,
                                end_col_offset=93,
                                arg='default',
                                value=Lambda(
                                    lineno=10,
                                    col_offset=34,
                                    end_lineno=10,
                                    end_col_offset=93,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=10, col_offset=41, end_lineno=10, end_col_offset=42, arg='s', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        lineno=10,
                                        col_offset=44,
                                        end_lineno=10,
                                        end_col_offset=93,
                                        value=Call(
                                            lineno=10,
                                            col_offset=44,
                                            end_lineno=10,
                                            end_col_offset=82,
                                            func=Attribute(
                                                lineno=10,
                                                col_offset=44,
                                                end_lineno=10,
                                                end_col_offset=80,
                                                value=Subscript(
                                                    lineno=10,
                                                    col_offset=44,
                                                    end_lineno=10,
                                                    end_col_offset=60,
                                                    value=Attribute(
                                                        lineno=10,
                                                        col_offset=44,
                                                        end_lineno=10,
                                                        end_col_offset=49,
                                                        value=Name(lineno=10, col_offset=44, end_lineno=10, end_col_offset=45, id='s', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(lineno=10, col_offset=50, end_lineno=10, end_col_offset=59, value='website', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='get_current_website',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='robots_txt',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=54,
                    name='action_save',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=12, col_offset=20, end_lineno=12, end_col_offset=24, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=75,
                            targets=[
                                Attribute(
                                    lineno=13,
                                    col_offset=8,
                                    end_lineno=13,
                                    end_col_offset=60,
                                    value=Call(
                                        lineno=13,
                                        col_offset=8,
                                        end_lineno=13,
                                        end_col_offset=49,
                                        func=Attribute(
                                            lineno=13,
                                            col_offset=8,
                                            end_lineno=13,
                                            end_col_offset=47,
                                            value=Subscript(
                                                lineno=13,
                                                col_offset=8,
                                                end_lineno=13,
                                                end_col_offset=27,
                                                value=Attribute(
                                                    lineno=13,
                                                    col_offset=8,
                                                    end_lineno=13,
                                                    end_col_offset=16,
                                                    value=Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=12, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=13, col_offset=17, end_lineno=13, end_col_offset=26, value='website', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_current_website',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='robots_txt',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                lineno=13,
                                col_offset=63,
                                end_lineno=13,
                                end_col_offset=75,
                                value=Name(lineno=13, col_offset=63, end_lineno=13, end_col_offset=67, id='self', ctx=Load()),
                                attr='content',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=54,
                            value=Dict(
                                lineno=14,
                                col_offset=15,
                                end_lineno=14,
                                end_col_offset=54,
                                keys=[Constant(lineno=14, col_offset=16, end_lineno=14, end_col_offset=22, value='type', kind=None)],
                                values=[Constant(lineno=14, col_offset=24, end_lineno=14, end_col_offset=53, value='ir.actions.act_window_close', kind=None)],
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