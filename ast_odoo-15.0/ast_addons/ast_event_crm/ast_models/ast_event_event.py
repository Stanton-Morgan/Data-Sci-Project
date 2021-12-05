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
            end_lineno=26,
            end_col_offset=59,
            name='EventEvent',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=17,
                    end_lineno=7,
                    end_col_offset=29,
                    value=Name(lineno=7, col_offset=17, end_lineno=7, end_col_offset=23, id='models', ctx=Load()),
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
                    end_col_offset=25,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=25, value='event.event', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=28,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=28, value='event.event', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=47,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=12, id='lead_ids', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=15,
                        end_lineno=13,
                        end_col_offset=47,
                        func=Attribute(
                            lineno=11,
                            col_offset=15,
                            end_lineno=11,
                            end_col_offset=30,
                            value=Name(lineno=11, col_offset=15, end_lineno=11, end_col_offset=21, id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=12, col_offset=8, end_lineno=12, end_col_offset=18, value='crm.lead', kind=None),
                            Constant(lineno=12, col_offset=20, end_lineno=12, end_col_offset=30, value='event_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=32,
                                end_lineno=12,
                                end_col_offset=46,
                                arg='string',
                                value=Constant(lineno=12, col_offset=39, end_lineno=12, end_col_offset=46, value='Leads', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=48,
                                end_lineno=12,
                                end_col_offset=87,
                                arg='groups',
                                value=Constant(lineno=12, col_offset=55, end_lineno=12, end_col_offset=87, value='sales_team.group_sale_salesman', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=46,
                                arg='help',
                                value=Constant(lineno=13, col_offset=13, end_lineno=13, end_col_offset=46, value='Leads generated from this event', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=58,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=14, id='lead_count', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=17,
                        end_lineno=16,
                        end_col_offset=58,
                        func=Attribute(
                            lineno=14,
                            col_offset=17,
                            end_lineno=14,
                            end_col_offset=31,
                            value=Name(lineno=14, col_offset=17, end_lineno=14, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=24,
                                arg='string',
                                value=Constant(lineno=15, col_offset=15, end_lineno=15, end_col_offset=24, value='# Leads', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=26,
                                end_lineno=15,
                                end_col_offset=55,
                                arg='compute',
                                value=Constant(lineno=15, col_offset=34, end_lineno=15, end_col_offset=55, value='_compute_lead_count', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=57,
                                end_lineno=15,
                                end_col_offset=96,
                                arg='groups',
                                value=Constant(lineno=15, col_offset=64, end_lineno=15, end_col_offset=96, value='sales_team.group_sale_salesman', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=8,
                                end_lineno=16,
                                end_col_offset=57,
                                arg='help',
                                value=Constant(lineno=16, col_offset=13, end_lineno=16, end_col_offset=57, value='Counter for the leads linked to this event', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=19,
                    col_offset=4,
                    end_lineno=26,
                    end_col_offset=59,
                    name='_compute_lead_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=19, col_offset=28, end_lineno=19, end_col_offset=32, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=9,
                            targets=[Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=17, id='lead_data', ctx=Store())],
                            value=Call(
                                lineno=20,
                                col_offset=20,
                                end_lineno=23,
                                end_col_offset=9,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=20,
                                    end_lineno=20,
                                    end_col_offset=51,
                                    value=Subscript(
                                        lineno=20,
                                        col_offset=20,
                                        end_lineno=20,
                                        end_col_offset=40,
                                        value=Attribute(
                                            lineno=20,
                                            col_offset=20,
                                            end_lineno=20,
                                            end_col_offset=28,
                                            value=Name(lineno=20, col_offset=20, end_lineno=20, end_col_offset=24, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=20, col_offset=29, end_lineno=20, end_col_offset=39, value='crm.lead', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=21,
                                        col_offset=12,
                                        end_lineno=21,
                                        end_col_offset=42,
                                        elts=[
                                            Tuple(
                                                lineno=21,
                                                col_offset=13,
                                                end_lineno=21,
                                                end_col_offset=41,
                                                elts=[
                                                    Constant(lineno=21, col_offset=14, end_lineno=21, end_col_offset=24, value='event_id', kind=None),
                                                    Constant(lineno=21, col_offset=26, end_lineno=21, end_col_offset=30, value='in', kind=None),
                                                    Attribute(
                                                        lineno=21,
                                                        col_offset=32,
                                                        end_lineno=21,
                                                        end_col_offset=40,
                                                        value=Name(lineno=21, col_offset=32, end_lineno=21, end_col_offset=36, id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=22,
                                        col_offset=12,
                                        end_lineno=22,
                                        end_col_offset=24,
                                        elts=[Constant(lineno=22, col_offset=13, end_lineno=22, end_col_offset=23, value='event_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=22,
                                        col_offset=26,
                                        end_lineno=22,
                                        end_col_offset=38,
                                        elts=[Constant(lineno=22, col_offset=27, end_lineno=22, end_col_offset=37, value='event_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=89,
                            targets=[Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=19, id='mapped_data', ctx=Store())],
                            value=DictComp(
                                lineno=24,
                                col_offset=22,
                                end_lineno=24,
                                end_col_offset=89,
                                key=Subscript(
                                    lineno=24,
                                    col_offset=23,
                                    end_lineno=24,
                                    end_col_offset=42,
                                    value=Subscript(
                                        lineno=24,
                                        col_offset=23,
                                        end_lineno=24,
                                        end_col_offset=39,
                                        value=Name(lineno=24, col_offset=23, end_lineno=24, end_col_offset=27, id='item', ctx=Load()),
                                        slice=Constant(lineno=24, col_offset=28, end_lineno=24, end_col_offset=38, value='event_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(lineno=24, col_offset=40, end_lineno=24, end_col_offset=41, value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    lineno=24,
                                    col_offset=44,
                                    end_lineno=24,
                                    end_col_offset=66,
                                    value=Name(lineno=24, col_offset=44, end_lineno=24, end_col_offset=48, id='item', ctx=Load()),
                                    slice=Constant(lineno=24, col_offset=49, end_lineno=24, end_col_offset=65, value='event_id_count', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(lineno=24, col_offset=71, end_lineno=24, end_col_offset=75, id='item', ctx=Store()),
                                        iter=Name(lineno=24, col_offset=79, end_lineno=24, end_col_offset=88, id='lead_data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=25,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=59,
                            target=Name(lineno=25, col_offset=12, end_lineno=25, end_col_offset=17, id='event', ctx=Store()),
                            iter=Name(lineno=25, col_offset=21, end_lineno=25, end_col_offset=25, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=26,
                                    col_offset=12,
                                    end_lineno=26,
                                    end_col_offset=59,
                                    targets=[
                                        Attribute(
                                            lineno=26,
                                            col_offset=12,
                                            end_lineno=26,
                                            end_col_offset=28,
                                            value=Name(lineno=26, col_offset=12, end_lineno=26, end_col_offset=17, id='event', ctx=Load()),
                                            attr='lead_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=26,
                                        col_offset=31,
                                        end_lineno=26,
                                        end_col_offset=59,
                                        func=Attribute(
                                            lineno=26,
                                            col_offset=31,
                                            end_lineno=26,
                                            end_col_offset=46,
                                            value=Name(lineno=26, col_offset=31, end_lineno=26, end_col_offset=42, id='mapped_data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=26,
                                                col_offset=47,
                                                end_lineno=26,
                                                end_col_offset=55,
                                                value=Name(lineno=26, col_offset=47, end_lineno=26, end_col_offset=52, id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(lineno=26, col_offset=57, end_lineno=26, end_col_offset=58, value=0, kind=None),
                                        ],
                                        keywords=[],
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
                            lineno=18,
                            col_offset=5,
                            end_lineno=18,
                            end_col_offset=28,
                            func=Attribute(
                                lineno=18,
                                col_offset=5,
                                end_lineno=18,
                                end_col_offset=16,
                                value=Name(lineno=18, col_offset=5, end_lineno=18, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=18, col_offset=17, end_lineno=18, end_col_offset=27, value='lead_ids', kind=None)],
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
