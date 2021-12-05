Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=20,
            module='usb',
            names=[alias(name='core', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=54,
            module='odoo.addons.hw_drivers.interface',
            names=[alias(name='Interface', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=29,
            end_col_offset=26,
            name='USBInterface',
            bases=[Name(lineno=9, col_offset=19, end_lineno=9, end_col_offset=28, id='Interface', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=27,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=19, id='connection_type', ctx=Store())],
                    value=Constant(lineno=10, col_offset=22, end_lineno=10, end_col_offset=27, value='usb', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=29,
                    end_col_offset=26,
                    name='get_devices',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=12, col_offset=20, end_lineno=12, end_col_offset=24, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=13,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=11,
                            value=Constant(lineno=13, col_offset=8, end_lineno=19, end_col_offset=11, value="\n        USB devices are identified by a combination of their `idVendor` and\n        `idProduct`. We can't be sure this combination in unique per equipment.\n        To still allow connecting multiple similar equipments, we complete the\n        identifier by a counter. The drawbacks are we can't be sure the equipments\n        will get the same identifiers after a reboot or a disconnect/reconnect.\n        ", kind=None),
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=24,
                            targets=[Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=19, id='usb_devices', ctx=Store())],
                            value=Dict(lineno=20, col_offset=22, end_lineno=20, end_col_offset=24, keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=39,
                            targets=[Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=12, id='devs', ctx=Store())],
                            value=Call(
                                lineno=21,
                                col_offset=15,
                                end_lineno=21,
                                end_col_offset=39,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=15,
                                    end_lineno=21,
                                    end_col_offset=24,
                                    value=Name(lineno=21, col_offset=15, end_lineno=21, end_col_offset=19, id='core', ctx=Load()),
                                    attr='find',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=21,
                                        col_offset=25,
                                        end_lineno=21,
                                        end_col_offset=38,
                                        arg='find_all',
                                        value=Constant(lineno=21, col_offset=34, end_lineno=21, end_col_offset=38, value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=15,
                            targets=[Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=11, id='cpt', ctx=Store())],
                            value=Constant(lineno=22, col_offset=14, end_lineno=22, end_col_offset=15, value=2, kind=None),
                            type_comment=None,
                        ),
                        For(
                            lineno=23,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=41,
                            target=Name(lineno=23, col_offset=12, end_lineno=23, end_col_offset=15, id='dev', ctx=Store()),
                            iter=Name(lineno=23, col_offset=19, end_lineno=23, end_col_offset=23, id='devs', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=24,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=72,
                                    targets=[Name(lineno=24, col_offset=12, end_lineno=24, end_col_offset=22, id='identifier', ctx=Store())],
                                    value=BinOp(
                                        lineno=24,
                                        col_offset=25,
                                        end_lineno=24,
                                        end_col_offset=72,
                                        left=Constant(lineno=24, col_offset=25, end_lineno=24, end_col_offset=40, value='usb_%04x:%04x', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            lineno=24,
                                            col_offset=43,
                                            end_lineno=24,
                                            end_col_offset=72,
                                            elts=[
                                                Attribute(
                                                    lineno=24,
                                                    col_offset=44,
                                                    end_lineno=24,
                                                    end_col_offset=56,
                                                    value=Name(lineno=24, col_offset=44, end_lineno=24, end_col_offset=47, id='dev', ctx=Load()),
                                                    attr='idVendor',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    lineno=24,
                                                    col_offset=58,
                                                    end_lineno=24,
                                                    end_col_offset=71,
                                                    value=Name(lineno=24, col_offset=58, end_lineno=24, end_col_offset=61, id='dev', ctx=Load()),
                                                    attr='idProduct',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    lineno=25,
                                    col_offset=12,
                                    end_lineno=27,
                                    end_col_offset=24,
                                    test=Compare(
                                        lineno=25,
                                        col_offset=15,
                                        end_lineno=25,
                                        end_col_offset=40,
                                        left=Name(lineno=25, col_offset=15, end_lineno=25, end_col_offset=25, id='identifier', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(lineno=25, col_offset=29, end_lineno=25, end_col_offset=40, id='usb_devices', ctx=Load())],
                                    ),
                                    body=[
                                        AugAssign(
                                            lineno=26,
                                            col_offset=16,
                                            end_lineno=26,
                                            end_col_offset=41,
                                            target=Name(lineno=26, col_offset=16, end_lineno=26, end_col_offset=26, id='identifier', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                lineno=26,
                                                col_offset=30,
                                                end_lineno=26,
                                                end_col_offset=41,
                                                left=Constant(lineno=26, col_offset=30, end_lineno=26, end_col_offset=35, value='_%s', kind=None),
                                                op=Mod(),
                                                right=Name(lineno=26, col_offset=38, end_lineno=26, end_col_offset=41, id='cpt', ctx=Load()),
                                            ),
                                        ),
                                        AugAssign(
                                            lineno=27,
                                            col_offset=16,
                                            end_lineno=27,
                                            end_col_offset=24,
                                            target=Name(lineno=27, col_offset=16, end_lineno=27, end_col_offset=19, id='cpt', ctx=Store()),
                                            op=Add(),
                                            value=Constant(lineno=27, col_offset=23, end_lineno=27, end_col_offset=24, value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    lineno=28,
                                    col_offset=12,
                                    end_lineno=28,
                                    end_col_offset=41,
                                    targets=[
                                        Subscript(
                                            lineno=28,
                                            col_offset=12,
                                            end_lineno=28,
                                            end_col_offset=35,
                                            value=Name(lineno=28, col_offset=12, end_lineno=28, end_col_offset=23, id='usb_devices', ctx=Load()),
                                            slice=Name(lineno=28, col_offset=24, end_lineno=28, end_col_offset=34, id='identifier', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(lineno=28, col_offset=38, end_lineno=28, end_col_offset=41, id='dev', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=26,
                            value=Name(lineno=29, col_offset=15, end_lineno=29, end_col_offset=26, id='usb_devices', ctx=Load()),
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
