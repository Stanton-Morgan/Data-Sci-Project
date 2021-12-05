Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=35,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='api', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=14,
            end_col_offset=18,
            name='IrUiMenu',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=15,
                    end_lineno=7,
                    end_col_offset=27,
                    value=Name(lineno=7, col_offset=15, end_lineno=7, end_col_offset=21, id='models', ctx=Load()),
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
                    end_col_offset=27,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=27, value='ir.ui.menu', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=18,
                    name='_load_menus_blacklist',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=30, end_lineno=10, end_col_offset=34, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=45,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=11,
                                col_offset=14,
                                end_lineno=11,
                                end_col_offset=45,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=14,
                                    end_lineno=11,
                                    end_col_offset=43,
                                    value=Call(
                                        lineno=11,
                                        col_offset=14,
                                        end_lineno=11,
                                        end_col_offset=21,
                                        func=Name(lineno=11, col_offset=14, end_lineno=11, end_col_offset=19, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_load_menus_blacklist',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=12,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=62,
                            test=Call(
                                lineno=12,
                                col_offset=11,
                                end_lineno=12,
                                end_col_offset=54,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=11,
                                    end_lineno=12,
                                    end_col_offset=34,
                                    value=Attribute(
                                        lineno=12,
                                        col_offset=11,
                                        end_lineno=12,
                                        end_col_offset=24,
                                        value=Attribute(
                                            lineno=12,
                                            col_offset=11,
                                            end_lineno=12,
                                            end_col_offset=19,
                                            value=Name(lineno=12, col_offset=11, end_lineno=12, end_col_offset=15, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=12, col_offset=35, end_lineno=12, end_col_offset=53, value='hr.group_hr_user', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    lineno=13,
                                    col_offset=12,
                                    end_lineno=13,
                                    end_col_offset=62,
                                    value=Call(
                                        lineno=13,
                                        col_offset=12,
                                        end_lineno=13,
                                        end_col_offset=62,
                                        func=Attribute(
                                            lineno=13,
                                            col_offset=12,
                                            end_lineno=13,
                                            end_col_offset=22,
                                            value=Name(lineno=13, col_offset=12, end_lineno=13, end_col_offset=15, id='res', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=13,
                                                col_offset=23,
                                                end_lineno=13,
                                                end_col_offset=61,
                                                value=Call(
                                                    lineno=13,
                                                    col_offset=23,
                                                    end_lineno=13,
                                                    end_col_offset=58,
                                                    func=Attribute(
                                                        lineno=13,
                                                        col_offset=23,
                                                        end_lineno=13,
                                                        end_col_offset=35,
                                                        value=Attribute(
                                                            lineno=13,
                                                            col_offset=23,
                                                            end_lineno=13,
                                                            end_col_offset=31,
                                                            value=Name(lineno=13, col_offset=23, end_lineno=13, end_col_offset=27, id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(lineno=13, col_offset=36, end_lineno=13, end_col_offset=57, value='hr.menu_hr_employee', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=18,
                            value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=18, id='res', ctx=Load()),
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
