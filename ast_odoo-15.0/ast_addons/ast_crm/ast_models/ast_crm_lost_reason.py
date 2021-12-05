Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=34,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=29,
            end_col_offset=9,
            name='LostReason',
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
                    end_col_offset=29,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=29, value='crm.lost.reason', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=37,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=37, value='Opp. Lost Reason', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=68,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=11,
                        end_lineno=11,
                        end_col_offset=68,
                        func=Attribute(
                            lineno=11,
                            col_offset=11,
                            end_lineno=11,
                            end_col_offset=22,
                            value=Name(lineno=11, col_offset=11, end_lineno=11, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=23, end_lineno=11, end_col_offset=36, value='Description', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=38,
                                end_lineno=11,
                                end_col_offset=51,
                                arg='required',
                                value=Constant(lineno=11, col_offset=47, end_lineno=11, end_col_offset=51, value=True, kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=53,
                                end_lineno=11,
                                end_col_offset=67,
                                arg='translate',
                                value=Constant(lineno=11, col_offset=63, end_lineno=11, end_col_offset=67, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=51,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=10, id='active', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=13,
                        end_lineno=12,
                        end_col_offset=51,
                        func=Attribute(
                            lineno=12,
                            col_offset=13,
                            end_lineno=12,
                            end_col_offset=27,
                            value=Name(lineno=12, col_offset=13, end_lineno=12, end_col_offset=19, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=28, end_lineno=12, end_col_offset=36, value='Active', kind=None)],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=38,
                                end_lineno=12,
                                end_col_offset=50,
                                arg='default',
                                value=Constant(lineno=12, col_offset=46, end_lineno=12, end_col_offset=50, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=79,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=15, id='leads_count', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=18,
                        end_lineno=13,
                        end_col_offset=79,
                        func=Attribute(
                            lineno=13,
                            col_offset=18,
                            end_lineno=13,
                            end_col_offset=32,
                            value=Name(lineno=13, col_offset=18, end_lineno=13, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=33, end_lineno=13, end_col_offset=46, value='Leads Count', kind=None)],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=48,
                                end_lineno=13,
                                end_col_offset=78,
                                arg='compute',
                                value=Constant(lineno=13, col_offset=56, end_lineno=13, end_col_offset=78, value='_compute_leads_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=62,
                    name='_compute_leads_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=15, col_offset=29, end_lineno=15, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=152,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=17, id='lead_data', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=20,
                                end_lineno=16,
                                end_col_offset=152,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=20,
                                    end_lineno=16,
                                    end_col_offset=83,
                                    value=Call(
                                        lineno=16,
                                        col_offset=20,
                                        end_lineno=16,
                                        end_col_offset=72,
                                        func=Attribute(
                                            lineno=16,
                                            col_offset=20,
                                            end_lineno=16,
                                            end_col_offset=53,
                                            value=Subscript(
                                                lineno=16,
                                                col_offset=20,
                                                end_lineno=16,
                                                end_col_offset=40,
                                                value=Attribute(
                                                    lineno=16,
                                                    col_offset=20,
                                                    end_lineno=16,
                                                    end_col_offset=28,
                                                    value=Name(lineno=16, col_offset=20, end_lineno=16, end_col_offset=24, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=16, col_offset=29, end_lineno=16, end_col_offset=39, value='crm.lead', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                lineno=16,
                                                col_offset=54,
                                                end_lineno=16,
                                                end_col_offset=71,
                                                arg='active_test',
                                                value=Constant(lineno=16, col_offset=66, end_lineno=16, end_col_offset=71, value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=16,
                                        col_offset=84,
                                        end_lineno=16,
                                        end_col_offset=117,
                                        elts=[
                                            Tuple(
                                                lineno=16,
                                                col_offset=85,
                                                end_lineno=16,
                                                end_col_offset=116,
                                                elts=[
                                                    Constant(lineno=16, col_offset=86, end_lineno=16, end_col_offset=99, value='lost_reason', kind=None),
                                                    Constant(lineno=16, col_offset=101, end_lineno=16, end_col_offset=105, value='in', kind=None),
                                                    Attribute(
                                                        lineno=16,
                                                        col_offset=107,
                                                        end_lineno=16,
                                                        end_col_offset=115,
                                                        value=Name(lineno=16, col_offset=107, end_lineno=16, end_col_offset=111, id='self', ctx=Load()),
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
                                        lineno=16,
                                        col_offset=119,
                                        end_lineno=16,
                                        end_col_offset=134,
                                        elts=[Constant(lineno=16, col_offset=120, end_lineno=16, end_col_offset=133, value='lost_reason', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=16,
                                        col_offset=136,
                                        end_lineno=16,
                                        end_col_offset=151,
                                        elts=[Constant(lineno=16, col_offset=137, end_lineno=16, end_col_offset=150, value='lost_reason', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=101,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=19, id='mapped_data', ctx=Store())],
                            value=Call(
                                lineno=17,
                                col_offset=22,
                                end_lineno=17,
                                end_col_offset=101,
                                func=Name(lineno=17, col_offset=22, end_lineno=17, end_col_offset=26, id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        lineno=17,
                                        col_offset=26,
                                        end_lineno=17,
                                        end_col_offset=101,
                                        elt=Tuple(
                                            lineno=17,
                                            col_offset=27,
                                            end_lineno=17,
                                            end_col_offset=78,
                                            elts=[
                                                Subscript(
                                                    lineno=17,
                                                    col_offset=28,
                                                    end_lineno=17,
                                                    end_col_offset=50,
                                                    value=Subscript(
                                                        lineno=17,
                                                        col_offset=28,
                                                        end_lineno=17,
                                                        end_col_offset=47,
                                                        value=Name(lineno=17, col_offset=28, end_lineno=17, end_col_offset=32, id='data', ctx=Load()),
                                                        slice=Constant(lineno=17, col_offset=33, end_lineno=17, end_col_offset=46, value='lost_reason', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(lineno=17, col_offset=48, end_lineno=17, end_col_offset=49, value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    lineno=17,
                                                    col_offset=52,
                                                    end_lineno=17,
                                                    end_col_offset=77,
                                                    value=Name(lineno=17, col_offset=52, end_lineno=17, end_col_offset=56, id='data', ctx=Load()),
                                                    slice=Constant(lineno=17, col_offset=57, end_lineno=17, end_col_offset=76, value='lost_reason_count', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(lineno=17, col_offset=83, end_lineno=17, end_col_offset=87, id='data', ctx=Store()),
                                                iter=Name(lineno=17, col_offset=91, end_lineno=17, end_col_offset=100, id='lead_data', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=18,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=62,
                            target=Name(lineno=18, col_offset=12, end_lineno=18, end_col_offset=18, id='reason', ctx=Store()),
                            iter=Name(lineno=18, col_offset=22, end_lineno=18, end_col_offset=26, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=19,
                                    end_col_offset=62,
                                    targets=[
                                        Attribute(
                                            lineno=19,
                                            col_offset=12,
                                            end_lineno=19,
                                            end_col_offset=30,
                                            value=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=18, id='reason', ctx=Load()),
                                            attr='leads_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=19,
                                        col_offset=33,
                                        end_lineno=19,
                                        end_col_offset=62,
                                        func=Attribute(
                                            lineno=19,
                                            col_offset=33,
                                            end_lineno=19,
                                            end_col_offset=48,
                                            value=Name(lineno=19, col_offset=33, end_lineno=19, end_col_offset=44, id='mapped_data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=19,
                                                col_offset=49,
                                                end_lineno=19,
                                                end_col_offset=58,
                                                value=Name(lineno=19, col_offset=49, end_lineno=19, end_col_offset=55, id='reason', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(lineno=19, col_offset=60, end_lineno=19, end_col_offset=61, value=0, kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=29,
                    end_col_offset=9,
                    name='action_lost_leads',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=21, col_offset=26, end_lineno=21, end_col_offset=30, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=22,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=9,
                            value=Dict(
                                lineno=22,
                                col_offset=15,
                                end_lineno=29,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=23, col_offset=12, end_lineno=23, end_col_offset=18, value='name', kind=None),
                                    Constant(lineno=24, col_offset=12, end_lineno=24, end_col_offset=23, value='view_mode', kind=None),
                                    Constant(lineno=25, col_offset=12, end_lineno=25, end_col_offset=20, value='domain', kind=None),
                                    Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=23, value='res_model', kind=None),
                                    Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=18, value='type', kind=None),
                                    Constant(lineno=28, col_offset=12, end_lineno=28, end_col_offset=21, value='context', kind=None),
                                ],
                                values=[
                                    Call(
                                        lineno=23,
                                        col_offset=20,
                                        end_lineno=23,
                                        end_col_offset=30,
                                        func=Name(lineno=23, col_offset=20, end_lineno=23, end_col_offset=21, id='_', ctx=Load()),
                                        args=[Constant(lineno=23, col_offset=22, end_lineno=23, end_col_offset=29, value='Leads', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(lineno=24, col_offset=25, end_lineno=24, end_col_offset=36, value='tree,form', kind=None),
                                    List(
                                        lineno=25,
                                        col_offset=22,
                                        end_lineno=25,
                                        end_col_offset=55,
                                        elts=[
                                            Tuple(
                                                lineno=25,
                                                col_offset=23,
                                                end_lineno=25,
                                                end_col_offset=54,
                                                elts=[
                                                    Constant(lineno=25, col_offset=24, end_lineno=25, end_col_offset=37, value='lost_reason', kind=None),
                                                    Constant(lineno=25, col_offset=39, end_lineno=25, end_col_offset=43, value='in', kind=None),
                                                    Attribute(
                                                        lineno=25,
                                                        col_offset=45,
                                                        end_lineno=25,
                                                        end_col_offset=53,
                                                        value=Name(lineno=25, col_offset=45, end_lineno=25, end_col_offset=49, id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=26, col_offset=25, end_lineno=26, end_col_offset=35, value='crm.lead', kind=None),
                                    Constant(lineno=27, col_offset=20, end_lineno=27, end_col_offset=43, value='ir.actions.act_window', kind=None),
                                    Dict(
                                        lineno=28,
                                        col_offset=23,
                                        end_lineno=28,
                                        end_col_offset=62,
                                        keys=[
                                            Constant(lineno=28, col_offset=24, end_lineno=28, end_col_offset=32, value='create', kind=None),
                                            Constant(lineno=28, col_offset=41, end_lineno=28, end_col_offset=54, value='active_test', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=28, col_offset=34, end_lineno=28, end_col_offset=39, value=False, kind=None),
                                            Constant(lineno=28, col_offset=56, end_lineno=28, end_col_offset=61, value=False, kind=None),
                                        ],
                                    ),
                                ],
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
