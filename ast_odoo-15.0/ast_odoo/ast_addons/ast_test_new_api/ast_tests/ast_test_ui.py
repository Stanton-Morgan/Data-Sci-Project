Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=17,
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=34,
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=62,
            module='odoo.addons.base.tests.common',
            names=[alias(name='HttpCaseWithUserDemo', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=10,
            col_offset=0,
            end_lineno=21,
            end_col_offset=72,
            name='TestUi',
            bases=[Name(lineno=10, col_offset=13, end_lineno=10, end_col_offset=33, id='HttpCaseWithUserDemo', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=72,
                    name='test_01_admin_widget_x2many',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=12, col_offset=36, end_lineno=12, end_col_offset=40, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=20,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=72,
                            value=Call(
                                lineno=20,
                                col_offset=8,
                                end_lineno=21,
                                end_col_offset=72,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=23,
                                    value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=20, col_offset=24, end_lineno=20, end_col_offset=69, value='/web#action=test_new_api.action_discussions', kind=None),
                                    Constant(lineno=21, col_offset=12, end_lineno=21, end_col_offset=27, value='widget_x2many', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=21,
                                        col_offset=29,
                                        end_lineno=21,
                                        end_col_offset=43,
                                        arg='step_delay',
                                        value=Constant(lineno=21, col_offset=40, end_lineno=21, end_col_offset=43, value=100, kind=None),
                                    ),
                                    keyword(
                                        lineno=21,
                                        col_offset=45,
                                        end_lineno=21,
                                        end_col_offset=58,
                                        arg='login',
                                        value=Constant(lineno=21, col_offset=51, end_lineno=21, end_col_offset=58, value='admin', kind=None),
                                    ),
                                    keyword(
                                        lineno=21,
                                        col_offset=60,
                                        end_lineno=21,
                                        end_col_offset=71,
                                        arg='timeout',
                                        value=Constant(lineno=21, col_offset=68, end_lineno=21, end_col_offset=71, value=120, kind=None),
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
                    lineno=9,
                    col_offset=1,
                    end_lineno=9,
                    end_col_offset=56,
                    func=Attribute(
                        lineno=9,
                        col_offset=1,
                        end_lineno=9,
                        end_col_offset=25,
                        value=Attribute(
                            lineno=9,
                            col_offset=1,
                            end_lineno=9,
                            end_col_offset=18,
                            value=Attribute(
                                lineno=9,
                                col_offset=1,
                                end_lineno=9,
                                end_col_offset=11,
                                value=Name(lineno=9, col_offset=1, end_lineno=9, end_col_offset=5, id='odoo', ctx=Load()),
                                attr='tests',
                                ctx=Load(),
                            ),
                            attr='common',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(lineno=9, col_offset=26, end_lineno=9, end_col_offset=40, value='post_install', kind=None),
                        Constant(lineno=9, col_offset=42, end_lineno=9, end_col_offset=55, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            lineno=25,
            col_offset=0,
            end_lineno=41,
            end_col_offset=43,
            name='TestUiTranslation',
            bases=[
                Attribute(
                    lineno=25,
                    col_offset=24,
                    end_lineno=25,
                    end_col_offset=43,
                    value=Attribute(
                        lineno=25,
                        col_offset=24,
                        end_lineno=25,
                        end_col_offset=34,
                        value=Name(lineno=25, col_offset=24, end_lineno=25, end_col_offset=28, id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=28,
                    col_offset=4,
                    end_lineno=41,
                    end_col_offset=43,
                    name='test_01_sql_constraints',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=28, col_offset=32, end_lineno=28, end_col_offset=36, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=52,
                            value=Call(
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=52,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=43,
                                    value=Subscript(
                                        lineno=30,
                                        col_offset=8,
                                        end_lineno=30,
                                        end_col_offset=28,
                                        value=Attribute(
                                            lineno=30,
                                            col_offset=8,
                                            end_lineno=30,
                                            end_col_offset=16,
                                            value=Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=30, col_offset=17, end_lineno=30, end_col_offset=27, value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=30, col_offset=44, end_lineno=30, end_col_offset=51, value='fr_FR', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=80,
                            value=Call(
                                lineno=31,
                                col_offset=8,
                                end_lineno=31,
                                end_col_offset=80,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=8,
                                    end_lineno=31,
                                    end_col_offset=69,
                                    value=Call(
                                        lineno=31,
                                        col_offset=8,
                                        end_lineno=31,
                                        end_col_offset=48,
                                        func=Attribute(
                                            lineno=31,
                                            col_offset=8,
                                            end_lineno=31,
                                            end_col_offset=20,
                                            value=Attribute(
                                                lineno=31,
                                                col_offset=8,
                                                end_lineno=31,
                                                end_col_offset=16,
                                                value=Name(lineno=31, col_offset=8, end_lineno=31, end_col_offset=12, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=31, col_offset=21, end_lineno=31, end_col_offset=47, value='base.module_test_new_api', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_update_translations',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=31,
                                        col_offset=70,
                                        end_lineno=31,
                                        end_col_offset=79,
                                        elts=[Constant(lineno=31, col_offset=71, end_lineno=31, end_col_offset=78, value='fr_FR', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=97,
                            targets=[Name(lineno=32, col_offset=8, end_lineno=32, end_col_offset=18, id='constraint', ctx=Store())],
                            value=Call(
                                lineno=32,
                                col_offset=21,
                                end_lineno=32,
                                end_col_offset=97,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=21,
                                    end_lineno=32,
                                    end_col_offset=33,
                                    value=Attribute(
                                        lineno=32,
                                        col_offset=21,
                                        end_lineno=32,
                                        end_col_offset=29,
                                        value=Name(lineno=32, col_offset=21, end_lineno=32, end_col_offset=25, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=32, col_offset=34, end_lineno=32, end_col_offset=96, value='test_new_api.constraint_test_new_api_category_positive_color', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=33,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=63,
                            targets=[Name(lineno=33, col_offset=8, end_lineno=33, end_col_offset=15, id='message', ctx=Store())],
                            value=Attribute(
                                lineno=33,
                                col_offset=18,
                                end_lineno=33,
                                end_col_offset=63,
                                value=Call(
                                    lineno=33,
                                    col_offset=18,
                                    end_lineno=33,
                                    end_col_offset=55,
                                    func=Attribute(
                                        lineno=33,
                                        col_offset=18,
                                        end_lineno=33,
                                        end_col_offset=41,
                                        value=Name(lineno=33, col_offset=18, end_lineno=33, end_col_offset=28, id='constraint', ctx=Load()),
                                        attr='with_context',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            lineno=33,
                                            col_offset=42,
                                            end_lineno=33,
                                            end_col_offset=54,
                                            arg='lang',
                                            value=Constant(lineno=33, col_offset=47, end_lineno=33, end_col_offset=54, value='fr_FR', kind=None),
                                        ),
                                    ],
                                ),
                                attr='message',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=80,
                            value=Call(
                                lineno=34,
                                col_offset=8,
                                end_lineno=34,
                                end_col_offset=80,
                                func=Attribute(
                                    lineno=34,
                                    col_offset=8,
                                    end_lineno=34,
                                    end_col_offset=24,
                                    value=Name(lineno=34, col_offset=8, end_lineno=34, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=34, col_offset=25, end_lineno=34, end_col_offset=32, id='message', ctx=Load()),
                                    Constant(lineno=34, col_offset=34, end_lineno=34, end_col_offset=79, value='La couleur doit être une valeur positive !', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=40,
                            col_offset=8,
                            end_lineno=41,
                            end_col_offset=43,
                            value=Call(
                                lineno=40,
                                col_offset=8,
                                end_lineno=41,
                                end_col_offset=43,
                                func=Attribute(
                                    lineno=40,
                                    col_offset=8,
                                    end_lineno=40,
                                    end_col_offset=23,
                                    value=Name(lineno=40, col_offset=8, end_lineno=40, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=40, col_offset=24, end_lineno=40, end_col_offset=68, value='/web#action=test_new_api.action_categories', kind=None),
                                    Constant(lineno=41, col_offset=12, end_lineno=41, end_col_offset=27, value='sql_constaint', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=41,
                                        col_offset=29,
                                        end_lineno=41,
                                        end_col_offset=42,
                                        arg='login',
                                        value=Constant(lineno=41, col_offset=35, end_lineno=41, end_col_offset=42, value='admin', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=27,
                            col_offset=5,
                            end_lineno=27,
                            end_col_offset=44,
                            func=Name(lineno=27, col_offset=5, end_lineno=27, end_col_offset=16, id='mute_logger', ctx=Load()),
                            args=[
                                Constant(lineno=27, col_offset=17, end_lineno=27, end_col_offset=30, value='odoo.sql_db', kind=None),
                                Constant(lineno=27, col_offset=32, end_lineno=27, end_col_offset=43, value='odoo.http', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    lineno=24,
                    col_offset=1,
                    end_lineno=24,
                    end_col_offset=49,
                    func=Attribute(
                        lineno=24,
                        col_offset=1,
                        end_lineno=24,
                        end_col_offset=18,
                        value=Attribute(
                            lineno=24,
                            col_offset=1,
                            end_lineno=24,
                            end_col_offset=11,
                            value=Name(lineno=24, col_offset=1, end_lineno=24, end_col_offset=5, id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(lineno=24, col_offset=19, end_lineno=24, end_col_offset=32, value='-at_install', kind=None),
                        Constant(lineno=24, col_offset=34, end_lineno=24, end_col_offset=48, value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
