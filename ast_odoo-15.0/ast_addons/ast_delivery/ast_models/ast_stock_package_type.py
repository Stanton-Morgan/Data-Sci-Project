Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=19,
            end_col_offset=45,
            name='PackageType',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=18,
                    end_lineno=7,
                    end_col_offset=30,
                    value=Name(lineno=7, col_offset=18, end_lineno=7, end_col_offset=24, id='models', ctx=Load()),
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
                    end_col_offset=35,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=35, value='stock.package.type', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=54,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=24, id='shipper_package_code', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=27,
                        end_lineno=10,
                        end_col_offset=54,
                        func=Attribute(
                            lineno=10,
                            col_offset=27,
                            end_lineno=10,
                            end_col_offset=38,
                            value=Name(lineno=10, col_offset=27, end_lineno=10, end_col_offset=33, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=39, end_lineno=10, end_col_offset=53, value='Carrier Code', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=115,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=24, id='package_carrier_type', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=27,
                        end_lineno=11,
                        end_col_offset=115,
                        func=Attribute(
                            lineno=11,
                            col_offset=27,
                            end_lineno=11,
                            end_col_offset=43,
                            value=Name(lineno=11, col_offset=27, end_lineno=11, end_col_offset=33, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                lineno=11,
                                col_offset=44,
                                end_lineno=11,
                                end_col_offset=80,
                                elts=[
                                    Tuple(
                                        lineno=11,
                                        col_offset=45,
                                        end_lineno=11,
                                        end_col_offset=79,
                                        elts=[
                                            Constant(lineno=11, col_offset=46, end_lineno=11, end_col_offset=52, value='none', kind=None),
                                            Constant(lineno=11, col_offset=54, end_lineno=11, end_col_offset=78, value='No carrier integration', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=82,
                                end_lineno=11,
                                end_col_offset=98,
                                arg='string',
                                value=Constant(lineno=11, col_offset=89, end_lineno=11, end_col_offset=98, value='Carrier', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=100,
                                end_lineno=11,
                                end_col_offset=114,
                                arg='default',
                                value=Constant(lineno=11, col_offset=108, end_lineno=11, end_col_offset=114, value='none', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=45,
                    name='_onchange_carrier_type',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=31, end_lineno=14, end_col_offset=35, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=118,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=18, id='carrier_id', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=21,
                                end_lineno=15,
                                end_col_offset=118,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=21,
                                    end_lineno=15,
                                    end_col_offset=56,
                                    value=Subscript(
                                        lineno=15,
                                        col_offset=21,
                                        end_lineno=15,
                                        end_col_offset=49,
                                        value=Attribute(
                                            lineno=15,
                                            col_offset=21,
                                            end_lineno=15,
                                            end_col_offset=29,
                                            value=Name(lineno=15, col_offset=21, end_lineno=15, end_col_offset=25, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=15, col_offset=30, end_lineno=15, end_col_offset=48, value='delivery.carrier', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=15,
                                        col_offset=57,
                                        end_lineno=15,
                                        end_col_offset=108,
                                        elts=[
                                            Tuple(
                                                lineno=15,
                                                col_offset=58,
                                                end_lineno=15,
                                                end_col_offset=107,
                                                elts=[
                                                    Constant(lineno=15, col_offset=59, end_lineno=15, end_col_offset=74, value='delivery_type', kind=None),
                                                    Constant(lineno=15, col_offset=76, end_lineno=15, end_col_offset=79, value='=', kind=None),
                                                    Attribute(
                                                        lineno=15,
                                                        col_offset=81,
                                                        end_lineno=15,
                                                        end_col_offset=106,
                                                        value=Name(lineno=15, col_offset=81, end_lineno=15, end_col_offset=85, id='self', ctx=Load()),
                                                        attr='package_carrier_type',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=15,
                                        col_offset=110,
                                        end_lineno=15,
                                        end_col_offset=117,
                                        arg='limit',
                                        value=Constant(lineno=15, col_offset=116, end_lineno=15, end_col_offset=117, value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=16,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=45,
                            test=Name(lineno=16, col_offset=11, end_lineno=16, end_col_offset=21, id='carrier_id', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=85,
                                    targets=[
                                        Attribute(
                                            lineno=17,
                                            col_offset=12,
                                            end_lineno=17,
                                            end_col_offset=37,
                                            value=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=16, id='self', ctx=Load()),
                                            attr='shipper_package_code',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=17,
                                        col_offset=40,
                                        end_lineno=17,
                                        end_col_offset=85,
                                        func=Attribute(
                                            lineno=17,
                                            col_offset=40,
                                            end_lineno=17,
                                            end_col_offset=83,
                                            value=Name(lineno=17, col_offset=40, end_lineno=17, end_col_offset=50, id='carrier_id', ctx=Load()),
                                            attr='_get_default_custom_package_code',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=19,
                                    end_col_offset=45,
                                    targets=[
                                        Attribute(
                                            lineno=19,
                                            col_offset=12,
                                            end_lineno=19,
                                            end_col_offset=37,
                                            value=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=16, id='self', ctx=Load()),
                                            attr='shipper_package_code',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(lineno=19, col_offset=40, end_lineno=19, end_col_offset=45, value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=13,
                            col_offset=5,
                            end_lineno=13,
                            end_col_offset=41,
                            func=Attribute(
                                lineno=13,
                                col_offset=5,
                                end_lineno=13,
                                end_col_offset=17,
                                value=Name(lineno=13, col_offset=5, end_lineno=13, end_col_offset=8, id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=13, col_offset=18, end_lineno=13, end_col_offset=40, value='package_carrier_type', kind=None)],
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
