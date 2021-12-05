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
            end_lineno=11,
            end_col_offset=79,
            name='ResConfigSettings',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=24,
                    end_lineno=7,
                    end_col_offset=45,
                    value=Name(lineno=7, col_offset=24, end_lineno=7, end_col_offset=30, id='models', ctx=Load()),
                    attr='TransientModel',
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
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=36, value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=84,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=14, id='pad_server', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=17,
                        end_lineno=10,
                        end_col_offset=84,
                        func=Attribute(
                            lineno=10,
                            col_offset=17,
                            end_lineno=10,
                            end_col_offset=28,
                            value=Name(lineno=10, col_offset=17, end_lineno=10, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=29,
                                end_lineno=10,
                                end_col_offset=62,
                                arg='config_parameter',
                                value=Constant(lineno=10, col_offset=46, end_lineno=10, end_col_offset=62, value='pad.pad_server', kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=64,
                                end_lineno=10,
                                end_col_offset=83,
                                arg='string',
                                value=Constant(lineno=10, col_offset=71, end_lineno=10, end_col_offset=83, value='Pad Server', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=79,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=11, id='pad_key', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=14,
                        end_lineno=11,
                        end_col_offset=79,
                        func=Attribute(
                            lineno=11,
                            col_offset=14,
                            end_lineno=11,
                            end_col_offset=25,
                            value=Name(lineno=11, col_offset=14, end_lineno=11, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=26,
                                end_lineno=11,
                                end_col_offset=56,
                                arg='config_parameter',
                                value=Constant(lineno=11, col_offset=43, end_lineno=11, end_col_offset=56, value='pad.pad_key', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=58,
                                end_lineno=11,
                                end_col_offset=78,
                                arg='string',
                                value=Constant(lineno=11, col_offset=65, end_lineno=11, end_col_offset=78, value='Pad API Key', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)