Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=11,
            end_col_offset=37,
            name='ContractType',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=19,
                    end_lineno=7,
                    end_col_offset=31,
                    value=Name(lineno=7, col_offset=19, end_lineno=7, end_col_offset=25, id='models', ctx=Load()),
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
                    end_col_offset=30,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=30, value='hr.contract.type', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=34,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=34, value='Contract Type', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=37,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=11,
                        end_lineno=11,
                        end_col_offset=37,
                        func=Attribute(
                            lineno=11,
                            col_offset=11,
                            end_lineno=11,
                            end_col_offset=22,
                            value=Name(lineno=11, col_offset=11, end_lineno=11, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=23,
                                end_lineno=11,
                                end_col_offset=36,
                                arg='required',
                                value=Constant(lineno=11, col_offset=32, end_lineno=11, end_col_offset=36, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            lineno=13,
            col_offset=0,
            end_lineno=21,
            end_col_offset=115,
            name='HrPayrollStructureType',
            bases=[
                Attribute(
                    lineno=13,
                    col_offset=29,
                    end_lineno=13,
                    end_col_offset=41,
                    value=Name(lineno=13, col_offset=29, end_lineno=13, end_col_offset=35, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=39,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=14, col_offset=12, end_lineno=14, end_col_offset=39, value='hr.payroll.structure.type', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=34,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=15, col_offset=19, end_lineno=15, end_col_offset=34, value='Contract Type', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=39,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=11,
                        end_lineno=17,
                        end_col_offset=39,
                        func=Attribute(
                            lineno=17,
                            col_offset=11,
                            end_lineno=17,
                            end_col_offset=22,
                            value=Name(lineno=17, col_offset=11, end_lineno=17, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=23, end_lineno=17, end_col_offset=38, value='Contract Type', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=67,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=32, id='default_resource_calendar_id', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=35,
                        end_lineno=20,
                        end_col_offset=67,
                        func=Attribute(
                            lineno=18,
                            col_offset=35,
                            end_lineno=18,
                            end_col_offset=50,
                            value=Name(lineno=18, col_offset=35, end_lineno=18, end_col_offset=41, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=19, col_offset=8, end_lineno=19, end_col_offset=27, value='resource.calendar', kind=None),
                            Constant(lineno=19, col_offset=29, end_lineno=19, end_col_offset=52, value='Default Working Hours', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=66,
                                arg='default',
                                value=Lambda(
                                    lineno=20,
                                    col_offset=16,
                                    end_lineno=20,
                                    end_col_offset=66,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=20, col_offset=23, end_lineno=20, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        lineno=20,
                                        col_offset=29,
                                        end_lineno=20,
                                        end_col_offset=66,
                                        value=Attribute(
                                            lineno=20,
                                            col_offset=29,
                                            end_lineno=20,
                                            end_col_offset=45,
                                            value=Attribute(
                                                lineno=20,
                                                col_offset=29,
                                                end_lineno=20,
                                                end_col_offset=37,
                                                value=Name(lineno=20, col_offset=29, end_lineno=20, end_col_offset=33, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=21,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=115,
                    targets=[Name(lineno=21, col_offset=4, end_lineno=21, end_col_offset=14, id='country_id', ctx=Store())],
                    value=Call(
                        lineno=21,
                        col_offset=17,
                        end_lineno=21,
                        end_col_offset=115,
                        func=Attribute(
                            lineno=21,
                            col_offset=17,
                            end_lineno=21,
                            end_col_offset=32,
                            value=Name(lineno=21, col_offset=17, end_lineno=21, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=21, col_offset=33, end_lineno=21, end_col_offset=46, value='res.country', kind=None)],
                        keywords=[
                            keyword(
                                lineno=21,
                                col_offset=48,
                                end_lineno=21,
                                end_col_offset=64,
                                arg='string',
                                value=Constant(lineno=21, col_offset=55, end_lineno=21, end_col_offset=64, value='Country', kind=None),
                            ),
                            keyword(
                                lineno=21,
                                col_offset=66,
                                end_lineno=21,
                                end_col_offset=114,
                                arg='default',
                                value=Lambda(
                                    lineno=21,
                                    col_offset=74,
                                    end_lineno=21,
                                    end_col_offset=114,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=21, col_offset=81, end_lineno=21, end_col_offset=85, arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        lineno=21,
                                        col_offset=87,
                                        end_lineno=21,
                                        end_col_offset=114,
                                        value=Attribute(
                                            lineno=21,
                                            col_offset=87,
                                            end_lineno=21,
                                            end_col_offset=103,
                                            value=Attribute(
                                                lineno=21,
                                                col_offset=87,
                                                end_lineno=21,
                                                end_col_offset=95,
                                                value=Name(lineno=21, col_offset=87, end_lineno=21, end_col_offset=91, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='country_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
