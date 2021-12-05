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
            end_lineno=14,
            end_col_offset=98,
            name='IrExports',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=16,
                    end_lineno=7,
                    end_col_offset=28,
                    value=Name(lineno=7, col_offset=16, end_lineno=7, end_col_offset=22, id='models', ctx=Load()),
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
                    end_col_offset=24,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=24, value='ir.exports', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=28,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=28, value='Exports', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=19,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=10, col_offset=13, end_lineno=10, end_col_offset=19, value='name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=44,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=11,
                        end_lineno=12,
                        end_col_offset=44,
                        func=Attribute(
                            lineno=12,
                            col_offset=11,
                            end_lineno=12,
                            end_col_offset=22,
                            value=Name(lineno=12, col_offset=11, end_lineno=12, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=23,
                                end_lineno=12,
                                end_col_offset=43,
                                arg='string',
                                value=Constant(lineno=12, col_offset=30, end_lineno=12, end_col_offset=43, value='Export Name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=38,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=12, id='resource', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=15,
                        end_lineno=13,
                        end_col_offset=38,
                        func=Attribute(
                            lineno=13,
                            col_offset=15,
                            end_lineno=13,
                            end_col_offset=26,
                            value=Name(lineno=13, col_offset=15, end_lineno=13, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=27,
                                end_lineno=13,
                                end_col_offset=37,
                                arg='index',
                                value=Constant(lineno=13, col_offset=33, end_lineno=13, end_col_offset=37, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=98,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=17, id='export_fields', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=20,
                        end_lineno=14,
                        end_col_offset=98,
                        func=Attribute(
                            lineno=14,
                            col_offset=20,
                            end_lineno=14,
                            end_col_offset=35,
                            value=Name(lineno=14, col_offset=20, end_lineno=14, end_col_offset=26, id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=14, col_offset=36, end_lineno=14, end_col_offset=53, value='ir.exports.line', kind=None),
                            Constant(lineno=14, col_offset=55, end_lineno=14, end_col_offset=66, value='export_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=68,
                                end_lineno=14,
                                end_col_offset=86,
                                arg='string',
                                value=Constant(lineno=14, col_offset=75, end_lineno=14, end_col_offset=86, value='Export ID', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=88,
                                end_lineno=14,
                                end_col_offset=97,
                                arg='copy',
                                value=Constant(lineno=14, col_offset=93, end_lineno=14, end_col_offset=97, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            lineno=17,
            col_offset=0,
            end_lineno=23,
            end_col_offset=94,
            name='IrExportsLine',
            bases=[
                Attribute(
                    lineno=17,
                    col_offset=20,
                    end_lineno=17,
                    end_col_offset=32,
                    value=Name(lineno=17, col_offset=20, end_lineno=17, end_col_offset=26, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=29,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=18, col_offset=12, end_lineno=18, end_col_offset=29, value='ir.exports.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=33,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=19, col_offset=19, end_lineno=19, end_col_offset=33, value='Exports Line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=20,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=17,
                    targets=[Name(lineno=20, col_offset=4, end_lineno=20, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=20, col_offset=13, end_lineno=20, end_col_offset=17, value='id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=22,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=43,
                    targets=[Name(lineno=22, col_offset=4, end_lineno=22, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=22,
                        col_offset=11,
                        end_lineno=22,
                        end_col_offset=43,
                        func=Attribute(
                            lineno=22,
                            col_offset=11,
                            end_lineno=22,
                            end_col_offset=22,
                            value=Name(lineno=22, col_offset=11, end_lineno=22, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=22,
                                col_offset=23,
                                end_lineno=22,
                                end_col_offset=42,
                                arg='string',
                                value=Constant(lineno=22, col_offset=30, end_lineno=22, end_col_offset=42, value='Field Name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=23,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=94,
                    targets=[Name(lineno=23, col_offset=4, end_lineno=23, end_col_offset=13, id='export_id', ctx=Store())],
                    value=Call(
                        lineno=23,
                        col_offset=16,
                        end_lineno=23,
                        end_col_offset=94,
                        func=Attribute(
                            lineno=23,
                            col_offset=16,
                            end_lineno=23,
                            end_col_offset=31,
                            value=Name(lineno=23, col_offset=16, end_lineno=23, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=23, col_offset=32, end_lineno=23, end_col_offset=44, value='ir.exports', kind=None)],
                        keywords=[
                            keyword(
                                lineno=23,
                                col_offset=46,
                                end_lineno=23,
                                end_col_offset=61,
                                arg='string',
                                value=Constant(lineno=23, col_offset=53, end_lineno=23, end_col_offset=61, value='Export', kind=None),
                            ),
                            keyword(
                                lineno=23,
                                col_offset=63,
                                end_lineno=23,
                                end_col_offset=73,
                                arg='index',
                                value=Constant(lineno=23, col_offset=69, end_lineno=23, end_col_offset=73, value=True, kind=None),
                            ),
                            keyword(
                                lineno=23,
                                col_offset=75,
                                end_lineno=23,
                                end_col_offset=93,
                                arg='ondelete',
                                value=Constant(lineno=23, col_offset=84, end_lineno=23, end_col_offset=93, value='cascade', kind=None),
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