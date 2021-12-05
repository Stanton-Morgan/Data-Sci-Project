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
            end_lineno=20,
            end_col_offset=34,
            name='ResPartner',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=17,
                    end_lineno=7,
                    end_col_offset=29,
                    value=Name(lineno=7, col_offset=17, end_lineno=7, end_col_offset=23, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=25,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=25, value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=51,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=List(
                        lineno=9,
                        col_offset=15,
                        end_lineno=9,
                        end_col_offset=51,
                        elts=[
                            Constant(lineno=9, col_offset=16, end_lineno=9, end_col_offset=29, value='res.partner', kind=None),
                            Constant(lineno=9, col_offset=31, end_lineno=9, end_col_offset=50, value='mail.thread.phone', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=19,
                    name='_sms_get_default_partners',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=34, end_lineno=11, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=11,
                            value=Constant(lineno=12, col_offset=8, end_lineno=14, end_col_offset=11, value=' Override of mail.thread method.\n            SMS recipients on partners are the partners themselves.\n        ', kind=None),
                        ),
                        Return(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=19,
                            value=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=19, id='self', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=17,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=34,
                    name='_phone_get_number_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=17, col_offset=33, end_lineno=17, end_col_offset=37, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=18,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=36,
                            value=Constant(lineno=18, col_offset=8, end_lineno=19, end_col_offset=36, value=' This method returns the fields to use to find the number to use to\n        send an SMS on a record. ', kind=None),
                        ),
                        Return(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=34,
                            value=List(
                                lineno=20,
                                col_offset=15,
                                end_lineno=20,
                                end_col_offset=34,
                                elts=[
                                    Constant(lineno=20, col_offset=16, end_lineno=20, end_col_offset=24, value='mobile', kind=None),
                                    Constant(lineno=20, col_offset=26, end_lineno=20, end_col_offset=33, value='phone', kind=None),
                                ],
                                ctx=Load(),
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
