Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=44,
            end_col_offset=53,
            name='ResPartnerMondialRelay',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=29,
                    end_lineno=7,
                    end_col_offset=41,
                    value=Name(lineno=7, col_offset=29, end_lineno=7, end_col_offset=35, id='models', ctx=Load()),
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
                    end_col_offset=28,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=28, value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=72,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=19, id='is_mondialrelay', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=22,
                        end_lineno=10,
                        end_col_offset=72,
                        func=Attribute(
                            lineno=10,
                            col_offset=22,
                            end_lineno=10,
                            end_col_offset=36,
                            value=Name(lineno=10, col_offset=22, end_lineno=10, end_col_offset=28, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=37,
                                end_lineno=10,
                                end_col_offset=71,
                                arg='compute',
                                value=Constant(lineno=10, col_offset=45, end_lineno=10, end_col_offset=71, value='_compute_is_mondialrelay', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=65,
                    name='_compute_is_mondialrelay',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=33, end_lineno=13, end_col_offset=37, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            lineno=14,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=65,
                            target=Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=13, id='p', ctx=Store()),
                            iter=Name(lineno=14, col_offset=17, end_lineno=14, end_col_offset=21, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=15,
                                    col_offset=12,
                                    end_lineno=15,
                                    end_col_offset=65,
                                    targets=[
                                        Attribute(
                                            lineno=15,
                                            col_offset=12,
                                            end_lineno=15,
                                            end_col_offset=29,
                                            value=Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=13, id='p', ctx=Load()),
                                            attr='is_mondialrelay',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        lineno=15,
                                        col_offset=32,
                                        end_lineno=15,
                                        end_col_offset=65,
                                        op=And(),
                                        values=[
                                            Attribute(
                                                lineno=15,
                                                col_offset=32,
                                                end_lineno=15,
                                                end_col_offset=37,
                                                value=Name(lineno=15, col_offset=32, end_lineno=15, end_col_offset=33, id='p', ctx=Load()),
                                                attr='ref',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                lineno=15,
                                                col_offset=42,
                                                end_lineno=15,
                                                end_col_offset=65,
                                                func=Attribute(
                                                    lineno=15,
                                                    col_offset=42,
                                                    end_lineno=15,
                                                    end_col_offset=58,
                                                    value=Attribute(
                                                        lineno=15,
                                                        col_offset=42,
                                                        end_lineno=15,
                                                        end_col_offset=47,
                                                        value=Name(lineno=15, col_offset=42, end_lineno=15, end_col_offset=43, id='p', ctx=Load()),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(lineno=15, col_offset=59, end_lineno=15, end_col_offset=64, value='MR#', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
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
                            lineno=12,
                            col_offset=5,
                            end_lineno=12,
                            end_col_offset=23,
                            func=Attribute(
                                lineno=12,
                                col_offset=5,
                                end_lineno=12,
                                end_col_offset=16,
                                value=Name(lineno=12, col_offset=5, end_lineno=12, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=12, col_offset=17, end_lineno=12, end_col_offset=22, value='ref', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=18,
                    col_offset=4,
                    end_lineno=39,
                    end_col_offset=22,
                    name='_mondialrelay_search_or_create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=18, col_offset=39, end_lineno=18, end_col_offset=43, arg='self', annotation=None, type_comment=None),
                            arg(lineno=18, col_offset=45, end_lineno=18, end_col_offset=49, arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=34,
                            targets=[Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=11, id='ref', ctx=Store())],
                            value=BinOp(
                                lineno=19,
                                col_offset=14,
                                end_lineno=19,
                                end_col_offset=34,
                                left=Constant(lineno=19, col_offset=14, end_lineno=19, end_col_offset=21, value='MR#%s', kind=None),
                                op=Mod(),
                                right=Subscript(
                                    lineno=19,
                                    col_offset=24,
                                    end_lineno=19,
                                    end_col_offset=34,
                                    value=Name(lineno=19, col_offset=24, end_lineno=19, end_col_offset=28, id='data', ctx=Load()),
                                    slice=Constant(lineno=19, col_offset=29, end_lineno=19, end_col_offset=33, value='id', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=10,
                            targets=[Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=15, id='partner', ctx=Store())],
                            value=Call(
                                lineno=20,
                                col_offset=18,
                                end_lineno=26,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=18,
                                    end_lineno=20,
                                    end_col_offset=29,
                                    value=Name(lineno=20, col_offset=18, end_lineno=20, end_col_offset=22, id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=20,
                                        col_offset=30,
                                        end_lineno=26,
                                        end_col_offset=9,
                                        elts=[
                                            Tuple(
                                                lineno=21,
                                                col_offset=12,
                                                end_lineno=21,
                                                end_col_offset=62,
                                                elts=[
                                                    Constant(lineno=21, col_offset=13, end_lineno=21, end_col_offset=17, value='id', kind=None),
                                                    Constant(lineno=21, col_offset=19, end_lineno=21, end_col_offset=29, value='child_of', kind=None),
                                                    Attribute(
                                                        lineno=21,
                                                        col_offset=31,
                                                        end_lineno=21,
                                                        end_col_offset=61,
                                                        value=Attribute(
                                                            lineno=21,
                                                            col_offset=31,
                                                            end_lineno=21,
                                                            end_col_offset=57,
                                                            value=Name(lineno=21, col_offset=31, end_lineno=21, end_col_offset=35, id='self', ctx=Load()),
                                                            attr='commercial_partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=22,
                                                col_offset=12,
                                                end_lineno=22,
                                                end_col_offset=29,
                                                elts=[
                                                    Constant(lineno=22, col_offset=13, end_lineno=22, end_col_offset=18, value='ref', kind=None),
                                                    Constant(lineno=22, col_offset=20, end_lineno=22, end_col_offset=23, value='=', kind=None),
                                                    Name(lineno=22, col_offset=25, end_lineno=22, end_col_offset=28, id='ref', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=24,
                                                col_offset=12,
                                                end_lineno=24,
                                                end_col_offset=43,
                                                elts=[
                                                    Constant(lineno=24, col_offset=13, end_lineno=24, end_col_offset=21, value='street', kind=None),
                                                    Constant(lineno=24, col_offset=23, end_lineno=24, end_col_offset=26, value='=', kind=None),
                                                    Subscript(
                                                        lineno=24,
                                                        col_offset=28,
                                                        end_lineno=24,
                                                        end_col_offset=42,
                                                        value=Name(lineno=24, col_offset=28, end_lineno=24, end_col_offset=32, id='data', ctx=Load()),
                                                        slice=Constant(lineno=24, col_offset=33, end_lineno=24, end_col_offset=41, value='street', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=25,
                                                col_offset=12,
                                                end_lineno=25,
                                                end_col_offset=37,
                                                elts=[
                                                    Constant(lineno=25, col_offset=13, end_lineno=25, end_col_offset=18, value='zip', kind=None),
                                                    Constant(lineno=25, col_offset=20, end_lineno=25, end_col_offset=23, value='=', kind=None),
                                                    Subscript(
                                                        lineno=25,
                                                        col_offset=25,
                                                        end_lineno=25,
                                                        end_col_offset=36,
                                                        value=Name(lineno=25, col_offset=25, end_lineno=25, end_col_offset=29, id='data', ctx=Load()),
                                                        slice=Constant(lineno=25, col_offset=30, end_lineno=25, end_col_offset=35, value='zip', kind=None),
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
                        If(
                            lineno=27,
                            col_offset=8,
                            end_lineno=38,
                            end_col_offset=14,
                            test=UnaryOp(
                                lineno=27,
                                col_offset=11,
                                end_lineno=27,
                                end_col_offset=22,
                                op=Not(),
                                operand=Name(lineno=27, col_offset=15, end_lineno=27, end_col_offset=22, id='partner', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    lineno=28,
                                    col_offset=12,
                                    end_lineno=38,
                                    end_col_offset=14,
                                    targets=[Name(lineno=28, col_offset=12, end_lineno=28, end_col_offset=19, id='partner', ctx=Store())],
                                    value=Call(
                                        lineno=28,
                                        col_offset=22,
                                        end_lineno=38,
                                        end_col_offset=14,
                                        func=Attribute(
                                            lineno=28,
                                            col_offset=22,
                                            end_lineno=28,
                                            end_col_offset=33,
                                            value=Name(lineno=28, col_offset=22, end_lineno=28, end_col_offset=26, id='self', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=28,
                                                col_offset=34,
                                                end_lineno=38,
                                                end_col_offset=13,
                                                keys=[
                                                    Constant(lineno=29, col_offset=16, end_lineno=29, end_col_offset=21, value='ref', kind=None),
                                                    Constant(lineno=30, col_offset=16, end_lineno=30, end_col_offset=22, value='name', kind=None),
                                                    Constant(lineno=31, col_offset=16, end_lineno=31, end_col_offset=24, value='street', kind=None),
                                                    Constant(lineno=32, col_offset=16, end_lineno=32, end_col_offset=25, value='street2', kind=None),
                                                    Constant(lineno=33, col_offset=16, end_lineno=33, end_col_offset=21, value='zip', kind=None),
                                                    Constant(lineno=34, col_offset=16, end_lineno=34, end_col_offset=22, value='city', kind=None),
                                                    Constant(lineno=35, col_offset=16, end_lineno=35, end_col_offset=28, value='country_id', kind=None),
                                                    Constant(lineno=36, col_offset=16, end_lineno=36, end_col_offset=22, value='type', kind=None),
                                                    Constant(lineno=37, col_offset=16, end_lineno=37, end_col_offset=27, value='parent_id', kind=None),
                                                ],
                                                values=[
                                                    Name(lineno=29, col_offset=23, end_lineno=29, end_col_offset=26, id='ref', ctx=Load()),
                                                    Subscript(
                                                        lineno=30,
                                                        col_offset=24,
                                                        end_lineno=30,
                                                        end_col_offset=36,
                                                        value=Name(lineno=30, col_offset=24, end_lineno=30, end_col_offset=28, id='data', ctx=Load()),
                                                        slice=Constant(lineno=30, col_offset=29, end_lineno=30, end_col_offset=35, value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        lineno=31,
                                                        col_offset=26,
                                                        end_lineno=31,
                                                        end_col_offset=40,
                                                        value=Name(lineno=31, col_offset=26, end_lineno=31, end_col_offset=30, id='data', ctx=Load()),
                                                        slice=Constant(lineno=31, col_offset=31, end_lineno=31, end_col_offset=39, value='street', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        lineno=32,
                                                        col_offset=27,
                                                        end_lineno=32,
                                                        end_col_offset=42,
                                                        value=Name(lineno=32, col_offset=27, end_lineno=32, end_col_offset=31, id='data', ctx=Load()),
                                                        slice=Constant(lineno=32, col_offset=32, end_lineno=32, end_col_offset=41, value='street2', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        lineno=33,
                                                        col_offset=23,
                                                        end_lineno=33,
                                                        end_col_offset=34,
                                                        value=Name(lineno=33, col_offset=23, end_lineno=33, end_col_offset=27, id='data', ctx=Load()),
                                                        slice=Constant(lineno=33, col_offset=28, end_lineno=33, end_col_offset=33, value='zip', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        lineno=34,
                                                        col_offset=24,
                                                        end_lineno=34,
                                                        end_col_offset=36,
                                                        value=Name(lineno=34, col_offset=24, end_lineno=34, end_col_offset=28, id='data', ctx=Load()),
                                                        slice=Constant(lineno=34, col_offset=29, end_lineno=34, end_col_offset=35, value='city', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        lineno=35,
                                                        col_offset=30,
                                                        end_lineno=35,
                                                        end_col_offset=79,
                                                        value=Call(
                                                            lineno=35,
                                                            col_offset=30,
                                                            end_lineno=35,
                                                            end_col_offset=76,
                                                            func=Attribute(
                                                                lineno=35,
                                                                col_offset=30,
                                                                end_lineno=35,
                                                                end_col_offset=42,
                                                                value=Attribute(
                                                                    lineno=35,
                                                                    col_offset=30,
                                                                    end_lineno=35,
                                                                    end_col_offset=38,
                                                                    value=Name(lineno=35, col_offset=30, end_lineno=35, end_col_offset=34, id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                BinOp(
                                                                    lineno=35,
                                                                    col_offset=43,
                                                                    end_lineno=35,
                                                                    end_col_offset=75,
                                                                    left=Constant(lineno=35, col_offset=43, end_lineno=35, end_col_offset=52, value='base.%s', kind=None),
                                                                    op=Mod(),
                                                                    right=Subscript(
                                                                        lineno=35,
                                                                        col_offset=55,
                                                                        end_lineno=35,
                                                                        end_col_offset=75,
                                                                        value=Name(lineno=35, col_offset=55, end_lineno=35, end_col_offset=59, id='data', ctx=Load()),
                                                                        slice=Constant(lineno=35, col_offset=60, end_lineno=35, end_col_offset=74, value='country_code', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=36, col_offset=24, end_lineno=36, end_col_offset=34, value='delivery', kind=None),
                                                    Attribute(
                                                        lineno=37,
                                                        col_offset=29,
                                                        end_lineno=37,
                                                        end_col_offset=36,
                                                        value=Name(lineno=37, col_offset=29, end_lineno=37, end_col_offset=33, id='self', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=39,
                            col_offset=8,
                            end_lineno=39,
                            end_col_offset=22,
                            value=Name(lineno=39, col_offset=15, end_lineno=39, end_col_offset=22, id='partner', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=17,
                            col_offset=5,
                            end_lineno=17,
                            end_col_offset=14,
                            value=Name(lineno=17, col_offset=5, end_lineno=17, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=41,
                    col_offset=4,
                    end_lineno=44,
                    end_col_offset=53,
                    name='_avatar_get_placeholder_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=41, col_offset=37, end_lineno=41, end_col_offset=41, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            lineno=42,
                            col_offset=8,
                            end_lineno=43,
                            end_col_offset=70,
                            test=Attribute(
                                lineno=42,
                                col_offset=11,
                                end_lineno=42,
                                end_col_offset=31,
                                value=Name(lineno=42, col_offset=11, end_lineno=42, end_col_offset=15, id='self', ctx=Load()),
                                attr='is_mondialrelay',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    lineno=43,
                                    col_offset=12,
                                    end_lineno=43,
                                    end_col_offset=70,
                                    value=Constant(lineno=43, col_offset=19, end_lineno=43, end_col_offset=70, value='delivery_mondialrelay/static/src/img/truck_mr.png', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=44,
                            col_offset=8,
                            end_lineno=44,
                            end_col_offset=53,
                            value=Call(
                                lineno=44,
                                col_offset=15,
                                end_lineno=44,
                                end_col_offset=53,
                                func=Attribute(
                                    lineno=44,
                                    col_offset=15,
                                    end_lineno=44,
                                    end_col_offset=51,
                                    value=Call(
                                        lineno=44,
                                        col_offset=15,
                                        end_lineno=44,
                                        end_col_offset=22,
                                        func=Name(lineno=44, col_offset=15, end_lineno=44, end_col_offset=20, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_avatar_get_placeholder_path',
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