Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=43,
            module='odoo.addons.iap.tools',
            names=[alias(name='iap_tools', asname=None)],
            level=0,
        ),
        Assign(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=45,
            targets=[Name(lineno=7, col_offset=0, end_lineno=7, end_col_offset=16, id='DEFAULT_ENDPOINT', ctx=Store())],
            value=Constant(lineno=7, col_offset=19, end_lineno=7, end_col_offset=45, value='https://iap-sms.odoo.com', kind=None),
            type_comment=None,
        ),
        ClassDef(
            lineno=10,
            col_offset=0,
            end_lineno=76,
            end_col_offset=9,
            name='SmsApi',
            bases=[
                Attribute(
                    lineno=10,
                    col_offset=13,
                    end_lineno=10,
                    end_col_offset=33,
                    value=Name(lineno=10, col_offset=13, end_lineno=10, end_col_offset=19, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=21,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=11, col_offset=12, end_lineno=11, end_col_offset=21, value='sms.api', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=28,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=12, col_offset=19, end_lineno=12, end_col_offset=28, value='SMS API', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=78,
                    name='_contact_iap',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=15, col_offset=21, end_lineno=15, end_col_offset=25, arg='self', annotation=None, type_comment=None),
                            arg(lineno=15, col_offset=27, end_lineno=15, end_col_offset=41, arg='local_endpoint', annotation=None, type_comment=None),
                            arg(lineno=15, col_offset=43, end_lineno=15, end_col_offset=49, arg='params', annotation=None, type_comment=None),
                        ],
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
                            end_col_offset=52,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=15, id='account', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=18,
                                end_lineno=16,
                                end_col_offset=52,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=18,
                                    end_lineno=16,
                                    end_col_offset=45,
                                    value=Subscript(
                                        lineno=16,
                                        col_offset=18,
                                        end_lineno=16,
                                        end_col_offset=41,
                                        value=Attribute(
                                            lineno=16,
                                            col_offset=18,
                                            end_lineno=16,
                                            end_col_offset=26,
                                            value=Name(lineno=16, col_offset=18, end_lineno=16, end_col_offset=22, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=16, col_offset=27, end_lineno=16, end_col_offset=40, value='iap.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=16, col_offset=46, end_lineno=16, end_col_offset=51, value='sms', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=55,
                            targets=[
                                Subscript(
                                    lineno=17,
                                    col_offset=8,
                                    end_lineno=17,
                                    end_col_offset=31,
                                    value=Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=14, id='params', ctx=Load()),
                                    slice=Constant(lineno=17, col_offset=15, end_lineno=17, end_col_offset=30, value='account_token', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                lineno=17,
                                col_offset=34,
                                end_lineno=17,
                                end_col_offset=55,
                                value=Name(lineno=17, col_offset=34, end_lineno=17, end_col_offset=41, id='account', ctx=Load()),
                                attr='account_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=101,
                            targets=[Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=16, id='endpoint', ctx=Store())],
                            value=Call(
                                lineno=18,
                                col_offset=19,
                                end_lineno=18,
                                end_col_offset=101,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=19,
                                    end_lineno=18,
                                    end_col_offset=67,
                                    value=Call(
                                        lineno=18,
                                        col_offset=19,
                                        end_lineno=18,
                                        end_col_offset=57,
                                        func=Attribute(
                                            lineno=18,
                                            col_offset=19,
                                            end_lineno=18,
                                            end_col_offset=55,
                                            value=Subscript(
                                                lineno=18,
                                                col_offset=19,
                                                end_lineno=18,
                                                end_col_offset=50,
                                                value=Attribute(
                                                    lineno=18,
                                                    col_offset=19,
                                                    end_lineno=18,
                                                    end_col_offset=27,
                                                    value=Name(lineno=18, col_offset=19, end_lineno=18, end_col_offset=23, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=18, col_offset=28, end_lineno=18, end_col_offset=49, value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=18, col_offset=68, end_lineno=18, end_col_offset=82, value='sms.endpoint', kind=None),
                                    Name(lineno=18, col_offset=84, end_lineno=18, end_col_offset=100, id='DEFAULT_ENDPOINT', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=78,
                            value=Call(
                                lineno=20,
                                col_offset=15,
                                end_lineno=20,
                                end_col_offset=78,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=15,
                                    end_lineno=20,
                                    end_col_offset=36,
                                    value=Name(lineno=20, col_offset=15, end_lineno=20, end_col_offset=24, id='iap_tools', ctx=Load()),
                                    attr='iap_jsonrpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        lineno=20,
                                        col_offset=37,
                                        end_lineno=20,
                                        end_col_offset=62,
                                        left=Name(lineno=20, col_offset=37, end_lineno=20, end_col_offset=45, id='endpoint', ctx=Load()),
                                        op=Add(),
                                        right=Name(lineno=20, col_offset=48, end_lineno=20, end_col_offset=62, id='local_endpoint', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=20,
                                        col_offset=64,
                                        end_lineno=20,
                                        end_col_offset=77,
                                        arg='params',
                                        value=Name(lineno=20, col_offset=71, end_lineno=20, end_col_offset=77, id='params', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=14,
                            col_offset=5,
                            end_lineno=14,
                            end_col_offset=14,
                            value=Name(lineno=14, col_offset=5, end_lineno=14, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=23,
                    col_offset=4,
                    end_lineno=35,
                    end_col_offset=61,
                    name='_send_sms',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=23, col_offset=18, end_lineno=23, end_col_offset=22, arg='self', annotation=None, type_comment=None),
                            arg(lineno=23, col_offset=24, end_lineno=23, end_col_offset=31, arg='numbers', annotation=None, type_comment=None),
                            arg(lineno=23, col_offset=33, end_lineno=23, end_col_offset=40, arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=24,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=11,
                            value=Constant(lineno=24, col_offset=8, end_lineno=30, end_col_offset=11, value=' Send a single message to several numbers\n\n        :param numbers: list of E164 formatted phone numbers\n        :param message: content to send\n\n        :raises ? TDE FIXME\n        ', kind=None),
                        ),
                        Assign(
                            lineno=31,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=9,
                            targets=[Name(lineno=31, col_offset=8, end_lineno=31, end_col_offset=14, id='params', ctx=Store())],
                            value=Dict(
                                lineno=31,
                                col_offset=17,
                                end_lineno=34,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=32, col_offset=12, end_lineno=32, end_col_offset=21, value='numbers', kind=None),
                                    Constant(lineno=33, col_offset=12, end_lineno=33, end_col_offset=21, value='message', kind=None),
                                ],
                                values=[
                                    Name(lineno=32, col_offset=23, end_lineno=32, end_col_offset=30, id='numbers', ctx=Load()),
                                    Name(lineno=33, col_offset=23, end_lineno=33, end_col_offset=30, id='message', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=35,
                            col_offset=8,
                            end_lineno=35,
                            end_col_offset=61,
                            value=Call(
                                lineno=35,
                                col_offset=15,
                                end_lineno=35,
                                end_col_offset=61,
                                func=Attribute(
                                    lineno=35,
                                    col_offset=15,
                                    end_lineno=35,
                                    end_col_offset=32,
                                    value=Name(lineno=35, col_offset=15, end_lineno=35, end_col_offset=19, id='self', ctx=Load()),
                                    attr='_contact_iap',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=35, col_offset=33, end_lineno=35, end_col_offset=52, value='/iap/message_send', kind=None),
                                    Name(lineno=35, col_offset=54, end_lineno=35, end_col_offset=60, id='params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=22,
                            col_offset=5,
                            end_lineno=22,
                            end_col_offset=14,
                            value=Name(lineno=22, col_offset=5, end_lineno=22, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=38,
                    col_offset=4,
                    end_lineno=58,
                    end_col_offset=59,
                    name='_send_sms_batch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=38, col_offset=24, end_lineno=38, end_col_offset=28, arg='self', annotation=None, type_comment=None),
                            arg(lineno=38, col_offset=30, end_lineno=38, end_col_offset=38, arg='messages', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=39,
                            col_offset=8,
                            end_lineno=54,
                            end_col_offset=11,
                            value=Constant(lineno=39, col_offset=8, end_lineno=54, end_col_offset=11, value=" Send SMS using IAP in batch mode\n\n        :param messages: list of SMS to send, structured as dict [{\n            'res_id':  integer: ID of sms.sms,\n            'number':  string: E164 formatted phone number,\n            'content': string: content to send\n        }]\n\n        :return: return of /iap/sms/1/send controller which is a list of dict [{\n            'res_id': integer: ID of sms.sms,\n            'state':  string: 'insufficient_credit' or 'wrong_number_format' or 'success',\n            'credit': integer: number of credits spent to send this SMS,\n        }]\n\n        :raises: normally none\n        ", kind=None),
                        ),
                        Assign(
                            lineno=55,
                            col_offset=8,
                            end_lineno=57,
                            end_col_offset=9,
                            targets=[Name(lineno=55, col_offset=8, end_lineno=55, end_col_offset=14, id='params', ctx=Store())],
                            value=Dict(
                                lineno=55,
                                col_offset=17,
                                end_lineno=57,
                                end_col_offset=9,
                                keys=[Constant(lineno=56, col_offset=12, end_lineno=56, end_col_offset=22, value='messages', kind=None)],
                                values=[Name(lineno=56, col_offset=24, end_lineno=56, end_col_offset=32, id='messages', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=58,
                            col_offset=8,
                            end_lineno=58,
                            end_col_offset=59,
                            value=Call(
                                lineno=58,
                                col_offset=15,
                                end_lineno=58,
                                end_col_offset=59,
                                func=Attribute(
                                    lineno=58,
                                    col_offset=15,
                                    end_lineno=58,
                                    end_col_offset=32,
                                    value=Name(lineno=58, col_offset=15, end_lineno=58, end_col_offset=19, id='self', ctx=Load()),
                                    attr='_contact_iap',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=58, col_offset=33, end_lineno=58, end_col_offset=50, value='/iap/sms/2/send', kind=None),
                                    Name(lineno=58, col_offset=52, end_lineno=58, end_col_offset=58, id='params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=37,
                            col_offset=5,
                            end_lineno=37,
                            end_col_offset=14,
                            value=Name(lineno=37, col_offset=5, end_lineno=37, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=61,
                    col_offset=4,
                    end_lineno=76,
                    end_col_offset=9,
                    name='_get_sms_api_error_messages',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=61, col_offset=36, end_lineno=61, end_col_offset=40, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=62,
                            col_offset=8,
                            end_lineno=65,
                            end_col_offset=65,
                            value=Constant(lineno=62, col_offset=8, end_lineno=65, end_col_offset=65, value=" Returns a dict containing the error message to display for every known error 'state'\n        resulting from the '_send_sms_batch' method.\n        We prefer a dict instead of a message-per-error-state based method so we only call\n        the 'get_credits_url' once, to avoid extra RPC calls. ", kind=None),
                        ),
                        Assign(
                            lineno=67,
                            col_offset=8,
                            end_lineno=67,
                            end_col_offset=92,
                            targets=[Name(lineno=67, col_offset=8, end_lineno=67, end_col_offset=23, id='buy_credits_url', ctx=Store())],
                            value=Call(
                                lineno=67,
                                col_offset=26,
                                end_lineno=67,
                                end_col_offset=92,
                                func=Attribute(
                                    lineno=67,
                                    col_offset=26,
                                    end_lineno=67,
                                    end_col_offset=72,
                                    value=Subscript(
                                        lineno=67,
                                        col_offset=26,
                                        end_lineno=67,
                                        end_col_offset=56,
                                        value=Attribute(
                                            lineno=67,
                                            col_offset=26,
                                            end_lineno=67,
                                            end_col_offset=41,
                                            value=Call(
                                                lineno=67,
                                                col_offset=26,
                                                end_lineno=67,
                                                end_col_offset=37,
                                                func=Attribute(
                                                    lineno=67,
                                                    col_offset=26,
                                                    end_lineno=67,
                                                    end_col_offset=35,
                                                    value=Name(lineno=67, col_offset=26, end_lineno=67, end_col_offset=30, id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=67, col_offset=42, end_lineno=67, end_col_offset=55, value='iap.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_credits_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=67,
                                        col_offset=73,
                                        end_lineno=67,
                                        end_col_offset=91,
                                        arg='service_name',
                                        value=Constant(lineno=67, col_offset=86, end_lineno=67, end_col_offset=91, value='sms', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=68,
                            col_offset=8,
                            end_lineno=71,
                            end_col_offset=9,
                            targets=[Name(lineno=68, col_offset=8, end_lineno=68, end_col_offset=19, id='buy_credits', ctx=Store())],
                            value=BinOp(
                                lineno=68,
                                col_offset=22,
                                end_lineno=71,
                                end_col_offset=9,
                                left=Constant(lineno=68, col_offset=22, end_lineno=68, end_col_offset=59, value='<a href="%s" target="_blank">%s</a>', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    lineno=68,
                                    col_offset=62,
                                    end_lineno=71,
                                    end_col_offset=9,
                                    elts=[
                                        Name(lineno=69, col_offset=12, end_lineno=69, end_col_offset=27, id='buy_credits_url', ctx=Load()),
                                        Call(
                                            lineno=70,
                                            col_offset=12,
                                            end_lineno=70,
                                            end_col_offset=29,
                                            func=Name(lineno=70, col_offset=12, end_lineno=70, end_col_offset=13, id='_', ctx=Load()),
                                            args=[Constant(lineno=70, col_offset=14, end_lineno=70, end_col_offset=28, value='Buy credits.', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=72,
                            col_offset=8,
                            end_lineno=76,
                            end_col_offset=9,
                            value=Dict(
                                lineno=72,
                                col_offset=15,
                                end_lineno=76,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=73, col_offset=12, end_lineno=73, end_col_offset=26, value='unregistered', kind=None),
                                    Constant(lineno=74, col_offset=12, end_lineno=74, end_col_offset=33, value='insufficient_credit', kind=None),
                                    Constant(lineno=75, col_offset=12, end_lineno=75, end_col_offset=33, value='wrong_number_format', kind=None),
                                ],
                                values=[
                                    Call(
                                        lineno=73,
                                        col_offset=28,
                                        end_lineno=73,
                                        end_col_offset=72,
                                        func=Name(lineno=73, col_offset=28, end_lineno=73, end_col_offset=29, id='_', ctx=Load()),
                                        args=[Constant(lineno=73, col_offset=30, end_lineno=73, end_col_offset=71, value="You don't have an eligible IAP account.", kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        lineno=74,
                                        col_offset=35,
                                        end_lineno=74,
                                        end_col_offset=116,
                                        func=Attribute(
                                            lineno=74,
                                            col_offset=35,
                                            end_lineno=74,
                                            end_col_offset=43,
                                            value=Constant(lineno=74, col_offset=35, end_lineno=74, end_col_offset=38, value=' ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                lineno=74,
                                                col_offset=44,
                                                end_lineno=74,
                                                end_col_offset=115,
                                                elts=[
                                                    Call(
                                                        lineno=74,
                                                        col_offset=45,
                                                        end_lineno=74,
                                                        end_col_offset=101,
                                                        func=Name(lineno=74, col_offset=45, end_lineno=74, end_col_offset=46, id='_', ctx=Load()),
                                                        args=[Constant(lineno=74, col_offset=47, end_lineno=74, end_col_offset=100, value="You don't have enough credits on your IAP account.", kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(lineno=74, col_offset=103, end_lineno=74, end_col_offset=114, id='buy_credits', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        lineno=75,
                                        col_offset=35,
                                        end_lineno=75,
                                        end_col_offset=101,
                                        func=Name(lineno=75, col_offset=35, end_lineno=75, end_col_offset=36, id='_', ctx=Load()),
                                        args=[Constant(lineno=75, col_offset=37, end_lineno=75, end_col_offset=100, value="The number you're trying to reach is not correctly formatted.", kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=60,
                            col_offset=5,
                            end_lineno=60,
                            end_col_offset=14,
                            value=Name(lineno=60, col_offset=5, end_lineno=60, end_col_offset=8, id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
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
