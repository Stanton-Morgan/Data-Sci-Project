Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=43,
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=41,
            end_col_offset=97,
            name='IrCronTrigger',
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
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=32,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=32, value='ir.cron.trigger', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=41,
                    end_col_offset=97,
                    name='_check_image_cron_is_not_already_triggered',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=51, end_lineno=11, end_col_offset=55, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=11,
                            value=Constant(lineno=12, col_offset=8, end_lineno=24, end_col_offset=11, value=' Ensure that there is a maximum of one trigger at a time for `ir_cron_fetch_image`.\n\n        This cron is triggered in an optimal way to retrieve fastly the images without blocking a\n        worker for a long amount of time. It fetches images in multiples batches to allow other\n        crons to run in between. The cron also schedules itself if there are remaining products to\n        be processed or if it encounters errors like a rate limit reached, a ConnectionTimeout, or\n        service unavailable. Multiple triggers at the same will trouble the rate limit management\n        and/or errors handling. More information in `product_fetch_image_wizard.py`.\n\n        :return: None\n        :raise ValidationError: If the maximum number of coexisting triggers for\n                                `ir_cron_fetch_image` is reached\n        ', kind=None),
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=9,
                            targets=[Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=27, id='ir_cron_fetch_image', ctx=Store())],
                            value=Call(
                                lineno=25,
                                col_offset=30,
                                end_lineno=27,
                                end_col_offset=9,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=30,
                                    end_lineno=25,
                                    end_col_offset=42,
                                    value=Attribute(
                                        lineno=25,
                                        col_offset=30,
                                        end_lineno=25,
                                        end_col_offset=38,
                                        value=Name(lineno=25, col_offset=30, end_lineno=25, end_col_offset=34, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=48, value='product_images.ir_cron_fetch_image', kind=None)],
                                keywords=[
                                    keyword(
                                        lineno=26,
                                        col_offset=50,
                                        end_lineno=26,
                                        end_col_offset=74,
                                        arg='raise_if_not_found',
                                        value=Constant(lineno=26, col_offset=69, end_lineno=26, end_col_offset=74, value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=29,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=18,
                            test=BoolOp(
                                lineno=29,
                                col_offset=11,
                                end_lineno=29,
                                end_col_offset=76,
                                op=And(),
                                values=[
                                    Name(lineno=29, col_offset=11, end_lineno=29, end_col_offset=30, id='ir_cron_fetch_image', ctx=Load()),
                                    Compare(
                                        lineno=29,
                                        col_offset=35,
                                        end_lineno=29,
                                        end_col_offset=76,
                                        left=Attribute(
                                            lineno=29,
                                            col_offset=35,
                                            end_lineno=29,
                                            end_col_offset=50,
                                            value=Attribute(
                                                lineno=29,
                                                col_offset=35,
                                                end_lineno=29,
                                                end_col_offset=47,
                                                value=Name(lineno=29, col_offset=35, end_lineno=29, end_col_offset=39, id='self', ctx=Load()),
                                                attr='cron_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                lineno=29,
                                                col_offset=54,
                                                end_lineno=29,
                                                end_col_offset=76,
                                                value=Name(lineno=29, col_offset=54, end_lineno=29, end_col_offset=73, id='ir_cron_fetch_image', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[Return(lineno=30, col_offset=12, end_lineno=30, end_col_offset=18, value=None)],
                            orelse=[],
                        ),
                        Assign(
                            lineno=32,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=9,
                            targets=[Name(lineno=32, col_offset=8, end_lineno=32, end_col_offset=27, id='cron_triggers_count', ctx=Store())],
                            value=Call(
                                lineno=32,
                                col_offset=30,
                                end_lineno=34,
                                end_col_offset=9,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=30,
                                    end_lineno=32,
                                    end_col_offset=70,
                                    value=Subscript(
                                        lineno=32,
                                        col_offset=30,
                                        end_lineno=32,
                                        end_col_offset=57,
                                        value=Attribute(
                                            lineno=32,
                                            col_offset=30,
                                            end_lineno=32,
                                            end_col_offset=38,
                                            value=Name(lineno=32, col_offset=30, end_lineno=32, end_col_offset=34, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=32, col_offset=39, end_lineno=32, end_col_offset=56, value='ir.cron.trigger', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=33,
                                        col_offset=12,
                                        end_lineno=33,
                                        end_col_offset=54,
                                        elts=[
                                            Tuple(
                                                lineno=33,
                                                col_offset=13,
                                                end_lineno=33,
                                                end_col_offset=53,
                                                elts=[
                                                    Constant(lineno=33, col_offset=14, end_lineno=33, end_col_offset=23, value='cron_id', kind=None),
                                                    Constant(lineno=33, col_offset=25, end_lineno=33, end_col_offset=28, value='=', kind=None),
                                                    Attribute(
                                                        lineno=33,
                                                        col_offset=30,
                                                        end_lineno=33,
                                                        end_col_offset=52,
                                                        value=Name(lineno=33, col_offset=30, end_lineno=33, end_col_offset=49, id='ir_cron_fetch_image', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=39,
                            col_offset=8,
                            end_lineno=39,
                            end_col_offset=98,
                            targets=[Name(lineno=39, col_offset=8, end_lineno=39, end_col_offset=36, id='max_coexisting_cron_triggers', ctx=Store())],
                            value=IfExp(
                                lineno=39,
                                col_offset=39,
                                end_lineno=39,
                                end_col_offset=98,
                                test=Call(
                                    lineno=39,
                                    col_offset=44,
                                    end_lineno=39,
                                    end_col_offset=91,
                                    func=Attribute(
                                        lineno=39,
                                        col_offset=44,
                                        end_lineno=39,
                                        end_col_offset=64,
                                        value=Attribute(
                                            lineno=39,
                                            col_offset=44,
                                            end_lineno=39,
                                            end_col_offset=60,
                                            value=Attribute(
                                                lineno=39,
                                                col_offset=44,
                                                end_lineno=39,
                                                end_col_offset=52,
                                                value=Name(lineno=39, col_offset=44, end_lineno=39, end_col_offset=48, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=39, col_offset=65, end_lineno=39, end_col_offset=90, value='automatically_triggered', kind=None)],
                                    keywords=[],
                                ),
                                body=Constant(lineno=39, col_offset=39, end_lineno=39, end_col_offset=40, value=2, kind=None),
                                orelse=Constant(lineno=39, col_offset=97, end_lineno=39, end_col_offset=98, value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=40,
                            col_offset=8,
                            end_lineno=41,
                            end_col_offset=97,
                            test=Compare(
                                lineno=40,
                                col_offset=11,
                                end_lineno=40,
                                end_col_offset=61,
                                left=Name(lineno=40, col_offset=11, end_lineno=40, end_col_offset=30, id='cron_triggers_count', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Name(lineno=40, col_offset=33, end_lineno=40, end_col_offset=61, id='max_coexisting_cron_triggers', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    lineno=41,
                                    col_offset=12,
                                    end_lineno=41,
                                    end_col_offset=97,
                                    exc=Call(
                                        lineno=41,
                                        col_offset=18,
                                        end_lineno=41,
                                        end_col_offset=97,
                                        func=Name(lineno=41, col_offset=18, end_lineno=41, end_col_offset=33, id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=41,
                                                col_offset=34,
                                                end_lineno=41,
                                                end_col_offset=96,
                                                func=Name(lineno=41, col_offset=34, end_lineno=41, end_col_offset=35, id='_', ctx=Load()),
                                                args=[Constant(lineno=41, col_offset=36, end_lineno=41, end_col_offset=95, value='This action is already scheduled. Please try again later.', kind=None)],
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
                            lineno=10,
                            col_offset=5,
                            end_lineno=10,
                            end_col_offset=30,
                            func=Attribute(
                                lineno=10,
                                col_offset=5,
                                end_lineno=10,
                                end_col_offset=19,
                                value=Name(lineno=10, col_offset=5, end_lineno=10, end_col_offset=8, id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=10, col_offset=20, end_lineno=10, end_col_offset=29, value='cron_id', kind=None)],
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