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
            end_lineno=19,
            end_col_offset=81,
            name='MailShortcode',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=20,
                    end_lineno=7,
                    end_col_offset=32,
                    value=Name(lineno=7, col_offset=20, end_lineno=7, end_col_offset=26, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    lineno=8,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=7,
                    value=Constant(lineno=8, col_offset=4, end_lineno=12, end_col_offset=7, value=' Shortcode\n        Canned Responses, allowing the user to defined shortcuts in its message. Should be applied before storing message in database.\n        Emoji allowing replacing text with image for visual effect. Should be applied when the message is displayed (only for final rendering).\n        These shortcodes are global and are available for every user.\n    ', kind=None),
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=28,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=14, col_offset=12, end_lineno=14, end_col_offset=28, value='mail.shortcode', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=48,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=15, col_offset=19, end_lineno=15, end_col_offset=48, value='Canned Response / Shortcode', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=128,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=10, id='source', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=13,
                        end_lineno=16,
                        end_col_offset=128,
                        func=Attribute(
                            lineno=16,
                            col_offset=13,
                            end_lineno=16,
                            end_col_offset=24,
                            value=Name(lineno=16, col_offset=13, end_lineno=16, end_col_offset=19, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=16, col_offset=25, end_lineno=16, end_col_offset=35, value='Shortcut', kind=None)],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=37,
                                end_lineno=16,
                                end_col_offset=50,
                                arg='required',
                                value=Constant(lineno=16, col_offset=46, end_lineno=16, end_col_offset=50, value=True, kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=52,
                                end_lineno=16,
                                end_col_offset=62,
                                arg='index',
                                value=Constant(lineno=16, col_offset=58, end_lineno=16, end_col_offset=62, value=True, kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=64,
                                end_lineno=16,
                                end_col_offset=127,
                                arg='help',
                                value=Constant(lineno=16, col_offset=69, end_lineno=16, end_col_offset=127, value='The shortcut which must be replaced in the Chat Messages', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=126,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=16, id='substitution', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=19,
                        end_lineno=17,
                        end_col_offset=126,
                        func=Attribute(
                            lineno=17,
                            col_offset=19,
                            end_lineno=17,
                            end_col_offset=30,
                            value=Name(lineno=17, col_offset=19, end_lineno=17, end_col_offset=25, id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=31, end_lineno=17, end_col_offset=45, value='Substitution', kind=None)],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=47,
                                end_lineno=17,
                                end_col_offset=60,
                                arg='required',
                                value=Constant(lineno=17, col_offset=56, end_lineno=17, end_col_offset=60, value=True, kind=None),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=62,
                                end_lineno=17,
                                end_col_offset=72,
                                arg='index',
                                value=Constant(lineno=17, col_offset=68, end_lineno=17, end_col_offset=72, value=True, kind=None),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=74,
                                end_lineno=17,
                                end_col_offset=125,
                                arg='help',
                                value=Constant(lineno=17, col_offset=79, end_lineno=17, end_col_offset=125, value='The escaped html code replacing the shortcut', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=44,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=15, id='description', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=18,
                        end_lineno=18,
                        end_col_offset=44,
                        func=Attribute(
                            lineno=18,
                            col_offset=18,
                            end_lineno=18,
                            end_col_offset=29,
                            value=Name(lineno=18, col_offset=18, end_lineno=18, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=18, col_offset=30, end_lineno=18, end_col_offset=43, value='Description', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=81,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=15, id='message_ids', ctx=Store())],
                    value=Call(
                        lineno=19,
                        col_offset=18,
                        end_lineno=19,
                        end_col_offset=81,
                        func=Attribute(
                            lineno=19,
                            col_offset=18,
                            end_lineno=19,
                            end_col_offset=33,
                            value=Name(lineno=19, col_offset=18, end_lineno=19, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=19, col_offset=34, end_lineno=19, end_col_offset=48, value='mail.message', kind=None)],
                        keywords=[
                            keyword(
                                lineno=19,
                                col_offset=50,
                                end_lineno=19,
                                end_col_offset=67,
                                arg='string',
                                value=Constant(lineno=19, col_offset=57, end_lineno=19, end_col_offset=67, value='Messages', kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=69,
                                end_lineno=19,
                                end_col_offset=80,
                                arg='store',
                                value=Constant(lineno=19, col_offset=75, end_lineno=19, end_col_offset=80, value=False, kind=None),
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
