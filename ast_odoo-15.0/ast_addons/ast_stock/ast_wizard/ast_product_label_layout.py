Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=35,
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=34,
            end_col_offset=27,
            name='ProductLabelLayout',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=25,
                    end_lineno=8,
                    end_col_offset=46,
                    value=Name(lineno=8, col_offset=25, end_lineno=8, end_col_offset=31, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=37,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=37, value='product.label.layout', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=55,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=17, id='move_line_ids', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=20,
                        end_lineno=11,
                        end_col_offset=55,
                        func=Attribute(
                            lineno=11,
                            col_offset=20,
                            end_lineno=11,
                            end_col_offset=36,
                            value=Name(lineno=11, col_offset=20, end_lineno=11, end_col_offset=26, id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=37, end_lineno=11, end_col_offset=54, value='stock.move.line', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=91,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=20, id='picking_quantity', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=23,
                        end_lineno=14,
                        end_col_offset=91,
                        func=Attribute(
                            lineno=12,
                            col_offset=23,
                            end_lineno=12,
                            end_col_offset=39,
                            value=Name(lineno=12, col_offset=23, end_lineno=12, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                lineno=12,
                                col_offset=40,
                                end_lineno=14,
                                end_col_offset=29,
                                elts=[
                                    Tuple(
                                        lineno=13,
                                        col_offset=8,
                                        end_lineno=13,
                                        end_col_offset=42,
                                        elts=[
                                            Constant(lineno=13, col_offset=9, end_lineno=13, end_col_offset=18, value='picking', kind=None),
                                            Constant(lineno=13, col_offset=20, end_lineno=13, end_col_offset=41, value='Transfer Quantities', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=14,
                                        col_offset=8,
                                        end_lineno=14,
                                        end_col_offset=28,
                                        elts=[
                                            Constant(lineno=14, col_offset=9, end_lineno=14, end_col_offset=17, value='custom', kind=None),
                                            Constant(lineno=14, col_offset=19, end_lineno=14, end_col_offset=27, value='Custom', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=31,
                                end_lineno=14,
                                end_col_offset=57,
                                arg='string',
                                value=Constant(lineno=14, col_offset=38, end_lineno=14, end_col_offset=57, value='Quantity to print', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=59,
                                end_lineno=14,
                                end_col_offset=72,
                                arg='required',
                                value=Constant(lineno=14, col_offset=68, end_lineno=14, end_col_offset=72, value=True, kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=74,
                                end_lineno=14,
                                end_col_offset=90,
                                arg='default',
                                value=Constant(lineno=14, col_offset=82, end_lineno=14, end_col_offset=90, value='custom', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=67,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=16, id='print_format', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=19,
                        end_lineno=18,
                        end_col_offset=67,
                        func=Attribute(
                            lineno=15,
                            col_offset=19,
                            end_lineno=15,
                            end_col_offset=35,
                            value=Name(lineno=15, col_offset=19, end_lineno=15, end_col_offset=25, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=36,
                                end_lineno=18,
                                end_col_offset=5,
                                arg='selection_add',
                                value=List(
                                    lineno=15,
                                    col_offset=50,
                                    end_lineno=18,
                                    end_col_offset=5,
                                    elts=[
                                        Tuple(
                                            lineno=16,
                                            col_offset=8,
                                            end_lineno=16,
                                            end_col_offset=29,
                                            elts=[
                                                Constant(lineno=16, col_offset=9, end_lineno=16, end_col_offset=14, value='zpl', kind=None),
                                                Constant(lineno=16, col_offset=16, end_lineno=16, end_col_offset=28, value='ZPL Labels', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=17,
                                            col_offset=8,
                                            end_lineno=17,
                                            end_col_offset=46,
                                            elts=[
                                                Constant(lineno=17, col_offset=9, end_lineno=17, end_col_offset=20, value='zplxprice', kind=None),
                                                Constant(lineno=17, col_offset=22, end_lineno=17, end_col_offset=45, value='ZPL Labels with price', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                lineno=18,
                                col_offset=7,
                                end_lineno=18,
                                end_col_offset=66,
                                arg='ondelete',
                                value=Dict(
                                    lineno=18,
                                    col_offset=16,
                                    end_lineno=18,
                                    end_col_offset=66,
                                    keys=[
                                        Constant(lineno=18, col_offset=17, end_lineno=18, end_col_offset=22, value='zpl', kind=None),
                                        Constant(lineno=18, col_offset=39, end_lineno=18, end_col_offset=50, value='zplxprice', kind=None),
                                    ],
                                    values=[
                                        Constant(lineno=18, col_offset=24, end_lineno=18, end_col_offset=37, value='set default', kind=None),
                                        Constant(lineno=18, col_offset=52, end_lineno=18, end_col_offset=65, value='set default', kind=None),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=20,
                    col_offset=4,
                    end_lineno=34,
                    end_col_offset=27,
                    name='_prepare_report_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=20, col_offset=29, end_lineno=20, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=53,
                            targets=[
                                Tuple(
                                    lineno=21,
                                    col_offset=8,
                                    end_lineno=21,
                                    end_col_offset=20,
                                    elts=[
                                        Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=14, id='xml_id', ctx=Store()),
                                        Name(lineno=21, col_offset=16, end_lineno=21, end_col_offset=20, id='data', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=21,
                                col_offset=23,
                                end_lineno=21,
                                end_col_offset=53,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=23,
                                    end_lineno=21,
                                    end_col_offset=51,
                                    value=Call(
                                        lineno=21,
                                        col_offset=23,
                                        end_lineno=21,
                                        end_col_offset=30,
                                        func=Name(lineno=21, col_offset=23, end_lineno=21, end_col_offset=28, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_prepare_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=23,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=50,
                            test=Compare(
                                lineno=23,
                                col_offset=11,
                                end_lineno=23,
                                end_col_offset=37,
                                left=Constant(lineno=23, col_offset=11, end_lineno=23, end_col_offset=16, value='zpl', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        lineno=23,
                                        col_offset=20,
                                        end_lineno=23,
                                        end_col_offset=37,
                                        value=Name(lineno=23, col_offset=20, end_lineno=23, end_col_offset=24, id='self', ctx=Load()),
                                        attr='print_format',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    lineno=24,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=50,
                                    targets=[Name(lineno=24, col_offset=12, end_lineno=24, end_col_offset=18, id='xml_id', ctx=Store())],
                                    value=Constant(lineno=24, col_offset=21, end_lineno=24, end_col_offset=50, value='stock.label_product_product', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            lineno=26,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=84,
                            test=BoolOp(
                                lineno=26,
                                col_offset=11,
                                end_lineno=26,
                                end_col_offset=68,
                                op=And(),
                                values=[
                                    Compare(
                                        lineno=26,
                                        col_offset=11,
                                        end_lineno=26,
                                        end_col_offset=45,
                                        left=Attribute(
                                            lineno=26,
                                            col_offset=11,
                                            end_lineno=26,
                                            end_col_offset=32,
                                            value=Name(lineno=26, col_offset=11, end_lineno=26, end_col_offset=15, id='self', ctx=Load()),
                                            attr='picking_quantity',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(lineno=26, col_offset=36, end_lineno=26, end_col_offset=45, value='picking', kind=None)],
                                    ),
                                    Attribute(
                                        lineno=26,
                                        col_offset=50,
                                        end_lineno=26,
                                        end_col_offset=68,
                                        value=Name(lineno=26, col_offset=50, end_lineno=26, end_col_offset=54, id='self', ctx=Load()),
                                        attr='move_line_ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    lineno=27,
                                    col_offset=12,
                                    end_lineno=27,
                                    end_col_offset=36,
                                    targets=[Name(lineno=27, col_offset=12, end_lineno=27, end_col_offset=17, id='qties', ctx=Store())],
                                    value=Call(
                                        lineno=27,
                                        col_offset=20,
                                        end_lineno=27,
                                        end_col_offset=36,
                                        func=Name(lineno=27, col_offset=20, end_lineno=27, end_col_offset=31, id='defaultdict', ctx=Load()),
                                        args=[Name(lineno=27, col_offset=32, end_lineno=27, end_col_offset=35, id='int', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=28,
                                    col_offset=12,
                                    end_lineno=28,
                                    end_col_offset=91,
                                    targets=[Name(lineno=28, col_offset=12, end_lineno=28, end_col_offset=20, id='uom_unit', ctx=Store())],
                                    value=Call(
                                        lineno=28,
                                        col_offset=23,
                                        end_lineno=28,
                                        end_col_offset=91,
                                        func=Attribute(
                                            lineno=28,
                                            col_offset=23,
                                            end_lineno=28,
                                            end_col_offset=35,
                                            value=Attribute(
                                                lineno=28,
                                                col_offset=23,
                                                end_lineno=28,
                                                end_col_offset=31,
                                                value=Name(lineno=28, col_offset=23, end_lineno=28, end_col_offset=27, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=28, col_offset=36, end_lineno=28, end_col_offset=64, value='uom.product_uom_categ_unit', kind=None)],
                                        keywords=[
                                            keyword(
                                                lineno=28,
                                                col_offset=66,
                                                end_lineno=28,
                                                end_col_offset=90,
                                                arg='raise_if_not_found',
                                                value=Constant(lineno=28, col_offset=85, end_lineno=28, end_col_offset=90, value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    lineno=29,
                                    col_offset=12,
                                    end_lineno=31,
                                    end_col_offset=62,
                                    target=Name(lineno=29, col_offset=16, end_lineno=29, end_col_offset=20, id='line', ctx=Store()),
                                    iter=Attribute(
                                        lineno=29,
                                        col_offset=24,
                                        end_lineno=29,
                                        end_col_offset=42,
                                        value=Name(lineno=29, col_offset=24, end_lineno=29, end_col_offset=28, id='self', ctx=Load()),
                                        attr='move_line_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            lineno=30,
                                            col_offset=16,
                                            end_lineno=31,
                                            end_col_offset=62,
                                            test=Compare(
                                                lineno=30,
                                                col_offset=19,
                                                end_lineno=30,
                                                end_col_offset=62,
                                                left=Attribute(
                                                    lineno=30,
                                                    col_offset=19,
                                                    end_lineno=30,
                                                    end_col_offset=50,
                                                    value=Attribute(
                                                        lineno=30,
                                                        col_offset=19,
                                                        end_lineno=30,
                                                        end_col_offset=38,
                                                        value=Name(lineno=30, col_offset=19, end_lineno=30, end_col_offset=23, id='line', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='category_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(lineno=30, col_offset=54, end_lineno=30, end_col_offset=62, id='uom_unit', ctx=Load())],
                                            ),
                                            body=[
                                                AugAssign(
                                                    lineno=31,
                                                    col_offset=20,
                                                    end_lineno=31,
                                                    end_col_offset=62,
                                                    target=Subscript(
                                                        lineno=31,
                                                        col_offset=20,
                                                        end_lineno=31,
                                                        end_col_offset=45,
                                                        value=Name(lineno=31, col_offset=20, end_lineno=31, end_col_offset=25, id='qties', ctx=Load()),
                                                        slice=Attribute(
                                                            lineno=31,
                                                            col_offset=26,
                                                            end_lineno=31,
                                                            end_col_offset=44,
                                                            value=Attribute(
                                                                lineno=31,
                                                                col_offset=26,
                                                                end_lineno=31,
                                                                end_col_offset=41,
                                                                value=Name(lineno=31, col_offset=26, end_lineno=31, end_col_offset=30, id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Attribute(
                                                        lineno=31,
                                                        col_offset=49,
                                                        end_lineno=31,
                                                        end_col_offset=62,
                                                        value=Name(lineno=31, col_offset=49, end_lineno=31, end_col_offset=53, id='line', ctx=Load()),
                                                        attr='qty_done',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=33,
                                    col_offset=12,
                                    end_lineno=33,
                                    end_col_offset=84,
                                    targets=[
                                        Subscript(
                                            lineno=33,
                                            col_offset=12,
                                            end_lineno=33,
                                            end_col_offset=39,
                                            value=Name(lineno=33, col_offset=12, end_lineno=33, end_col_offset=16, id='data', ctx=Load()),
                                            slice=Constant(lineno=33, col_offset=17, end_lineno=33, end_col_offset=38, value='quantity_by_product', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=DictComp(
                                        lineno=33,
                                        col_offset=42,
                                        end_lineno=33,
                                        end_col_offset=84,
                                        key=Name(lineno=33, col_offset=43, end_lineno=33, end_col_offset=44, id='p', ctx=Load()),
                                        value=Call(
                                            lineno=33,
                                            col_offset=46,
                                            end_lineno=33,
                                            end_col_offset=52,
                                            func=Name(lineno=33, col_offset=46, end_lineno=33, end_col_offset=49, id='int', ctx=Load()),
                                            args=[Name(lineno=33, col_offset=50, end_lineno=33, end_col_offset=51, id='q', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    lineno=33,
                                                    col_offset=57,
                                                    end_lineno=33,
                                                    end_col_offset=61,
                                                    elts=[
                                                        Name(lineno=33, col_offset=57, end_lineno=33, end_col_offset=58, id='p', ctx=Store()),
                                                        Name(lineno=33, col_offset=60, end_lineno=33, end_col_offset=61, id='q', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    lineno=33,
                                                    col_offset=65,
                                                    end_lineno=33,
                                                    end_col_offset=78,
                                                    func=Attribute(
                                                        lineno=33,
                                                        col_offset=65,
                                                        end_lineno=33,
                                                        end_col_offset=76,
                                                        value=Name(lineno=33, col_offset=65, end_lineno=33, end_col_offset=70, id='qties', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[Name(lineno=33, col_offset=82, end_lineno=33, end_col_offset=83, id='q', ctx=Load())],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=27,
                            value=Tuple(
                                lineno=34,
                                col_offset=15,
                                end_lineno=34,
                                end_col_offset=27,
                                elts=[
                                    Name(lineno=34, col_offset=15, end_lineno=34, end_col_offset=21, id='xml_id', ctx=Load()),
                                    Name(lineno=34, col_offset=23, end_lineno=34, end_col_offset=27, id='data', ctx=Load()),
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
