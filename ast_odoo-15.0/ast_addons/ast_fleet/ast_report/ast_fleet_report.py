Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=24,
            module='psycopg2',
            names=[alias(name='sql', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=22,
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=147,
            end_col_offset=14,
            name='FleetReport',
            bases=[
                Attribute(
                    lineno=9,
                    col_offset=18,
                    end_lineno=9,
                    end_col_offset=30,
                    value=Name(lineno=9, col_offset=18, end_lineno=9, end_col_offset=24, id='models', ctx=Load()),
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
                    end_col_offset=39,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=39, value='fleet.vehicle.cost.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=42,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=11, col_offset=19, end_lineno=11, end_col_offset=42, value='Fleet Analysis Report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=17,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=9, id='_auto', ctx=Store())],
                    value=Constant(lineno=12, col_offset=12, end_lineno=12, end_col_offset=17, value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=30,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=13, col_offset=13, end_lineno=13, end_col_offset=30, value='date_start desc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=73,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=14, id='company_id', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=17,
                        end_lineno=15,
                        end_col_offset=73,
                        func=Attribute(
                            lineno=15,
                            col_offset=17,
                            end_lineno=15,
                            end_col_offset=32,
                            value=Name(lineno=15, col_offset=17, end_lineno=15, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=15, col_offset=33, end_lineno=15, end_col_offset=46, value='res.company', kind=None),
                            Constant(lineno=15, col_offset=48, end_lineno=15, end_col_offset=57, value='Company', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=59,
                                end_lineno=15,
                                end_col_offset=72,
                                arg='readonly',
                                value=Constant(lineno=15, col_offset=68, end_lineno=15, end_col_offset=72, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=75,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=14, id='vehicle_id', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=17,
                        end_lineno=16,
                        end_col_offset=75,
                        func=Attribute(
                            lineno=16,
                            col_offset=17,
                            end_lineno=16,
                            end_col_offset=32,
                            value=Name(lineno=16, col_offset=17, end_lineno=16, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=16, col_offset=33, end_lineno=16, end_col_offset=48, value='fleet.vehicle', kind=None),
                            Constant(lineno=16, col_offset=50, end_lineno=16, end_col_offset=59, value='Vehicle', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=61,
                                end_lineno=16,
                                end_col_offset=74,
                                arg='readonly',
                                value=Constant(lineno=16, col_offset=70, end_lineno=16, end_col_offset=74, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=53,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=11,
                        end_lineno=17,
                        end_col_offset=53,
                        func=Attribute(
                            lineno=17,
                            col_offset=11,
                            end_lineno=17,
                            end_col_offset=22,
                            value=Name(lineno=17, col_offset=11, end_lineno=17, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=23, end_lineno=17, end_col_offset=37, value='Vehicle Name', kind=None)],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=39,
                                end_lineno=17,
                                end_col_offset=52,
                                arg='readonly',
                                value=Constant(lineno=17, col_offset=48, end_lineno=17, end_col_offset=52, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=71,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=13, id='driver_id', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=16,
                        end_lineno=18,
                        end_col_offset=71,
                        func=Attribute(
                            lineno=18,
                            col_offset=16,
                            end_lineno=18,
                            end_col_offset=31,
                            value=Name(lineno=18, col_offset=16, end_lineno=18, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=18, col_offset=32, end_lineno=18, end_col_offset=45, value='res.partner', kind=None),
                            Constant(lineno=18, col_offset=47, end_lineno=18, end_col_offset=55, value='Driver', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=18,
                                col_offset=57,
                                end_lineno=18,
                                end_col_offset=70,
                                arg='readonly',
                                value=Constant(lineno=18, col_offset=66, end_lineno=18, end_col_offset=70, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=50,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=13, id='fuel_type', ctx=Store())],
                    value=Call(
                        lineno=19,
                        col_offset=16,
                        end_lineno=19,
                        end_col_offset=50,
                        func=Attribute(
                            lineno=19,
                            col_offset=16,
                            end_lineno=19,
                            end_col_offset=27,
                            value=Name(lineno=19, col_offset=16, end_lineno=19, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=19, col_offset=28, end_lineno=19, end_col_offset=34, value='Fuel', kind=None)],
                        keywords=[
                            keyword(
                                lineno=19,
                                col_offset=36,
                                end_lineno=19,
                                end_col_offset=49,
                                arg='readonly',
                                value=Constant(lineno=19, col_offset=45, end_lineno=19, end_col_offset=49, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=20,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=51,
                    targets=[Name(lineno=20, col_offset=4, end_lineno=20, end_col_offset=14, id='date_start', ctx=Store())],
                    value=Call(
                        lineno=20,
                        col_offset=17,
                        end_lineno=20,
                        end_col_offset=51,
                        func=Attribute(
                            lineno=20,
                            col_offset=17,
                            end_lineno=20,
                            end_col_offset=28,
                            value=Name(lineno=20, col_offset=17, end_lineno=20, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=20, col_offset=29, end_lineno=20, end_col_offset=35, value='Date', kind=None)],
                        keywords=[
                            keyword(
                                lineno=20,
                                col_offset=37,
                                end_lineno=20,
                                end_col_offset=50,
                                arg='readonly',
                                value=Constant(lineno=20, col_offset=46, end_lineno=20, end_col_offset=50, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=21,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=86,
                    targets=[Name(lineno=21, col_offset=4, end_lineno=21, end_col_offset=16, id='vehicle_type', ctx=Store())],
                    value=Call(
                        lineno=21,
                        col_offset=19,
                        end_lineno=21,
                        end_col_offset=86,
                        func=Attribute(
                            lineno=21,
                            col_offset=19,
                            end_lineno=21,
                            end_col_offset=35,
                            value=Name(lineno=21, col_offset=19, end_lineno=21, end_col_offset=25, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                lineno=21,
                                col_offset=36,
                                end_lineno=21,
                                end_col_offset=70,
                                elts=[
                                    Tuple(
                                        lineno=21,
                                        col_offset=37,
                                        end_lineno=21,
                                        end_col_offset=51,
                                        elts=[
                                            Constant(lineno=21, col_offset=38, end_lineno=21, end_col_offset=43, value='car', kind=None),
                                            Constant(lineno=21, col_offset=45, end_lineno=21, end_col_offset=50, value='Car', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=21,
                                        col_offset=53,
                                        end_lineno=21,
                                        end_col_offset=69,
                                        elts=[
                                            Constant(lineno=21, col_offset=54, end_lineno=21, end_col_offset=60, value='bike', kind=None),
                                            Constant(lineno=21, col_offset=62, end_lineno=21, end_col_offset=68, value='Bike', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                lineno=21,
                                col_offset=72,
                                end_lineno=21,
                                end_col_offset=85,
                                arg='readonly',
                                value=Constant(lineno=21, col_offset=81, end_lineno=21, end_col_offset=85, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=23,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=46,
                    targets=[Name(lineno=23, col_offset=4, end_lineno=23, end_col_offset=8, id='cost', ctx=Store())],
                    value=Call(
                        lineno=23,
                        col_offset=11,
                        end_lineno=23,
                        end_col_offset=46,
                        func=Attribute(
                            lineno=23,
                            col_offset=11,
                            end_lineno=23,
                            end_col_offset=23,
                            value=Name(lineno=23, col_offset=11, end_lineno=23, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=23, col_offset=24, end_lineno=23, end_col_offset=30, value='Cost', kind=None)],
                        keywords=[
                            keyword(
                                lineno=23,
                                col_offset=32,
                                end_lineno=23,
                                end_col_offset=45,
                                arg='readonly',
                                value=Constant(lineno=23, col_offset=41, end_lineno=23, end_col_offset=45, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=24,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=21,
                    targets=[Name(lineno=24, col_offset=4, end_lineno=24, end_col_offset=13, id='cost_type', ctx=Store())],
                    value=Call(
                        lineno=24,
                        col_offset=16,
                        end_lineno=27,
                        end_col_offset=21,
                        func=Attribute(
                            lineno=24,
                            col_offset=16,
                            end_lineno=24,
                            end_col_offset=32,
                            value=Name(lineno=24, col_offset=16, end_lineno=24, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=24,
                                col_offset=33,
                                end_lineno=24,
                                end_col_offset=51,
                                arg='string',
                                value=Constant(lineno=24, col_offset=40, end_lineno=24, end_col_offset=51, value='Cost Type', kind=None),
                            ),
                            keyword(
                                lineno=24,
                                col_offset=53,
                                end_lineno=27,
                                end_col_offset=5,
                                arg='selection',
                                value=List(
                                    lineno=24,
                                    col_offset=63,
                                    end_lineno=27,
                                    end_col_offset=5,
                                    elts=[
                                        Tuple(
                                            lineno=25,
                                            col_offset=8,
                                            end_lineno=25,
                                            end_col_offset=32,
                                            elts=[
                                                Constant(lineno=25, col_offset=9, end_lineno=25, end_col_offset=19, value='contract', kind=None),
                                                Constant(lineno=25, col_offset=21, end_lineno=25, end_col_offset=31, value='Contract', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=26,
                                            col_offset=8,
                                            end_lineno=26,
                                            end_col_offset=30,
                                            elts=[
                                                Constant(lineno=26, col_offset=9, end_lineno=26, end_col_offset=18, value='service', kind=None),
                                                Constant(lineno=26, col_offset=20, end_lineno=26, end_col_offset=29, value='Service', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                lineno=27,
                                col_offset=7,
                                end_lineno=27,
                                end_col_offset=20,
                                arg='readonly',
                                value=Constant(lineno=27, col_offset=16, end_lineno=27, end_col_offset=20, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=29,
                    col_offset=4,
                    end_lineno=147,
                    end_col_offset=14,
                    name='init',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=29, col_offset=13, end_lineno=29, end_col_offset=17, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=30,
                            col_offset=8,
                            end_lineno=141,
                            end_col_offset=3,
                            targets=[Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=13, id='query', ctx=Store())],
                            value=Constant(lineno=30, col_offset=16, end_lineno=141, end_col_offset=3, value="\nWITH service_costs AS (\n    SELECT\n        ve.id AS vehicle_id,\n        ve.company_id AS company_id,\n        ve.name AS name,\n        ve.driver_id AS driver_id,\n        ve.fuel_type AS fuel_type,\n        date(date_trunc('month', d)) AS date_start,\n        vem.vehicle_type as vehicle_type,\n        COALESCE(sum(se.amount), 0) AS\n        COST,\n        'service' AS cost_type\n    FROM\n        fleet_vehicle ve\n    JOIN\n        fleet_vehicle_model vem ON vem.id = ve.model_id\n    CROSS JOIN generate_series((\n            SELECT\n                min(date)\n                FROM fleet_vehicle_log_services), CURRENT_DATE + '1 month'::interval, '1 month') d\n        LEFT JOIN fleet_vehicle_log_services se ON se.vehicle_id = ve.id\n            AND date_trunc('month', se.date) = date_trunc('month', d)\n    WHERE\n        ve.active AND se.active AND se.state != 'cancelled'\n    GROUP BY\n        ve.id,\n        ve.company_id,\n        vem.vehicle_type,\n        ve.name,\n        date_start,\n        d\n    ORDER BY\n        ve.id,\n        date_start\n),\ncontract_costs AS (\n    SELECT\n        ve.id AS vehicle_id,\n        ve.company_id AS company_id,\n        ve.name AS name,\n        ve.driver_id AS driver_id,\n        ve.fuel_type AS fuel_type,\n        date(date_trunc('month', d)) AS date_start,\n        vem.vehicle_type as vehicle_type,\n        (COALESCE(sum(co.amount), 0) + COALESCE(sum(cod.cost_generated * extract(day FROM least (date_trunc('month', d) + interval '1 month', cod.expiration_date) - greatest (date_trunc('month', d), cod.start_date))), 0) + COALESCE(sum(com.cost_generated), 0) + COALESCE(sum(coy.cost_generated), 0)) AS\n        COST,\n        'contract' AS cost_type\n    FROM\n        fleet_vehicle ve\n    JOIN\n        fleet_vehicle_model vem ON vem.id = ve.model_id\n    CROSS JOIN generate_series((\n            SELECT\n                min(acquisition_date)\n                FROM fleet_vehicle), CURRENT_DATE + '1 month'::interval, '1 month') d\n        LEFT JOIN fleet_vehicle_log_contract co ON co.vehicle_id = ve.id\n            AND date_trunc('month', co.date) = date_trunc('month', d)\n        LEFT JOIN fleet_vehicle_log_contract cod ON cod.vehicle_id = ve.id\n            AND date_trunc('month', cod.start_date) <= date_trunc('month', d)\n            AND date_trunc('month', cod.expiration_date) >= date_trunc('month', d)\n            AND cod.cost_frequency = 'daily'\n    LEFT JOIN fleet_vehicle_log_contract com ON com.vehicle_id = ve.id\n        AND date_trunc('month', com.start_date) <= date_trunc('month', d)\n        AND date_trunc('month', com.expiration_date) >= date_trunc('month', d)\n        AND com.cost_frequency = 'monthly'\n    LEFT JOIN fleet_vehicle_log_contract coy ON coy.vehicle_id = ve.id\n        AND date_trunc('month', coy.date) = date_trunc('month', d)\n        AND date_trunc('month', coy.start_date) <= date_trunc('month', d)\n        AND date_trunc('month', coy.expiration_date) >= date_trunc('month', d)\n        AND coy.cost_frequency = 'yearly'\n    WHERE\n        ve.active\n    GROUP BY\n        ve.id,\n        ve.company_id,\n        vem.vehicle_type,\n        ve.name,\n        date_start,\n        d\n    ORDER BY\n        ve.id,\n        date_start\n)\nSELECT\n    vehicle_id AS id,\n    company_id,\n    vehicle_id,\n    name,\n    driver_id,\n    fuel_type,\n    date_start,\n    vehicle_type,\n    COST,\n    'service' as cost_type\nFROM\n    service_costs sc\nUNION ALL (\n    SELECT\n        vehicle_id AS id,\n        company_id,\n        vehicle_id,\n        name,\n        driver_id,\n        fuel_type,\n        date_start,\n        vehicle_type,\n        COST,\n        'contract' as cost_type\n    FROM\n        contract_costs cc)\n", kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=142,
                            col_offset=8,
                            end_lineno=142,
                            end_col_offset=59,
                            value=Call(
                                lineno=142,
                                col_offset=8,
                                end_lineno=142,
                                end_col_offset=59,
                                func=Attribute(
                                    lineno=142,
                                    col_offset=8,
                                    end_lineno=142,
                                    end_col_offset=33,
                                    value=Name(lineno=142, col_offset=8, end_lineno=142, end_col_offset=13, id='tools', ctx=Load()),
                                    attr='drop_view_if_exists',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=142,
                                        col_offset=34,
                                        end_lineno=142,
                                        end_col_offset=45,
                                        value=Attribute(
                                            lineno=142,
                                            col_offset=34,
                                            end_lineno=142,
                                            end_col_offset=42,
                                            value=Name(lineno=142, col_offset=34, end_lineno=142, end_col_offset=38, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=142,
                                        col_offset=47,
                                        end_lineno=142,
                                        end_col_offset=58,
                                        value=Name(lineno=142, col_offset=47, end_lineno=142, end_col_offset=51, id='self', ctx=Load()),
                                        attr='_table',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=143,
                            col_offset=8,
                            end_lineno=147,
                            end_col_offset=14,
                            value=Call(
                                lineno=143,
                                col_offset=8,
                                end_lineno=147,
                                end_col_offset=14,
                                func=Attribute(
                                    lineno=143,
                                    col_offset=8,
                                    end_lineno=143,
                                    end_col_offset=27,
                                    value=Attribute(
                                        lineno=143,
                                        col_offset=8,
                                        end_lineno=143,
                                        end_col_offset=19,
                                        value=Attribute(
                                            lineno=143,
                                            col_offset=8,
                                            end_lineno=143,
                                            end_col_offset=16,
                                            value=Name(lineno=143, col_offset=8, end_lineno=143, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=144,
                                        col_offset=12,
                                        end_lineno=147,
                                        end_col_offset=13,
                                        func=Attribute(
                                            lineno=144,
                                            col_offset=12,
                                            end_lineno=144,
                                            end_col_offset=67,
                                            value=Call(
                                                lineno=144,
                                                col_offset=12,
                                                end_lineno=144,
                                                end_col_offset=60,
                                                func=Attribute(
                                                    lineno=144,
                                                    col_offset=12,
                                                    end_lineno=144,
                                                    end_col_offset=19,
                                                    value=Name(lineno=144, col_offset=12, end_lineno=144, end_col_offset=15, id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(lineno=144, col_offset=20, end_lineno=144, end_col_offset=59, value='CREATE or REPLACE VIEW {} as ({})', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                lineno=145,
                                                col_offset=16,
                                                end_lineno=145,
                                                end_col_offset=43,
                                                func=Attribute(
                                                    lineno=145,
                                                    col_offset=16,
                                                    end_lineno=145,
                                                    end_col_offset=30,
                                                    value=Name(lineno=145, col_offset=16, end_lineno=145, end_col_offset=19, id='sql', ctx=Load()),
                                                    attr='Identifier',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        lineno=145,
                                                        col_offset=31,
                                                        end_lineno=145,
                                                        end_col_offset=42,
                                                        value=Name(lineno=145, col_offset=31, end_lineno=145, end_col_offset=35, id='self', ctx=Load()),
                                                        attr='_table',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                lineno=146,
                                                col_offset=16,
                                                end_lineno=146,
                                                end_col_offset=30,
                                                func=Attribute(
                                                    lineno=146,
                                                    col_offset=16,
                                                    end_lineno=146,
                                                    end_col_offset=23,
                                                    value=Name(lineno=146, col_offset=16, end_lineno=146, end_col_offset=19, id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(lineno=146, col_offset=24, end_lineno=146, end_col_offset=29, id='query', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
