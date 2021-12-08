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
            end_lineno=17,
            end_col_offset=84,
            name='EventBoothCategory',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=25,
                    end_lineno=7,
                    end_col_offset=37,
                    value=Name(lineno=7, col_offset=25, end_lineno=7, end_col_offset=31, id='models', ctx=Load()),
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
                    end_col_offset=34,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=34, value='event.booth.category', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=41,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=41, value='Event Booth Category', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=30,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=List(
                        lineno=10,
                        col_offset=15,
                        end_lineno=10,
                        end_col_offset=30,
                        elts=[Constant(lineno=10, col_offset=16, end_lineno=10, end_col_offset=29, value='image.mixin', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=27,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=11, col_offset=13, end_lineno=11, end_col_offset=27, value='sequence ASC', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=41,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=10, id='active', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=13,
                        end_lineno=13,
                        end_col_offset=41,
                        func=Attribute(
                            lineno=13,
                            col_offset=13,
                            end_lineno=13,
                            end_col_offset=27,
                            value=Name(lineno=13, col_offset=13, end_lineno=13, end_col_offset=19, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=28,
                                end_lineno=13,
                                end_col_offset=40,
                                arg='default',
                                value=Constant(lineno=13, col_offset=36, end_lineno=13, end_col_offset=40, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=68,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=11,
                        end_lineno=14,
                        end_col_offset=68,
                        func=Attribute(
                            lineno=14,
                            col_offset=11,
                            end_lineno=14,
                            end_col_offset=22,
                            value=Name(lineno=14, col_offset=11, end_lineno=14, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=23,
                                end_lineno=14,
                                end_col_offset=36,
                                arg='string',
                                value=Constant(lineno=14, col_offset=30, end_lineno=14, end_col_offset=36, value='Name', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=38,
                                end_lineno=14,
                                end_col_offset=51,
                                arg='required',
                                value=Constant(lineno=14, col_offset=47, end_lineno=14, end_col_offset=51, value=True, kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=53,
                                end_lineno=14,
                                end_col_offset=67,
                                arg='translate',
                                value=Constant(lineno=14, col_offset=63, end_lineno=14, end_col_offset=67, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=60,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=12, id='sequence', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=15,
                        end_lineno=15,
                        end_col_offset=60,
                        func=Attribute(
                            lineno=15,
                            col_offset=15,
                            end_lineno=15,
                            end_col_offset=29,
                            value=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=30,
                                end_lineno=15,
                                end_col_offset=47,
                                arg='string',
                                value=Constant(lineno=15, col_offset=37, end_lineno=15, end_col_offset=47, value='Sequence', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=49,
                                end_lineno=15,
                                end_col_offset=59,
                                arg='default',
                                value=Constant(lineno=15, col_offset=57, end_lineno=15, end_col_offset=59, value=10, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=67,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=15, id='description', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=18,
                        end_lineno=16,
                        end_col_offset=67,
                        func=Attribute(
                            lineno=16,
                            col_offset=18,
                            end_lineno=16,
                            end_col_offset=29,
                            value=Name(lineno=16, col_offset=18, end_lineno=16, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=30,
                                end_lineno=16,
                                end_col_offset=50,
                                arg='string',
                                value=Constant(lineno=16, col_offset=37, end_lineno=16, end_col_offset=50, value='Description', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=52,
                                end_lineno=16,
                                end_col_offset=66,
                                arg='translate',
                                value=Constant(lineno=16, col_offset=62, end_lineno=16, end_col_offset=66, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=84,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=13, id='booth_ids', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=16,
                        end_lineno=17,
                        end_col_offset=84,
                        func=Attribute(
                            lineno=17,
                            col_offset=16,
                            end_lineno=17,
                            end_col_offset=31,
                            value=Name(lineno=17, col_offset=16, end_lineno=17, end_col_offset=22, id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=17, col_offset=32, end_lineno=17, end_col_offset=45, value='event.booth', kind=None),
                            Constant(lineno=17, col_offset=47, end_lineno=17, end_col_offset=66, value='booth_category_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=68,
                                end_lineno=17,
                                end_col_offset=83,
                                arg='string',
                                value=Constant(lineno=17, col_offset=75, end_lineno=17, end_col_offset=83, value='Booths', kind=None),
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