Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=16,
            end_col_offset=5,
            name='ResCompany',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=17,
                    end_lineno=6,
                    end_col_offset=29,
                    value=Name(lineno=6, col_offset=17, end_lineno=6, end_col_offset=23, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=28,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=28, value='res.company', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=94,
                    name='_get_default_nomenclature',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=34, end_lineno=9, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=10,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=94,
                            value=Call(
                                lineno=10,
                                col_offset=15,
                                end_lineno=10,
                                end_col_offset=94,
                                func=Attribute(
                                    lineno=10,
                                    col_offset=15,
                                    end_lineno=10,
                                    end_col_offset=27,
                                    value=Attribute(
                                        lineno=10,
                                        col_offset=15,
                                        end_lineno=10,
                                        end_col_offset=23,
                                        value=Name(lineno=10, col_offset=15, end_lineno=10, end_col_offset=19, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=10, col_offset=28, end_lineno=10, end_col_offset=67, value='barcodes.default_barcode_nomenclature', kind=None)],
                                keywords=[
                                    keyword(
                                        lineno=10,
                                        col_offset=69,
                                        end_lineno=10,
                                        end_col_offset=93,
                                        arg='raise_if_not_found',
                                        value=Constant(lineno=10, col_offset=88, end_lineno=10, end_col_offset=93, value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=5,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=19, id='nomenclature_id', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=22,
                        end_lineno=16,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=12,
                            col_offset=22,
                            end_lineno=12,
                            end_col_offset=37,
                            value=Name(lineno=12, col_offset=22, end_lineno=12, end_col_offset=28, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=8, end_lineno=13, end_col_offset=30, value='barcode.nomenclature', kind=None)],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=29,
                                arg='string',
                                value=Constant(lineno=14, col_offset=15, end_lineno=14, end_col_offset=29, value='Nomenclature', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=41,
                                arg='default',
                                value=Name(lineno=15, col_offset=16, end_lineno=15, end_col_offset=41, id='_get_default_nomenclature', ctx=Load()),
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
