Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=39,
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=37,
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=23,
            end_col_offset=84,
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
                    end_lineno=13,
                    end_col_offset=40,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=17, id='detailed_type', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=20,
                        end_lineno=13,
                        end_col_offset=40,
                        func=Attribute(
                            lineno=11,
                            col_offset=20,
                            end_lineno=11,
                            end_col_offset=36,
                            value=Name(lineno=11, col_offset=20, end_lineno=11, end_col_offset=26, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=37,
                                end_lineno=13,
                                end_col_offset=5,
                                arg='selection_add',
                                value=List(
                                    lineno=11,
                                    col_offset=51,
                                    end_lineno=13,
                                    end_col_offset=5,
                                    elts=[
                                        Tuple(
                                            lineno=12,
                                            col_offset=8,
                                            end_lineno=12,
                                            end_col_offset=29,
                                            elts=[
                                                Constant(lineno=12, col_offset=9, end_lineno=12, end_col_offset=15, value='gift', kind=None),
                                                Constant(lineno=12, col_offset=17, end_lineno=12, end_col_offset=28, value='Gift Card', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=7,
                                end_lineno=13,
                                end_col_offset=39,
                                arg='ondelete',
                                value=Dict(
                                    lineno=13,
                                    col_offset=16,
                                    end_lineno=13,
                                    end_col_offset=39,
                                    keys=[Constant(lineno=13, col_offset=17, end_lineno=13, end_col_offset=23, value='gift', kind=None)],
                                    values=[Constant(lineno=13, col_offset=25, end_lineno=13, end_col_offset=38, value='set service', kind=None)],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=27,
                    name='_detailed_type_mapping',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=15, col_offset=31, end_lineno=15, end_col_offset=35, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=55,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=20, id='type_mapping', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=23,
                                end_lineno=16,
                                end_col_offset=55,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=23,
                                    end_lineno=16,
                                    end_col_offset=53,
                                    value=Call(
                                        lineno=16,
                                        col_offset=23,
                                        end_lineno=16,
                                        end_col_offset=30,
                                        func=Name(lineno=16, col_offset=23, end_lineno=16, end_col_offset=28, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_detailed_type_mapping',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=40,
                            targets=[
                                Subscript(
                                    lineno=17,
                                    col_offset=8,
                                    end_lineno=17,
                                    end_col_offset=28,
                                    value=Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=20, id='type_mapping', ctx=Load()),
                                    slice=Constant(lineno=17, col_offset=21, end_lineno=17, end_col_offset=27, value='gift', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(lineno=17, col_offset=31, end_lineno=17, end_col_offset=40, value='service', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=27,
                            value=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=27, id='type_mapping', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=84,
                    name='_unlink_gift_card_product',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=21, col_offset=34, end_lineno=21, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            lineno=22,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=84,
                            test=Compare(
                                lineno=22,
                                col_offset=11,
                                end_lineno=22,
                                end_col_offset=87,
                                left=Attribute(
                                    lineno=22,
                                    col_offset=11,
                                    end_lineno=22,
                                    end_col_offset=79,
                                    value=Call(
                                        lineno=22,
                                        col_offset=11,
                                        end_lineno=22,
                                        end_col_offset=63,
                                        func=Attribute(
                                            lineno=22,
                                            col_offset=11,
                                            end_lineno=22,
                                            end_col_offset=23,
                                            value=Attribute(
                                                lineno=22,
                                                col_offset=11,
                                                end_lineno=22,
                                                end_col_offset=19,
                                                value=Name(lineno=22, col_offset=11, end_lineno=22, end_col_offset=15, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=22, col_offset=24, end_lineno=22, end_col_offset=62, value='gift_card.pay_with_gift_card_product', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='product_tmpl_id',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[Name(lineno=22, col_offset=83, end_lineno=22, end_col_offset=87, id='self', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    lineno=23,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=84,
                                    exc=Call(
                                        lineno=23,
                                        col_offset=18,
                                        end_lineno=23,
                                        end_col_offset=84,
                                        func=Name(lineno=23, col_offset=18, end_lineno=23, end_col_offset=27, id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=23,
                                                col_offset=28,
                                                end_lineno=23,
                                                end_col_offset=83,
                                                func=Name(lineno=23, col_offset=28, end_lineno=23, end_col_offset=29, id='_', ctx=Load()),
                                                args=[Constant(lineno=23, col_offset=30, end_lineno=23, end_col_offset=82, value='Deleting the Gift Card Pay product is not allowed.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=20,
                            col_offset=5,
                            end_lineno=20,
                            end_col_offset=37,
                            func=Attribute(
                                lineno=20,
                                col_offset=5,
                                end_lineno=20,
                                end_col_offset=17,
                                value=Name(lineno=20, col_offset=5, end_lineno=20, end_col_offset=8, id='api', ctx=Load()),
                                attr='ondelete',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    lineno=20,
                                    col_offset=18,
                                    end_lineno=20,
                                    end_col_offset=36,
                                    arg='at_uninstall',
                                    value=Constant(lineno=20, col_offset=31, end_lineno=20, end_col_offset=36, value=False, kind=None),
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
