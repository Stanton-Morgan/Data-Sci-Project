Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=73,
            module='odoo.addons.crm.tests.test_crm_lead_merge',
            names=[alias(name='TestLeadMergeCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=65,
            module='odoo.addons.event_crm.tests.common',
            names=[alias(name='TestEventCrmCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=43,
            module='odoo.tests.common',
            names=[
                alias(name='tagged', asname=None),
                alias(name='users', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=10,
            col_offset=0,
            end_lineno=37,
            end_col_offset=72,
            name='TestLeadCrmMerge',
            bases=[
                Name(lineno=10, col_offset=23, end_lineno=10, end_col_offset=42, id='TestLeadMergeCommon', ctx=Load()),
                Name(lineno=10, col_offset=44, end_lineno=10, end_col_offset=62, id='TestEventCrmCommon', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=37,
                    end_col_offset=72,
                    name='test_merge_method_dependencies',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=39, end_lineno=13, end_col_offset=43, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=14,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=11,
                            value=Constant(lineno=14, col_offset=8, end_lineno=22, end_col_offset=11, value=' Test if dependences for leads are not lost while merging leads. In\n        this test leads are ordered as\n\n        lead_w_contact -----------lead---seq=30\n        lead_w_email -------------lead---seq=3\n        lead_1 -------------------lead---seq=1\n        lead_w_partner_company ---lead---seq=1----------------registrations\n        lead_w_partner -----------lead---seq=False\n        ', kind=None),
                        ),
                        Expr(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=67,
                            value=Call(
                                lineno=23,
                                col_offset=8,
                                end_lineno=23,
                                end_col_offset=67,
                                func=Attribute(
                                    lineno=23,
                                    col_offset=8,
                                    end_lineno=23,
                                    end_col_offset=47,
                                    value=Attribute(
                                        lineno=23,
                                        col_offset=8,
                                        end_lineno=23,
                                        end_col_offset=40,
                                        value=Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=27, id='TestLeadMergeCommon', ctx=Load()),
                                        attr='merge_fields',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=23, col_offset=48, end_lineno=23, end_col_offset=66, value='registration_ids', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=10,
                            targets=[Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=20, id='registration', ctx=Store())],
                            value=Call(
                                lineno=25,
                                col_offset=23,
                                end_lineno=29,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=23,
                                    end_lineno=25,
                                    end_col_offset=67,
                                    value=Call(
                                        lineno=25,
                                        col_offset=23,
                                        end_lineno=25,
                                        end_col_offset=60,
                                        func=Attribute(
                                            lineno=25,
                                            col_offset=23,
                                            end_lineno=25,
                                            end_col_offset=58,
                                            value=Subscript(
                                                lineno=25,
                                                col_offset=23,
                                                end_lineno=25,
                                                end_col_offset=53,
                                                value=Attribute(
                                                    lineno=25,
                                                    col_offset=23,
                                                    end_lineno=25,
                                                    end_col_offset=31,
                                                    value=Name(lineno=25, col_offset=23, end_lineno=25, end_col_offset=27, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=25, col_offset=32, end_lineno=25, end_col_offset=52, value='event.registration', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=25,
                                        col_offset=68,
                                        end_lineno=29,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=24, value='partner_id', kind=None),
                                            Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=22, value='event_id', kind=None),
                                            Constant(lineno=28, col_offset=12, end_lineno=28, end_col_offset=22, value='lead_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                lineno=26,
                                                col_offset=26,
                                                end_lineno=26,
                                                end_col_offset=48,
                                                value=Attribute(
                                                    lineno=26,
                                                    col_offset=26,
                                                    end_lineno=26,
                                                    end_col_offset=45,
                                                    value=Name(lineno=26, col_offset=26, end_lineno=26, end_col_offset=30, id='self', ctx=Load()),
                                                    attr='event_customer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=27,
                                                col_offset=24,
                                                end_lineno=27,
                                                end_col_offset=39,
                                                value=Attribute(
                                                    lineno=27,
                                                    col_offset=24,
                                                    end_lineno=27,
                                                    end_col_offset=36,
                                                    value=Name(lineno=27, col_offset=24, end_lineno=27, end_col_offset=28, id='self', ctx=Load()),
                                                    attr='event_0',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                lineno=28,
                                                col_offset=24,
                                                end_lineno=28,
                                                end_col_offset=61,
                                                elts=[
                                                    Tuple(
                                                        lineno=28,
                                                        col_offset=25,
                                                        end_lineno=28,
                                                        end_col_offset=60,
                                                        elts=[
                                                            Constant(lineno=28, col_offset=26, end_lineno=28, end_col_offset=27, value=4, kind=None),
                                                            Attribute(
                                                                lineno=28,
                                                                col_offset=29,
                                                                end_lineno=28,
                                                                end_col_offset=59,
                                                                value=Attribute(
                                                                    lineno=28,
                                                                    col_offset=29,
                                                                    end_lineno=28,
                                                                    end_col_offset=56,
                                                                    value=Name(lineno=28, col_offset=29, end_lineno=28, end_col_offset=33, id='self', ctx=Load()),
                                                                    attr='lead_w_partner_company',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=84,
                            value=Call(
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=84,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=24,
                                    value=Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=30,
                                        col_offset=25,
                                        end_lineno=30,
                                        end_col_offset=69,
                                        value=Attribute(
                                            lineno=30,
                                            col_offset=25,
                                            end_lineno=30,
                                            end_col_offset=52,
                                            value=Name(lineno=30, col_offset=25, end_lineno=30, end_col_offset=29, id='self', ctx=Load()),
                                            attr='lead_w_partner_company',
                                            ctx=Load(),
                                        ),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
                                    Name(lineno=30, col_offset=71, end_lineno=30, end_col_offset=83, id='registration', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=99,
                            targets=[Name(lineno=32, col_offset=8, end_lineno=32, end_col_offset=13, id='leads', ctx=Store())],
                            value=Call(
                                lineno=32,
                                col_offset=16,
                                end_lineno=32,
                                end_col_offset=99,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=16,
                                    end_lineno=32,
                                    end_col_offset=85,
                                    value=Call(
                                        lineno=32,
                                        col_offset=16,
                                        end_lineno=32,
                                        end_col_offset=59,
                                        func=Attribute(
                                            lineno=32,
                                            col_offset=16,
                                            end_lineno=32,
                                            end_col_offset=43,
                                            value=Subscript(
                                                lineno=32,
                                                col_offset=16,
                                                end_lineno=32,
                                                end_col_offset=36,
                                                value=Attribute(
                                                    lineno=32,
                                                    col_offset=16,
                                                    end_lineno=32,
                                                    end_col_offset=24,
                                                    value=Name(lineno=32, col_offset=16, end_lineno=32, end_col_offset=20, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=32, col_offset=25, end_lineno=32, end_col_offset=35, value='crm.lead', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=32,
                                                col_offset=44,
                                                end_lineno=32,
                                                end_col_offset=58,
                                                value=Attribute(
                                                    lineno=32,
                                                    col_offset=44,
                                                    end_lineno=32,
                                                    end_col_offset=54,
                                                    value=Name(lineno=32, col_offset=44, end_lineno=32, end_col_offset=48, id='self', ctx=Load()),
                                                    attr='leads',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_sort_by_confidence_level',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=32,
                                        col_offset=86,
                                        end_lineno=32,
                                        end_col_offset=98,
                                        arg='reverse',
                                        value=Constant(lineno=32, col_offset=94, end_lineno=32, end_col_offset=98, value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            lineno=33,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=72,
                            items=[
                                withitem(
                                    context_expr=Call(
                                        lineno=33,
                                        col_offset=13,
                                        end_lineno=36,
                                        end_col_offset=36,
                                        func=Attribute(
                                            lineno=33,
                                            col_offset=13,
                                            end_lineno=33,
                                            end_col_offset=34,
                                            value=Name(lineno=33, col_offset=13, end_lineno=33, end_col_offset=17, id='self', ctx=Load()),
                                            attr='assertLeadMerged',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=33,
                                                col_offset=35,
                                                end_lineno=33,
                                                end_col_offset=54,
                                                value=Name(lineno=33, col_offset=35, end_lineno=33, end_col_offset=39, id='self', ctx=Load()),
                                                attr='lead_w_contact',
                                                ctx=Load(),
                                            ),
                                            Name(lineno=33, col_offset=56, end_lineno=33, end_col_offset=61, id='leads', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                lineno=34,
                                                col_offset=35,
                                                end_lineno=34,
                                                end_col_offset=64,
                                                arg='name',
                                                value=Attribute(
                                                    lineno=34,
                                                    col_offset=40,
                                                    end_lineno=34,
                                                    end_col_offset=64,
                                                    value=Attribute(
                                                        lineno=34,
                                                        col_offset=40,
                                                        end_lineno=34,
                                                        end_col_offset=59,
                                                        value=Name(lineno=34, col_offset=40, end_lineno=34, end_col_offset=44, id='self', ctx=Load()),
                                                        attr='lead_w_contact',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                lineno=35,
                                                col_offset=35,
                                                end_lineno=35,
                                                end_col_offset=64,
                                                arg='registration_ids',
                                                value=Name(lineno=35, col_offset=52, end_lineno=35, end_col_offset=64, id='registration', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    lineno=37,
                                    col_offset=12,
                                    end_lineno=37,
                                    end_col_offset=72,
                                    value=Call(
                                        lineno=37,
                                        col_offset=12,
                                        end_lineno=37,
                                        end_col_offset=72,
                                        func=Attribute(
                                            lineno=37,
                                            col_offset=12,
                                            end_lineno=37,
                                            end_col_offset=36,
                                            value=Name(lineno=37, col_offset=12, end_lineno=37, end_col_offset=17, id='leads', ctx=Load()),
                                            attr='_merge_opportunity',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                lineno=37,
                                                col_offset=37,
                                                end_lineno=37,
                                                end_col_offset=54,
                                                arg='auto_unlink',
                                                value=Constant(lineno=37, col_offset=49, end_lineno=37, end_col_offset=54, value=False, kind=None),
                                            ),
                                            keyword(
                                                lineno=37,
                                                col_offset=56,
                                                end_lineno=37,
                                                end_col_offset=71,
                                                arg='max_length',
                                                value=Constant(lineno=37, col_offset=67, end_lineno=37, end_col_offset=71, value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=12,
                            col_offset=5,
                            end_lineno=12,
                            end_col_offset=32,
                            func=Name(lineno=12, col_offset=5, end_lineno=12, end_col_offset=10, id='users', ctx=Load()),
                            args=[Constant(lineno=12, col_offset=11, end_lineno=12, end_col_offset=31, value='user_sales_manager', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    lineno=9,
                    col_offset=1,
                    end_lineno=9,
                    end_col_offset=22,
                    func=Name(lineno=9, col_offset=1, end_lineno=9, end_col_offset=7, id='tagged', ctx=Load()),
                    args=[Constant(lineno=9, col_offset=8, end_lineno=9, end_col_offset=21, value='lead_manage', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)