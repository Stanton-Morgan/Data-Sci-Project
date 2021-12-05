Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=38,
            module='odoo.tests.common',
            names=[alias(name='BaseCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=30,
            module='controllers',
            names=[alias(name='main', asname=None)],
            level=2,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=55,
            end_col_offset=10,
            name='ActionMungerTest',
            bases=[Name(lineno=7, col_offset=23, end_lineno=7, end_col_offset=31, id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=8,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=41,
                    name='test_actual_treeview',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=8, col_offset=29, end_lineno=8, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=9,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=9,
                            targets=[Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=14, id='action', ctx=Store())],
                            value=Dict(
                                lineno=9,
                                col_offset=17,
                                end_lineno=15,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=19, value='views', kind=None),
                                    Constant(lineno=12, col_offset=12, end_lineno=12, end_col_offset=23, value='view_type', kind=None),
                                    Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=21, value='view_id', kind=None),
                                    Constant(lineno=14, col_offset=12, end_lineno=14, end_col_offset=23, value='view_mode', kind=None),
                                ],
                                values=[
                                    List(
                                        lineno=10,
                                        col_offset=21,
                                        end_lineno=11,
                                        end_col_offset=42,
                                        elts=[
                                            List(
                                                lineno=10,
                                                col_offset=22,
                                                end_lineno=10,
                                                end_col_offset=37,
                                                elts=[
                                                    Constant(lineno=10, col_offset=23, end_lineno=10, end_col_offset=28, value=False, kind=None),
                                                    Constant(lineno=10, col_offset=30, end_lineno=10, end_col_offset=36, value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                lineno=10,
                                                col_offset=39,
                                                end_lineno=10,
                                                end_col_offset=54,
                                                elts=[
                                                    Constant(lineno=10, col_offset=40, end_lineno=10, end_col_offset=45, value=False, kind=None),
                                                    Constant(lineno=10, col_offset=47, end_lineno=10, end_col_offset=53, value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                lineno=11,
                                                col_offset=22,
                                                end_lineno=11,
                                                end_col_offset=41,
                                                elts=[
                                                    Constant(lineno=11, col_offset=23, end_lineno=11, end_col_offset=28, value=False, kind=None),
                                                    Constant(lineno=11, col_offset=30, end_lineno=11, end_col_offset=40, value='calendar', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=12, col_offset=25, end_lineno=12, end_col_offset=31, value='tree', kind=None),
                                    Constant(lineno=13, col_offset=23, end_lineno=13, end_col_offset=28, value=False, kind=None),
                                    Constant(lineno=14, col_offset=25, end_lineno=14, end_col_offset=45, value='tree,form,calendar', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=31,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=15, id='changed', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=18,
                                end_lineno=16,
                                end_col_offset=31,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=18,
                                    end_lineno=16,
                                    end_col_offset=29,
                                    value=Name(lineno=16, col_offset=18, end_lineno=16, end_col_offset=24, id='action', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Delete(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=31,
                            targets=[
                                Subscript(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=31,
                                    value=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, id='action', ctx=Load()),
                                    slice=Constant(lineno=17, col_offset=19, end_lineno=17, end_col_offset=30, value='view_type', kind=None),
                                    ctx=Del(),
                                ),
                            ],
                        ),
                        Expr(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=36,
                            value=Call(
                                lineno=18,
                                col_offset=8,
                                end_lineno=18,
                                end_col_offset=36,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=8,
                                    end_lineno=18,
                                    end_col_offset=27,
                                    value=Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=12, id='main', ctx=Load()),
                                    attr='fix_view_modes',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=18, col_offset=28, end_lineno=18, end_col_offset=35, id='changed', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=41,
                            value=Call(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=41,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=24,
                                    value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=20, col_offset=25, end_lineno=20, end_col_offset=32, id='changed', ctx=Load()),
                                    Name(lineno=20, col_offset=34, end_lineno=20, end_col_offset=40, id='action', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=22,
                    col_offset=4,
                    end_lineno=37,
                    end_col_offset=10,
                    name='test_list_view',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=22, col_offset=23, end_lineno=22, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=9,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=14, id='action', ctx=Store())],
                            value=Dict(
                                lineno=23,
                                col_offset=17,
                                end_lineno=29,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=24, col_offset=12, end_lineno=24, end_col_offset=19, value='views', kind=None),
                                    Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=23, value='view_type', kind=None),
                                    Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=21, value='view_id', kind=None),
                                    Constant(lineno=28, col_offset=12, end_lineno=28, end_col_offset=23, value='view_mode', kind=None),
                                ],
                                values=[
                                    List(
                                        lineno=24,
                                        col_offset=21,
                                        end_lineno=25,
                                        end_col_offset=42,
                                        elts=[
                                            List(
                                                lineno=24,
                                                col_offset=22,
                                                end_lineno=24,
                                                end_col_offset=37,
                                                elts=[
                                                    Constant(lineno=24, col_offset=23, end_lineno=24, end_col_offset=28, value=False, kind=None),
                                                    Constant(lineno=24, col_offset=30, end_lineno=24, end_col_offset=36, value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                lineno=24,
                                                col_offset=39,
                                                end_lineno=24,
                                                end_col_offset=54,
                                                elts=[
                                                    Constant(lineno=24, col_offset=40, end_lineno=24, end_col_offset=45, value=False, kind=None),
                                                    Constant(lineno=24, col_offset=47, end_lineno=24, end_col_offset=53, value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                lineno=25,
                                                col_offset=22,
                                                end_lineno=25,
                                                end_col_offset=41,
                                                elts=[
                                                    Constant(lineno=25, col_offset=23, end_lineno=25, end_col_offset=28, value=False, kind=None),
                                                    Constant(lineno=25, col_offset=30, end_lineno=25, end_col_offset=40, value='calendar', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=26, col_offset=25, end_lineno=26, end_col_offset=31, value='form', kind=None),
                                    Constant(lineno=27, col_offset=23, end_lineno=27, end_col_offset=28, value=False, kind=None),
                                    Constant(lineno=28, col_offset=25, end_lineno=28, end_col_offset=45, value='tree,form,calendar', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=35,
                            value=Call(
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=35,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=27,
                                    value=Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=12, id='main', ctx=Load()),
                                    attr='fix_view_modes',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=30, col_offset=28, end_lineno=30, end_col_offset=34, id='action', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=32,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=10,
                            value=Call(
                                lineno=32,
                                col_offset=8,
                                end_lineno=37,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=8,
                                    end_lineno=32,
                                    end_col_offset=24,
                                    value=Name(lineno=32, col_offset=8, end_lineno=32, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=32, col_offset=25, end_lineno=32, end_col_offset=31, id='action', ctx=Load()),
                                    Dict(
                                        lineno=32,
                                        col_offset=33,
                                        end_lineno=37,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=33, col_offset=12, end_lineno=33, end_col_offset=19, value='views', kind=None),
                                            Constant(lineno=35, col_offset=12, end_lineno=35, end_col_offset=21, value='view_id', kind=None),
                                            Constant(lineno=36, col_offset=12, end_lineno=36, end_col_offset=23, value='view_mode', kind=None),
                                        ],
                                        values=[
                                            List(
                                                lineno=33,
                                                col_offset=21,
                                                end_lineno=34,
                                                end_col_offset=42,
                                                elts=[
                                                    List(
                                                        lineno=33,
                                                        col_offset=22,
                                                        end_lineno=33,
                                                        end_col_offset=37,
                                                        elts=[
                                                            Constant(lineno=33, col_offset=23, end_lineno=33, end_col_offset=28, value=False, kind=None),
                                                            Constant(lineno=33, col_offset=30, end_lineno=33, end_col_offset=36, value='list', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        lineno=33,
                                                        col_offset=39,
                                                        end_lineno=33,
                                                        end_col_offset=54,
                                                        elts=[
                                                            Constant(lineno=33, col_offset=40, end_lineno=33, end_col_offset=45, value=False, kind=None),
                                                            Constant(lineno=33, col_offset=47, end_lineno=33, end_col_offset=53, value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        lineno=34,
                                                        col_offset=22,
                                                        end_lineno=34,
                                                        end_col_offset=41,
                                                        elts=[
                                                            Constant(lineno=34, col_offset=23, end_lineno=34, end_col_offset=28, value=False, kind=None),
                                                            Constant(lineno=34, col_offset=30, end_lineno=34, end_col_offset=40, value='calendar', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(lineno=35, col_offset=23, end_lineno=35, end_col_offset=28, value=False, kind=None),
                                            Constant(lineno=36, col_offset=25, end_lineno=36, end_col_offset=45, value='list,form,calendar', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=39,
                    col_offset=4,
                    end_lineno=55,
                    end_col_offset=10,
                    name='test_redundant_views',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=39, col_offset=29, end_lineno=39, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=41,
                            col_offset=8,
                            end_lineno=47,
                            end_col_offset=9,
                            targets=[Name(lineno=41, col_offset=8, end_lineno=41, end_col_offset=14, id='action', ctx=Store())],
                            value=Dict(
                                lineno=41,
                                col_offset=17,
                                end_lineno=47,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=42, col_offset=12, end_lineno=42, end_col_offset=19, value='views', kind=None),
                                    Constant(lineno=44, col_offset=12, end_lineno=44, end_col_offset=23, value='view_type', kind=None),
                                    Constant(lineno=45, col_offset=12, end_lineno=45, end_col_offset=21, value='view_id', kind=None),
                                    Constant(lineno=46, col_offset=12, end_lineno=46, end_col_offset=23, value='view_mode', kind=None),
                                ],
                                values=[
                                    List(
                                        lineno=42,
                                        col_offset=21,
                                        end_lineno=43,
                                        end_col_offset=56,
                                        elts=[
                                            List(
                                                lineno=42,
                                                col_offset=22,
                                                end_lineno=42,
                                                end_col_offset=37,
                                                elts=[
                                                    Constant(lineno=42, col_offset=23, end_lineno=42, end_col_offset=28, value=False, kind=None),
                                                    Constant(lineno=42, col_offset=30, end_lineno=42, end_col_offset=36, value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                lineno=42,
                                                col_offset=39,
                                                end_lineno=42,
                                                end_col_offset=54,
                                                elts=[
                                                    Constant(lineno=42, col_offset=40, end_lineno=42, end_col_offset=45, value=False, kind=None),
                                                    Constant(lineno=42, col_offset=47, end_lineno=42, end_col_offset=53, value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                lineno=43,
                                                col_offset=22,
                                                end_lineno=43,
                                                end_col_offset=41,
                                                elts=[
                                                    Constant(lineno=43, col_offset=23, end_lineno=43, end_col_offset=28, value=False, kind=None),
                                                    Constant(lineno=43, col_offset=30, end_lineno=43, end_col_offset=40, value='calendar', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                lineno=43,
                                                col_offset=43,
                                                end_lineno=43,
                                                end_col_offset=55,
                                                elts=[
                                                    Constant(lineno=43, col_offset=44, end_lineno=43, end_col_offset=46, value=42, kind=None),
                                                    Constant(lineno=43, col_offset=48, end_lineno=43, end_col_offset=54, value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=44, col_offset=25, end_lineno=44, end_col_offset=31, value='form', kind=None),
                                    Constant(lineno=45, col_offset=23, end_lineno=45, end_col_offset=28, value=False, kind=None),
                                    Constant(lineno=46, col_offset=25, end_lineno=46, end_col_offset=45, value='tree,form,calendar', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=48,
                            col_offset=8,
                            end_lineno=48,
                            end_col_offset=35,
                            value=Call(
                                lineno=48,
                                col_offset=8,
                                end_lineno=48,
                                end_col_offset=35,
                                func=Attribute(
                                    lineno=48,
                                    col_offset=8,
                                    end_lineno=48,
                                    end_col_offset=27,
                                    value=Name(lineno=48, col_offset=8, end_lineno=48, end_col_offset=12, id='main', ctx=Load()),
                                    attr='fix_view_modes',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=48, col_offset=28, end_lineno=48, end_col_offset=34, id='action', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=50,
                            col_offset=8,
                            end_lineno=55,
                            end_col_offset=10,
                            value=Call(
                                lineno=50,
                                col_offset=8,
                                end_lineno=55,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=50,
                                    col_offset=8,
                                    end_lineno=50,
                                    end_col_offset=24,
                                    value=Name(lineno=50, col_offset=8, end_lineno=50, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=50, col_offset=25, end_lineno=50, end_col_offset=31, id='action', ctx=Load()),
                                    Dict(
                                        lineno=50,
                                        col_offset=33,
                                        end_lineno=55,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=51, col_offset=12, end_lineno=51, end_col_offset=19, value='views', kind=None),
                                            Constant(lineno=53, col_offset=12, end_lineno=53, end_col_offset=21, value='view_id', kind=None),
                                            Constant(lineno=54, col_offset=12, end_lineno=54, end_col_offset=23, value='view_mode', kind=None),
                                        ],
                                        values=[
                                            List(
                                                lineno=51,
                                                col_offset=21,
                                                end_lineno=52,
                                                end_col_offset=56,
                                                elts=[
                                                    List(
                                                        lineno=51,
                                                        col_offset=22,
                                                        end_lineno=51,
                                                        end_col_offset=37,
                                                        elts=[
                                                            Constant(lineno=51, col_offset=23, end_lineno=51, end_col_offset=28, value=False, kind=None),
                                                            Constant(lineno=51, col_offset=30, end_lineno=51, end_col_offset=36, value='list', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        lineno=51,
                                                        col_offset=39,
                                                        end_lineno=51,
                                                        end_col_offset=54,
                                                        elts=[
                                                            Constant(lineno=51, col_offset=40, end_lineno=51, end_col_offset=45, value=False, kind=None),
                                                            Constant(lineno=51, col_offset=47, end_lineno=51, end_col_offset=53, value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        lineno=52,
                                                        col_offset=22,
                                                        end_lineno=52,
                                                        end_col_offset=41,
                                                        elts=[
                                                            Constant(lineno=52, col_offset=23, end_lineno=52, end_col_offset=28, value=False, kind=None),
                                                            Constant(lineno=52, col_offset=30, end_lineno=52, end_col_offset=40, value='calendar', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        lineno=52,
                                                        col_offset=43,
                                                        end_lineno=52,
                                                        end_col_offset=55,
                                                        elts=[
                                                            Constant(lineno=52, col_offset=44, end_lineno=52, end_col_offset=46, value=42, kind=None),
                                                            Constant(lineno=52, col_offset=48, end_lineno=52, end_col_offset=54, value='list', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(lineno=53, col_offset=23, end_lineno=53, end_col_offset=28, value=False, kind=None),
                                            Constant(lineno=54, col_offset=25, end_lineno=54, end_col_offset=45, value='list,form,calendar', kind=None),
                                        ],
                                    ),
                                ],
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
