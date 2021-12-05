Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=11,
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=31,
            module='odoo.tests',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=15,
            end_col_offset=118,
            name='TestMailGuestPages',
            bases=[Name(lineno=8, col_offset=25, end_lineno=8, end_col_offset=33, id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=118,
                    name='test_mail_channel_as_guest',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=35, end_lineno=9, end_col_offset=39, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=10,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=65,
                            value=Constant(lineno=10, col_offset=8, end_lineno=11, end_col_offset=65, value='Checks that the invite page redirects to the channel and that all\n        modules load correctly on the welcome and channel page', kind=None),
                        ),
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=10,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=15, id='channel', ctx=Store())],
                            value=Call(
                                lineno=12,
                                col_offset=18,
                                end_lineno=14,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=18,
                                    end_lineno=12,
                                    end_col_offset=49,
                                    value=Subscript(
                                        lineno=12,
                                        col_offset=18,
                                        end_lineno=12,
                                        end_col_offset=42,
                                        value=Attribute(
                                            lineno=12,
                                            col_offset=18,
                                            end_lineno=12,
                                            end_col_offset=26,
                                            value=Name(lineno=12, col_offset=18, end_lineno=12, end_col_offset=22, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=12, col_offset=27, end_lineno=12, end_col_offset=41, value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=12,
                                        col_offset=50,
                                        end_lineno=14,
                                        end_col_offset=9,
                                        keys=[Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=18, value='name', kind=None)],
                                        values=[Constant(lineno=13, col_offset=20, end_lineno=13, end_col_offset=34, value='Test channel', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=118,
                            value=Call(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=118,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=8,
                                    end_lineno=15,
                                    end_col_offset=23,
                                    value=Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    JoinedStr(
                                        lineno=15,
                                        col_offset=24,
                                        end_lineno=15,
                                        end_col_offset=60,
                                        values=[
                                            Constant(lineno=15, col_offset=24, end_lineno=15, end_col_offset=60, value='/chat/', kind=None),
                                            FormattedValue(
                                                lineno=15,
                                                col_offset=24,
                                                end_lineno=15,
                                                end_col_offset=60,
                                                value=Attribute(
                                                    lineno=15,
                                                    col_offset=33,
                                                    end_lineno=15,
                                                    end_col_offset=43,
                                                    value=Name(lineno=15, col_offset=33, end_lineno=15, end_col_offset=40, id='channel', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(lineno=15, col_offset=24, end_lineno=15, end_col_offset=60, value='/', kind=None),
                                            FormattedValue(
                                                lineno=15,
                                                col_offset=24,
                                                end_lineno=15,
                                                end_col_offset=60,
                                                value=Attribute(
                                                    lineno=15,
                                                    col_offset=46,
                                                    end_lineno=15,
                                                    end_col_offset=58,
                                                    value=Name(lineno=15, col_offset=46, end_lineno=15, end_col_offset=53, id='channel', ctx=Load()),
                                                    attr='uuid',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                    Constant(lineno=15, col_offset=62, end_lineno=15, end_col_offset=117, value='mail/static/tests/tours/mail_channel_as_guest_tour.js', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    lineno=7,
                    col_offset=1,
                    end_lineno=7,
                    end_col_offset=49,
                    func=Attribute(
                        lineno=7,
                        col_offset=1,
                        end_lineno=7,
                        end_col_offset=18,
                        value=Attribute(
                            lineno=7,
                            col_offset=1,
                            end_lineno=7,
                            end_col_offset=11,
                            value=Name(lineno=7, col_offset=1, end_lineno=7, end_col_offset=5, id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(lineno=7, col_offset=19, end_lineno=7, end_col_offset=32, value='-at_install', kind=None),
                        Constant(lineno=7, col_offset=34, end_lineno=7, end_col_offset=48, value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
