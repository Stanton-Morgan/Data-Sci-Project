Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=29,
            end_col_offset=62,
            name='ResConfigSettings',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=24,
                    end_lineno=7,
                    end_col_offset=45,
                    value=Name(lineno=7, col_offset=24, end_lineno=7, end_col_offset=30, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=36,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=36, value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=49,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=21, id='module_event_sale', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=24,
                        end_lineno=10,
                        end_col_offset=49,
                        func=Attribute(
                            lineno=10,
                            col_offset=24,
                            end_lineno=10,
                            end_col_offset=38,
                            value=Name(lineno=10, col_offset=24, end_lineno=10, end_col_offset=30, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=39, end_lineno=10, end_col_offset=48, value='Tickets', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=66,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=29, id='module_website_event_meet', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=32,
                        end_lineno=11,
                        end_col_offset=66,
                        func=Attribute(
                            lineno=11,
                            col_offset=32,
                            end_lineno=11,
                            end_col_offset=46,
                            value=Name(lineno=11, col_offset=32, end_lineno=11, end_col_offset=38, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=47, end_lineno=11, end_col_offset=65, value='Discussion Rooms', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=68,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=30, id='module_website_event_track', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=33,
                        end_lineno=12,
                        end_col_offset=68,
                        func=Attribute(
                            lineno=12,
                            col_offset=33,
                            end_lineno=12,
                            end_col_offset=47,
                            value=Name(lineno=12, col_offset=33, end_lineno=12, end_col_offset=39, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=48, end_lineno=12, end_col_offset=67, value='Tracks and Agenda', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=65,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=35, id='module_website_event_track_live', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=38,
                        end_lineno=13,
                        end_col_offset=65,
                        func=Attribute(
                            lineno=13,
                            col_offset=38,
                            end_lineno=13,
                            end_col_offset=52,
                            value=Name(lineno=13, col_offset=38, end_lineno=13, end_col_offset=44, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=53, end_lineno=13, end_col_offset=64, value='Live Mode', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=70,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=35, id='module_website_event_track_quiz', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=38,
                        end_lineno=14,
                        end_col_offset=70,
                        func=Attribute(
                            lineno=14,
                            col_offset=38,
                            end_lineno=14,
                            end_col_offset=52,
                            value=Name(lineno=14, col_offset=38, end_lineno=14, end_col_offset=44, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=14, col_offset=53, end_lineno=14, end_col_offset=69, value='Quiz on Tracks', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=72,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=34, id='module_website_event_exhibitor', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=37,
                        end_lineno=15,
                        end_col_offset=72,
                        func=Attribute(
                            lineno=15,
                            col_offset=37,
                            end_lineno=15,
                            end_col_offset=51,
                            value=Name(lineno=15, col_offset=37, end_lineno=15, end_col_offset=43, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=15, col_offset=52, end_lineno=15, end_col_offset=71, value='Advanced Sponsors', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=74,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=34, id='module_website_event_questions', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=37,
                        end_lineno=16,
                        end_col_offset=74,
                        func=Attribute(
                            lineno=16,
                            col_offset=37,
                            end_lineno=16,
                            end_col_offset=51,
                            value=Name(lineno=16, col_offset=37, end_lineno=16, end_col_offset=43, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=16, col_offset=52, end_lineno=16, end_col_offset=73, value='Registration Survey', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=52,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=24, id='module_event_barcode', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=27,
                        end_lineno=17,
                        end_col_offset=52,
                        func=Attribute(
                            lineno=17,
                            col_offset=27,
                            end_lineno=17,
                            end_col_offset=41,
                            value=Name(lineno=17, col_offset=27, end_lineno=17, end_col_offset=33, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=42, end_lineno=17, end_col_offset=51, value='Barcode', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=66,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=29, id='module_website_event_sale', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=32,
                        end_lineno=18,
                        end_col_offset=66,
                        func=Attribute(
                            lineno=18,
                            col_offset=32,
                            end_lineno=18,
                            end_col_offset=46,
                            value=Name(lineno=18, col_offset=32, end_lineno=18, end_col_offset=38, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=18, col_offset=47, end_lineno=18, end_col_offset=65, value='Online Ticketing', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=59,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=22, id='module_event_booth', ctx=Store())],
                    value=Call(
                        lineno=19,
                        col_offset=25,
                        end_lineno=19,
                        end_col_offset=59,
                        func=Attribute(
                            lineno=19,
                            col_offset=25,
                            end_lineno=19,
                            end_col_offset=39,
                            value=Name(lineno=19, col_offset=25, end_lineno=19, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=19, col_offset=40, end_lineno=19, end_col_offset=58, value='Booth Management', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=22,
                    col_offset=4,
                    end_lineno=29,
                    end_col_offset=62,
                    name='_onchange_module_website_event_track',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=22, col_offset=45, end_lineno=22, end_col_offset=49, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=23,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=39,
                            value=Constant(lineno=23, col_offset=8, end_lineno=25, end_col_offset=39, value=' Reset sub-modules, otherwise you may have track to False but still\n        have track_live or track_quiz to True, meaning track will come back due\n        to dependencies of modules. ', kind=None),
                        ),
                        For(
                            lineno=26,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=62,
                            target=Name(lineno=26, col_offset=12, end_lineno=26, end_col_offset=18, id='config', ctx=Store()),
                            iter=Name(lineno=26, col_offset=22, end_lineno=26, end_col_offset=26, id='self', ctx=Load()),
                            body=[
                                If(
                                    lineno=27,
                                    col_offset=12,
                                    end_lineno=29,
                                    end_col_offset=62,
                                    test=UnaryOp(
                                        lineno=27,
                                        col_offset=15,
                                        end_lineno=27,
                                        end_col_offset=52,
                                        op=Not(),
                                        operand=Attribute(
                                            lineno=27,
                                            col_offset=19,
                                            end_lineno=27,
                                            end_col_offset=52,
                                            value=Name(lineno=27, col_offset=19, end_lineno=27, end_col_offset=25, id='config', ctx=Load()),
                                            attr='module_website_event_track',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            lineno=28,
                                            col_offset=16,
                                            end_lineno=28,
                                            end_col_offset=62,
                                            targets=[
                                                Attribute(
                                                    lineno=28,
                                                    col_offset=16,
                                                    end_lineno=28,
                                                    end_col_offset=54,
                                                    value=Name(lineno=28, col_offset=16, end_lineno=28, end_col_offset=22, id='config', ctx=Load()),
                                                    attr='module_website_event_track_live',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(lineno=28, col_offset=57, end_lineno=28, end_col_offset=62, value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            lineno=29,
                                            col_offset=16,
                                            end_lineno=29,
                                            end_col_offset=62,
                                            targets=[
                                                Attribute(
                                                    lineno=29,
                                                    col_offset=16,
                                                    end_lineno=29,
                                                    end_col_offset=54,
                                                    value=Name(lineno=29, col_offset=16, end_lineno=29, end_col_offset=22, id='config', ctx=Load()),
                                                    attr='module_website_event_track_quiz',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(lineno=29, col_offset=57, end_lineno=29, end_col_offset=62, value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=21,
                            col_offset=5,
                            end_lineno=21,
                            end_col_offset=47,
                            func=Attribute(
                                lineno=21,
                                col_offset=5,
                                end_lineno=21,
                                end_col_offset=17,
                                value=Name(lineno=21, col_offset=5, end_lineno=21, end_col_offset=8, id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=21, col_offset=18, end_lineno=21, end_col_offset=46, value='module_website_event_track', kind=None)],
                            keywords=[],
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