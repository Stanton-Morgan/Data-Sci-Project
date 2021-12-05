Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=21,
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=12,
            end_col_offset=17,
            name='HrAttendance',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=19,
                    end_lineno=8,
                    end_col_offset=34,
                    value=Name(lineno=8, col_offset=19, end_lineno=8, end_col_offset=23, id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=17,
                    name='kiosk_keepalive',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=24, end_lineno=10, end_col_offset=28, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=51,
                            targets=[
                                Attribute(
                                    lineno=11,
                                    col_offset=8,
                                    end_lineno=11,
                                    end_col_offset=44,
                                    value=Attribute(
                                        lineno=11,
                                        col_offset=8,
                                        end_lineno=11,
                                        end_col_offset=35,
                                        value=Attribute(
                                            lineno=11,
                                            col_offset=8,
                                            end_lineno=11,
                                            end_col_offset=27,
                                            value=Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=15, id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='modified',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(lineno=11, col_offset=47, end_lineno=11, end_col_offset=51, value=True, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=17,
                            value=Dict(lineno=12, col_offset=15, end_lineno=12, end_col_offset=17, keys=[], values=[]),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=9,
                            col_offset=5,
                            end_lineno=9,
                            end_col_offset=75,
                            func=Attribute(
                                lineno=9,
                                col_offset=5,
                                end_lineno=9,
                                end_col_offset=15,
                                value=Name(lineno=9, col_offset=5, end_lineno=9, end_col_offset=9, id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=9, col_offset=16, end_lineno=9, end_col_offset=48, value='/hr_attendance/kiosk_keepalive', kind=None)],
                            keywords=[
                                keyword(
                                    lineno=9,
                                    col_offset=50,
                                    end_lineno=9,
                                    end_col_offset=61,
                                    arg='auth',
                                    value=Constant(lineno=9, col_offset=55, end_lineno=9, end_col_offset=61, value='user', kind=None),
                                ),
                                keyword(
                                    lineno=9,
                                    col_offset=63,
                                    end_lineno=9,
                                    end_col_offset=74,
                                    arg='type',
                                    value=Constant(lineno=9, col_offset=68, end_lineno=9, end_col_offset=74, value='json', kind=None),
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
