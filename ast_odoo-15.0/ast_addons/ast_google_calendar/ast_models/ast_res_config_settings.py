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
            end_col_offset=111,
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
                    end_col_offset=102,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=17, id='cal_client_id', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=20,
                        end_lineno=10,
                        end_col_offset=102,
                        func=Attribute(
                            lineno=10,
                            col_offset=20,
                            end_lineno=10,
                            end_col_offset=31,
                            value=Name(lineno=10, col_offset=20, end_lineno=10, end_col_offset=26, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=32, end_lineno=10, end_col_offset=43, value='Client_id', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=45,
                                end_lineno=10,
                                end_col_offset=89,
                                arg='config_parameter',
                                value=Constant(lineno=10, col_offset=62, end_lineno=10, end_col_offset=89, value='google_calendar_client_id', kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=91,
                                end_lineno=10,
                                end_col_offset=101,
                                arg='default',
                                value=Constant(lineno=10, col_offset=99, end_lineno=10, end_col_offset=101, value='', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=111,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=21, id='cal_client_secret', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=24,
                        end_lineno=11,
                        end_col_offset=111,
                        func=Attribute(
                            lineno=11,
                            col_offset=24,
                            end_lineno=11,
                            end_col_offset=35,
                            value=Name(lineno=11, col_offset=24, end_lineno=11, end_col_offset=30, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=36, end_lineno=11, end_col_offset=48, value='Client_key', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=50,
                                end_lineno=11,
                                end_col_offset=98,
                                arg='config_parameter',
                                value=Constant(lineno=11, col_offset=67, end_lineno=11, end_col_offset=98, value='google_calendar_client_secret', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=100,
                                end_lineno=11,
                                end_col_offset=110,
                                arg='default',
                                value=Constant(lineno=11, col_offset=108, end_lineno=11, end_col_offset=110, value='', kind=None),
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
