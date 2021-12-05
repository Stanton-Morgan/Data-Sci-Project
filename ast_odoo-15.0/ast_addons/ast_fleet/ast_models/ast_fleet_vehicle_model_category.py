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
            end_lineno=17,
            end_col_offset=31,
            name='FleetVehicleModelCategory',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=32,
                    end_lineno=7,
                    end_col_offset=44,
                    value=Name(lineno=7, col_offset=32, end_lineno=7, end_col_offset=38, id='models', ctx=Load()),
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
                    end_col_offset=42,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=42, value='fleet.vehicle.model.category', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=42,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=42, value='Category of the model', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=35,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=10, col_offset=13, end_lineno=10, end_col_offset=35, value='sequence asc, id asc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=5,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=20, id='_sql_constraints', ctx=Store())],
                    value=List(
                        lineno=12,
                        col_offset=23,
                        end_lineno=14,
                        end_col_offset=5,
                        elts=[
                            Tuple(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=70,
                                elts=[
                                    Constant(lineno=13, col_offset=9, end_lineno=13, end_col_offset=20, value='name_uniq', kind=None),
                                    Constant(lineno=13, col_offset=22, end_lineno=13, end_col_offset=37, value='UNIQUE (name)', kind=None),
                                    Constant(lineno=13, col_offset=39, end_lineno=13, end_col_offset=69, value='Category name must be unique', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=37,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=11,
                        end_lineno=16,
                        end_col_offset=37,
                        func=Attribute(
                            lineno=16,
                            col_offset=11,
                            end_lineno=16,
                            end_col_offset=22,
                            value=Name(lineno=16, col_offset=11, end_lineno=16, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=23,
                                end_lineno=16,
                                end_col_offset=36,
                                arg='required',
                                value=Constant(lineno=16, col_offset=32, end_lineno=16, end_col_offset=36, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=31,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=12, id='sequence', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=15,
                        end_lineno=17,
                        end_col_offset=31,
                        func=Attribute(
                            lineno=17,
                            col_offset=15,
                            end_lineno=17,
                            end_col_offset=29,
                            value=Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)