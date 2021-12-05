Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=77,
            module='odoo.addons.website_event.controllers.main',
            names=[alias(name='WebsiteEventController', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=12,
            end_col_offset=21,
            name='EventOnlineController',
            bases=[Name(lineno=7, col_offset=28, end_lineno=7, end_col_offset=50, id='WebsiteEventController', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=21,
                    name='_get_registration_confirm_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=9, col_offset=41, end_lineno=9, end_col_offset=45, arg='self', annotation=None, type_comment=None),
                            arg(lineno=9, col_offset=47, end_lineno=9, end_col_offset=52, arg='event', annotation=None, type_comment=None),
                            arg(lineno=9, col_offset=54, end_lineno=9, end_col_offset=68, arg='attendees_sudo', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=10,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=107,
                            targets=[Name(lineno=10, col_offset=8, end_lineno=10, end_col_offset=14, id='values', ctx=Store())],
                            value=Call(
                                lineno=10,
                                col_offset=17,
                                end_lineno=10,
                                end_col_offset=107,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=17,
                                    end_lineno=10,
                                    end_col_offset=84,
                                    value=Call(
                                        lineno=10,
                                        col_offset=17,
                                        end_lineno=10,
                                        end_col_offset=51,
                                        func=Name(lineno=10, col_offset=17, end_lineno=10, end_col_offset=22, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=10, col_offset=23, end_lineno=10, end_col_offset=44, id='EventOnlineController', ctx=Load()),
                                            Name(lineno=10, col_offset=46, end_lineno=10, end_col_offset=50, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_registration_confirm_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=10, col_offset=85, end_lineno=10, end_col_offset=90, id='event', ctx=Load()),
                                    Name(lineno=10, col_offset=92, end_lineno=10, end_col_offset=106, id='attendees_sudo', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=38,
                            targets=[
                                Subscript(
                                    lineno=11,
                                    col_offset=8,
                                    end_lineno=11,
                                    end_col_offset=31,
                                    value=Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=14, id='values', ctx=Load()),
                                    slice=Constant(lineno=11, col_offset=15, end_lineno=11, end_col_offset=30, value='hide_sponsors', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(lineno=11, col_offset=34, end_lineno=11, end_col_offset=38, value=True, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=21,
                            value=Name(lineno=12, col_offset=15, end_lineno=12, end_col_offset=21, id='values', ctx=Load()),
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
