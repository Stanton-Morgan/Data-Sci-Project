Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=26,
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=44,
            end_col_offset=9,
            name='Users',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=12,
                    end_lineno=7,
                    end_col_offset=24,
                    value=Name(lineno=7, col_offset=12, end_lineno=7, end_col_offset=18, id='models', ctx=Load()),
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
                    end_col_offset=26,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=26, value='res.users', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=21,
                    name='action_open_my_account_settings',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=40, end_lineno=10, end_col_offset=44, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=9,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=14, id='action', ctx=Store())],
                            value=Dict(
                                lineno=11,
                                col_offset=17,
                                end_lineno=17,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=12, col_offset=12, end_lineno=12, end_col_offset=18, value='name', kind=None),
                                    Constant(lineno=13, col_offset=12, end_lineno=13, end_col_offset=18, value='type', kind=None),
                                    Constant(lineno=14, col_offset=12, end_lineno=14, end_col_offset=23, value='res_model', kind=None),
                                    Constant(lineno=15, col_offset=12, end_lineno=15, end_col_offset=19, value='views', kind=None),
                                    Constant(lineno=16, col_offset=12, end_lineno=16, end_col_offset=20, value='res_id', kind=None),
                                ],
                                values=[
                                    Call(
                                        lineno=12,
                                        col_offset=20,
                                        end_lineno=12,
                                        end_col_offset=41,
                                        func=Name(lineno=12, col_offset=20, end_lineno=12, end_col_offset=21, id='_', ctx=Load()),
                                        args=[Constant(lineno=12, col_offset=22, end_lineno=12, end_col_offset=40, value='Account Security', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(lineno=13, col_offset=20, end_lineno=13, end_col_offset=43, value='ir.actions.act_window', kind=None),
                                    Constant(lineno=14, col_offset=25, end_lineno=14, end_col_offset=36, value='res.users', kind=None),
                                    List(
                                        lineno=15,
                                        col_offset=21,
                                        end_lineno=15,
                                        end_col_offset=86,
                                        elts=[
                                            List(
                                                lineno=15,
                                                col_offset=22,
                                                end_lineno=15,
                                                end_col_offset=85,
                                                elts=[
                                                    Attribute(
                                                        lineno=15,
                                                        col_offset=23,
                                                        end_lineno=15,
                                                        end_col_offset=76,
                                                        value=Call(
                                                            lineno=15,
                                                            col_offset=23,
                                                            end_lineno=15,
                                                            end_col_offset=73,
                                                            func=Attribute(
                                                                lineno=15,
                                                                col_offset=23,
                                                                end_lineno=15,
                                                                end_col_offset=35,
                                                                value=Attribute(
                                                                    lineno=15,
                                                                    col_offset=23,
                                                                    end_lineno=15,
                                                                    end_col_offset=31,
                                                                    value=Name(lineno=15, col_offset=23, end_lineno=15, end_col_offset=27, id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(lineno=15, col_offset=36, end_lineno=15, end_col_offset=72, value='auth_totp_mail.res_users_view_form', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=15, col_offset=78, end_lineno=15, end_col_offset=84, value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=16,
                                        col_offset=22,
                                        end_lineno=16,
                                        end_col_offset=29,
                                        value=Name(lineno=16, col_offset=22, end_lineno=16, end_col_offset=26, id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=21,
                            value=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=21, id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=20,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=85,
                    name='get_totp_invite_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=20, col_offset=28, end_lineno=20, end_col_offset=32, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=85,
                            value=Constant(lineno=21, col_offset=15, end_lineno=21, end_col_offset=85, value='/web#action=auth_totp_mail.action_activate_two_factor_authentication', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=23,
                    col_offset=4,
                    end_lineno=44,
                    end_col_offset=9,
                    name='action_totp_invite',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=23, col_offset=27, end_lineno=23, end_col_offset=31, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=82,
                            targets=[Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=23, id='invite_template', ctx=Store())],
                            value=Call(
                                lineno=24,
                                col_offset=26,
                                end_lineno=24,
                                end_col_offset=82,
                                func=Attribute(
                                    lineno=24,
                                    col_offset=26,
                                    end_lineno=24,
                                    end_col_offset=38,
                                    value=Attribute(
                                        lineno=24,
                                        col_offset=26,
                                        end_lineno=24,
                                        end_col_offset=34,
                                        value=Name(lineno=24, col_offset=26, end_lineno=24, end_col_offset=30, id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=24, col_offset=39, end_lineno=24, end_col_offset=81, value='auth_totp_mail.mail_template_totp_invite', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=81,
                            targets=[Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=23, id='users_to_invite', ctx=Store())],
                            value=Call(
                                lineno=25,
                                col_offset=26,
                                end_lineno=25,
                                end_col_offset=81,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=26,
                                    end_lineno=25,
                                    end_col_offset=46,
                                    value=Call(
                                        lineno=25,
                                        col_offset=26,
                                        end_lineno=25,
                                        end_col_offset=37,
                                        func=Attribute(
                                            lineno=25,
                                            col_offset=26,
                                            end_lineno=25,
                                            end_col_offset=35,
                                            value=Name(lineno=25, col_offset=26, end_lineno=25, end_col_offset=30, id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        lineno=25,
                                        col_offset=47,
                                        end_lineno=25,
                                        end_col_offset=80,
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(lineno=25, col_offset=54, end_lineno=25, end_col_offset=58, arg='user', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            lineno=25,
                                            col_offset=60,
                                            end_lineno=25,
                                            end_col_offset=80,
                                            op=Not(),
                                            operand=Attribute(
                                                lineno=25,
                                                col_offset=64,
                                                end_lineno=25,
                                                end_col_offset=80,
                                                value=Name(lineno=25, col_offset=64, end_lineno=25, end_col_offset=68, id='user', ctx=Load()),
                                                attr='totp_secret',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=26,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=82,
                            target=Name(lineno=26, col_offset=12, end_lineno=26, end_col_offset=16, id='user', ctx=Store()),
                            iter=Name(lineno=26, col_offset=20, end_lineno=26, end_col_offset=35, id='users_to_invite', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=27,
                                    col_offset=12,
                                    end_lineno=30,
                                    end_col_offset=13,
                                    targets=[Name(lineno=27, col_offset=12, end_lineno=27, end_col_offset=24, id='email_values', ctx=Store())],
                                    value=Dict(
                                        lineno=27,
                                        col_offset=27,
                                        end_lineno=30,
                                        end_col_offset=13,
                                        keys=[
                                            Constant(lineno=28, col_offset=16, end_lineno=28, end_col_offset=28, value='email_from', kind=None),
                                            Constant(lineno=29, col_offset=16, end_lineno=29, end_col_offset=27, value='author_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                lineno=28,
                                                col_offset=30,
                                                end_lineno=28,
                                                end_col_offset=59,
                                                value=Attribute(
                                                    lineno=28,
                                                    col_offset=30,
                                                    end_lineno=28,
                                                    end_col_offset=43,
                                                    value=Attribute(
                                                        lineno=28,
                                                        col_offset=30,
                                                        end_lineno=28,
                                                        end_col_offset=38,
                                                        value=Name(lineno=28, col_offset=30, end_lineno=28, end_col_offset=34, id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='email_formatted',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=29,
                                                col_offset=29,
                                                end_lineno=29,
                                                end_col_offset=56,
                                                value=Attribute(
                                                    lineno=29,
                                                    col_offset=29,
                                                    end_lineno=29,
                                                    end_col_offset=53,
                                                    value=Attribute(
                                                        lineno=29,
                                                        col_offset=29,
                                                        end_lineno=29,
                                                        end_col_offset=42,
                                                        value=Attribute(
                                                            lineno=29,
                                                            col_offset=29,
                                                            end_lineno=29,
                                                            end_col_offset=37,
                                                            value=Name(lineno=29, col_offset=29, end_lineno=29, end_col_offset=33, id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    lineno=31,
                                    col_offset=12,
                                    end_lineno=32,
                                    end_col_offset=82,
                                    value=Call(
                                        lineno=31,
                                        col_offset=12,
                                        end_lineno=32,
                                        end_col_offset=82,
                                        func=Attribute(
                                            lineno=31,
                                            col_offset=12,
                                            end_lineno=31,
                                            end_col_offset=37,
                                            value=Name(lineno=31, col_offset=12, end_lineno=31, end_col_offset=27, id='invite_template', ctx=Load()),
                                            attr='send_mail',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=31,
                                                col_offset=38,
                                                end_lineno=31,
                                                end_col_offset=45,
                                                value=Name(lineno=31, col_offset=38, end_lineno=31, end_col_offset=42, id='user', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                lineno=31,
                                                col_offset=47,
                                                end_lineno=31,
                                                end_col_offset=62,
                                                arg='force_send',
                                                value=Constant(lineno=31, col_offset=58, end_lineno=31, end_col_offset=62, value=True, kind=None),
                                            ),
                                            keyword(
                                                lineno=31,
                                                col_offset=64,
                                                end_lineno=31,
                                                end_col_offset=89,
                                                arg='email_values',
                                                value=Name(lineno=31, col_offset=77, end_lineno=31, end_col_offset=89, id='email_values', ctx=Load()),
                                            ),
                                            keyword(
                                                lineno=32,
                                                col_offset=38,
                                                end_lineno=32,
                                                end_col_offset=81,
                                                arg='notif_layout',
                                                value=Constant(lineno=32, col_offset=51, end_lineno=32, end_col_offset=81, value='mail.mail_notification_light', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=35,
                            col_offset=8,
                            end_lineno=44,
                            end_col_offset=9,
                            value=Dict(
                                lineno=35,
                                col_offset=15,
                                end_lineno=44,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=36, col_offset=12, end_lineno=36, end_col_offset=18, value='type', kind=None),
                                    Constant(lineno=37, col_offset=12, end_lineno=37, end_col_offset=17, value='tag', kind=None),
                                    Constant(lineno=38, col_offset=12, end_lineno=38, end_col_offset=20, value='params', kind=None),
                                ],
                                values=[
                                    Constant(lineno=36, col_offset=20, end_lineno=36, end_col_offset=39, value='ir.actions.client', kind=None),
                                    Constant(lineno=37, col_offset=19, end_lineno=37, end_col_offset=41, value='display_notification', kind=None),
                                    Dict(
                                        lineno=38,
                                        col_offset=22,
                                        end_lineno=43,
                                        end_col_offset=13,
                                        keys=[
                                            Constant(lineno=39, col_offset=16, end_lineno=39, end_col_offset=22, value='type', kind=None),
                                            Constant(lineno=40, col_offset=16, end_lineno=40, end_col_offset=24, value='sticky', kind=None),
                                            Constant(lineno=41, col_offset=16, end_lineno=41, end_col_offset=25, value='message', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=39, col_offset=24, end_lineno=39, end_col_offset=30, value='info', kind=None),
                                            Constant(lineno=40, col_offset=26, end_lineno=40, end_col_offset=31, value=False, kind=None),
                                            Call(
                                                lineno=41,
                                                col_offset=27,
                                                end_lineno=42,
                                                end_col_offset=71,
                                                func=Name(lineno=41, col_offset=27, end_lineno=41, end_col_offset=28, id='_', ctx=Load()),
                                                args=[
                                                    Constant(lineno=41, col_offset=29, end_lineno=41, end_col_offset=109, value='Invitation to use two-factor authentication sent for the following user(s): %s', kind=None),
                                                    Call(
                                                        lineno=42,
                                                        col_offset=29,
                                                        end_lineno=42,
                                                        end_col_offset=70,
                                                        func=Attribute(
                                                            lineno=42,
                                                            col_offset=29,
                                                            end_lineno=42,
                                                            end_col_offset=38,
                                                            value=Constant(lineno=42, col_offset=29, end_lineno=42, end_col_offset=33, value=', ', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                lineno=42,
                                                                col_offset=39,
                                                                end_lineno=42,
                                                                end_col_offset=69,
                                                                func=Attribute(
                                                                    lineno=42,
                                                                    col_offset=39,
                                                                    end_lineno=42,
                                                                    end_col_offset=61,
                                                                    value=Name(lineno=42, col_offset=39, end_lineno=42, end_col_offset=54, id='users_to_invite', ctx=Load()),
                                                                    attr='mapped',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(lineno=42, col_offset=62, end_lineno=42, end_col_offset=68, value='name', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
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