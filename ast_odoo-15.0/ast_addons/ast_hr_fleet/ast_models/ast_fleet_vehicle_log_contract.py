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
            lineno=6,
            col_offset=0,
            end_lineno=12,
            end_col_offset=5,
            name='FleetVehicleLogContract',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=30,
                    end_lineno=6,
                    end_col_offset=42,
                    value=Name(lineno=6, col_offset=30, end_lineno=6, end_col_offset=36, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=43,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=43, value='fleet.vehicle.log.contract', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=5,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=25, id='purchaser_employee_id', ctx=Store())],
                    value=Call(
                        lineno=9,
                        col_offset=28,
                        end_lineno=12,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=9,
                            col_offset=28,
                            end_lineno=9,
                            end_col_offset=43,
                            value=Name(lineno=9, col_offset=28, end_lineno=9, end_col_offset=34, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=8,
                                end_lineno=10,
                                end_col_offset=47,
                                arg='related',
                                value=Constant(lineno=10, col_offset=16, end_lineno=10, end_col_offset=47, value='vehicle_id.driver_employee_id', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=34,
                                arg='string',
                                value=Constant(lineno=11, col_offset=15, end_lineno=11, end_col_offset=34, value='Driver (Employee)', kind=None),
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