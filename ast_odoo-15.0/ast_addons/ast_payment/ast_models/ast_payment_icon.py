Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=21,
            end_col_offset=52,
            name='PaymentIcon',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=18,
                    end_lineno=6,
                    end_col_offset=30,
                    value=Name(lineno=6, col_offset=18, end_lineno=6, end_col_offset=24, id='models', ctx=Load()),
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
                    end_col_offset=26,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=7, col_offset=12, end_lineno=7, end_col_offset=26, value='payment.icon', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=33,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=8, col_offset=19, end_lineno=8, end_col_offset=33, value='Payment Icon', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=29,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=9, col_offset=13, end_lineno=9, end_col_offset=29, value='sequence, name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=37,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=11,
                        end_lineno=11,
                        end_col_offset=37,
                        func=Attribute(
                            lineno=11,
                            col_offset=11,
                            end_lineno=11,
                            end_col_offset=22,
                            value=Name(lineno=11, col_offset=11, end_lineno=11, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=23,
                                end_lineno=11,
                                end_col_offset=36,
                                arg='string',
                                value=Constant(lineno=11, col_offset=30, end_lineno=11, end_col_offset=36, value='Name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=66,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=16, id='acquirer_ids', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=19,
                        end_lineno=14,
                        end_col_offset=66,
                        func=Attribute(
                            lineno=12,
                            col_offset=19,
                            end_lineno=12,
                            end_col_offset=35,
                            value=Name(lineno=12, col_offset=19, end_lineno=12, end_col_offset=25, id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=26,
                                arg='string',
                                value=Constant(lineno=13, col_offset=15, end_lineno=13, end_col_offset=26, value='Acquirers', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=28,
                                end_lineno=13,
                                end_col_offset=59,
                                arg='comodel_name',
                                value=Constant(lineno=13, col_offset=41, end_lineno=13, end_col_offset=59, value='payment.acquirer', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=65,
                                arg='help',
                                value=Constant(lineno=14, col_offset=13, end_lineno=14, end_col_offset=65, value='The list of acquirers supporting this payment icon', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=90,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=9, id='image', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=12,
                        end_lineno=17,
                        end_col_offset=90,
                        func=Attribute(
                            lineno=15,
                            col_offset=12,
                            end_lineno=15,
                            end_col_offset=24,
                            value=Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=18, id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=8,
                                end_lineno=16,
                                end_col_offset=22,
                                arg='string',
                                value=Constant(lineno=16, col_offset=15, end_lineno=16, end_col_offset=22, value='Image', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=24,
                                end_lineno=16,
                                end_col_offset=36,
                                arg='max_width',
                                value=Constant(lineno=16, col_offset=34, end_lineno=16, end_col_offset=36, value=64, kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=38,
                                end_lineno=16,
                                end_col_offset=51,
                                arg='max_height',
                                value=Constant(lineno=16, col_offset=49, end_lineno=16, end_col_offset=51, value=64, kind=None),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=8,
                                end_lineno=17,
                                end_col_offset=89,
                                arg='help',
                                value=Constant(lineno=17, col_offset=13, end_lineno=17, end_col_offset=89, value='This field holds the image used for this payment icon, limited to 64x64 px', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=22,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=22, id='image_payment_form', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=25,
                        end_lineno=20,
                        end_col_offset=22,
                        func=Attribute(
                            lineno=18,
                            col_offset=25,
                            end_lineno=18,
                            end_col_offset=37,
                            value=Name(lineno=18, col_offset=25, end_lineno=18, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=19,
                                col_offset=8,
                                end_lineno=19,
                                end_col_offset=52,
                                arg='string',
                                value=Constant(lineno=19, col_offset=15, end_lineno=19, end_col_offset=52, value='Image displayed on the payment form', kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=54,
                                end_lineno=19,
                                end_col_offset=69,
                                arg='related',
                                value=Constant(lineno=19, col_offset=62, end_lineno=19, end_col_offset=69, value='image', kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=71,
                                end_lineno=19,
                                end_col_offset=81,
                                arg='store',
                                value=Constant(lineno=19, col_offset=77, end_lineno=19, end_col_offset=81, value=True, kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=83,
                                end_lineno=19,
                                end_col_offset=95,
                                arg='max_width',
                                value=Constant(lineno=19, col_offset=93, end_lineno=19, end_col_offset=95, value=45, kind=None),
                            ),
                            keyword(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=21,
                                arg='max_height',
                                value=Constant(lineno=20, col_offset=19, end_lineno=20, end_col_offset=21, value=30, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=21,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=52,
                    targets=[Name(lineno=21, col_offset=4, end_lineno=21, end_col_offset=12, id='sequence', ctx=Store())],
                    value=Call(
                        lineno=21,
                        col_offset=15,
                        end_lineno=21,
                        end_col_offset=52,
                        func=Attribute(
                            lineno=21,
                            col_offset=15,
                            end_lineno=21,
                            end_col_offset=29,
                            value=Name(lineno=21, col_offset=15, end_lineno=21, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=21, col_offset=30, end_lineno=21, end_col_offset=40, value='Sequence', kind=None)],
                        keywords=[
                            keyword(
                                lineno=21,
                                col_offset=42,
                                end_lineno=21,
                                end_col_offset=51,
                                arg='default',
                                value=Constant(lineno=21, col_offset=50, end_lineno=21, end_col_offset=51, value=1, kind=None),
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