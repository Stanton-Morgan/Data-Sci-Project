Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=14,
            end_col_offset=18,
            name='AccountPaymentMethod',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=27,
                    end_lineno=7,
                    end_col_offset=39,
                    value=Name(lineno=7, col_offset=27, end_lineno=7, end_col_offset=33, id='models', ctx=Load()),
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
                    end_col_offset=39,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=39, value='account.payment.method', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=18,
                    name='_get_payment_method_information',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=40, end_lineno=11, end_col_offset=44, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=55,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=12,
                                col_offset=14,
                                end_lineno=12,
                                end_col_offset=55,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=14,
                                    end_lineno=12,
                                    end_col_offset=53,
                                    value=Call(
                                        lineno=12,
                                        col_offset=14,
                                        end_lineno=12,
                                        end_col_offset=21,
                                        func=Name(lineno=12, col_offset=14, end_lineno=12, end_col_offset=19, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_payment_method_information',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=80,
                            targets=[
                                Subscript(
                                    lineno=13,
                                    col_offset=8,
                                    end_lineno=13,
                                    end_col_offset=24,
                                    value=Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=11, id='res', ctx=Load()),
                                    slice=Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=23, value='payumoney', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                lineno=13,
                                col_offset=27,
                                end_lineno=13,
                                end_col_offset=80,
                                keys=[
                                    Constant(lineno=13, col_offset=28, end_lineno=13, end_col_offset=34, value='mode', kind=None),
                                    Constant(lineno=13, col_offset=46, end_lineno=13, end_col_offset=54, value='domain', kind=None),
                                ],
                                values=[
                                    Constant(lineno=13, col_offset=36, end_lineno=13, end_col_offset=44, value='unique', kind=None),
                                    List(
                                        lineno=13,
                                        col_offset=56,
                                        end_lineno=13,
                                        end_col_offset=79,
                                        elts=[
                                            Tuple(
                                                lineno=13,
                                                col_offset=57,
                                                end_lineno=13,
                                                end_col_offset=78,
                                                elts=[
                                                    Constant(lineno=13, col_offset=58, end_lineno=13, end_col_offset=64, value='type', kind=None),
                                                    Constant(lineno=13, col_offset=66, end_lineno=13, end_col_offset=69, value='=', kind=None),
                                                    Constant(lineno=13, col_offset=71, end_lineno=13, end_col_offset=77, value='bank', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=18,
                            value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=18, id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=10,
                            col_offset=5,
                            end_lineno=10,
                            end_col_offset=14,
                            value=Name(lineno=10, col_offset=5, end_lineno=10, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
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
