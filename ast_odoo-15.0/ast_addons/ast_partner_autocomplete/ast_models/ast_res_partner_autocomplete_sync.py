Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=14,
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
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
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=38,
            end_col_offset=22,
            name='ResPartnerAutocompleteSync',
            bases=[
                Attribute(
                    lineno=9,
                    col_offset=33,
                    end_lineno=9,
                    end_col_offset=45,
                    value=Name(lineno=9, col_offset=33, end_lineno=9, end_col_offset=39, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=43,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=43, value='res.partner.autocomplete.sync', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=46,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=11, col_offset=19, end_lineno=11, end_col_offset=46, value='Partner Autocomplete Sync', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=85,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=14, id='partner_id', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=17,
                        end_lineno=13,
                        end_col_offset=85,
                        func=Attribute(
                            lineno=13,
                            col_offset=17,
                            end_lineno=13,
                            end_col_offset=32,
                            value=Name(lineno=13, col_offset=17, end_lineno=13, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=33, end_lineno=13, end_col_offset=46, value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=48,
                                end_lineno=13,
                                end_col_offset=64,
                                arg='string',
                                value=Constant(lineno=13, col_offset=55, end_lineno=13, end_col_offset=64, value='Partner', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=66,
                                end_lineno=13,
                                end_col_offset=84,
                                arg='ondelete',
                                value=Constant(lineno=13, col_offset=75, end_lineno=13, end_col_offset=84, value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=57,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=11, id='synched', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=14,
                        end_lineno=14,
                        end_col_offset=57,
                        func=Attribute(
                            lineno=14,
                            col_offset=14,
                            end_lineno=14,
                            end_col_offset=28,
                            value=Name(lineno=14, col_offset=14, end_lineno=14, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=14, col_offset=29, end_lineno=14, end_col_offset=41, value='Is synched', kind=None)],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=43,
                                end_lineno=14,
                                end_col_offset=56,
                                arg='default',
                                value=Constant(lineno=14, col_offset=51, end_lineno=14, end_col_offset=56, value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=17,
                    col_offset=4,
                    end_lineno=32,
                    end_col_offset=49,
                    name='start_sync',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=17, col_offset=19, end_lineno=17, end_col_offset=23, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=62,
                            targets=[Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=21, id='to_sync_items', ctx=Store())],
                            value=Call(
                                lineno=18,
                                col_offset=24,
                                end_lineno=18,
                                end_col_offset=62,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=24,
                                    end_lineno=18,
                                    end_col_offset=35,
                                    value=Name(lineno=18, col_offset=24, end_lineno=18, end_col_offset=28, id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=18,
                                        col_offset=36,
                                        end_lineno=18,
                                        end_col_offset=61,
                                        elts=[
                                            Tuple(
                                                lineno=18,
                                                col_offset=37,
                                                end_lineno=18,
                                                end_col_offset=60,
                                                elts=[
                                                    Constant(lineno=18, col_offset=38, end_lineno=18, end_col_offset=47, value='synched', kind=None),
                                                    Constant(lineno=18, col_offset=49, end_lineno=18, end_col_offset=52, value='=', kind=None),
                                                    Constant(lineno=18, col_offset=54, end_lineno=18, end_col_offset=59, value=False, kind=None),
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
                            lineno=19,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=49,
                            target=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=24, id='to_sync_item', ctx=Store()),
                            iter=Name(lineno=19, col_offset=28, end_lineno=19, end_col_offset=41, id='to_sync_items', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=20,
                                    col_offset=12,
                                    end_lineno=20,
                                    end_col_offset=45,
                                    targets=[Name(lineno=20, col_offset=12, end_lineno=20, end_col_offset=19, id='partner', ctx=Store())],
                                    value=Attribute(
                                        lineno=20,
                                        col_offset=22,
                                        end_lineno=20,
                                        end_col_offset=45,
                                        value=Name(lineno=20, col_offset=22, end_lineno=20, end_col_offset=34, id='to_sync_item', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=13,
                                    targets=[Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=18, id='params', ctx=Store())],
                                    value=Dict(
                                        lineno=22,
                                        col_offset=21,
                                        end_lineno=24,
                                        end_col_offset=13,
                                        keys=[Constant(lineno=23, col_offset=16, end_lineno=23, end_col_offset=29, value='partner_gid', kind=None)],
                                        values=[
                                            Attribute(
                                                lineno=23,
                                                col_offset=31,
                                                end_lineno=23,
                                                end_col_offset=50,
                                                value=Name(lineno=23, col_offset=31, end_lineno=23, end_col_offset=38, id='partner', ctx=Load()),
                                                attr='partner_gid',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    lineno=26,
                                    col_offset=12,
                                    end_lineno=30,
                                    end_col_offset=81,
                                    test=BoolOp(
                                        lineno=26,
                                        col_offset=15,
                                        end_lineno=26,
                                        end_col_offset=68,
                                        op=And(),
                                        values=[
                                            Attribute(
                                                lineno=26,
                                                col_offset=15,
                                                end_lineno=26,
                                                end_col_offset=26,
                                                value=Name(lineno=26, col_offset=15, end_lineno=26, end_col_offset=22, id='partner', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                lineno=26,
                                                col_offset=31,
                                                end_lineno=26,
                                                end_col_offset=68,
                                                func=Attribute(
                                                    lineno=26,
                                                    col_offset=31,
                                                    end_lineno=26,
                                                    end_col_offset=55,
                                                    value=Name(lineno=26, col_offset=31, end_lineno=26, end_col_offset=38, id='partner', ctx=Load()),
                                                    attr='_is_vat_syncable',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        lineno=26,
                                                        col_offset=56,
                                                        end_lineno=26,
                                                        end_col_offset=67,
                                                        value=Name(lineno=26, col_offset=56, end_lineno=26, end_col_offset=63, id='partner', ctx=Load()),
                                                        attr='vat',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=27,
                                            col_offset=16,
                                            end_lineno=27,
                                            end_col_offset=43,
                                            targets=[
                                                Subscript(
                                                    lineno=27,
                                                    col_offset=16,
                                                    end_lineno=27,
                                                    end_col_offset=29,
                                                    value=Name(lineno=27, col_offset=16, end_lineno=27, end_col_offset=22, id='params', ctx=Load()),
                                                    slice=Constant(lineno=27, col_offset=23, end_lineno=27, end_col_offset=28, value='vat', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                lineno=27,
                                                col_offset=32,
                                                end_lineno=27,
                                                end_col_offset=43,
                                                value=Name(lineno=27, col_offset=32, end_lineno=27, end_col_offset=39, id='partner', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            lineno=28,
                                            col_offset=16,
                                            end_lineno=28,
                                            end_col_offset=107,
                                            targets=[
                                                Tuple(
                                                    lineno=28,
                                                    col_offset=16,
                                                    end_lineno=28,
                                                    end_col_offset=24,
                                                    elts=[
                                                        Name(lineno=28, col_offset=16, end_lineno=28, end_col_offset=17, id='_', ctx=Store()),
                                                        Name(lineno=28, col_offset=19, end_lineno=28, end_col_offset=24, id='error', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                lineno=28,
                                                col_offset=27,
                                                end_lineno=28,
                                                end_col_offset=107,
                                                func=Attribute(
                                                    lineno=28,
                                                    col_offset=27,
                                                    end_lineno=28,
                                                    end_col_offset=89,
                                                    value=Subscript(
                                                        lineno=28,
                                                        col_offset=27,
                                                        end_lineno=28,
                                                        end_col_offset=59,
                                                        value=Attribute(
                                                            lineno=28,
                                                            col_offset=27,
                                                            end_lineno=28,
                                                            end_col_offset=35,
                                                            value=Name(lineno=28, col_offset=27, end_lineno=28, end_col_offset=31, id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(lineno=28, col_offset=36, end_lineno=28, end_col_offset=58, value='iap.autocomplete.api', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_request_partner_autocomplete',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(lineno=28, col_offset=90, end_lineno=28, end_col_offset=98, value='update', kind=None),
                                                    Name(lineno=28, col_offset=100, end_lineno=28, end_col_offset=106, id='params', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            lineno=29,
                                            col_offset=16,
                                            end_lineno=30,
                                            end_col_offset=81,
                                            test=Name(lineno=29, col_offset=19, end_lineno=29, end_col_offset=24, id='error', ctx=Load()),
                                            body=[
                                                Expr(
                                                    lineno=30,
                                                    col_offset=20,
                                                    end_lineno=30,
                                                    end_col_offset=81,
                                                    value=Call(
                                                        lineno=30,
                                                        col_offset=20,
                                                        end_lineno=30,
                                                        end_col_offset=81,
                                                        func=Attribute(
                                                            lineno=30,
                                                            col_offset=20,
                                                            end_lineno=30,
                                                            end_col_offset=33,
                                                            value=Name(lineno=30, col_offset=20, end_lineno=30, end_col_offset=27, id='_logger', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                lineno=30,
                                                                col_offset=34,
                                                                end_lineno=30,
                                                                end_col_offset=80,
                                                                left=Constant(lineno=30, col_offset=34, end_lineno=30, end_col_offset=67, value='Send Partner to sync failed: %s', kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    lineno=30,
                                                                    col_offset=70,
                                                                    end_lineno=30,
                                                                    end_col_offset=80,
                                                                    func=Name(lineno=30, col_offset=70, end_lineno=30, end_col_offset=73, id='str', ctx=Load()),
                                                                    args=[Name(lineno=30, col_offset=74, end_lineno=30, end_col_offset=79, id='error', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    lineno=32,
                                    col_offset=12,
                                    end_lineno=32,
                                    end_col_offset=49,
                                    value=Call(
                                        lineno=32,
                                        col_offset=12,
                                        end_lineno=32,
                                        end_col_offset=49,
                                        func=Attribute(
                                            lineno=32,
                                            col_offset=12,
                                            end_lineno=32,
                                            end_col_offset=30,
                                            value=Name(lineno=32, col_offset=12, end_lineno=32, end_col_offset=24, id='to_sync_item', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=32,
                                                col_offset=31,
                                                end_lineno=32,
                                                end_col_offset=48,
                                                keys=[Constant(lineno=32, col_offset=32, end_lineno=32, end_col_offset=41, value='synched', kind=None)],
                                                values=[Constant(lineno=32, col_offset=43, end_lineno=32, end_col_offset=47, value=True, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=16,
                            col_offset=5,
                            end_lineno=16,
                            end_col_offset=14,
                            value=Name(lineno=16, col_offset=5, end_lineno=16, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=34,
                    col_offset=4,
                    end_lineno=38,
                    end_col_offset=22,
                    name='add_to_queue',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=34, col_offset=21, end_lineno=34, end_col_offset=25, arg='self', annotation=None, type_comment=None),
                            arg(lineno=34, col_offset=27, end_lineno=34, end_col_offset=37, arg='partner_id', annotation=None, type_comment=None),
                        ],
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
                            end_col_offset=64,
                            targets=[Name(lineno=35, col_offset=8, end_lineno=35, end_col_offset=15, id='to_sync', ctx=Store())],
                            value=Call(
                                lineno=35,
                                col_offset=18,
                                end_lineno=35,
                                end_col_offset=64,
                                func=Attribute(
                                    lineno=35,
                                    col_offset=18,
                                    end_lineno=35,
                                    end_col_offset=29,
                                    value=Name(lineno=35, col_offset=18, end_lineno=35, end_col_offset=22, id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=35,
                                        col_offset=30,
                                        end_lineno=35,
                                        end_col_offset=63,
                                        elts=[
                                            Tuple(
                                                lineno=35,
                                                col_offset=31,
                                                end_lineno=35,
                                                end_col_offset=62,
                                                elts=[
                                                    Constant(lineno=35, col_offset=32, end_lineno=35, end_col_offset=44, value='partner_id', kind=None),
                                                    Constant(lineno=35, col_offset=46, end_lineno=35, end_col_offset=49, value='=', kind=None),
                                                    Name(lineno=35, col_offset=51, end_lineno=35, end_col_offset=61, id='partner_id', ctx=Load()),
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
                            lineno=36,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=61,
                            test=UnaryOp(
                                lineno=36,
                                col_offset=11,
                                end_lineno=36,
                                end_col_offset=22,
                                op=Not(),
                                operand=Name(lineno=36, col_offset=15, end_lineno=36, end_col_offset=22, id='to_sync', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    lineno=37,
                                    col_offset=12,
                                    end_lineno=37,
                                    end_col_offset=61,
                                    targets=[Name(lineno=37, col_offset=12, end_lineno=37, end_col_offset=19, id='to_sync', ctx=Store())],
                                    value=Call(
                                        lineno=37,
                                        col_offset=22,
                                        end_lineno=37,
                                        end_col_offset=61,
                                        func=Attribute(
                                            lineno=37,
                                            col_offset=22,
                                            end_lineno=37,
                                            end_col_offset=33,
                                            value=Name(lineno=37, col_offset=22, end_lineno=37, end_col_offset=26, id='self', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=37,
                                                col_offset=34,
                                                end_lineno=37,
                                                end_col_offset=60,
                                                keys=[Constant(lineno=37, col_offset=35, end_lineno=37, end_col_offset=47, value='partner_id', kind=None)],
                                                values=[Name(lineno=37, col_offset=49, end_lineno=37, end_col_offset=59, id='partner_id', ctx=Load())],
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
                            lineno=38,
                            col_offset=8,
                            end_lineno=38,
                            end_col_offset=22,
                            value=Name(lineno=38, col_offset=15, end_lineno=38, end_col_offset=22, id='to_sync', ctx=Load()),
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
