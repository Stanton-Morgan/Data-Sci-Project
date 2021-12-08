Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=47,
            module='odoo.tools.translate',
            names=[alias(name='html_translate', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=24,
            end_col_offset=49,
            name='ProductTemplate',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=22,
                    end_lineno=8,
                    end_col_offset=34,
                    value=Name(lineno=8, col_offset=22, end_lineno=8, end_col_offset=28, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=33,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=33, value='product.template', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=91,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=30, id='quotation_only_description', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=33,
                        end_lineno=12,
                        end_col_offset=91,
                        func=Attribute(
                            lineno=11,
                            col_offset=33,
                            end_lineno=11,
                            end_col_offset=44,
                            value=Name(lineno=11, col_offset=33, end_lineno=11, end_col_offset=39, id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=45, end_lineno=11, end_col_offset=73, value='Quotation Only Description', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=75,
                                end_lineno=11,
                                end_col_offset=100,
                                arg='sanitize_attributes',
                                value=Constant(lineno=11, col_offset=95, end_lineno=11, end_col_offset=100, value=False, kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=32,
                                arg='translate',
                                value=Name(lineno=12, col_offset=18, end_lineno=12, end_col_offset=32, id='html_translate', ctx=Load()),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=34,
                                end_lineno=12,
                                end_col_offset=90,
                                arg='help',
                                value=Constant(lineno=12, col_offset=39, end_lineno=12, end_col_offset=90, value='The quotation description (not used on eCommerce)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=164,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=25, id='quotation_description', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=28,
                        end_lineno=15,
                        end_col_offset=164,
                        func=Attribute(
                            lineno=14,
                            col_offset=28,
                            end_lineno=14,
                            end_col_offset=39,
                            value=Name(lineno=14, col_offset=28, end_lineno=14, end_col_offset=34, id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=14, col_offset=40, end_lineno=14, end_col_offset=63, value='Quotation Description', kind=None)],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=65,
                                end_lineno=14,
                                end_col_offset=105,
                                arg='compute',
                                value=Constant(lineno=14, col_offset=73, end_lineno=14, end_col_offset=105, value='_compute_quotation_description', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=33,
                                arg='sanitize_attributes',
                                value=Constant(lineno=15, col_offset=28, end_lineno=15, end_col_offset=33, value=False, kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=35,
                                end_lineno=15,
                                end_col_offset=163,
                                arg='help',
                                value=Constant(lineno=15, col_offset=40, end_lineno=15, end_col_offset=163, value='This field uses the Quotation Only Description if it is defined, otherwise it will try to read the eCommerce Description.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=17,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=49,
                    name='_compute_quotation_description',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=17, col_offset=39, end_lineno=17, end_col_offset=43, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            lineno=18,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=49,
                            target=Name(lineno=18, col_offset=12, end_lineno=18, end_col_offset=18, id='record', ctx=Store()),
                            iter=Name(lineno=18, col_offset=22, end_lineno=18, end_col_offset=26, id='self', ctx=Load()),
                            body=[
                                If(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=49,
                                    test=Attribute(
                                        lineno=19,
                                        col_offset=15,
                                        end_lineno=19,
                                        end_col_offset=48,
                                        value=Name(lineno=19, col_offset=15, end_lineno=19, end_col_offset=21, id='record', ctx=Load()),
                                        attr='quotation_only_description',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            lineno=20,
                                            col_offset=16,
                                            end_lineno=20,
                                            end_col_offset=80,
                                            targets=[
                                                Attribute(
                                                    lineno=20,
                                                    col_offset=16,
                                                    end_lineno=20,
                                                    end_col_offset=44,
                                                    value=Name(lineno=20, col_offset=16, end_lineno=20, end_col_offset=22, id='record', ctx=Load()),
                                                    attr='quotation_description',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                lineno=20,
                                                col_offset=47,
                                                end_lineno=20,
                                                end_col_offset=80,
                                                value=Name(lineno=20, col_offset=47, end_lineno=20, end_col_offset=53, id='record', ctx=Load()),
                                                attr='quotation_only_description',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            lineno=21,
                                            col_offset=12,
                                            end_lineno=24,
                                            end_col_offset=49,
                                            test=BoolOp(
                                                lineno=21,
                                                col_offset=17,
                                                end_lineno=21,
                                                end_col_offset=86,
                                                op=And(),
                                                values=[
                                                    Call(
                                                        lineno=21,
                                                        col_offset=17,
                                                        end_lineno=21,
                                                        end_col_offset=55,
                                                        func=Name(lineno=21, col_offset=17, end_lineno=21, end_col_offset=24, id='hasattr', ctx=Load()),
                                                        args=[
                                                            Name(lineno=21, col_offset=25, end_lineno=21, end_col_offset=31, id='record', ctx=Load()),
                                                            Constant(lineno=21, col_offset=33, end_lineno=21, end_col_offset=54, value='website_description', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        lineno=21,
                                                        col_offset=60,
                                                        end_lineno=21,
                                                        end_col_offset=86,
                                                        value=Name(lineno=21, col_offset=60, end_lineno=21, end_col_offset=66, id='record', ctx=Load()),
                                                        attr='website_description',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    lineno=22,
                                                    col_offset=16,
                                                    end_lineno=22,
                                                    end_col_offset=73,
                                                    targets=[
                                                        Attribute(
                                                            lineno=22,
                                                            col_offset=16,
                                                            end_lineno=22,
                                                            end_col_offset=44,
                                                            value=Name(lineno=22, col_offset=16, end_lineno=22, end_col_offset=22, id='record', ctx=Load()),
                                                            attr='quotation_description',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        lineno=22,
                                                        col_offset=47,
                                                        end_lineno=22,
                                                        end_col_offset=73,
                                                        value=Name(lineno=22, col_offset=47, end_lineno=22, end_col_offset=53, id='record', ctx=Load()),
                                                        attr='website_description',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    lineno=24,
                                                    col_offset=16,
                                                    end_lineno=24,
                                                    end_col_offset=49,
                                                    targets=[
                                                        Attribute(
                                                            lineno=24,
                                                            col_offset=16,
                                                            end_lineno=24,
                                                            end_col_offset=44,
                                                            value=Name(lineno=24, col_offset=16, end_lineno=24, end_col_offset=22, id='record', ctx=Load()),
                                                            attr='quotation_description',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(lineno=24, col_offset=47, end_lineno=24, end_col_offset=49, value='', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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