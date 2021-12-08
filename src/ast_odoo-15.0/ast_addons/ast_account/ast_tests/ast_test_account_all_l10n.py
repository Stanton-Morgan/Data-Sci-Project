Module(
    body=[
        Import(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=14,
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=33,
            module='odoo.tests',
            names=[alias(name='standalone', asname=None)],
            level=0,
        ),
        Assign(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=37,
            targets=[Name(lineno=7, col_offset=0, end_lineno=7, end_col_offset=7, id='_logger', ctx=Store())],
            value=Call(
                lineno=7,
                col_offset=10,
                end_lineno=7,
                end_col_offset=37,
                func=Attribute(
                    lineno=7,
                    col_offset=10,
                    end_lineno=7,
                    end_col_offset=27,
                    value=Name(lineno=7, col_offset=10, end_lineno=7, end_col_offset=17, id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(lineno=7, col_offset=28, end_lineno=7, end_col_offset=36, id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            lineno=11,
            col_offset=0,
            end_lineno=41,
            end_col_offset=80,
            name='test_all_l10n',
            args=arguments(
                posonlyargs=[],
                args=[arg(lineno=11, col_offset=18, end_lineno=11, end_col_offset=21, arg='env', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    lineno=12,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=7,
                    value=Constant(lineno=12, col_offset=4, end_lineno=15, end_col_offset=7, value=' This test will install all the l10n_* modules.\n    As the module install is not yet fully transactional, the modules will\n    remain installed after the test.\n    ', kind=None),
                ),
                Assert(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=81,
                    test=Attribute(
                        lineno=16,
                        col_offset=11,
                        end_lineno=16,
                        end_col_offset=46,
                        value=Call(
                            lineno=16,
                            col_offset=11,
                            end_lineno=16,
                            end_col_offset=41,
                            func=Attribute(
                                lineno=16,
                                col_offset=11,
                                end_lineno=16,
                                end_col_offset=18,
                                value=Name(lineno=16, col_offset=11, end_lineno=16, end_col_offset=14, id='env', ctx=Load()),
                                attr='ref',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=16, col_offset=19, end_lineno=16, end_col_offset=40, value='base.module_account', kind=None)],
                            keywords=[],
                        ),
                        attr='demo',
                        ctx=Load(),
                    ),
                    msg=Constant(lineno=16, col_offset=48, end_lineno=16, end_col_offset=81, value='Need the demo to test with data', kind=None),
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=6,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=13, id='l10n_mods', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=16,
                        end_lineno=20,
                        end_col_offset=6,
                        func=Attribute(
                            lineno=17,
                            col_offset=16,
                            end_lineno=17,
                            end_col_offset=46,
                            value=Subscript(
                                lineno=17,
                                col_offset=16,
                                end_lineno=17,
                                end_col_offset=39,
                                value=Name(lineno=17, col_offset=16, end_lineno=17, end_col_offset=19, id='env', ctx=Load()),
                                slice=Constant(lineno=17, col_offset=20, end_lineno=17, end_col_offset=38, value='ir.module.module', kind=None),
                                ctx=Load(),
                            ),
                            attr='search',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                lineno=17,
                                col_offset=47,
                                end_lineno=20,
                                end_col_offset=5,
                                elts=[
                                    Tuple(
                                        lineno=18,
                                        col_offset=8,
                                        end_lineno=18,
                                        end_col_offset=33,
                                        elts=[
                                            Constant(lineno=18, col_offset=9, end_lineno=18, end_col_offset=15, value='name', kind=None),
                                            Constant(lineno=18, col_offset=17, end_lineno=18, end_col_offset=23, value='like', kind=None),
                                            Constant(lineno=18, col_offset=25, end_lineno=18, end_col_offset=32, value='l10n%', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=19,
                                        col_offset=8,
                                        end_lineno=19,
                                        end_col_offset=37,
                                        elts=[
                                            Constant(lineno=19, col_offset=9, end_lineno=19, end_col_offset=16, value='state', kind=None),
                                            Constant(lineno=19, col_offset=18, end_lineno=19, end_col_offset=21, value='=', kind=None),
                                            Constant(lineno=19, col_offset=23, end_lineno=19, end_col_offset=36, value='uninstalled', kind=None),
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
                Expr(
                    lineno=21,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=40,
                    value=Call(
                        lineno=21,
                        col_offset=4,
                        end_lineno=21,
                        end_col_offset=40,
                        func=Attribute(
                            lineno=21,
                            col_offset=4,
                            end_lineno=21,
                            end_col_offset=38,
                            value=Name(lineno=21, col_offset=4, end_lineno=21, end_col_offset=13, id='l10n_mods', ctx=Load()),
                            attr='button_immediate_install',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Expr(
                    lineno=22,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=15,
                    value=Call(
                        lineno=22,
                        col_offset=4,
                        end_lineno=22,
                        end_col_offset=15,
                        func=Attribute(
                            lineno=22,
                            col_offset=4,
                            end_lineno=22,
                            end_col_offset=13,
                            value=Name(lineno=22, col_offset=4, end_lineno=22, end_col_offset=7, id='env', ctx=Load()),
                            attr='reset',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=23,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=15,
                    targets=[Name(lineno=23, col_offset=4, end_lineno=23, end_col_offset=7, id='env', ctx=Store())],
                    value=Call(
                        lineno=23,
                        col_offset=10,
                        end_lineno=23,
                        end_col_offset=15,
                        func=Name(lineno=23, col_offset=10, end_lineno=23, end_col_offset=13, id='env', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=25,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=6,
                    targets=[Name(lineno=25, col_offset=4, end_lineno=25, end_col_offset=8, id='coas', ctx=Store())],
                    value=Call(
                        lineno=25,
                        col_offset=11,
                        end_lineno=27,
                        end_col_offset=6,
                        func=Attribute(
                            lineno=25,
                            col_offset=11,
                            end_lineno=25,
                            end_col_offset=47,
                            value=Subscript(
                                lineno=25,
                                col_offset=11,
                                end_lineno=25,
                                end_col_offset=40,
                                value=Name(lineno=25, col_offset=11, end_lineno=25, end_col_offset=14, id='env', ctx=Load()),
                                slice=Constant(lineno=25, col_offset=15, end_lineno=25, end_col_offset=39, value='account.chart.template', kind=None),
                                ctx=Load(),
                            ),
                            attr='search',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                lineno=25,
                                col_offset=48,
                                end_lineno=27,
                                end_col_offset=5,
                                elts=[
                                    Tuple(
                                        lineno=26,
                                        col_offset=8,
                                        end_lineno=26,
                                        end_col_offset=77,
                                        elts=[
                                            Constant(lineno=26, col_offset=9, end_lineno=26, end_col_offset=13, value='id', kind=None),
                                            Constant(lineno=26, col_offset=15, end_lineno=26, end_col_offset=23, value='not in', kind=None),
                                            Attribute(
                                                lineno=26,
                                                col_offset=25,
                                                end_lineno=26,
                                                end_col_offset=76,
                                                value=Attribute(
                                                    lineno=26,
                                                    col_offset=25,
                                                    end_lineno=26,
                                                    end_col_offset=72,
                                                    value=Call(
                                                        lineno=26,
                                                        col_offset=25,
                                                        end_lineno=26,
                                                        end_col_offset=54,
                                                        func=Attribute(
                                                            lineno=26,
                                                            col_offset=25,
                                                            end_lineno=26,
                                                            end_col_offset=50,
                                                            value=Subscript(
                                                                lineno=26,
                                                                col_offset=25,
                                                                end_lineno=26,
                                                                end_col_offset=43,
                                                                value=Name(lineno=26, col_offset=25, end_lineno=26, end_col_offset=28, id='env', ctx=Load()),
                                                                slice=Constant(lineno=26, col_offset=29, end_lineno=26, end_col_offset=42, value='res.company', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[List(lineno=26, col_offset=51, end_lineno=26, end_col_offset=53, elts=[], ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='chart_template_id',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
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
                For(
                    lineno=28,
                    col_offset=4,
                    end_lineno=41,
                    end_col_offset=80,
                    target=Name(lineno=28, col_offset=8, end_lineno=28, end_col_offset=11, id='coa', ctx=Store()),
                    iter=Name(lineno=28, col_offset=15, end_lineno=28, end_col_offset=19, id='coas', ctx=Load()),
                    body=[
                        Assign(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=42,
                            targets=[Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=13, id='cname', ctx=Store())],
                            value=BinOp(
                                lineno=29,
                                col_offset=16,
                                end_lineno=29,
                                end_col_offset=42,
                                left=Constant(lineno=29, col_offset=16, end_lineno=29, end_col_offset=28, value='company_%s', kind=None),
                                op=Mod(),
                                right=Call(
                                    lineno=29,
                                    col_offset=31,
                                    end_lineno=29,
                                    end_col_offset=42,
                                    func=Name(lineno=29, col_offset=31, end_lineno=29, end_col_offset=34, id='str', ctx=Load()),
                                    args=[
                                        Attribute(
                                            lineno=29,
                                            col_offset=35,
                                            end_lineno=29,
                                            end_col_offset=41,
                                            value=Name(lineno=29, col_offset=35, end_lineno=29, end_col_offset=38, id='coa', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=30,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=10,
                            targets=[Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=15, id='company', ctx=Store())],
                            value=Call(
                                lineno=30,
                                col_offset=18,
                                end_lineno=33,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=18,
                                    end_lineno=30,
                                    end_col_offset=43,
                                    value=Subscript(
                                        lineno=30,
                                        col_offset=18,
                                        end_lineno=30,
                                        end_col_offset=36,
                                        value=Name(lineno=30, col_offset=18, end_lineno=30, end_col_offset=21, id='env', ctx=Load()),
                                        slice=Constant(lineno=30, col_offset=22, end_lineno=30, end_col_offset=35, value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=30,
                                        col_offset=44,
                                        end_lineno=33,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=31, col_offset=12, end_lineno=31, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=32, col_offset=12, end_lineno=32, end_col_offset=24, value='country_id', kind=None),
                                        ],
                                        values=[
                                            Name(lineno=31, col_offset=20, end_lineno=31, end_col_offset=25, id='cname', ctx=Load()),
                                            Attribute(
                                                lineno=32,
                                                col_offset=26,
                                                end_lineno=32,
                                                end_col_offset=43,
                                                value=Attribute(
                                                    lineno=32,
                                                    col_offset=26,
                                                    end_lineno=32,
                                                    end_col_offset=40,
                                                    value=Name(lineno=32, col_offset=26, end_lineno=32, end_col_offset=29, id='coa', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=39,
                            target=Attribute(
                                lineno=34,
                                col_offset=8,
                                end_lineno=34,
                                end_col_offset=28,
                                value=Attribute(
                                    lineno=34,
                                    col_offset=8,
                                    end_lineno=34,
                                    end_col_offset=16,
                                    value=Name(lineno=34, col_offset=8, end_lineno=34, end_col_offset=11, id='env', ctx=Load()),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='company_ids',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Name(lineno=34, col_offset=32, end_lineno=34, end_col_offset=39, id='company', ctx=Load()),
                        ),
                        Assign(
                            lineno=35,
                            col_offset=8,
                            end_lineno=35,
                            end_col_offset=37,
                            targets=[
                                Attribute(
                                    lineno=35,
                                    col_offset=8,
                                    end_lineno=35,
                                    end_col_offset=27,
                                    value=Attribute(
                                        lineno=35,
                                        col_offset=8,
                                        end_lineno=35,
                                        end_col_offset=16,
                                        value=Name(lineno=35, col_offset=8, end_lineno=35, end_col_offset=11, id='env', ctx=Load()),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='company_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(lineno=35, col_offset=30, end_lineno=35, end_col_offset=37, id='company', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=36,
                            col_offset=8,
                            end_lineno=36,
                            end_col_offset=73,
                            value=Call(
                                lineno=36,
                                col_offset=8,
                                end_lineno=36,
                                end_col_offset=73,
                                func=Attribute(
                                    lineno=36,
                                    col_offset=8,
                                    end_lineno=36,
                                    end_col_offset=20,
                                    value=Name(lineno=36, col_offset=8, end_lineno=36, end_col_offset=15, id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        lineno=36,
                                        col_offset=21,
                                        end_lineno=36,
                                        end_col_offset=72,
                                        left=Constant(lineno=36, col_offset=21, end_lineno=36, end_col_offset=52, value='Testing COA: %s (company: %s)', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            lineno=36,
                                            col_offset=55,
                                            end_lineno=36,
                                            end_col_offset=72,
                                            elts=[
                                                Attribute(
                                                    lineno=36,
                                                    col_offset=56,
                                                    end_lineno=36,
                                                    end_col_offset=64,
                                                    value=Name(lineno=36, col_offset=56, end_lineno=36, end_col_offset=59, id='coa', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Name(lineno=36, col_offset=66, end_lineno=36, end_col_offset=71, id='cname', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            lineno=37,
                            col_offset=8,
                            end_lineno=41,
                            end_col_offset=80,
                            body=[
                                With(
                                    lineno=38,
                                    col_offset=12,
                                    end_lineno=39,
                                    end_col_offset=33,
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                lineno=38,
                                                col_offset=17,
                                                end_lineno=38,
                                                end_col_offset=35,
                                                func=Attribute(
                                                    lineno=38,
                                                    col_offset=17,
                                                    end_lineno=38,
                                                    end_col_offset=33,
                                                    value=Attribute(
                                                        lineno=38,
                                                        col_offset=17,
                                                        end_lineno=38,
                                                        end_col_offset=23,
                                                        value=Name(lineno=38, col_offset=17, end_lineno=38, end_col_offset=20, id='env', ctx=Load()),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='savepoint',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            lineno=39,
                                            col_offset=16,
                                            end_lineno=39,
                                            end_col_offset=33,
                                            value=Call(
                                                lineno=39,
                                                col_offset=16,
                                                end_lineno=39,
                                                end_col_offset=33,
                                                func=Attribute(
                                                    lineno=39,
                                                    col_offset=16,
                                                    end_lineno=39,
                                                    end_col_offset=31,
                                                    value=Name(lineno=39, col_offset=16, end_lineno=39, end_col_offset=19, id='coa', ctx=Load()),
                                                    attr='try_loading',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    lineno=40,
                                    col_offset=8,
                                    end_lineno=41,
                                    end_col_offset=80,
                                    type=Name(lineno=40, col_offset=15, end_lineno=40, end_col_offset=24, id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            lineno=41,
                                            col_offset=12,
                                            end_lineno=41,
                                            end_col_offset=80,
                                            value=Call(
                                                lineno=41,
                                                col_offset=12,
                                                end_lineno=41,
                                                end_col_offset=80,
                                                func=Attribute(
                                                    lineno=41,
                                                    col_offset=12,
                                                    end_lineno=41,
                                                    end_col_offset=25,
                                                    value=Name(lineno=41, col_offset=12, end_lineno=41, end_col_offset=19, id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(lineno=41, col_offset=26, end_lineno=41, end_col_offset=54, value='Error when creating COA %s', kind=None),
                                                    Attribute(
                                                        lineno=41,
                                                        col_offset=56,
                                                        end_lineno=41,
                                                        end_col_offset=64,
                                                        value=Name(lineno=41, col_offset=56, end_lineno=41, end_col_offset=59, id='coa', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        lineno=41,
                                                        col_offset=66,
                                                        end_lineno=41,
                                                        end_col_offset=79,
                                                        arg='exc_info',
                                                        value=Constant(lineno=41, col_offset=75, end_lineno=41, end_col_offset=79, value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    lineno=10,
                    col_offset=1,
                    end_lineno=10,
                    end_col_offset=23,
                    func=Name(lineno=10, col_offset=1, end_lineno=10, end_col_offset=11, id='standalone', ctx=Load()),
                    args=[Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=22, value='all_l10n', kind=None)],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)