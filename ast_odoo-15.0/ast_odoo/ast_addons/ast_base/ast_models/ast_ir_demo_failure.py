Module(
    body=[
        ImportFrom(
            lineno=1,
            col_offset=0,
            end_lineno=1,
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
            lineno=4,
            col_offset=0,
            end_lineno=12,
            end_col_offset=57,
            name='DemoFailure',
            bases=[
                Attribute(
                    lineno=4,
                    col_offset=18,
                    end_lineno=4,
                    end_col_offset=39,
                    value=Name(lineno=4, col_offset=18, end_lineno=4, end_col_offset=24, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    lineno=5,
                    col_offset=4,
                    end_lineno=6,
                    end_col_offset=7,
                    value=Constant(lineno=5, col_offset=4, end_lineno=6, end_col_offset=7, value=' Stores modules for which we could not install demo data\n    ', kind=None),
                ),
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=29,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=7, col_offset=12, end_lineno=7, end_col_offset=29, value='ir.demo_failure', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=33,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=8, col_offset=19, end_lineno=8, end_col_offset=33, value='Demo failure', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=83,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=13, id='module_id', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=16,
                        end_lineno=10,
                        end_col_offset=83,
                        func=Attribute(
                            lineno=10,
                            col_offset=16,
                            end_lineno=10,
                            end_col_offset=31,
                            value=Name(lineno=10, col_offset=16, end_lineno=10, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=32, end_lineno=10, end_col_offset=50, value='ir.module.module', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=52,
                                end_lineno=10,
                                end_col_offset=65,
                                arg='required',
                                value=Constant(lineno=10, col_offset=61, end_lineno=10, end_col_offset=65, value=True, kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=67,
                                end_lineno=10,
                                end_col_offset=82,
                                arg='string',
                                value=Constant(lineno=10, col_offset=74, end_lineno=10, end_col_offset=82, value='Module', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=39,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=9, id='error', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=12,
                        end_lineno=11,
                        end_col_offset=39,
                        func=Attribute(
                            lineno=11,
                            col_offset=12,
                            end_lineno=11,
                            end_col_offset=23,
                            value=Name(lineno=11, col_offset=12, end_lineno=11, end_col_offset=18, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=24,
                                end_lineno=11,
                                end_col_offset=38,
                                arg='string',
                                value=Constant(lineno=11, col_offset=31, end_lineno=11, end_col_offset=38, value='Error', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=57,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=13, id='wizard_id', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=16,
                        end_lineno=12,
                        end_col_offset=57,
                        func=Attribute(
                            lineno=12,
                            col_offset=16,
                            end_lineno=12,
                            end_col_offset=31,
                            value=Name(lineno=12, col_offset=16, end_lineno=12, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=32, end_lineno=12, end_col_offset=56, value='ir.demo_failure.wizard', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            lineno=14,
            col_offset=0,
            end_lineno=31,
            end_col_offset=50,
            name='DemoFailureWizard',
            bases=[
                Attribute(
                    lineno=14,
                    col_offset=24,
                    end_lineno=14,
                    end_col_offset=45,
                    value=Name(lineno=14, col_offset=24, end_lineno=14, end_col_offset=30, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=36,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=15, col_offset=12, end_lineno=15, end_col_offset=36, value='ir.demo_failure.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=40,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=16, col_offset=19, end_lineno=16, end_col_offset=40, value='Demo Failure wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=5,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=15, id='failure_ids', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=18,
                        end_lineno=21,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=18,
                            col_offset=18,
                            end_lineno=18,
                            end_col_offset=33,
                            value=Name(lineno=18, col_offset=18, end_lineno=18, end_col_offset=24, id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=19, col_offset=8, end_lineno=19, end_col_offset=25, value='ir.demo_failure', kind=None),
                            Constant(lineno=19, col_offset=27, end_lineno=19, end_col_offset=38, value='wizard_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=19,
                                col_offset=40,
                                end_lineno=19,
                                end_col_offset=53,
                                arg='readonly',
                                value=Constant(lineno=19, col_offset=49, end_lineno=19, end_col_offset=53, value=True, kind=None),
                            ),
                            keyword(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=43,
                                arg='string',
                                value=Constant(lineno=20, col_offset=15, end_lineno=20, end_col_offset=43, value='Demo Installation Failures', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=22,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=70,
                    targets=[Name(lineno=22, col_offset=4, end_lineno=22, end_col_offset=18, id='failures_count', ctx=Store())],
                    value=Call(
                        lineno=22,
                        col_offset=21,
                        end_lineno=22,
                        end_col_offset=70,
                        func=Attribute(
                            lineno=22,
                            col_offset=21,
                            end_lineno=22,
                            end_col_offset=35,
                            value=Name(lineno=22, col_offset=21, end_lineno=22, end_col_offset=27, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=22,
                                col_offset=36,
                                end_lineno=22,
                                end_col_offset=69,
                                arg='compute',
                                value=Constant(lineno=22, col_offset=44, end_lineno=22, end_col_offset=69, value='_compute_failures_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=25,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=49,
                    name='_compute_failures_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=25, col_offset=32, end_lineno=25, end_col_offset=36, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            lineno=26,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=49,
                            target=Name(lineno=26, col_offset=12, end_lineno=26, end_col_offset=13, id='r', ctx=Store()),
                            iter=Name(lineno=26, col_offset=17, end_lineno=26, end_col_offset=21, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=27,
                                    col_offset=12,
                                    end_lineno=27,
                                    end_col_offset=49,
                                    targets=[
                                        Attribute(
                                            lineno=27,
                                            col_offset=12,
                                            end_lineno=27,
                                            end_col_offset=28,
                                            value=Name(lineno=27, col_offset=12, end_lineno=27, end_col_offset=13, id='r', ctx=Load()),
                                            attr='failures_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=27,
                                        col_offset=31,
                                        end_lineno=27,
                                        end_col_offset=49,
                                        func=Name(lineno=27, col_offset=31, end_lineno=27, end_col_offset=34, id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                lineno=27,
                                                col_offset=35,
                                                end_lineno=27,
                                                end_col_offset=48,
                                                value=Name(lineno=27, col_offset=35, end_lineno=27, end_col_offset=36, id='r', ctx=Load()),
                                                attr='failure_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=24,
                            col_offset=5,
                            end_lineno=24,
                            end_col_offset=31,
                            func=Attribute(
                                lineno=24,
                                col_offset=5,
                                end_lineno=24,
                                end_col_offset=16,
                                value=Name(lineno=24, col_offset=5, end_lineno=24, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=24, col_offset=17, end_lineno=24, end_col_offset=30, value='failure_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=29,
                    col_offset=4,
                    end_lineno=31,
                    end_col_offset=50,
                    name='done',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=29, col_offset=13, end_lineno=29, end_col_offset=17, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=50,
                            value=Call(
                                lineno=31,
                                col_offset=15,
                                end_lineno=31,
                                end_col_offset=50,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=15,
                                    end_lineno=31,
                                    end_col_offset=48,
                                    value=Subscript(
                                        lineno=31,
                                        col_offset=15,
                                        end_lineno=31,
                                        end_col_offset=43,
                                        value=Attribute(
                                            lineno=31,
                                            col_offset=15,
                                            end_lineno=31,
                                            end_col_offset=23,
                                            value=Name(lineno=31, col_offset=15, end_lineno=31, end_col_offset=19, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=31, col_offset=24, end_lineno=31, end_col_offset=42, value='ir.module.module', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='next',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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