Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=42,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=31,
            end_col_offset=21,
            name='AccountMove',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=18,
                    end_lineno=6,
                    end_col_offset=30,
                    value=Name(lineno=6, col_offset=18, end_lineno=6, end_col_offset=24, id='models', ctx=Load()),
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
                    end_col_offset=29,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=29, value='account.move', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=9,
                    col_offset=4,
                    end_lineno=25,
                    end_col_offset=19,
                    name='invoice_validate_send_email',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=9, col_offset=36, end_lineno=9, end_col_offset=40, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=12,
                            end_col_offset=47,
                            test=Attribute(
                                lineno=10,
                                col_offset=11,
                                end_lineno=10,
                                end_col_offset=22,
                                value=Attribute(
                                    lineno=10,
                                    col_offset=11,
                                    end_lineno=10,
                                    end_col_offset=19,
                                    value=Name(lineno=10, col_offset=11, end_lineno=10, end_col_offset=15, id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='su',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    lineno=12,
                                    col_offset=12,
                                    end_lineno=12,
                                    end_col_offset=47,
                                    targets=[Name(lineno=12, col_offset=12, end_lineno=12, end_col_offset=16, id='self', ctx=Store())],
                                    value=Call(
                                        lineno=12,
                                        col_offset=19,
                                        end_lineno=12,
                                        end_col_offset=47,
                                        func=Attribute(
                                            lineno=12,
                                            col_offset=19,
                                            end_lineno=12,
                                            end_col_offset=33,
                                            value=Name(lineno=12, col_offset=19, end_lineno=12, end_col_offset=23, id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=12, col_offset=34, end_lineno=12, end_col_offset=46, id='SUPERUSER_ID', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            lineno=13,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=21,
                            target=Name(lineno=13, col_offset=12, end_lineno=13, end_col_offset=19, id='invoice', ctx=Store()),
                            iter=Call(
                                lineno=13,
                                col_offset=23,
                                end_lineno=13,
                                end_col_offset=76,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=23,
                                    end_lineno=13,
                                    end_col_offset=36,
                                    value=Name(lineno=13, col_offset=23, end_lineno=13, end_col_offset=27, id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        lineno=13,
                                        col_offset=37,
                                        end_lineno=13,
                                        end_col_offset=75,
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(lineno=13, col_offset=44, end_lineno=13, end_col_offset=45, arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            lineno=13,
                                            col_offset=47,
                                            end_lineno=13,
                                            end_col_offset=75,
                                            left=Attribute(
                                                lineno=13,
                                                col_offset=47,
                                                end_lineno=13,
                                                end_col_offset=58,
                                                value=Name(lineno=13, col_offset=47, end_lineno=13, end_col_offset=48, id='x', ctx=Load()),
                                                attr='move_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(lineno=13, col_offset=62, end_lineno=13, end_col_offset=75, value='out_invoice', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=66,
                                    test=Compare(
                                        lineno=16,
                                        col_offset=15,
                                        end_lineno=16,
                                        end_col_offset=68,
                                        left=Attribute(
                                            lineno=16,
                                            col_offset=15,
                                            end_lineno=16,
                                            end_col_offset=33,
                                            value=Name(lineno=16, col_offset=15, end_lineno=16, end_col_offset=22, id='invoice', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                lineno=16,
                                                col_offset=41,
                                                end_lineno=16,
                                                end_col_offset=68,
                                                value=Name(lineno=16, col_offset=41, end_lineno=16, end_col_offset=48, id='invoice', ctx=Load()),
                                                attr='message_partner_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            lineno=17,
                                            col_offset=16,
                                            end_lineno=17,
                                            end_col_offset=66,
                                            value=Call(
                                                lineno=17,
                                                col_offset=16,
                                                end_lineno=17,
                                                end_col_offset=66,
                                                func=Attribute(
                                                    lineno=17,
                                                    col_offset=16,
                                                    end_lineno=17,
                                                    end_col_offset=41,
                                                    value=Name(lineno=17, col_offset=16, end_lineno=17, end_col_offset=23, id='invoice', ctx=Load()),
                                                    attr='message_subscribe',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        lineno=17,
                                                        col_offset=42,
                                                        end_lineno=17,
                                                        end_col_offset=65,
                                                        elts=[
                                                            Attribute(
                                                                lineno=17,
                                                                col_offset=43,
                                                                end_lineno=17,
                                                                end_col_offset=64,
                                                                value=Attribute(
                                                                    lineno=17,
                                                                    col_offset=43,
                                                                    end_lineno=17,
                                                                    end_col_offset=61,
                                                                    value=Name(lineno=17, col_offset=43, end_lineno=17, end_col_offset=50, id='invoice', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=21,
                                    target=Name(lineno=18, col_offset=16, end_lineno=18, end_col_offset=20, id='line', ctx=Store()),
                                    iter=Attribute(
                                        lineno=18,
                                        col_offset=24,
                                        end_lineno=18,
                                        end_col_offset=48,
                                        value=Name(lineno=18, col_offset=24, end_lineno=18, end_col_offset=31, id='invoice', ctx=Load()),
                                        attr='invoice_line_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            lineno=19,
                                            col_offset=16,
                                            end_lineno=24,
                                            end_col_offset=21,
                                            test=Attribute(
                                                lineno=19,
                                                col_offset=19,
                                                end_lineno=19,
                                                end_col_offset=52,
                                                value=Attribute(
                                                    lineno=19,
                                                    col_offset=19,
                                                    end_lineno=19,
                                                    end_col_offset=34,
                                                    value=Name(lineno=19, col_offset=19, end_lineno=19, end_col_offset=23, id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='email_template_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    lineno=20,
                                                    col_offset=20,
                                                    end_lineno=24,
                                                    end_col_offset=21,
                                                    value=Call(
                                                        lineno=20,
                                                        col_offset=20,
                                                        end_lineno=24,
                                                        end_col_offset=21,
                                                        func=Attribute(
                                                            lineno=20,
                                                            col_offset=20,
                                                            end_lineno=20,
                                                            end_col_offset=54,
                                                            value=Name(lineno=20, col_offset=20, end_lineno=20, end_col_offset=27, id='invoice', ctx=Load()),
                                                            attr='message_post_with_template',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                lineno=21,
                                                                col_offset=24,
                                                                end_lineno=21,
                                                                end_col_offset=60,
                                                                value=Attribute(
                                                                    lineno=21,
                                                                    col_offset=24,
                                                                    end_lineno=21,
                                                                    end_col_offset=57,
                                                                    value=Attribute(
                                                                        lineno=21,
                                                                        col_offset=24,
                                                                        end_lineno=21,
                                                                        end_col_offset=39,
                                                                        value=Name(lineno=21, col_offset=24, end_lineno=21, end_col_offset=28, id='line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='email_template_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                lineno=22,
                                                                col_offset=24,
                                                                end_lineno=22,
                                                                end_col_offset=50,
                                                                arg='composition_mode',
                                                                value=Constant(lineno=22, col_offset=41, end_lineno=22, end_col_offset=50, value='comment', kind=None),
                                                            ),
                                                            keyword(
                                                                lineno=23,
                                                                col_offset=24,
                                                                end_lineno=23,
                                                                end_col_offset=73,
                                                                arg='email_layout_xmlid',
                                                                value=Constant(lineno=23, col_offset=43, end_lineno=23, end_col_offset=73, value='mail.mail_notification_light', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=19,
                            value=Constant(lineno=25, col_offset=15, end_lineno=25, end_col_offset=19, value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=27,
                    col_offset=4,
                    end_lineno=31,
                    end_col_offset=21,
                    name='_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=27, col_offset=14, end_lineno=27, end_col_offset=18, arg='self', annotation=None, type_comment=None),
                            arg(lineno=27, col_offset=20, end_lineno=27, end_col_offset=24, arg='soft', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=27, col_offset=25, end_lineno=27, end_col_offset=29, value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=36,
                            targets=[Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=14, id='posted', ctx=Store())],
                            value=Call(
                                lineno=29,
                                col_offset=17,
                                end_lineno=29,
                                end_col_offset=36,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=17,
                                    end_lineno=29,
                                    end_col_offset=30,
                                    value=Call(
                                        lineno=29,
                                        col_offset=17,
                                        end_lineno=29,
                                        end_col_offset=24,
                                        func=Name(lineno=29, col_offset=17, end_lineno=29, end_col_offset=22, id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=29, col_offset=31, end_lineno=29, end_col_offset=35, id='soft', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=44,
                            value=Call(
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=44,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=42,
                                    value=Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=14, id='posted', ctx=Load()),
                                    attr='invoice_validate_send_email',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=21,
                            value=Name(lineno=31, col_offset=15, end_lineno=31, end_col_offset=21, id='posted', ctx=Load()),
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