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
            end_lineno=20,
            end_col_offset=51,
            name='SponsorType',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=18,
                    end_lineno=7,
                    end_col_offset=30,
                    value=Name(lineno=7, col_offset=18, end_lineno=7, end_col_offset=24, id='models', ctx=Load()),
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
                    end_col_offset=32,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=32, value='event.sponsor.type', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=40,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=40, value='Event Sponsor Level', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=23,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=10, col_offset=13, end_lineno=10, end_col_offset=23, value='sequence', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=82,
                    name='_default_sequence',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=12, col_offset=26, end_lineno=12, end_col_offset=30, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=82,
                            value=BinOp(
                                lineno=13,
                                col_offset=15,
                                end_lineno=13,
                                end_col_offset=82,
                                left=BoolOp(
                                    lineno=13,
                                    col_offset=16,
                                    end_lineno=13,
                                    end_col_offset=77,
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            lineno=13,
                                            col_offset=16,
                                            end_lineno=13,
                                            end_col_offset=72,
                                            value=Call(
                                                lineno=13,
                                                col_offset=16,
                                                end_lineno=13,
                                                end_col_offset=63,
                                                func=Attribute(
                                                    lineno=13,
                                                    col_offset=16,
                                                    end_lineno=13,
                                                    end_col_offset=27,
                                                    value=Name(lineno=13, col_offset=16, end_lineno=13, end_col_offset=20, id='self', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[List(lineno=13, col_offset=28, end_lineno=13, end_col_offset=30, elts=[], ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        lineno=13,
                                                        col_offset=32,
                                                        end_lineno=13,
                                                        end_col_offset=53,
                                                        arg='order',
                                                        value=Constant(lineno=13, col_offset=38, end_lineno=13, end_col_offset=53, value='sequence desc', kind=None),
                                                    ),
                                                    keyword(
                                                        lineno=13,
                                                        col_offset=55,
                                                        end_lineno=13,
                                                        end_col_offset=62,
                                                        arg='limit',
                                                        value=Constant(lineno=13, col_offset=61, end_lineno=13, end_col_offset=62, value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='sequence',
                                            ctx=Load(),
                                        ),
                                        Constant(lineno=13, col_offset=76, end_lineno=13, end_col_offset=77, value=0, kind=None),
                                    ],
                                ),
                                op=Add(),
                                right=Constant(lineno=13, col_offset=81, end_lineno=13, end_col_offset=82, value=1, kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=70,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=11,
                        end_lineno=15,
                        end_col_offset=70,
                        func=Attribute(
                            lineno=15,
                            col_offset=11,
                            end_lineno=15,
                            end_col_offset=22,
                            value=Name(lineno=15, col_offset=11, end_lineno=15, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=15, col_offset=23, end_lineno=15, end_col_offset=38, value='Sponsor Level', kind=None)],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=40,
                                end_lineno=15,
                                end_col_offset=53,
                                arg='required',
                                value=Constant(lineno=15, col_offset=49, end_lineno=15, end_col_offset=53, value=True, kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=55,
                                end_lineno=15,
                                end_col_offset=69,
                                arg='translate',
                                value=Constant(lineno=15, col_offset=65, end_lineno=15, end_col_offset=69, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=68,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=12, id='sequence', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=15,
                        end_lineno=16,
                        end_col_offset=68,
                        func=Attribute(
                            lineno=16,
                            col_offset=15,
                            end_lineno=16,
                            end_col_offset=29,
                            value=Name(lineno=16, col_offset=15, end_lineno=16, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=16, col_offset=30, end_lineno=16, end_col_offset=40, value='Sequence', kind=None)],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=42,
                                end_lineno=16,
                                end_col_offset=67,
                                arg='default',
                                value=Name(lineno=16, col_offset=50, end_lineno=16, end_col_offset=67, id='_default_sequence', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=51,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=24, id='display_ribbon_style', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=27,
                        end_lineno=20,
                        end_col_offset=51,
                        func=Attribute(
                            lineno=17,
                            col_offset=27,
                            end_lineno=17,
                            end_col_offset=43,
                            value=Name(lineno=17, col_offset=27, end_lineno=17, end_col_offset=33, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                lineno=18,
                                col_offset=8,
                                end_lineno=19,
                                end_col_offset=52,
                                elts=[
                                    Tuple(
                                        lineno=18,
                                        col_offset=9,
                                        end_lineno=18,
                                        end_col_offset=35,
                                        elts=[
                                            Constant(lineno=18, col_offset=10, end_lineno=18, end_col_offset=21, value='no_ribbon', kind=None),
                                            Constant(lineno=18, col_offset=23, end_lineno=18, end_col_offset=34, value='No Ribbon', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=18,
                                        col_offset=37,
                                        end_lineno=18,
                                        end_col_offset=53,
                                        elts=[
                                            Constant(lineno=18, col_offset=38, end_lineno=18, end_col_offset=44, value='Gold', kind=None),
                                            Constant(lineno=18, col_offset=46, end_lineno=18, end_col_offset=52, value='Gold', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=19,
                                        col_offset=9,
                                        end_lineno=19,
                                        end_col_offset=29,
                                        elts=[
                                            Constant(lineno=19, col_offset=10, end_lineno=19, end_col_offset=18, value='Silver', kind=None),
                                            Constant(lineno=19, col_offset=20, end_lineno=19, end_col_offset=28, value='Silver', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=19,
                                        col_offset=31,
                                        end_lineno=19,
                                        end_col_offset=51,
                                        elts=[
                                            Constant(lineno=19, col_offset=32, end_lineno=19, end_col_offset=40, value='Bronze', kind=None),
                                            Constant(lineno=19, col_offset=42, end_lineno=19, end_col_offset=50, value='Bronze', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=29,
                                arg='string',
                                value=Constant(lineno=20, col_offset=15, end_lineno=20, end_col_offset=29, value='Ribbon Style', kind=None),
                            ),
                            keyword(
                                lineno=20,
                                col_offset=31,
                                end_lineno=20,
                                end_col_offset=50,
                                arg='default',
                                value=Constant(lineno=20, col_offset=39, end_lineno=20, end_col_offset=50, value='no_ribbon', kind=None),
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
