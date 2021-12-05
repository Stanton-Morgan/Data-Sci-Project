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
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=44,
            module='odoo.tools',
            names=[alias(name='get_cache_key_counter', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=39,
            end_col_offset=33,
            name='TestOrmcache',
            bases=[Name(lineno=8, col_offset=19, end_lineno=8, end_col_offset=34, id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=39,
                    end_col_offset=33,
                    name='test_ormcache',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=22, end_lineno=9, end_col_offset=26, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=10,
                            end_col_offset=67,
                            value=Constant(lineno=10, col_offset=8, end_lineno=10, end_col_offset=67, value=' Test the effectiveness of the ormcache() decorator. ', kind=None),
                        ),
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=39,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=11, id='IMD', ctx=Store())],
                            value=Subscript(
                                lineno=11,
                                col_offset=14,
                                end_lineno=11,
                                end_col_offset=39,
                                value=Attribute(
                                    lineno=11,
                                    col_offset=14,
                                    end_lineno=11,
                                    end_col_offset=22,
                                    value=Name(lineno=11, col_offset=14, end_lineno=11, end_col_offset=18, id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(lineno=11, col_offset=23, end_lineno=11, end_col_offset=38, value='ir.model.data', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=35,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=13, id='XMLID', ctx=Store())],
                            value=Constant(lineno=12, col_offset=16, end_lineno=12, end_col_offset=35, value='base.group_no_one', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=77,
                            targets=[
                                Tuple(
                                    lineno=15,
                                    col_offset=8,
                                    end_lineno=15,
                                    end_col_offset=27,
                                    elts=[
                                        Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=13, id='cache', ctx=Store()),
                                        Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=18, id='key', ctx=Store()),
                                        Name(lineno=15, col_offset=20, end_lineno=15, end_col_offset=27, id='counter', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=15,
                                col_offset=30,
                                end_lineno=15,
                                end_col_offset=77,
                                func=Name(lineno=15, col_offset=30, end_lineno=15, end_col_offset=51, id='get_cache_key_counter', ctx=Load()),
                                args=[
                                    Attribute(
                                        lineno=15,
                                        col_offset=52,
                                        end_lineno=15,
                                        end_col_offset=69,
                                        value=Name(lineno=15, col_offset=52, end_lineno=15, end_col_offset=55, id='IMD', ctx=Load()),
                                        attr='_xmlid_lookup',
                                        ctx=Load(),
                                    ),
                                    Name(lineno=15, col_offset=71, end_lineno=15, end_col_offset=76, id='XMLID', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=25,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=11, id='hit', ctx=Store())],
                            value=Attribute(
                                lineno=16,
                                col_offset=14,
                                end_lineno=16,
                                end_col_offset=25,
                                value=Name(lineno=16, col_offset=14, end_lineno=16, end_col_offset=21, id='counter', ctx=Load()),
                                attr='hit',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=27,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=12, id='miss', ctx=Store())],
                            value=Attribute(
                                lineno=17,
                                col_offset=15,
                                end_lineno=17,
                                end_col_offset=27,
                                value=Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=22, id='counter', ctx=Load()),
                                attr='miss',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=26,
                            value=Call(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=26,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=24,
                                    value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=11, id='IMD', ctx=Load()),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=36,
                            value=Call(
                                lineno=21,
                                col_offset=8,
                                end_lineno=21,
                                end_col_offset=36,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=8,
                                    end_lineno=21,
                                    end_col_offset=24,
                                    value=Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=21, col_offset=25, end_lineno=21, end_col_offset=28, id='key', ctx=Load()),
                                    Name(lineno=21, col_offset=30, end_lineno=21, end_col_offset=35, id='cache', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=27,
                            value=Call(
                                lineno=24,
                                col_offset=8,
                                end_lineno=24,
                                end_col_offset=27,
                                func=Attribute(
                                    lineno=24,
                                    col_offset=8,
                                    end_lineno=24,
                                    end_col_offset=20,
                                    value=Attribute(
                                        lineno=24,
                                        col_offset=8,
                                        end_lineno=24,
                                        end_col_offset=16,
                                        value=Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=12, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=24, col_offset=21, end_lineno=24, end_col_offset=26, id='XMLID', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=42,
                            value=Call(
                                lineno=25,
                                col_offset=8,
                                end_lineno=25,
                                end_col_offset=42,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=8,
                                    end_lineno=25,
                                    end_col_offset=24,
                                    value=Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=25,
                                        col_offset=25,
                                        end_lineno=25,
                                        end_col_offset=36,
                                        value=Name(lineno=25, col_offset=25, end_lineno=25, end_col_offset=32, id='counter', ctx=Load()),
                                        attr='hit',
                                        ctx=Load(),
                                    ),
                                    Name(lineno=25, col_offset=38, end_lineno=25, end_col_offset=41, id='hit', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=48,
                            value=Call(
                                lineno=26,
                                col_offset=8,
                                end_lineno=26,
                                end_col_offset=48,
                                func=Attribute(
                                    lineno=26,
                                    col_offset=8,
                                    end_lineno=26,
                                    end_col_offset=24,
                                    value=Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=26,
                                        col_offset=25,
                                        end_lineno=26,
                                        end_col_offset=37,
                                        value=Name(lineno=26, col_offset=25, end_lineno=26, end_col_offset=32, id='counter', ctx=Load()),
                                        attr='miss',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        lineno=26,
                                        col_offset=39,
                                        end_lineno=26,
                                        end_col_offset=47,
                                        left=Name(lineno=26, col_offset=39, end_lineno=26, end_col_offset=43, id='miss', ctx=Load()),
                                        op=Add(),
                                        right=Constant(lineno=26, col_offset=46, end_lineno=26, end_col_offset=47, value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=27,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=33,
                            value=Call(
                                lineno=27,
                                col_offset=8,
                                end_lineno=27,
                                end_col_offset=33,
                                func=Attribute(
                                    lineno=27,
                                    col_offset=8,
                                    end_lineno=27,
                                    end_col_offset=21,
                                    value=Name(lineno=27, col_offset=8, end_lineno=27, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=27, col_offset=22, end_lineno=27, end_col_offset=25, id='key', ctx=Load()),
                                    Name(lineno=27, col_offset=27, end_lineno=27, end_col_offset=32, id='cache', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=27,
                            value=Call(
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=27,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=20,
                                    value=Attribute(
                                        lineno=30,
                                        col_offset=8,
                                        end_lineno=30,
                                        end_col_offset=16,
                                        value=Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=12, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=30, col_offset=21, end_lineno=30, end_col_offset=26, id='XMLID', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=46,
                            value=Call(
                                lineno=31,
                                col_offset=8,
                                end_lineno=31,
                                end_col_offset=46,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=8,
                                    end_lineno=31,
                                    end_col_offset=24,
                                    value=Name(lineno=31, col_offset=8, end_lineno=31, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=31,
                                        col_offset=25,
                                        end_lineno=31,
                                        end_col_offset=36,
                                        value=Name(lineno=31, col_offset=25, end_lineno=31, end_col_offset=32, id='counter', ctx=Load()),
                                        attr='hit',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        lineno=31,
                                        col_offset=38,
                                        end_lineno=31,
                                        end_col_offset=45,
                                        left=Name(lineno=31, col_offset=38, end_lineno=31, end_col_offset=41, id='hit', ctx=Load()),
                                        op=Add(),
                                        right=Constant(lineno=31, col_offset=44, end_lineno=31, end_col_offset=45, value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=48,
                            value=Call(
                                lineno=32,
                                col_offset=8,
                                end_lineno=32,
                                end_col_offset=48,
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
                                    Attribute(
                                        lineno=32,
                                        col_offset=25,
                                        end_lineno=32,
                                        end_col_offset=37,
                                        value=Name(lineno=32, col_offset=25, end_lineno=32, end_col_offset=32, id='counter', ctx=Load()),
                                        attr='miss',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        lineno=32,
                                        col_offset=39,
                                        end_lineno=32,
                                        end_col_offset=47,
                                        left=Name(lineno=32, col_offset=39, end_lineno=32, end_col_offset=43, id='miss', ctx=Load()),
                                        op=Add(),
                                        right=Constant(lineno=32, col_offset=46, end_lineno=32, end_col_offset=47, value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=33,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=33,
                            value=Call(
                                lineno=33,
                                col_offset=8,
                                end_lineno=33,
                                end_col_offset=33,
                                func=Attribute(
                                    lineno=33,
                                    col_offset=8,
                                    end_lineno=33,
                                    end_col_offset=21,
                                    value=Name(lineno=33, col_offset=8, end_lineno=33, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=33, col_offset=22, end_lineno=33, end_col_offset=25, id='key', ctx=Load()),
                                    Name(lineno=33, col_offset=27, end_lineno=33, end_col_offset=32, id='cache', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=36,
                            col_offset=8,
                            end_lineno=36,
                            end_col_offset=27,
                            value=Call(
                                lineno=36,
                                col_offset=8,
                                end_lineno=36,
                                end_col_offset=27,
                                func=Attribute(
                                    lineno=36,
                                    col_offset=8,
                                    end_lineno=36,
                                    end_col_offset=20,
                                    value=Attribute(
                                        lineno=36,
                                        col_offset=8,
                                        end_lineno=36,
                                        end_col_offset=16,
                                        value=Name(lineno=36, col_offset=8, end_lineno=36, end_col_offset=12, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=36, col_offset=21, end_lineno=36, end_col_offset=26, id='XMLID', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=37,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=46,
                            value=Call(
                                lineno=37,
                                col_offset=8,
                                end_lineno=37,
                                end_col_offset=46,
                                func=Attribute(
                                    lineno=37,
                                    col_offset=8,
                                    end_lineno=37,
                                    end_col_offset=24,
                                    value=Name(lineno=37, col_offset=8, end_lineno=37, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=37,
                                        col_offset=25,
                                        end_lineno=37,
                                        end_col_offset=36,
                                        value=Name(lineno=37, col_offset=25, end_lineno=37, end_col_offset=32, id='counter', ctx=Load()),
                                        attr='hit',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        lineno=37,
                                        col_offset=38,
                                        end_lineno=37,
                                        end_col_offset=45,
                                        left=Name(lineno=37, col_offset=38, end_lineno=37, end_col_offset=41, id='hit', ctx=Load()),
                                        op=Add(),
                                        right=Constant(lineno=37, col_offset=44, end_lineno=37, end_col_offset=45, value=2, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=38,
                            col_offset=8,
                            end_lineno=38,
                            end_col_offset=48,
                            value=Call(
                                lineno=38,
                                col_offset=8,
                                end_lineno=38,
                                end_col_offset=48,
                                func=Attribute(
                                    lineno=38,
                                    col_offset=8,
                                    end_lineno=38,
                                    end_col_offset=24,
                                    value=Name(lineno=38, col_offset=8, end_lineno=38, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=38,
                                        col_offset=25,
                                        end_lineno=38,
                                        end_col_offset=37,
                                        value=Name(lineno=38, col_offset=25, end_lineno=38, end_col_offset=32, id='counter', ctx=Load()),
                                        attr='miss',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        lineno=38,
                                        col_offset=39,
                                        end_lineno=38,
                                        end_col_offset=47,
                                        left=Name(lineno=38, col_offset=39, end_lineno=38, end_col_offset=43, id='miss', ctx=Load()),
                                        op=Add(),
                                        right=Constant(lineno=38, col_offset=46, end_lineno=38, end_col_offset=47, value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=39,
                            col_offset=8,
                            end_lineno=39,
                            end_col_offset=33,
                            value=Call(
                                lineno=39,
                                col_offset=8,
                                end_lineno=39,
                                end_col_offset=33,
                                func=Attribute(
                                    lineno=39,
                                    col_offset=8,
                                    end_lineno=39,
                                    end_col_offset=21,
                                    value=Name(lineno=39, col_offset=8, end_lineno=39, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=39, col_offset=22, end_lineno=39, end_col_offset=25, id='key', ctx=Load()),
                                    Name(lineno=39, col_offset=27, end_lineno=39, end_col_offset=32, id='cache', ctx=Load()),
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
