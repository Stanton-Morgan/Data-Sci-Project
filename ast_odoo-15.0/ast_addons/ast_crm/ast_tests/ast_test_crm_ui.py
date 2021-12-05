Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=54,
            module='odoo.addons.crm.tests.common',
            names=[alias(name='TestCrmCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo.tests',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=43,
            module='odoo.tests.common',
            names=[
                alias(name='tagged', asname=None),
                alias(name='users', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=29,
            end_col_offset=62,
            name='TestUi',
            bases=[Name(lineno=9, col_offset=13, end_lineno=9, end_col_offset=21, id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=58,
                    name='test_01_crm_tour',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=25, end_lineno=11, end_col_offset=29, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=12,
                            end_col_offset=58,
                            value=Call(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=58,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=23,
                                    value=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=12, col_offset=24, end_lineno=12, end_col_offset=30, value='/web', kind=None),
                                    Constant(lineno=12, col_offset=32, end_lineno=12, end_col_offset=42, value='crm_tour', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=12,
                                        col_offset=44,
                                        end_lineno=12,
                                        end_col_offset=57,
                                        arg='login',
                                        value=Constant(lineno=12, col_offset=50, end_lineno=12, end_col_offset=57, value='admin', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=26,
                    end_col_offset=72,
                    name='test_02_crm_tour_rainbowman',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=36, end_lineno=14, end_col_offset=40, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=17,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=10,
                            value=Call(
                                lineno=17,
                                col_offset=8,
                                end_lineno=25,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=17,
                                    col_offset=8,
                                    end_lineno=17,
                                    end_col_offset=36,
                                    value=Subscript(
                                        lineno=17,
                                        col_offset=8,
                                        end_lineno=17,
                                        end_col_offset=29,
                                        value=Attribute(
                                            lineno=17,
                                            col_offset=8,
                                            end_lineno=17,
                                            end_col_offset=16,
                                            value=Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=17, col_offset=17, end_lineno=17, end_col_offset=28, value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=17,
                                        col_offset=37,
                                        end_lineno=25,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=18, col_offset=12, end_lineno=18, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=19, col_offset=12, end_lineno=19, end_col_offset=19, value='login', kind=None),
                                            Constant(lineno=20, col_offset=12, end_lineno=20, end_col_offset=22, value='password', kind=None),
                                            Constant(lineno=21, col_offset=12, end_lineno=21, end_col_offset=23, value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=18, col_offset=20, end_lineno=18, end_col_offset=40, value='Temporary CRM User', kind=None),
                                            Constant(lineno=19, col_offset=21, end_lineno=19, end_col_offset=36, value='temp_crm_user', kind=None),
                                            Constant(lineno=20, col_offset=24, end_lineno=20, end_col_offset=39, value='temp_crm_user', kind=None),
                                            List(
                                                lineno=21,
                                                col_offset=25,
                                                end_lineno=24,
                                                end_col_offset=19,
                                                elts=[
                                                    Tuple(
                                                        lineno=21,
                                                        col_offset=26,
                                                        end_lineno=24,
                                                        end_col_offset=18,
                                                        elts=[
                                                            Constant(lineno=21, col_offset=27, end_lineno=21, end_col_offset=28, value=6, kind=None),
                                                            Constant(lineno=21, col_offset=30, end_lineno=21, end_col_offset=31, value=0, kind=None),
                                                            List(
                                                                lineno=21,
                                                                col_offset=33,
                                                                end_lineno=24,
                                                                end_col_offset=17,
                                                                elts=[
                                                                    Call(
                                                                        lineno=22,
                                                                        col_offset=20,
                                                                        end_lineno=22,
                                                                        end_col_offset=47,
                                                                        func=Attribute(
                                                                            lineno=22,
                                                                            col_offset=20,
                                                                            end_lineno=22,
                                                                            end_col_offset=28,
                                                                            value=Name(lineno=22, col_offset=20, end_lineno=22, end_col_offset=24, id='self', ctx=Load()),
                                                                            attr='ref',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(lineno=22, col_offset=29, end_lineno=22, end_col_offset=46, value='base.group_user', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        lineno=23,
                                                                        col_offset=20,
                                                                        end_lineno=23,
                                                                        end_col_offset=62,
                                                                        func=Attribute(
                                                                            lineno=23,
                                                                            col_offset=20,
                                                                            end_lineno=23,
                                                                            end_col_offset=28,
                                                                            value=Name(lineno=23, col_offset=20, end_lineno=23, end_col_offset=24, id='self', ctx=Load()),
                                                                            attr='ref',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(lineno=23, col_offset=29, end_lineno=23, end_col_offset=61, value='sales_team.group_sale_salesman', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=72,
                            value=Call(
                                lineno=26,
                                col_offset=8,
                                end_lineno=26,
                                end_col_offset=72,
                                func=Attribute(
                                    lineno=26,
                                    col_offset=8,
                                    end_lineno=26,
                                    end_col_offset=23,
                                    value=Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=26, col_offset=24, end_lineno=26, end_col_offset=30, value='/web', kind=None),
                                    Constant(lineno=26, col_offset=32, end_lineno=26, end_col_offset=48, value='crm_rainbowman', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=26,
                                        col_offset=50,
                                        end_lineno=26,
                                        end_col_offset=71,
                                        arg='login',
                                        value=Constant(lineno=26, col_offset=56, end_lineno=26, end_col_offset=71, value='temp_crm_user', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=28,
                    col_offset=4,
                    end_lineno=29,
                    end_col_offset=62,
                    name='test_03_crm_tour_forecast',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=28, col_offset=34, end_lineno=28, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=62,
                            value=Call(
                                lineno=29,
                                col_offset=8,
                                end_lineno=29,
                                end_col_offset=62,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=8,
                                    end_lineno=29,
                                    end_col_offset=23,
                                    value=Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=29, col_offset=24, end_lineno=29, end_col_offset=30, value='/web', kind=None),
                                    Constant(lineno=29, col_offset=32, end_lineno=29, end_col_offset=46, value='crm_forecast', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=29,
                                        col_offset=48,
                                        end_lineno=29,
                                        end_col_offset=61,
                                        arg='login',
                                        value=Constant(lineno=29, col_offset=54, end_lineno=29, end_col_offset=61, value='admin', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    lineno=8,
                    col_offset=1,
                    end_lineno=8,
                    end_col_offset=38,
                    func=Name(lineno=8, col_offset=1, end_lineno=8, end_col_offset=7, id='tagged', ctx=Load()),
                    args=[
                        Constant(lineno=8, col_offset=8, end_lineno=8, end_col_offset=22, value='post_install', kind=None),
                        Constant(lineno=8, col_offset=24, end_lineno=8, end_col_offset=37, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            lineno=31,
            col_offset=0,
            end_lineno=35,
            end_col_offset=60,
            name='TestCRMLeadMisc',
            bases=[Name(lineno=31, col_offset=22, end_lineno=31, end_col_offset=35, id='TestCrmCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=34,
                    col_offset=4,
                    end_lineno=35,
                    end_col_offset=60,
                    name='test_team_my_pipeline',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=34, col_offset=30, end_lineno=34, end_col_offset=34, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=35,
                            col_offset=8,
                            end_lineno=35,
                            end_col_offset=60,
                            targets=[Name(lineno=35, col_offset=8, end_lineno=35, end_col_offset=14, id='action', ctx=Store())],
                            value=Call(
                                lineno=35,
                                col_offset=17,
                                end_lineno=35,
                                end_col_offset=60,
                                func=Attribute(
                                    lineno=35,
                                    col_offset=17,
                                    end_lineno=35,
                                    end_col_offset=58,
                                    value=Subscript(
                                        lineno=35,
                                        col_offset=17,
                                        end_lineno=35,
                                        end_col_offset=37,
                                        value=Attribute(
                                            lineno=35,
                                            col_offset=17,
                                            end_lineno=35,
                                            end_col_offset=25,
                                            value=Name(lineno=35, col_offset=17, end_lineno=35, end_col_offset=21, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=35, col_offset=26, end_lineno=35, end_col_offset=36, value='crm.team', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_your_pipeline',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=33,
                            col_offset=5,
                            end_lineno=33,
                            end_col_offset=30,
                            func=Name(lineno=33, col_offset=5, end_lineno=33, end_col_offset=10, id='users', ctx=Load()),
                            args=[Constant(lineno=33, col_offset=11, end_lineno=33, end_col_offset=29, value='user_sales_leads', kind=None)],
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
