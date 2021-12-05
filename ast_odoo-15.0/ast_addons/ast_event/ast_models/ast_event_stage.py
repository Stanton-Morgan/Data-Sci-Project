Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=34,
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=27,
            end_col_offset=95,
            name='EventStage',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=17,
                    end_lineno=7,
                    end_col_offset=29,
                    value=Name(lineno=7, col_offset=17, end_lineno=7, end_col_offset=23, id='models', ctx=Load()),
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
                    end_col_offset=25,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=25, value='event.stage', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=32,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=32, value='Event Stage', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=29,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=10, col_offset=13, end_lineno=10, end_col_offset=29, value='sequence, name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=74,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=11,
                        end_lineno=12,
                        end_col_offset=74,
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
                                end_col_offset=42,
                                arg='string',
                                value=Constant(lineno=12, col_offset=30, end_lineno=12, end_col_offset=42, value='Stage Name', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=44,
                                end_lineno=12,
                                end_col_offset=57,
                                arg='required',
                                value=Constant(lineno=12, col_offset=53, end_lineno=12, end_col_offset=57, value=True, kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=59,
                                end_lineno=12,
                                end_col_offset=73,
                                arg='translate',
                                value=Constant(lineno=12, col_offset=69, end_lineno=12, end_col_offset=73, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=73,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=15, id='description', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=18,
                        end_lineno=13,
                        end_col_offset=73,
                        func=Attribute(
                            lineno=13,
                            col_offset=18,
                            end_lineno=13,
                            end_col_offset=29,
                            value=Name(lineno=13, col_offset=18, end_lineno=13, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=30,
                                end_lineno=13,
                                end_col_offset=56,
                                arg='string',
                                value=Constant(lineno=13, col_offset=37, end_lineno=13, end_col_offset=56, value='Stage description', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=58,
                                end_lineno=13,
                                end_col_offset=72,
                                arg='translate',
                                value=Constant(lineno=13, col_offset=68, end_lineno=13, end_col_offset=72, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=52,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=12, id='sequence', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=15,
                        end_lineno=14,
                        end_col_offset=52,
                        func=Attribute(
                            lineno=14,
                            col_offset=15,
                            end_lineno=14,
                            end_col_offset=29,
                            value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=14, col_offset=30, end_lineno=14, end_col_offset=40, value='Sequence', kind=None)],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=42,
                                end_lineno=14,
                                end_col_offset=51,
                                arg='default',
                                value=Constant(lineno=14, col_offset=50, end_lineno=14, end_col_offset=51, value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=67,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=8, id='fold', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=11,
                        end_lineno=15,
                        end_col_offset=67,
                        func=Attribute(
                            lineno=15,
                            col_offset=11,
                            end_lineno=15,
                            end_col_offset=25,
                            value=Name(lineno=15, col_offset=11, end_lineno=15, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=26,
                                end_lineno=15,
                                end_col_offset=51,
                                arg='string',
                                value=Constant(lineno=15, col_offset=33, end_lineno=15, end_col_offset=51, value='Folded in Kanban', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=53,
                                end_lineno=15,
                                end_col_offset=66,
                                arg='default',
                                value=Constant(lineno=15, col_offset=61, end_lineno=15, end_col_offset=66, value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=158,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=12, id='pipe_end', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=15,
                        end_lineno=18,
                        end_col_offset=158,
                        func=Attribute(
                            lineno=16,
                            col_offset=15,
                            end_lineno=16,
                            end_col_offset=29,
                            value=Name(lineno=16, col_offset=15, end_lineno=16, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=8,
                                end_lineno=17,
                                end_col_offset=26,
                                arg='string',
                                value=Constant(lineno=17, col_offset=15, end_lineno=17, end_col_offset=26, value='End Stage', kind=None),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=28,
                                end_lineno=17,
                                end_col_offset=41,
                                arg='default',
                                value=Constant(lineno=17, col_offset=36, end_lineno=17, end_col_offset=41, value=False, kind=None),
                            ),
                            keyword(
                                lineno=18,
                                col_offset=8,
                                end_lineno=18,
                                end_col_offset=157,
                                arg='help',
                                value=Constant(lineno=18, col_offset=13, end_lineno=18, end_col_offset=157, value='Events will automatically be moved into this stage when they are finished. The event moved into this stage will automatically be set as green.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=96,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=18, id='legend_blocked', ctx=Store())],
                    value=Call(
                        lineno=19,
                        col_offset=21,
                        end_lineno=21,
                        end_col_offset=96,
                        func=Attribute(
                            lineno=19,
                            col_offset=21,
                            end_lineno=19,
                            end_col_offset=32,
                            value=Name(lineno=19, col_offset=21, end_lineno=19, end_col_offset=27, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=20, col_offset=8, end_lineno=20, end_col_offset=26, value='Red Kanban Label', kind=None)],
                        keywords=[
                            keyword(
                                lineno=20,
                                col_offset=28,
                                end_lineno=20,
                                end_col_offset=58,
                                arg='default',
                                value=Lambda(
                                    lineno=20,
                                    col_offset=36,
                                    end_lineno=20,
                                    end_col_offset=58,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=20, col_offset=43, end_lineno=20, end_col_offset=44, arg='s', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        lineno=20,
                                        col_offset=46,
                                        end_lineno=20,
                                        end_col_offset=58,
                                        func=Name(lineno=20, col_offset=46, end_lineno=20, end_col_offset=47, id='_', ctx=Load()),
                                        args=[Constant(lineno=20, col_offset=48, end_lineno=20, end_col_offset=57, value='Blocked', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                lineno=20,
                                col_offset=60,
                                end_lineno=20,
                                end_col_offset=74,
                                arg='translate',
                                value=Constant(lineno=20, col_offset=70, end_lineno=20, end_col_offset=74, value=True, kind=None),
                            ),
                            keyword(
                                lineno=20,
                                col_offset=76,
                                end_lineno=20,
                                end_col_offset=89,
                                arg='required',
                                value=Constant(lineno=20, col_offset=85, end_lineno=20, end_col_offset=89, value=True, kind=None),
                            ),
                            keyword(
                                lineno=21,
                                col_offset=8,
                                end_lineno=21,
                                end_col_offset=95,
                                arg='help',
                                value=Constant(lineno=21, col_offset=13, end_lineno=21, end_col_offset=95, value='Override the default value displayed for the blocked state for kanban selection.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=22,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=93,
                    targets=[Name(lineno=22, col_offset=4, end_lineno=22, end_col_offset=15, id='legend_done', ctx=Store())],
                    value=Call(
                        lineno=22,
                        col_offset=18,
                        end_lineno=24,
                        end_col_offset=93,
                        func=Attribute(
                            lineno=22,
                            col_offset=18,
                            end_lineno=22,
                            end_col_offset=29,
                            value=Name(lineno=22, col_offset=18, end_lineno=22, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=23, col_offset=8, end_lineno=23, end_col_offset=28, value='Green Kanban Label', kind=None)],
                        keywords=[
                            keyword(
                                lineno=23,
                                col_offset=30,
                                end_lineno=23,
                                end_col_offset=73,
                                arg='default',
                                value=Lambda(
                                    lineno=23,
                                    col_offset=38,
                                    end_lineno=23,
                                    end_col_offset=73,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=23, col_offset=45, end_lineno=23, end_col_offset=46, arg='s', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        lineno=23,
                                        col_offset=48,
                                        end_lineno=23,
                                        end_col_offset=73,
                                        func=Name(lineno=23, col_offset=48, end_lineno=23, end_col_offset=49, id='_', ctx=Load()),
                                        args=[Constant(lineno=23, col_offset=50, end_lineno=23, end_col_offset=72, value='Ready for Next Stage', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                lineno=23,
                                col_offset=75,
                                end_lineno=23,
                                end_col_offset=89,
                                arg='translate',
                                value=Constant(lineno=23, col_offset=85, end_lineno=23, end_col_offset=89, value=True, kind=None),
                            ),
                            keyword(
                                lineno=23,
                                col_offset=91,
                                end_lineno=23,
                                end_col_offset=104,
                                arg='required',
                                value=Constant(lineno=23, col_offset=100, end_lineno=23, end_col_offset=104, value=True, kind=None),
                            ),
                            keyword(
                                lineno=24,
                                col_offset=8,
                                end_lineno=24,
                                end_col_offset=92,
                                arg='help',
                                value=Constant(lineno=24, col_offset=13, end_lineno=24, end_col_offset=92, value='Override the default value displayed for the done state for kanban selection.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=25,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=95,
                    targets=[Name(lineno=25, col_offset=4, end_lineno=25, end_col_offset=17, id='legend_normal', ctx=Store())],
                    value=Call(
                        lineno=25,
                        col_offset=20,
                        end_lineno=27,
                        end_col_offset=95,
                        func=Attribute(
                            lineno=25,
                            col_offset=20,
                            end_lineno=25,
                            end_col_offset=31,
                            value=Name(lineno=25, col_offset=20, end_lineno=25, end_col_offset=26, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=26, col_offset=8, end_lineno=26, end_col_offset=27, value='Grey Kanban Label', kind=None)],
                        keywords=[
                            keyword(
                                lineno=26,
                                col_offset=29,
                                end_lineno=26,
                                end_col_offset=63,
                                arg='default',
                                value=Lambda(
                                    lineno=26,
                                    col_offset=37,
                                    end_lineno=26,
                                    end_col_offset=63,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=26, col_offset=44, end_lineno=26, end_col_offset=45, arg='s', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        lineno=26,
                                        col_offset=47,
                                        end_lineno=26,
                                        end_col_offset=63,
                                        func=Name(lineno=26, col_offset=47, end_lineno=26, end_col_offset=48, id='_', ctx=Load()),
                                        args=[Constant(lineno=26, col_offset=49, end_lineno=26, end_col_offset=62, value='In Progress', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                lineno=26,
                                col_offset=65,
                                end_lineno=26,
                                end_col_offset=79,
                                arg='translate',
                                value=Constant(lineno=26, col_offset=75, end_lineno=26, end_col_offset=79, value=True, kind=None),
                            ),
                            keyword(
                                lineno=26,
                                col_offset=81,
                                end_lineno=26,
                                end_col_offset=94,
                                arg='required',
                                value=Constant(lineno=26, col_offset=90, end_lineno=26, end_col_offset=94, value=True, kind=None),
                            ),
                            keyword(
                                lineno=27,
                                col_offset=8,
                                end_lineno=27,
                                end_col_offset=94,
                                arg='help',
                                value=Constant(lineno=27, col_offset=13, end_lineno=27, end_col_offset=94, value='Override the default value displayed for the normal state for kanban selection.', kind=None),
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
