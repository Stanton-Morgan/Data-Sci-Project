Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=45,
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=30,
            end_col_offset=61,
            name='TestMenu',
            bases=[Name(lineno=7, col_offset=15, end_lineno=7, end_col_offset=30, id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=61,
                    name='test_00_menu_deletion',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=30, end_lineno=9, end_col_offset=34, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=10,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=37,
                            value=Constant(lineno=10, col_offset=8, end_lineno=11, end_col_offset=37, value='Verify that menu deletion works properly when there are child menus, and those\n           are indeed made orphans', kind=None),
                        ),
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=37,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=12, id='Menu', ctx=Store())],
                            value=Subscript(
                                lineno=12,
                                col_offset=15,
                                end_lineno=12,
                                end_col_offset=37,
                                value=Attribute(
                                    lineno=12,
                                    col_offset=15,
                                    end_lineno=12,
                                    end_col_offset=23,
                                    value=Name(lineno=12, col_offset=15, end_lineno=12, end_col_offset=19, id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(lineno=12, col_offset=24, end_lineno=12, end_col_offset=36, value='ir.ui.menu', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=49,
                            targets=[Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=12, id='root', ctx=Store())],
                            value=Call(
                                lineno=13,
                                col_offset=15,
                                end_lineno=13,
                                end_col_offset=49,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=15,
                                    end_lineno=13,
                                    end_col_offset=26,
                                    value=Name(lineno=13, col_offset=15, end_lineno=13, end_col_offset=19, id='Menu', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=13,
                                        col_offset=27,
                                        end_lineno=13,
                                        end_col_offset=48,
                                        keys=[Constant(lineno=13, col_offset=28, end_lineno=13, end_col_offset=34, value='name', kind=None)],
                                        values=[Constant(lineno=13, col_offset=36, end_lineno=13, end_col_offset=47, value='Test root', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=76,
                            targets=[Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=14, id='child1', ctx=Store())],
                            value=Call(
                                lineno=14,
                                col_offset=17,
                                end_lineno=14,
                                end_col_offset=76,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=17,
                                    end_lineno=14,
                                    end_col_offset=28,
                                    value=Name(lineno=14, col_offset=17, end_lineno=14, end_col_offset=21, id='Menu', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=14,
                                        col_offset=29,
                                        end_lineno=14,
                                        end_col_offset=75,
                                        keys=[
                                            Constant(lineno=14, col_offset=30, end_lineno=14, end_col_offset=36, value='name', kind=None),
                                            Constant(lineno=14, col_offset=54, end_lineno=14, end_col_offset=65, value='parent_id', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=14, col_offset=38, end_lineno=14, end_col_offset=52, value='Test child 1', kind=None),
                                            Attribute(
                                                lineno=14,
                                                col_offset=67,
                                                end_lineno=14,
                                                end_col_offset=74,
                                                value=Name(lineno=14, col_offset=67, end_lineno=14, end_col_offset=71, id='root', ctx=Load()),
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
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=76,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=14, id='child2', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=17,
                                end_lineno=15,
                                end_col_offset=76,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=17,
                                    end_lineno=15,
                                    end_col_offset=28,
                                    value=Name(lineno=15, col_offset=17, end_lineno=15, end_col_offset=21, id='Menu', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=15,
                                        col_offset=29,
                                        end_lineno=15,
                                        end_col_offset=75,
                                        keys=[
                                            Constant(lineno=15, col_offset=30, end_lineno=15, end_col_offset=36, value='name', kind=None),
                                            Constant(lineno=15, col_offset=54, end_lineno=15, end_col_offset=65, value='parent_id', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=15, col_offset=38, end_lineno=15, end_col_offset=52, value='Test child 2', kind=None),
                                            Attribute(
                                                lineno=15,
                                                col_offset=67,
                                                end_lineno=15,
                                                end_col_offset=74,
                                                value=Name(lineno=15, col_offset=67, end_lineno=15, end_col_offset=71, id='root', ctx=Load()),
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
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=81,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=15, id='child21', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=18,
                                end_lineno=16,
                                end_col_offset=81,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=18,
                                    end_lineno=16,
                                    end_col_offset=29,
                                    value=Name(lineno=16, col_offset=18, end_lineno=16, end_col_offset=22, id='Menu', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=16,
                                        col_offset=30,
                                        end_lineno=16,
                                        end_col_offset=80,
                                        keys=[
                                            Constant(lineno=16, col_offset=31, end_lineno=16, end_col_offset=37, value='name', kind=None),
                                            Constant(lineno=16, col_offset=57, end_lineno=16, end_col_offset=68, value='parent_id', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=16, col_offset=39, end_lineno=16, end_col_offset=55, value='Test child 2-1', kind=None),
                                            Attribute(
                                                lineno=16,
                                                col_offset=70,
                                                end_lineno=16,
                                                end_col_offset=79,
                                                value=Name(lineno=16, col_offset=70, end_lineno=16, end_col_offset=76, id='child2', ctx=Load()),
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
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=61,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=15, id='all_ids', ctx=Store())],
                            value=List(
                                lineno=17,
                                col_offset=18,
                                end_lineno=17,
                                end_col_offset=61,
                                elts=[
                                    Attribute(
                                        lineno=17,
                                        col_offset=19,
                                        end_lineno=17,
                                        end_col_offset=26,
                                        value=Name(lineno=17, col_offset=19, end_lineno=17, end_col_offset=23, id='root', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=17,
                                        col_offset=28,
                                        end_lineno=17,
                                        end_col_offset=37,
                                        value=Name(lineno=17, col_offset=28, end_lineno=17, end_col_offset=34, id='child1', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=17,
                                        col_offset=39,
                                        end_lineno=17,
                                        end_col_offset=48,
                                        value=Name(lineno=17, col_offset=39, end_lineno=17, end_col_offset=45, id='child2', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=17,
                                        col_offset=50,
                                        end_lineno=17,
                                        end_col_offset=60,
                                        value=Name(lineno=17, col_offset=50, end_lineno=17, end_col_offset=57, id='child21', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=21,
                            value=Call(
                                lineno=21,
                                col_offset=8,
                                end_lineno=21,
                                end_col_offset=21,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=8,
                                    end_lineno=21,
                                    end_col_offset=19,
                                    value=Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=12, id='root', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=82,
                            targets=[Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=12, id='Menu', ctx=Store())],
                            value=Call(
                                lineno=24,
                                col_offset=15,
                                end_lineno=24,
                                end_col_offset=82,
                                func=Attribute(
                                    lineno=24,
                                    col_offset=15,
                                    end_lineno=24,
                                    end_col_offset=50,
                                    value=Subscript(
                                        lineno=24,
                                        col_offset=15,
                                        end_lineno=24,
                                        end_col_offset=37,
                                        value=Attribute(
                                            lineno=24,
                                            col_offset=15,
                                            end_lineno=24,
                                            end_col_offset=23,
                                            value=Name(lineno=24, col_offset=15, end_lineno=24, end_col_offset=19, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=24, col_offset=24, end_lineno=24, end_col_offset=36, value='ir.ui.menu', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=24,
                                        col_offset=51,
                                        end_lineno=24,
                                        end_col_offset=81,
                                        keys=[Constant(lineno=24, col_offset=52, end_lineno=24, end_col_offset=74, value='ir.ui.menu.full_list', kind=None)],
                                        values=[Constant(lineno=24, col_offset=76, end_lineno=24, end_col_offset=80, value=True, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=68,
                            targets=[Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=17, id='remaining', ctx=Store())],
                            value=Call(
                                lineno=26,
                                col_offset=20,
                                end_lineno=26,
                                end_col_offset=68,
                                func=Attribute(
                                    lineno=26,
                                    col_offset=20,
                                    end_lineno=26,
                                    end_col_offset=31,
                                    value=Name(lineno=26, col_offset=20, end_lineno=26, end_col_offset=24, id='Menu', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=26,
                                        col_offset=32,
                                        end_lineno=26,
                                        end_col_offset=55,
                                        elts=[
                                            Tuple(
                                                lineno=26,
                                                col_offset=33,
                                                end_lineno=26,
                                                end_col_offset=54,
                                                elts=[
                                                    Constant(lineno=26, col_offset=34, end_lineno=26, end_col_offset=38, value='id', kind=None),
                                                    Constant(lineno=26, col_offset=40, end_lineno=26, end_col_offset=44, value='in', kind=None),
                                                    Name(lineno=26, col_offset=46, end_lineno=26, end_col_offset=53, id='all_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=26,
                                        col_offset=57,
                                        end_lineno=26,
                                        end_col_offset=67,
                                        arg='order',
                                        value=Constant(lineno=26, col_offset=63, end_lineno=26, end_col_offset=67, value='id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=27,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=75,
                            value=Call(
                                lineno=27,
                                col_offset=8,
                                end_lineno=27,
                                end_col_offset=75,
                                func=Attribute(
                                    lineno=27,
                                    col_offset=8,
                                    end_lineno=27,
                                    end_col_offset=24,
                                    value=Name(lineno=27, col_offset=8, end_lineno=27, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=27,
                                        col_offset=25,
                                        end_lineno=27,
                                        end_col_offset=59,
                                        elts=[
                                            Attribute(
                                                lineno=27,
                                                col_offset=26,
                                                end_lineno=27,
                                                end_col_offset=35,
                                                value=Name(lineno=27, col_offset=26, end_lineno=27, end_col_offset=32, id='child1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=27,
                                                col_offset=37,
                                                end_lineno=27,
                                                end_col_offset=46,
                                                value=Name(lineno=27, col_offset=37, end_lineno=27, end_col_offset=43, id='child2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=27,
                                                col_offset=48,
                                                end_lineno=27,
                                                end_col_offset=58,
                                                value=Name(lineno=27, col_offset=48, end_lineno=27, end_col_offset=55, id='child21', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=27,
                                        col_offset=61,
                                        end_lineno=27,
                                        end_col_offset=74,
                                        value=Name(lineno=27, col_offset=61, end_lineno=27, end_col_offset=70, id='remaining', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=94,
                            targets=[Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=15, id='orphans', ctx=Store())],
                            value=Call(
                                lineno=29,
                                col_offset=19,
                                end_lineno=29,
                                end_col_offset=94,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=19,
                                    end_lineno=29,
                                    end_col_offset=30,
                                    value=Name(lineno=29, col_offset=19, end_lineno=29, end_col_offset=23, id='Menu', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=29,
                                        col_offset=31,
                                        end_lineno=29,
                                        end_col_offset=81,
                                        elts=[
                                            Tuple(
                                                lineno=29,
                                                col_offset=32,
                                                end_lineno=29,
                                                end_col_offset=53,
                                                elts=[
                                                    Constant(lineno=29, col_offset=33, end_lineno=29, end_col_offset=37, value='id', kind=None),
                                                    Constant(lineno=29, col_offset=39, end_lineno=29, end_col_offset=43, value='in', kind=None),
                                                    Name(lineno=29, col_offset=45, end_lineno=29, end_col_offset=52, id='all_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=29,
                                                col_offset=55,
                                                end_lineno=29,
                                                end_col_offset=80,
                                                elts=[
                                                    Constant(lineno=29, col_offset=56, end_lineno=29, end_col_offset=67, value='parent_id', kind=None),
                                                    Constant(lineno=29, col_offset=69, end_lineno=29, end_col_offset=72, value='=', kind=None),
                                                    Constant(lineno=29, col_offset=74, end_lineno=29, end_col_offset=79, value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=29,
                                        col_offset=83,
                                        end_lineno=29,
                                        end_col_offset=93,
                                        arg='order',
                                        value=Constant(lineno=29, col_offset=89, end_lineno=29, end_col_offset=93, value='id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=61,
                            value=Call(
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=61,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=24,
                                    value=Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=30,
                                        col_offset=25,
                                        end_lineno=30,
                                        end_col_offset=47,
                                        elts=[
                                            Attribute(
                                                lineno=30,
                                                col_offset=26,
                                                end_lineno=30,
                                                end_col_offset=35,
                                                value=Name(lineno=30, col_offset=26, end_lineno=30, end_col_offset=32, id='child1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=30,
                                                col_offset=37,
                                                end_lineno=30,
                                                end_col_offset=46,
                                                value=Name(lineno=30, col_offset=37, end_lineno=30, end_col_offset=43, id='child2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=30,
                                        col_offset=49,
                                        end_lineno=30,
                                        end_col_offset=60,
                                        value=Name(lineno=30, col_offset=49, end_lineno=30, end_col_offset=56, id='orphans', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
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
