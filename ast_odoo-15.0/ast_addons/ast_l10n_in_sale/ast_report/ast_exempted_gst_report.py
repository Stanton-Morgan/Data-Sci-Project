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
            end_lineno=15,
            end_col_offset=23,
            name='L10nInExemptedReport',
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
                    end_col_offset=40,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=40, value='l10n_in.exempted.report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=23,
                    name='_from',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=14, end_lineno=10, end_col_offset=18, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=60,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=16, id='from_str', ctx=Store())],
                            value=Call(
                                lineno=11,
                                col_offset=19,
                                end_lineno=11,
                                end_col_offset=60,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=19,
                                    end_lineno=11,
                                    end_col_offset=58,
                                    value=Call(
                                        lineno=11,
                                        col_offset=19,
                                        end_lineno=11,
                                        end_col_offset=52,
                                        func=Name(lineno=11, col_offset=19, end_lineno=11, end_col_offset=24, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=11, col_offset=25, end_lineno=11, end_col_offset=45, id='L10nInExemptedReport', ctx=Load()),
                                            Name(lineno=11, col_offset=47, end_lineno=11, end_col_offset=51, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_from',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=15,
                            target=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=16, id='from_str', ctx=Store()),
                            op=Add(),
                            value=Constant(lineno=12, col_offset=20, end_lineno=14, end_col_offset=15, value=" AND aml.product_id != COALESCE(\n            (SELECT value from ir_config_parameter where key = 'sale.default_deposit_product_id'), '0')::int\n            ", kind=None),
                        ),
                        Return(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=23,
                            value=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=23, id='from_str', ctx=Load()),
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
