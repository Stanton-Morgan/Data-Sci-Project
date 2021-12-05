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
            end_lineno=15,
            end_col_offset=5,
            name='ResCompany',
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
                    end_col_offset=28,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=28, value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=30,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=23, id='_check_company_auto', ctx=Store())],
                    value=Constant(lineno=9, col_offset=26, end_lineno=9, end_col_offset=30, value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=5,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=26, id='sale_order_template_id', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=29,
                        end_lineno=15,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=11,
                            col_offset=29,
                            end_lineno=11,
                            end_col_offset=44,
                            value=Name(lineno=11, col_offset=29, end_lineno=11, end_col_offset=35, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=8, end_lineno=12, end_col_offset=29, value='sale.order.template', kind=None)],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=31,
                                end_lineno=12,
                                end_col_offset=61,
                                arg='string',
                                value=Constant(lineno=12, col_offset=38, end_lineno=12, end_col_offset=61, value='Default Sale Template', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=75,
                                arg='domain',
                                value=Constant(lineno=13, col_offset=15, end_lineno=13, end_col_offset=75, value="['|', ('company_id', '=', False), ('company_id', '=', id)]", kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=26,
                                arg='check_company',
                                value=Constant(lineno=14, col_offset=22, end_lineno=14, end_col_offset=26, value=True, kind=None),
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