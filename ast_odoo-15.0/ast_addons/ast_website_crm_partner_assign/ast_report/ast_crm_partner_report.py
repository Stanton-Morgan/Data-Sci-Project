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
            end_lineno=58,
            end_col_offset=13,
            name='CrmPartnerReportAssign',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=29,
                    end_lineno=7,
                    end_col_offset=41,
                    value=Name(lineno=7, col_offset=29, end_lineno=7, end_col_offset=35, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=27,
                    value=Constant(lineno=8, col_offset=4, end_lineno=8, end_col_offset=27, value=' CRM Lead Report ', kind=None),
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=39,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=9, col_offset=12, end_lineno=9, end_col_offset=39, value='crm.partner.report.assign', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=17,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=9, id='_auto', ctx=Store())],
                    value=Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=17, value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=45,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=11, col_offset=19, end_lineno=11, end_col_offset=45, value='CRM Partnership Analysis', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=89,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=14, id='partner_id', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=17,
                        end_lineno=13,
                        end_col_offset=89,
                        func=Attribute(
                            lineno=13,
                            col_offset=17,
                            end_lineno=13,
                            end_col_offset=32,
                            value=Name(lineno=13, col_offset=17, end_lineno=13, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=13, col_offset=33, end_lineno=13, end_col_offset=46, value='res.partner', kind=None),
                            Constant(lineno=13, col_offset=48, end_lineno=13, end_col_offset=57, value='Partner', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=59,
                                end_lineno=13,
                                end_col_offset=73,
                                arg='required',
                                value=Constant(lineno=13, col_offset=68, end_lineno=13, end_col_offset=73, value=False, kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=75,
                                end_lineno=13,
                                end_col_offset=88,
                                arg='readonly',
                                value=Constant(lineno=13, col_offset=84, end_lineno=13, end_col_offset=88, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=75,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=12, id='grade_id', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=15,
                        end_lineno=14,
                        end_col_offset=75,
                        func=Attribute(
                            lineno=14,
                            col_offset=15,
                            end_lineno=14,
                            end_col_offset=30,
                            value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=14, col_offset=31, end_lineno=14, end_col_offset=50, value='res.partner.grade', kind=None),
                            Constant(lineno=14, col_offset=52, end_lineno=14, end_col_offset=59, value='Grade', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=61,
                                end_lineno=14,
                                end_col_offset=74,
                                arg='readonly',
                                value=Constant(lineno=14, col_offset=70, end_lineno=14, end_col_offset=74, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=84,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=14, id='activation', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=17,
                        end_lineno=15,
                        end_col_offset=84,
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
                            Constant(lineno=15, col_offset=33, end_lineno=15, end_col_offset=57, value='res.partner.activation', kind=None),
                            Constant(lineno=15, col_offset=59, end_lineno=15, end_col_offset=71, value='Activation', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=73,
                                end_lineno=15,
                                end_col_offset=83,
                                arg='index',
                                value=Constant(lineno=15, col_offset=79, end_lineno=15, end_col_offset=83, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=65,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=11, id='user_id', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=14,
                        end_lineno=16,
                        end_col_offset=65,
                        func=Attribute(
                            lineno=16,
                            col_offset=14,
                            end_lineno=16,
                            end_col_offset=29,
                            value=Name(lineno=16, col_offset=14, end_lineno=16, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=16, col_offset=30, end_lineno=16, end_col_offset=41, value='res.users', kind=None),
                            Constant(lineno=16, col_offset=43, end_lineno=16, end_col_offset=49, value='User', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=51,
                                end_lineno=16,
                                end_col_offset=64,
                                arg='readonly',
                                value=Constant(lineno=16, col_offset=60, end_lineno=16, end_col_offset=64, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=54,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=15, id='date_review', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=18,
                        end_lineno=17,
                        end_col_offset=54,
                        func=Attribute(
                            lineno=17,
                            col_offset=18,
                            end_lineno=17,
                            end_col_offset=29,
                            value=Name(lineno=17, col_offset=18, end_lineno=17, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=30, end_lineno=17, end_col_offset=53, value='Latest Partner Review', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=54,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=20, id='date_partnership', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=23,
                        end_lineno=18,
                        end_col_offset=54,
                        func=Attribute(
                            lineno=18,
                            col_offset=23,
                            end_lineno=18,
                            end_col_offset=34,
                            value=Name(lineno=18, col_offset=23, end_lineno=18, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=18, col_offset=35, end_lineno=18, end_col_offset=53, value='Partnership Date', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=73,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=14, id='country_id', ctx=Store())],
                    value=Call(
                        lineno=19,
                        col_offset=17,
                        end_lineno=19,
                        end_col_offset=73,
                        func=Attribute(
                            lineno=19,
                            col_offset=17,
                            end_lineno=19,
                            end_col_offset=32,
                            value=Name(lineno=19, col_offset=17, end_lineno=19, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=19, col_offset=33, end_lineno=19, end_col_offset=46, value='res.country', kind=None),
                            Constant(lineno=19, col_offset=48, end_lineno=19, end_col_offset=57, value='Country', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=19,
                                col_offset=59,
                                end_lineno=19,
                                end_col_offset=72,
                                arg='readonly',
                                value=Constant(lineno=19, col_offset=68, end_lineno=19, end_col_offset=72, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=20,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=70,
                    targets=[Name(lineno=20, col_offset=4, end_lineno=20, end_col_offset=11, id='team_id', ctx=Store())],
                    value=Call(
                        lineno=20,
                        col_offset=14,
                        end_lineno=20,
                        end_col_offset=70,
                        func=Attribute(
                            lineno=20,
                            col_offset=14,
                            end_lineno=20,
                            end_col_offset=29,
                            value=Name(lineno=20, col_offset=14, end_lineno=20, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=20, col_offset=30, end_lineno=20, end_col_offset=40, value='crm.team', kind=None),
                            Constant(lineno=20, col_offset=42, end_lineno=20, end_col_offset=54, value='Sales Team', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=20,
                                col_offset=56,
                                end_lineno=20,
                                end_col_offset=69,
                                arg='readonly',
                                value=Constant(lineno=20, col_offset=65, end_lineno=20, end_col_offset=69, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=21,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=73,
                    targets=[Name(lineno=21, col_offset=4, end_lineno=21, end_col_offset=21, id='nbr_opportunities', ctx=Store())],
                    value=Call(
                        lineno=21,
                        col_offset=24,
                        end_lineno=21,
                        end_col_offset=73,
                        func=Attribute(
                            lineno=21,
                            col_offset=24,
                            end_lineno=21,
                            end_col_offset=38,
                            value=Name(lineno=21, col_offset=24, end_lineno=21, end_col_offset=30, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=21, col_offset=39, end_lineno=21, end_col_offset=57, value='# of Opportunity', kind=None)],
                        keywords=[
                            keyword(
                                lineno=21,
                                col_offset=59,
                                end_lineno=21,
                                end_col_offset=72,
                                arg='readonly',
                                value=Constant(lineno=21, col_offset=68, end_lineno=21, end_col_offset=72, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=22,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=54,
                    targets=[Name(lineno=22, col_offset=4, end_lineno=22, end_col_offset=12, id='turnover', ctx=Store())],
                    value=Call(
                        lineno=22,
                        col_offset=15,
                        end_lineno=22,
                        end_col_offset=54,
                        func=Attribute(
                            lineno=22,
                            col_offset=15,
                            end_lineno=22,
                            end_col_offset=27,
                            value=Name(lineno=22, col_offset=15, end_lineno=22, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=22, col_offset=28, end_lineno=22, end_col_offset=38, value='Turnover', kind=None)],
                        keywords=[
                            keyword(
                                lineno=22,
                                col_offset=40,
                                end_lineno=22,
                                end_col_offset=53,
                                arg='readonly',
                                value=Constant(lineno=22, col_offset=49, end_lineno=22, end_col_offset=53, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=23,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=61,
                    targets=[Name(lineno=23, col_offset=4, end_lineno=23, end_col_offset=8, id='date', ctx=Store())],
                    value=Call(
                        lineno=23,
                        col_offset=11,
                        end_lineno=23,
                        end_col_offset=61,
                        func=Attribute(
                            lineno=23,
                            col_offset=11,
                            end_lineno=23,
                            end_col_offset=22,
                            value=Name(lineno=23, col_offset=11, end_lineno=23, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=23, col_offset=23, end_lineno=23, end_col_offset=45, value='Invoice Account Date', kind=None)],
                        keywords=[
                            keyword(
                                lineno=23,
                                col_offset=47,
                                end_lineno=23,
                                end_col_offset=60,
                                arg='readonly',
                                value=Constant(lineno=23, col_offset=56, end_lineno=23, end_col_offset=60, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=25,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=5,
                    targets=[Name(lineno=25, col_offset=4, end_lineno=25, end_col_offset=12, id='_depends', ctx=Store())],
                    value=Dict(
                        lineno=25,
                        col_offset=15,
                        end_lineno=30,
                        end_col_offset=5,
                        keys=[
                            Constant(lineno=26, col_offset=8, end_lineno=26, end_col_offset=32, value='account.invoice.report', kind=None),
                            Constant(lineno=27, col_offset=8, end_lineno=27, end_col_offset=18, value='crm.lead', kind=None),
                            Constant(lineno=28, col_offset=8, end_lineno=28, end_col_offset=21, value='res.partner', kind=None),
                        ],
                        values=[
                            List(
                                lineno=26,
                                col_offset=34,
                                end_lineno=26,
                                end_col_offset=104,
                                elts=[
                                    Constant(lineno=26, col_offset=35, end_lineno=26, end_col_offset=49, value='invoice_date', kind=None),
                                    Constant(lineno=26, col_offset=51, end_lineno=26, end_col_offset=63, value='partner_id', kind=None),
                                    Constant(lineno=26, col_offset=65, end_lineno=26, end_col_offset=81, value='price_subtotal', kind=None),
                                    Constant(lineno=26, col_offset=83, end_lineno=26, end_col_offset=90, value='state', kind=None),
                                    Constant(lineno=26, col_offset=92, end_lineno=26, end_col_offset=103, value='move_type', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            List(
                                lineno=27,
                                col_offset=20,
                                end_lineno=27,
                                end_col_offset=43,
                                elts=[Constant(lineno=27, col_offset=21, end_lineno=27, end_col_offset=42, value='partner_assigned_id', kind=None)],
                                ctx=Load(),
                            ),
                            List(
                                lineno=28,
                                col_offset=23,
                                end_lineno=29,
                                end_col_offset=70,
                                elts=[
                                    Constant(lineno=28, col_offset=24, end_lineno=28, end_col_offset=36, value='activation', kind=None),
                                    Constant(lineno=28, col_offset=38, end_lineno=28, end_col_offset=50, value='country_id', kind=None),
                                    Constant(lineno=28, col_offset=52, end_lineno=28, end_col_offset=70, value='date_partnership', kind=None),
                                    Constant(lineno=28, col_offset=72, end_lineno=28, end_col_offset=85, value='date_review', kind=None),
                                    Constant(lineno=29, col_offset=24, end_lineno=29, end_col_offset=34, value='grade_id', kind=None),
                                    Constant(lineno=29, col_offset=36, end_lineno=29, end_col_offset=47, value='parent_id', kind=None),
                                    Constant(lineno=29, col_offset=49, end_lineno=29, end_col_offset=58, value='team_id', kind=None),
                                    Constant(lineno=29, col_offset=60, end_lineno=29, end_col_offset=69, value='user_id', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=33,
                    col_offset=4,
                    end_lineno=58,
                    end_col_offset=13,
                    name='_table_query',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=33, col_offset=21, end_lineno=33, end_col_offset=25, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=34,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=11,
                            value=Constant(lineno=34, col_offset=8, end_lineno=37, end_col_offset=11, value='\n            CRM Lead Report\n            @param cr: the current row, from the database cursor\n        ', kind=None),
                        ),
                        Return(
                            lineno=38,
                            col_offset=8,
                            end_lineno=58,
                            end_col_offset=13,
                            value=Call(
                                lineno=38,
                                col_offset=15,
                                end_lineno=58,
                                end_col_offset=13,
                                func=Attribute(
                                    lineno=38,
                                    col_offset=15,
                                    end_lineno=56,
                                    end_col_offset=22,
                                    value=Constant(lineno=38, col_offset=15, end_lineno=56, end_col_offset=15, value="\n                SELECT\n                    COALESCE(2 * i.id, 2 * p.id + 1) AS id,\n                    p.id as partner_id,\n                    (SELECT country_id FROM res_partner a WHERE a.parent_id=p.id AND country_id is not null limit 1) as country_id,\n                    p.grade_id,\n                    p.activation,\n                    p.date_review,\n                    p.date_partnership,\n                    p.user_id,\n                    p.team_id,\n                    (SELECT count(id) FROM crm_lead WHERE partner_assigned_id=p.id) AS nbr_opportunities,\n                    i.price_subtotal as turnover,\n                    i.invoice_date as date\n                FROM\n                    res_partner p\n                    left join ({account_invoice_report}) i\n                        on (i.partner_id=p.id and i.move_type in ('out_invoice','out_refund') and i.state='open')\n            ", kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=57,
                                        col_offset=16,
                                        end_lineno=57,
                                        end_col_offset=86,
                                        arg='account_invoice_report',
                                        value=Attribute(
                                            lineno=57,
                                            col_offset=39,
                                            end_lineno=57,
                                            end_col_offset=86,
                                            value=Subscript(
                                                lineno=57,
                                                col_offset=39,
                                                end_lineno=57,
                                                end_col_offset=73,
                                                value=Attribute(
                                                    lineno=57,
                                                    col_offset=39,
                                                    end_lineno=57,
                                                    end_col_offset=47,
                                                    value=Name(lineno=57, col_offset=39, end_lineno=57, end_col_offset=43, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=57, col_offset=48, end_lineno=57, end_col_offset=72, value='account.invoice.report', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_table_query',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(lineno=32, col_offset=5, end_lineno=32, end_col_offset=13, id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
