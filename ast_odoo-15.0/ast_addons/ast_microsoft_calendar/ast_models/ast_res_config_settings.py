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
            end_lineno=11,
            end_col_offset=134,
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
                    end_col_offset=125,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=27, id='cal_microsoft_client_id', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=30,
                        end_lineno=10,
                        end_col_offset=125,
                        func=Attribute(
                            lineno=10,
                            col_offset=30,
                            end_lineno=10,
                            end_col_offset=41,
                            value=Name(lineno=10, col_offset=30, end_lineno=10, end_col_offset=36, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=42, end_lineno=10, end_col_offset=63, value='Microsoft Client_id', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=65,
                                end_lineno=10,
                                end_col_offset=112,
                                arg='config_parameter',
                                value=Constant(lineno=10, col_offset=82, end_lineno=10, end_col_offset=112, value='microsoft_calendar_client_id', kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=114,
                                end_lineno=10,
                                end_col_offset=124,
                                arg='default',
                                value=Constant(lineno=10, col_offset=122, end_lineno=10, end_col_offset=124, value='', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=134,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=31, id='cal_microsoft_client_secret', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=34,
                        end_lineno=11,
                        end_col_offset=134,
                        func=Attribute(
                            lineno=11,
                            col_offset=34,
                            end_lineno=11,
                            end_col_offset=45,
                            value=Name(lineno=11, col_offset=34, end_lineno=11, end_col_offset=40, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=46, end_lineno=11, end_col_offset=68, value='Microsoft Client_key', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=70,
                                end_lineno=11,
                                end_col_offset=121,
                                arg='config_parameter',
                                value=Constant(lineno=11, col_offset=87, end_lineno=11, end_col_offset=121, value='microsoft_calendar_client_secret', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=123,
                                end_lineno=11,
                                end_col_offset=133,
                                arg='default',
                                value=Constant(lineno=11, col_offset=131, end_lineno=11, end_col_offset=133, value='', kind=None),
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