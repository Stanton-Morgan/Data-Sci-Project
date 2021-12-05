Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=46,
            module='cups',
            names=[alias(name='Connection', asname='cups_connection')],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=18,
            module='re',
            names=[alias(name='sub', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=26,
            module='threading',
            names=[alias(name='Lock', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=54,
            module='odoo.addons.hw_drivers.interface',
            names=[alias(name='Interface', asname=None)],
            level=0,
        ),
        Assign(
            lineno=10,
            col_offset=0,
            end_lineno=10,
            end_col_offset=24,
            targets=[Name(lineno=10, col_offset=0, end_lineno=10, end_col_offset=4, id='conn', ctx=Store())],
            value=Call(
                lineno=10,
                col_offset=7,
                end_lineno=10,
                end_col_offset=24,
                func=Name(lineno=10, col_offset=7, end_lineno=10, end_col_offset=22, id='cups_connection', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            lineno=11,
            col_offset=0,
            end_lineno=11,
            end_col_offset=21,
            targets=[Name(lineno=11, col_offset=0, end_lineno=11, end_col_offset=4, id='PPDs', ctx=Store())],
            value=Call(
                lineno=11,
                col_offset=7,
                end_lineno=11,
                end_col_offset=21,
                func=Attribute(
                    lineno=11,
                    col_offset=7,
                    end_lineno=11,
                    end_col_offset=19,
                    value=Name(lineno=11, col_offset=7, end_lineno=11, end_col_offset=11, id='conn', ctx=Load()),
                    attr='getPPDs',
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            lineno=12,
            col_offset=0,
            end_lineno=12,
            end_col_offset=18,
            targets=[Name(lineno=12, col_offset=0, end_lineno=12, end_col_offset=9, id='cups_lock', ctx=Store())],
            value=Call(
                lineno=12,
                col_offset=12,
                end_lineno=12,
                end_col_offset=18,
                func=Name(lineno=12, col_offset=12, end_lineno=12, end_col_offset=16, id='Lock', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            lineno=14,
            col_offset=0,
            end_lineno=37,
            end_col_offset=30,
            name='PrinterInterface',
            bases=[Name(lineno=14, col_offset=23, end_lineno=14, end_col_offset=32, id='Interface', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=21,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=15, id='_loop_delay', ctx=Store())],
                    value=Constant(lineno=15, col_offset=18, end_lineno=15, end_col_offset=21, value=120, kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=31,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=19, id='connection_type', ctx=Store())],
                    value=Constant(lineno=16, col_offset=22, end_lineno=16, end_col_offset=31, value='printer', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=18,
                    col_offset=4,
                    end_lineno=37,
                    end_col_offset=30,
                    name='get_devices',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=18, col_offset=20, end_lineno=18, end_col_offset=24, arg='self', annotation=None, type_comment=None)],
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
                            end_col_offset=28,
                            targets=[Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=23, id='printer_devices', ctx=Store())],
                            value=Dict(lineno=19, col_offset=26, end_lineno=19, end_col_offset=28, keys=[], values=[]),
                            type_comment=None,
                        ),
                        With(
                            lineno=20,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=65,
                            items=[
                                withitem(
                                    context_expr=Name(lineno=20, col_offset=13, end_lineno=20, end_col_offset=22, id='cups_lock', ctx=Load()),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    lineno=21,
                                    col_offset=12,
                                    end_lineno=21,
                                    end_col_offset=41,
                                    targets=[Name(lineno=21, col_offset=12, end_lineno=21, end_col_offset=20, id='printers', ctx=Store())],
                                    value=Call(
                                        lineno=21,
                                        col_offset=23,
                                        end_lineno=21,
                                        end_col_offset=41,
                                        func=Attribute(
                                            lineno=21,
                                            col_offset=23,
                                            end_lineno=21,
                                            end_col_offset=39,
                                            value=Name(lineno=21, col_offset=23, end_lineno=21, end_col_offset=27, id='conn', ctx=Load()),
                                            attr='getPrinters',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=39,
                                    targets=[Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=19, id='devices', ctx=Store())],
                                    value=Call(
                                        lineno=22,
                                        col_offset=22,
                                        end_lineno=22,
                                        end_col_offset=39,
                                        func=Attribute(
                                            lineno=22,
                                            col_offset=22,
                                            end_lineno=22,
                                            end_col_offset=37,
                                            value=Name(lineno=22, col_offset=22, end_lineno=22, end_col_offset=26, id='conn', ctx=Load()),
                                            attr='getDevices',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    lineno=23,
                                    col_offset=12,
                                    end_lineno=26,
                                    end_col_offset=65,
                                    target=Name(lineno=23, col_offset=16, end_lineno=23, end_col_offset=23, id='printer', ctx=Store()),
                                    iter=Name(lineno=23, col_offset=27, end_lineno=23, end_col_offset=35, id='printers', ctx=Load()),
                                    body=[
                                        Assign(
                                            lineno=24,
                                            col_offset=16,
                                            end_lineno=24,
                                            end_col_offset=69,
                                            targets=[Name(lineno=24, col_offset=16, end_lineno=24, end_col_offset=20, id='path', ctx=Store())],
                                            value=Call(
                                                lineno=24,
                                                col_offset=23,
                                                end_lineno=24,
                                                end_col_offset=69,
                                                func=Attribute(
                                                    lineno=24,
                                                    col_offset=23,
                                                    end_lineno=24,
                                                    end_col_offset=48,
                                                    value=Call(
                                                        lineno=24,
                                                        col_offset=23,
                                                        end_lineno=24,
                                                        end_col_offset=44,
                                                        func=Attribute(
                                                            lineno=24,
                                                            col_offset=23,
                                                            end_lineno=24,
                                                            end_col_offset=35,
                                                            value=Name(lineno=24, col_offset=23, end_lineno=24, end_col_offset=31, id='printers', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(lineno=24, col_offset=36, end_lineno=24, end_col_offset=43, id='printer', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(lineno=24, col_offset=49, end_lineno=24, end_col_offset=61, value='device-uri', kind=None),
                                                    Constant(lineno=24, col_offset=63, end_lineno=24, end_col_offset=68, value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            lineno=25,
                                            col_offset=16,
                                            end_lineno=26,
                                            end_col_offset=65,
                                            test=BoolOp(
                                                lineno=25,
                                                col_offset=19,
                                                end_lineno=25,
                                                end_col_offset=43,
                                                op=And(),
                                                values=[
                                                    Name(lineno=25, col_offset=19, end_lineno=25, end_col_offset=23, id='path', ctx=Load()),
                                                    Compare(
                                                        lineno=25,
                                                        col_offset=28,
                                                        end_lineno=25,
                                                        end_col_offset=43,
                                                        left=Name(lineno=25, col_offset=28, end_lineno=25, end_col_offset=32, id='path', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(lineno=25, col_offset=36, end_lineno=25, end_col_offset=43, id='devices', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    lineno=26,
                                                    col_offset=20,
                                                    end_lineno=26,
                                                    end_col_offset=65,
                                                    value=Call(
                                                        lineno=26,
                                                        col_offset=20,
                                                        end_lineno=26,
                                                        end_col_offset=65,
                                                        func=Attribute(
                                                            lineno=26,
                                                            col_offset=20,
                                                            end_lineno=26,
                                                            end_col_offset=44,
                                                            value=Call(
                                                                lineno=26,
                                                                col_offset=20,
                                                                end_lineno=26,
                                                                end_col_offset=37,
                                                                func=Attribute(
                                                                    lineno=26,
                                                                    col_offset=20,
                                                                    end_lineno=26,
                                                                    end_col_offset=31,
                                                                    value=Name(lineno=26, col_offset=20, end_lineno=26, end_col_offset=27, id='devices', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(lineno=26, col_offset=32, end_lineno=26, end_col_offset=36, id='path', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                lineno=26,
                                                                col_offset=45,
                                                                end_lineno=26,
                                                                end_col_offset=64,
                                                                keys=[Constant(lineno=26, col_offset=46, end_lineno=26, end_col_offset=57, value='supported', kind=None)],
                                                                values=[Constant(lineno=26, col_offset=59, end_lineno=26, end_col_offset=63, value=True, kind=None)],
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
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        For(
                            lineno=27,
                            col_offset=8,
                            end_lineno=36,
                            end_col_offset=55,
                            target=Name(lineno=27, col_offset=12, end_lineno=27, end_col_offset=16, id='path', ctx=Store()),
                            iter=Name(lineno=27, col_offset=20, end_lineno=27, end_col_offset=27, id='devices', ctx=Load()),
                            body=[
                                If(
                                    lineno=28,
                                    col_offset=12,
                                    end_lineno=33,
                                    end_col_offset=59,
                                    test=Compare(
                                        lineno=28,
                                        col_offset=15,
                                        end_lineno=28,
                                        end_col_offset=30,
                                        left=Constant(lineno=28, col_offset=15, end_lineno=28, end_col_offset=22, value='uuid=', kind=None),
                                        ops=[In()],
                                        comparators=[Name(lineno=28, col_offset=26, end_lineno=28, end_col_offset=30, id='path', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=29,
                                            col_offset=16,
                                            end_lineno=29,
                                            end_col_offset=77,
                                            targets=[Name(lineno=29, col_offset=16, end_lineno=29, end_col_offset=26, id='identifier', ctx=Store())],
                                            value=Call(
                                                lineno=29,
                                                col_offset=29,
                                                end_lineno=29,
                                                end_col_offset=77,
                                                func=Name(lineno=29, col_offset=29, end_lineno=29, end_col_offset=32, id='sub', ctx=Load()),
                                                args=[
                                                    Constant(lineno=29, col_offset=33, end_lineno=29, end_col_offset=48, value='[^a-zA-Z0-9_]', kind=None),
                                                    Constant(lineno=29, col_offset=50, end_lineno=29, end_col_offset=52, value='', kind=None),
                                                    Subscript(
                                                        lineno=29,
                                                        col_offset=54,
                                                        end_lineno=29,
                                                        end_col_offset=76,
                                                        value=Call(
                                                            lineno=29,
                                                            col_offset=54,
                                                            end_lineno=29,
                                                            end_col_offset=73,
                                                            func=Attribute(
                                                                lineno=29,
                                                                col_offset=54,
                                                                end_lineno=29,
                                                                end_col_offset=64,
                                                                value=Name(lineno=29, col_offset=54, end_lineno=29, end_col_offset=58, id='path', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(lineno=29, col_offset=65, end_lineno=29, end_col_offset=72, value='uuid=', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(lineno=29, col_offset=74, end_lineno=29, end_col_offset=75, value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            lineno=30,
                                            col_offset=12,
                                            end_lineno=33,
                                            end_col_offset=59,
                                            test=Compare(
                                                lineno=30,
                                                col_offset=17,
                                                end_lineno=30,
                                                end_col_offset=34,
                                                left=Constant(lineno=30, col_offset=17, end_lineno=30, end_col_offset=26, value='serial=', kind=None),
                                                ops=[In()],
                                                comparators=[Name(lineno=30, col_offset=30, end_lineno=30, end_col_offset=34, id='path', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    lineno=31,
                                                    col_offset=16,
                                                    end_lineno=31,
                                                    end_col_offset=79,
                                                    targets=[Name(lineno=31, col_offset=16, end_lineno=31, end_col_offset=26, id='identifier', ctx=Store())],
                                                    value=Call(
                                                        lineno=31,
                                                        col_offset=29,
                                                        end_lineno=31,
                                                        end_col_offset=79,
                                                        func=Name(lineno=31, col_offset=29, end_lineno=31, end_col_offset=32, id='sub', ctx=Load()),
                                                        args=[
                                                            Constant(lineno=31, col_offset=33, end_lineno=31, end_col_offset=48, value='[^a-zA-Z0-9_]', kind=None),
                                                            Constant(lineno=31, col_offset=50, end_lineno=31, end_col_offset=52, value='', kind=None),
                                                            Subscript(
                                                                lineno=31,
                                                                col_offset=54,
                                                                end_lineno=31,
                                                                end_col_offset=78,
                                                                value=Call(
                                                                    lineno=31,
                                                                    col_offset=54,
                                                                    end_lineno=31,
                                                                    end_col_offset=75,
                                                                    func=Attribute(
                                                                        lineno=31,
                                                                        col_offset=54,
                                                                        end_lineno=31,
                                                                        end_col_offset=64,
                                                                        value=Name(lineno=31, col_offset=54, end_lineno=31, end_col_offset=58, id='path', ctx=Load()),
                                                                        attr='split',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(lineno=31, col_offset=65, end_lineno=31, end_col_offset=74, value='serial=', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                slice=Constant(lineno=31, col_offset=76, end_lineno=31, end_col_offset=77, value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    lineno=33,
                                                    col_offset=16,
                                                    end_lineno=33,
                                                    end_col_offset=59,
                                                    targets=[Name(lineno=33, col_offset=16, end_lineno=33, end_col_offset=26, id='identifier', ctx=Store())],
                                                    value=Call(
                                                        lineno=33,
                                                        col_offset=29,
                                                        end_lineno=33,
                                                        end_col_offset=59,
                                                        func=Name(lineno=33, col_offset=29, end_lineno=33, end_col_offset=32, id='sub', ctx=Load()),
                                                        args=[
                                                            Constant(lineno=33, col_offset=33, end_lineno=33, end_col_offset=48, value='[^a-zA-Z0-9_]', kind=None),
                                                            Constant(lineno=33, col_offset=50, end_lineno=33, end_col_offset=52, value='', kind=None),
                                                            Name(lineno=33, col_offset=54, end_lineno=33, end_col_offset=58, id='path', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    lineno=34,
                                    col_offset=12,
                                    end_lineno=34,
                                    end_col_offset=52,
                                    targets=[
                                        Subscript(
                                            lineno=34,
                                            col_offset=12,
                                            end_lineno=34,
                                            end_col_offset=39,
                                            value=Subscript(
                                                lineno=34,
                                                col_offset=12,
                                                end_lineno=34,
                                                end_col_offset=25,
                                                value=Name(lineno=34, col_offset=12, end_lineno=34, end_col_offset=19, id='devices', ctx=Load()),
                                                slice=Name(lineno=34, col_offset=20, end_lineno=34, end_col_offset=24, id='path', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(lineno=34, col_offset=26, end_lineno=34, end_col_offset=38, value='identifier', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(lineno=34, col_offset=42, end_lineno=34, end_col_offset=52, id='identifier', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=35,
                                    col_offset=12,
                                    end_lineno=35,
                                    end_col_offset=39,
                                    targets=[
                                        Subscript(
                                            lineno=35,
                                            col_offset=12,
                                            end_lineno=35,
                                            end_col_offset=32,
                                            value=Subscript(
                                                lineno=35,
                                                col_offset=12,
                                                end_lineno=35,
                                                end_col_offset=25,
                                                value=Name(lineno=35, col_offset=12, end_lineno=35, end_col_offset=19, id='devices', ctx=Load()),
                                                slice=Name(lineno=35, col_offset=20, end_lineno=35, end_col_offset=24, id='path', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(lineno=35, col_offset=26, end_lineno=35, end_col_offset=31, value='url', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(lineno=35, col_offset=35, end_lineno=35, end_col_offset=39, id='path', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=36,
                                    col_offset=12,
                                    end_lineno=36,
                                    end_col_offset=55,
                                    targets=[
                                        Subscript(
                                            lineno=36,
                                            col_offset=12,
                                            end_lineno=36,
                                            end_col_offset=39,
                                            value=Name(lineno=36, col_offset=12, end_lineno=36, end_col_offset=27, id='printer_devices', ctx=Load()),
                                            slice=Name(lineno=36, col_offset=28, end_lineno=36, end_col_offset=38, id='identifier', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        lineno=36,
                                        col_offset=42,
                                        end_lineno=36,
                                        end_col_offset=55,
                                        value=Name(lineno=36, col_offset=42, end_lineno=36, end_col_offset=49, id='devices', ctx=Load()),
                                        slice=Name(lineno=36, col_offset=50, end_lineno=36, end_col_offset=54, id='path', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=37,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=30,
                            value=Name(lineno=37, col_offset=15, end_lineno=37, end_col_offset=30, id='printer_devices', ctx=Load()),
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