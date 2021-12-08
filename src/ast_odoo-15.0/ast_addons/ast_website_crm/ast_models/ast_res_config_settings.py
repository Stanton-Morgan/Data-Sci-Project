Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
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
            end_lineno=20,
            end_col_offset=86,
            name='ResConfigSettings',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=24,
                    end_lineno=6,
                    end_col_offset=45,
                    value=Name(lineno=6, col_offset=24, end_lineno=6, end_col_offset=30, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=36,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=36, value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=41,
                    name='_get_crm_default_team_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=37, end_lineno=9, end_col_offset=41, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            lineno=10,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=53,
                            test=UnaryOp(
                                lineno=10,
                                col_offset=11,
                                end_lineno=10,
                                end_col_offset=60,
                                op=Not(),
                                operand=Call(
                                    lineno=10,
                                    col_offset=15,
                                    end_lineno=10,
                                    end_col_offset=60,
                                    func=Attribute(
                                        lineno=10,
                                        col_offset=15,
                                        end_lineno=10,
                                        end_col_offset=38,
                                        value=Attribute(
                                            lineno=10,
                                            col_offset=15,
                                            end_lineno=10,
                                            end_col_offset=28,
                                            value=Attribute(
                                                lineno=10,
                                                col_offset=15,
                                                end_lineno=10,
                                                end_col_offset=23,
                                                value=Name(lineno=10, col_offset=15, end_lineno=10, end_col_offset=19, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='has_group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=10, col_offset=39, end_lineno=10, end_col_offset=59, value='crm.group_use_lead', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    lineno=11,
                                    col_offset=12,
                                    end_lineno=11,
                                    end_col_offset=53,
                                    value=List(
                                        lineno=11,
                                        col_offset=19,
                                        end_lineno=11,
                                        end_col_offset=53,
                                        elts=[
                                            Tuple(
                                                lineno=11,
                                                col_offset=20,
                                                end_lineno=11,
                                                end_col_offset=52,
                                                elts=[
                                                    Constant(lineno=11, col_offset=21, end_lineno=11, end_col_offset=40, value='use_opportunities', kind=None),
                                                    Constant(lineno=11, col_offset=42, end_lineno=11, end_col_offset=45, value='=', kind=None),
                                                    Constant(lineno=11, col_offset=47, end_lineno=11, end_col_offset=51, value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=41,
                            value=List(
                                lineno=12,
                                col_offset=15,
                                end_lineno=12,
                                end_col_offset=41,
                                elts=[
                                    Tuple(
                                        lineno=12,
                                        col_offset=16,
                                        end_lineno=12,
                                        end_col_offset=40,
                                        elts=[
                                            Constant(lineno=12, col_offset=17, end_lineno=12, end_col_offset=28, value='use_leads', kind=None),
                                            Constant(lineno=12, col_offset=30, end_lineno=12, end_col_offset=33, value='=', kind=None),
                                            Constant(lineno=12, col_offset=35, end_lineno=12, end_col_offset=39, value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=85,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=23, id='crm_default_team_id', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=26,
                        end_lineno=17,
                        end_col_offset=85,
                        func=Attribute(
                            lineno=14,
                            col_offset=26,
                            end_lineno=14,
                            end_col_offset=41,
                            value=Name(lineno=14, col_offset=26, end_lineno=14, end_col_offset=32, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=15, col_offset=8, end_lineno=15, end_col_offset=18, value='crm.team', kind=None)],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=20,
                                end_lineno=15,
                                end_col_offset=47,
                                arg='string',
                                value=Constant(lineno=15, col_offset=27, end_lineno=15, end_col_offset=47, value='Default Sales Team', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=49,
                                end_lineno=15,
                                end_col_offset=89,
                                arg='related',
                                value=Constant(lineno=15, col_offset=57, end_lineno=15, end_col_offset=89, value='website_id.crm_default_team_id', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=91,
                                end_lineno=15,
                                end_col_offset=105,
                                arg='readonly',
                                value=Constant(lineno=15, col_offset=100, end_lineno=15, end_col_offset=105, value=False, kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=8,
                                end_lineno=16,
                                end_col_offset=63,
                                arg='domain',
                                value=Lambda(
                                    lineno=16,
                                    col_offset=15,
                                    end_lineno=16,
                                    end_col_offset=63,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=16, col_offset=22, end_lineno=16, end_col_offset=26, arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        lineno=16,
                                        col_offset=28,
                                        end_lineno=16,
                                        end_col_offset=63,
                                        func=Attribute(
                                            lineno=16,
                                            col_offset=28,
                                            end_lineno=16,
                                            end_col_offset=61,
                                            value=Name(lineno=16, col_offset=28, end_lineno=16, end_col_offset=32, id='self', ctx=Load()),
                                            attr='_get_crm_default_team_domain',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                lineno=17,
                                col_offset=8,
                                end_lineno=17,
                                end_col_offset=84,
                                arg='help',
                                value=Constant(lineno=17, col_offset=13, end_lineno=17, end_col_offset=84, value='Default Sales Team for new leads created through the Contact Us form.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=86,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=23, id='crm_default_user_id', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=26,
                        end_lineno=20,
                        end_col_offset=86,
                        func=Attribute(
                            lineno=18,
                            col_offset=26,
                            end_lineno=18,
                            end_col_offset=41,
                            value=Name(lineno=18, col_offset=26, end_lineno=18, end_col_offset=32, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=19, col_offset=8, end_lineno=19, end_col_offset=19, value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                lineno=19,
                                col_offset=21,
                                end_lineno=19,
                                end_col_offset=49,
                                arg='string',
                                value=Constant(lineno=19, col_offset=28, end_lineno=19, end_col_offset=49, value='Default Salesperson', kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=51,
                                end_lineno=19,
                                end_col_offset=91,
                                arg='related',
                                value=Constant(lineno=19, col_offset=59, end_lineno=19, end_col_offset=91, value='website_id.crm_default_user_id', kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=93,
                                end_lineno=19,
                                end_col_offset=123,
                                arg='domain',
                                value=List(
                                    lineno=19,
                                    col_offset=100,
                                    end_lineno=19,
                                    end_col_offset=123,
                                    elts=[
                                        Tuple(
                                            lineno=19,
                                            col_offset=101,
                                            end_lineno=19,
                                            end_col_offset=122,
                                            elts=[
                                                Constant(lineno=19, col_offset=102, end_lineno=19, end_col_offset=109, value='share', kind=None),
                                                Constant(lineno=19, col_offset=111, end_lineno=19, end_col_offset=114, value='=', kind=None),
                                                Constant(lineno=19, col_offset=116, end_lineno=19, end_col_offset=121, value=False, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=125,
                                end_lineno=19,
                                end_col_offset=139,
                                arg='readonly',
                                value=Constant(lineno=19, col_offset=134, end_lineno=19, end_col_offset=139, value=False, kind=None),
                            ),
                            keyword(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=85,
                                arg='help',
                                value=Constant(lineno=20, col_offset=13, end_lineno=20, end_col_offset=85, value='Default salesperson for new leads created through the Contact Us form.', kind=None),
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