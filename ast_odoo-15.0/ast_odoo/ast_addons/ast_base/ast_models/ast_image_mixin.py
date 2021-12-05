Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=19,
            end_col_offset=106,
            name='ImageMixin',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=17,
                    end_lineno=7,
                    end_col_offset=37,
                    value=Name(lineno=7, col_offset=17, end_lineno=7, end_col_offset=23, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=25,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=25, value='image.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=32,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=32, value='Image Mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=71,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=14, id='image_1920', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=17,
                        end_lineno=13,
                        end_col_offset=71,
                        func=Attribute(
                            lineno=13,
                            col_offset=17,
                            end_lineno=13,
                            end_col_offset=29,
                            value=Name(lineno=13, col_offset=17, end_lineno=13, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=30, end_lineno=13, end_col_offset=37, value='Image', kind=None)],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=39,
                                end_lineno=13,
                                end_col_offset=53,
                                arg='max_width',
                                value=Constant(lineno=13, col_offset=49, end_lineno=13, end_col_offset=53, value=1920, kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=55,
                                end_lineno=13,
                                end_col_offset=70,
                                arg='max_height',
                                value=Constant(lineno=13, col_offset=66, end_lineno=13, end_col_offset=70, value=1920, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=110,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=14, id='image_1024', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=17,
                        end_lineno=16,
                        end_col_offset=110,
                        func=Attribute(
                            lineno=16,
                            col_offset=17,
                            end_lineno=16,
                            end_col_offset=29,
                            value=Name(lineno=16, col_offset=17, end_lineno=16, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=16, col_offset=30, end_lineno=16, end_col_offset=42, value='Image 1024', kind=None)],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=44,
                                end_lineno=16,
                                end_col_offset=64,
                                arg='related',
                                value=Constant(lineno=16, col_offset=52, end_lineno=16, end_col_offset=64, value='image_1920', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=66,
                                end_lineno=16,
                                end_col_offset=80,
                                arg='max_width',
                                value=Constant(lineno=16, col_offset=76, end_lineno=16, end_col_offset=80, value=1024, kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=82,
                                end_lineno=16,
                                end_col_offset=97,
                                arg='max_height',
                                value=Constant(lineno=16, col_offset=93, end_lineno=16, end_col_offset=97, value=1024, kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=99,
                                end_lineno=16,
                                end_col_offset=109,
                                arg='store',
                                value=Constant(lineno=16, col_offset=105, end_lineno=16, end_col_offset=109, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=106,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=13, id='image_512', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=16,
                        end_lineno=17,
                        end_col_offset=106,
                        func=Attribute(
                            lineno=17,
                            col_offset=16,
                            end_lineno=17,
                            end_col_offset=28,
                            value=Name(lineno=17, col_offset=16, end_lineno=17, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=29, end_lineno=17, end_col_offset=40, value='Image 512', kind=None)],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=42,
                                end_lineno=17,
                                end_col_offset=62,
                                arg='related',
                                value=Constant(lineno=17, col_offset=50, end_lineno=17, end_col_offset=62, value='image_1920', kind=None),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=64,
                                end_lineno=17,
                                end_col_offset=77,
                                arg='max_width',
                                value=Constant(lineno=17, col_offset=74, end_lineno=17, end_col_offset=77, value=512, kind=None),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=79,
                                end_lineno=17,
                                end_col_offset=93,
                                arg='max_height',
                                value=Constant(lineno=17, col_offset=90, end_lineno=17, end_col_offset=93, value=512, kind=None),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=95,
                                end_lineno=17,
                                end_col_offset=105,
                                arg='store',
                                value=Constant(lineno=17, col_offset=101, end_lineno=17, end_col_offset=105, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=106,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=13, id='image_256', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=16,
                        end_lineno=18,
                        end_col_offset=106,
                        func=Attribute(
                            lineno=18,
                            col_offset=16,
                            end_lineno=18,
                            end_col_offset=28,
                            value=Name(lineno=18, col_offset=16, end_lineno=18, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=18, col_offset=29, end_lineno=18, end_col_offset=40, value='Image 256', kind=None)],
                        keywords=[
                            keyword(
                                lineno=18,
                                col_offset=42,
                                end_lineno=18,
                                end_col_offset=62,
                                arg='related',
                                value=Constant(lineno=18, col_offset=50, end_lineno=18, end_col_offset=62, value='image_1920', kind=None),
                            ),
                            keyword(
                                lineno=18,
                                col_offset=64,
                                end_lineno=18,
                                end_col_offset=77,
                                arg='max_width',
                                value=Constant(lineno=18, col_offset=74, end_lineno=18, end_col_offset=77, value=256, kind=None),
                            ),
                            keyword(
                                lineno=18,
                                col_offset=79,
                                end_lineno=18,
                                end_col_offset=93,
                                arg='max_height',
                                value=Constant(lineno=18, col_offset=90, end_lineno=18, end_col_offset=93, value=256, kind=None),
                            ),
                            keyword(
                                lineno=18,
                                col_offset=95,
                                end_lineno=18,
                                end_col_offset=105,
                                arg='store',
                                value=Constant(lineno=18, col_offset=101, end_lineno=18, end_col_offset=105, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=106,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=13, id='image_128', ctx=Store())],
                    value=Call(
                        lineno=19,
                        col_offset=16,
                        end_lineno=19,
                        end_col_offset=106,
                        func=Attribute(
                            lineno=19,
                            col_offset=16,
                            end_lineno=19,
                            end_col_offset=28,
                            value=Name(lineno=19, col_offset=16, end_lineno=19, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=19, col_offset=29, end_lineno=19, end_col_offset=40, value='Image 128', kind=None)],
                        keywords=[
                            keyword(
                                lineno=19,
                                col_offset=42,
                                end_lineno=19,
                                end_col_offset=62,
                                arg='related',
                                value=Constant(lineno=19, col_offset=50, end_lineno=19, end_col_offset=62, value='image_1920', kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=64,
                                end_lineno=19,
                                end_col_offset=77,
                                arg='max_width',
                                value=Constant(lineno=19, col_offset=74, end_lineno=19, end_col_offset=77, value=128, kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=79,
                                end_lineno=19,
                                end_col_offset=93,
                                arg='max_height',
                                value=Constant(lineno=19, col_offset=90, end_lineno=19, end_col_offset=93, value=128, kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=95,
                                end_lineno=19,
                                end_col_offset=105,
                                arg='store',
                                value=Constant(lineno=19, col_offset=101, end_lineno=19, end_col_offset=105, value=True, kind=None),
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
