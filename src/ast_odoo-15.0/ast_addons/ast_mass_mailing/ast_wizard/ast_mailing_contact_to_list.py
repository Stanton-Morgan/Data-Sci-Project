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
            lineno=6,
            col_offset=0,
            end_lineno=52,
            end_col_offset=9,
            name='MailingContactToList',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=27,
                    end_lineno=6,
                    end_col_offset=48,
                    value=Name(lineno=6, col_offset=27, end_lineno=6, end_col_offset=33, id='models', ctx=Load()),
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
                    end_col_offset=37,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=7, col_offset=12, end_lineno=7, end_col_offset=37, value='mailing.contact.to.list', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=49,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=8, col_offset=19, end_lineno=8, end_col_offset=49, value='Add Contacts to Mailing List', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=72,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=15, id='contact_ids', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=18,
                        end_lineno=10,
                        end_col_offset=72,
                        func=Attribute(
                            lineno=10,
                            col_offset=18,
                            end_lineno=10,
                            end_col_offset=34,
                            value=Name(lineno=10, col_offset=18, end_lineno=10, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=35, end_lineno=10, end_col_offset=52, value='mailing.contact', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=54,
                                end_lineno=10,
                                end_col_offset=71,
                                arg='string',
                                value=Constant(lineno=10, col_offset=61, end_lineno=10, end_col_offset=71, value='Contacts', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=91,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=19, id='mailing_list_id', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=22,
                        end_lineno=11,
                        end_col_offset=91,
                        func=Attribute(
                            lineno=11,
                            col_offset=22,
                            end_lineno=11,
                            end_col_offset=37,
                            value=Name(lineno=11, col_offset=22, end_lineno=11, end_col_offset=28, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=38, end_lineno=11, end_col_offset=52, value='mailing.list', kind=None)],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=54,
                                end_lineno=11,
                                end_col_offset=75,
                                arg='string',
                                value=Constant(lineno=11, col_offset=61, end_lineno=11, end_col_offset=75, value='Mailing List', kind=None),
                            ),
                            keyword(
                                lineno=11,
                                col_offset=77,
                                end_lineno=11,
                                end_col_offset=90,
                                arg='required',
                                value=Constant(lineno=11, col_offset=86, end_lineno=11, end_col_offset=90, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=90,
                    name='action_add_contacts',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=28, end_lineno=13, end_col_offset=32, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=14,
                            end_col_offset=73,
                            value=Constant(lineno=14, col_offset=8, end_lineno=14, end_col_offset=73, value=' Simply add contacts to the mailing list and close wizard. ', kind=None),
                        ),
                        Return(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=90,
                            value=Call(
                                lineno=15,
                                col_offset=15,
                                end_lineno=15,
                                end_col_offset=90,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=15,
                                    end_lineno=15,
                                    end_col_offset=49,
                                    value=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=19, id='self', ctx=Load()),
                                    attr='_add_contacts_to_mailing_list',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=15,
                                        col_offset=50,
                                        end_lineno=15,
                                        end_col_offset=89,
                                        keys=[Constant(lineno=15, col_offset=51, end_lineno=15, end_col_offset=57, value='type', kind=None)],
                                        values=[Constant(lineno=15, col_offset=59, end_lineno=15, end_col_offset=88, value='ir.actions.act_window_close', kind=None)],
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
                FunctionDef(
                    lineno=17,
                    col_offset=4,
                    end_lineno=28,
                    end_col_offset=57,
                    name='action_add_contacts_and_send_mailing',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=17, col_offset=45, end_lineno=17, end_col_offset=49, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=18,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=22,
                            value=Constant(lineno=18, col_offset=8, end_lineno=19, end_col_offset=22, value=' Add contacts to the mailing list and redirect to a new mailing on\n        this list. ', kind=None),
                        ),
                        Expr(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=25,
                            value=Call(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=23,
                                    value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=103,
                            targets=[Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=14, id='action', ctx=Store())],
                            value=Call(
                                lineno=22,
                                col_offset=17,
                                end_lineno=22,
                                end_col_offset=103,
                                func=Attribute(
                                    lineno=22,
                                    col_offset=17,
                                    end_lineno=22,
                                    end_col_offset=59,
                                    value=Subscript(
                                        lineno=22,
                                        col_offset=17,
                                        end_lineno=22,
                                        end_col_offset=47,
                                        value=Attribute(
                                            lineno=22,
                                            col_offset=17,
                                            end_lineno=22,
                                            end_col_offset=25,
                                            value=Name(lineno=22, col_offset=17, end_lineno=22, end_col_offset=21, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=22, col_offset=26, end_lineno=22, end_col_offset=46, value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=22, col_offset=60, end_lineno=22, end_col_offset=102, value='mass_mailing.mailing_mailing_action_mail', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=43,
                            targets=[
                                Subscript(
                                    lineno=23,
                                    col_offset=8,
                                    end_lineno=23,
                                    end_col_offset=23,
                                    value=Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=14, id='action', ctx=Load()),
                                    slice=Constant(lineno=23, col_offset=15, end_lineno=23, end_col_offset=22, value='views', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                lineno=23,
                                col_offset=26,
                                end_lineno=23,
                                end_col_offset=43,
                                elts=[
                                    List(
                                        lineno=23,
                                        col_offset=27,
                                        end_lineno=23,
                                        end_col_offset=42,
                                        elts=[
                                            Constant(lineno=23, col_offset=28, end_lineno=23, end_col_offset=33, value=False, kind=None),
                                            Constant(lineno=23, col_offset=35, end_lineno=23, end_col_offset=41, value='form', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=36,
                            targets=[
                                Subscript(
                                    lineno=24,
                                    col_offset=8,
                                    end_lineno=24,
                                    end_col_offset=24,
                                    value=Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=14, id='action', ctx=Load()),
                                    slice=Constant(lineno=24, col_offset=15, end_lineno=24, end_col_offset=23, value='target', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(lineno=24, col_offset=27, end_lineno=24, end_col_offset=36, value='current', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=9,
                            targets=[
                                Subscript(
                                    lineno=25,
                                    col_offset=8,
                                    end_lineno=25,
                                    end_col_offset=25,
                                    value=Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=14, id='action', ctx=Load()),
                                    slice=Constant(lineno=25, col_offset=15, end_lineno=25, end_col_offset=24, value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                lineno=25,
                                col_offset=28,
                                end_lineno=27,
                                end_col_offset=9,
                                keys=[Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=38, value='default_contact_list_ids', kind=None)],
                                values=[
                                    List(
                                        lineno=26,
                                        col_offset=40,
                                        end_lineno=26,
                                        end_col_offset=65,
                                        elts=[
                                            Attribute(
                                                lineno=26,
                                                col_offset=41,
                                                end_lineno=26,
                                                end_col_offset=64,
                                                value=Attribute(
                                                    lineno=26,
                                                    col_offset=41,
                                                    end_lineno=26,
                                                    end_col_offset=61,
                                                    value=Name(lineno=26, col_offset=41, end_lineno=26, end_col_offset=45, id='self', ctx=Load()),
                                                    attr='mailing_list_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=28,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=57,
                            value=Call(
                                lineno=28,
                                col_offset=15,
                                end_lineno=28,
                                end_col_offset=57,
                                func=Attribute(
                                    lineno=28,
                                    col_offset=15,
                                    end_lineno=28,
                                    end_col_offset=49,
                                    value=Name(lineno=28, col_offset=15, end_lineno=28, end_col_offset=19, id='self', ctx=Load()),
                                    attr='_add_contacts_to_mailing_list',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=28, col_offset=50, end_lineno=28, end_col_offset=56, id='action', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=30,
                    col_offset=4,
                    end_lineno=52,
                    end_col_offset=9,
                    name='_add_contacts_to_mailing_list',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=30, col_offset=38, end_lineno=30, end_col_offset=42, arg='self', annotation=None, type_comment=None),
                            arg(lineno=30, col_offset=44, end_lineno=30, end_col_offset=50, arg='action', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=25,
                            value=Call(
                                lineno=31,
                                col_offset=8,
                                end_lineno=31,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=8,
                                    end_lineno=31,
                                    end_col_offset=23,
                                    value=Name(lineno=31, col_offset=8, end_lineno=31, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=33,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=62,
                            targets=[Name(lineno=33, col_offset=8, end_lineno=33, end_col_offset=22, id='previous_count', ctx=Store())],
                            value=Call(
                                lineno=33,
                                col_offset=25,
                                end_lineno=33,
                                end_col_offset=62,
                                func=Name(lineno=33, col_offset=25, end_lineno=33, end_col_offset=28, id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        lineno=33,
                                        col_offset=29,
                                        end_lineno=33,
                                        end_col_offset=61,
                                        value=Attribute(
                                            lineno=33,
                                            col_offset=29,
                                            end_lineno=33,
                                            end_col_offset=49,
                                            value=Name(lineno=33, col_offset=29, end_lineno=33, end_col_offset=33, id='self', ctx=Load()),
                                            attr='mailing_list_id',
                                            ctx=Load(),
                                        ),
                                        attr='contact_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=34,
                            col_offset=8,
                            end_lineno=39,
                            end_col_offset=14,
                            value=Call(
                                lineno=34,
                                col_offset=8,
                                end_lineno=39,
                                end_col_offset=14,
                                func=Attribute(
                                    lineno=34,
                                    col_offset=8,
                                    end_lineno=34,
                                    end_col_offset=34,
                                    value=Attribute(
                                        lineno=34,
                                        col_offset=8,
                                        end_lineno=34,
                                        end_col_offset=28,
                                        value=Name(lineno=34, col_offset=8, end_lineno=34, end_col_offset=12, id='self', ctx=Load()),
                                        attr='mailing_list_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=34,
                                        col_offset=35,
                                        end_lineno=39,
                                        end_col_offset=13,
                                        keys=[Constant(lineno=35, col_offset=12, end_lineno=35, end_col_offset=25, value='contact_ids', kind=None)],
                                        values=[
                                            ListComp(
                                                lineno=35,
                                                col_offset=27,
                                                end_lineno=38,
                                                end_col_offset=67,
                                                elt=Tuple(
                                                    lineno=36,
                                                    col_offset=16,
                                                    end_lineno=36,
                                                    end_col_offset=31,
                                                    elts=[
                                                        Constant(lineno=36, col_offset=17, end_lineno=36, end_col_offset=18, value=4, kind=None),
                                                        Attribute(
                                                            lineno=36,
                                                            col_offset=20,
                                                            end_lineno=36,
                                                            end_col_offset=30,
                                                            value=Name(lineno=36, col_offset=20, end_lineno=36, end_col_offset=27, id='contact', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(lineno=37, col_offset=20, end_lineno=37, end_col_offset=27, id='contact', ctx=Store()),
                                                        iter=Attribute(
                                                            lineno=37,
                                                            col_offset=31,
                                                            end_lineno=37,
                                                            end_col_offset=47,
                                                            value=Name(lineno=37, col_offset=31, end_lineno=37, end_col_offset=35, id='self', ctx=Load()),
                                                            attr='contact_ids',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                lineno=38,
                                                                col_offset=19,
                                                                end_lineno=38,
                                                                end_col_offset=66,
                                                                left=Name(lineno=38, col_offset=19, end_lineno=38, end_col_offset=26, id='contact', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Attribute(
                                                                        lineno=38,
                                                                        col_offset=34,
                                                                        end_lineno=38,
                                                                        end_col_offset=66,
                                                                        value=Attribute(
                                                                            lineno=38,
                                                                            col_offset=34,
                                                                            end_lineno=38,
                                                                            end_col_offset=54,
                                                                            value=Name(lineno=38, col_offset=34, end_lineno=38, end_col_offset=38, id='self', ctx=Load()),
                                                                            attr='mailing_list_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='contact_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=41,
                            col_offset=8,
                            end_lineno=52,
                            end_col_offset=9,
                            value=Dict(
                                lineno=41,
                                col_offset=15,
                                end_lineno=52,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=42, col_offset=12, end_lineno=42, end_col_offset=18, value='type', kind=None),
                                    Constant(lineno=43, col_offset=12, end_lineno=43, end_col_offset=17, value='tag', kind=None),
                                    Constant(lineno=44, col_offset=12, end_lineno=44, end_col_offset=20, value='params', kind=None),
                                ],
                                values=[
                                    Constant(lineno=42, col_offset=20, end_lineno=42, end_col_offset=39, value='ir.actions.client', kind=None),
                                    Constant(lineno=43, col_offset=19, end_lineno=43, end_col_offset=41, value='display_notification', kind=None),
                                    Dict(
                                        lineno=44,
                                        col_offset=22,
                                        end_lineno=51,
                                        end_col_offset=13,
                                        keys=[
                                            Constant(lineno=45, col_offset=16, end_lineno=45, end_col_offset=22, value='type', kind=None),
                                            Constant(lineno=46, col_offset=16, end_lineno=46, end_col_offset=25, value='message', kind=None),
                                            Constant(lineno=49, col_offset=16, end_lineno=49, end_col_offset=24, value='sticky', kind=None),
                                            Constant(lineno=50, col_offset=16, end_lineno=50, end_col_offset=22, value='next', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=45, col_offset=24, end_lineno=45, end_col_offset=30, value='info', kind=None),
                                            Call(
                                                lineno=46,
                                                col_offset=27,
                                                end_lineno=48,
                                                end_col_offset=29,
                                                func=Name(lineno=46, col_offset=27, end_lineno=46, end_col_offset=28, id='_', ctx=Load()),
                                                args=[
                                                    Constant(lineno=46, col_offset=29, end_lineno=46, end_col_offset=68, value='%s Mailing Contacts have been added. ', kind=None),
                                                    BinOp(
                                                        lineno=47,
                                                        col_offset=29,
                                                        end_lineno=47,
                                                        end_col_offset=83,
                                                        left=Call(
                                                            lineno=47,
                                                            col_offset=29,
                                                            end_lineno=47,
                                                            end_col_offset=66,
                                                            func=Name(lineno=47, col_offset=29, end_lineno=47, end_col_offset=32, id='len', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    lineno=47,
                                                                    col_offset=33,
                                                                    end_lineno=47,
                                                                    end_col_offset=65,
                                                                    value=Attribute(
                                                                        lineno=47,
                                                                        col_offset=33,
                                                                        end_lineno=47,
                                                                        end_col_offset=53,
                                                                        value=Name(lineno=47, col_offset=33, end_lineno=47, end_col_offset=37, id='self', ctx=Load()),
                                                                        attr='mailing_list_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='contact_ids',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Name(lineno=47, col_offset=69, end_lineno=47, end_col_offset=83, id='previous_count', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(lineno=49, col_offset=26, end_lineno=49, end_col_offset=31, value=False, kind=None),
                                            Name(lineno=50, col_offset=24, end_lineno=50, end_col_offset=30, id='action', ctx=Load()),
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