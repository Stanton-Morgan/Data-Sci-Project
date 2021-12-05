Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=21,
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=58,
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='unslug', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=24,
            end_col_offset=34,
            name='WebsitePartnerPage',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=25,
                    end_lineno=8,
                    end_col_offset=40,
                    value=Name(lineno=8, col_offset=25, end_lineno=8, end_col_offset=29, id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=34,
                    name='partners_detail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=12, col_offset=24, end_lineno=12, end_col_offset=28, arg='self', annotation=None, type_comment=None),
                            arg(lineno=12, col_offset=30, end_lineno=12, end_col_offset=40, arg='partner_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(lineno=12, col_offset=44, end_lineno=12, end_col_offset=48, arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=42,
                            targets=[
                                Tuple(
                                    lineno=13,
                                    col_offset=8,
                                    end_lineno=13,
                                    end_col_offset=21,
                                    elts=[
                                        Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=9, id='_', ctx=Store()),
                                        Name(lineno=13, col_offset=11, end_lineno=13, end_col_offset=21, id='partner_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=13,
                                col_offset=24,
                                end_lineno=13,
                                end_col_offset=42,
                                func=Name(lineno=13, col_offset=24, end_lineno=13, end_col_offset=30, id='unslug', ctx=Load()),
                                args=[Name(lineno=13, col_offset=31, end_lineno=13, end_col_offset=41, id='partner_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=14,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=77,
                            test=Name(lineno=14, col_offset=11, end_lineno=14, end_col_offset=21, id='partner_id', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=15,
                                    col_offset=12,
                                    end_lineno=15,
                                    end_col_offset=79,
                                    targets=[Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=24, id='partner_sudo', ctx=Store())],
                                    value=Call(
                                        lineno=15,
                                        col_offset=27,
                                        end_lineno=15,
                                        end_col_offset=79,
                                        func=Attribute(
                                            lineno=15,
                                            col_offset=27,
                                            end_lineno=15,
                                            end_col_offset=67,
                                            value=Call(
                                                lineno=15,
                                                col_offset=27,
                                                end_lineno=15,
                                                end_col_offset=60,
                                                func=Attribute(
                                                    lineno=15,
                                                    col_offset=27,
                                                    end_lineno=15,
                                                    end_col_offset=58,
                                                    value=Subscript(
                                                        lineno=15,
                                                        col_offset=27,
                                                        end_lineno=15,
                                                        end_col_offset=53,
                                                        value=Attribute(
                                                            lineno=15,
                                                            col_offset=27,
                                                            end_lineno=15,
                                                            end_col_offset=38,
                                                            value=Name(lineno=15, col_offset=27, end_lineno=15, end_col_offset=34, id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(lineno=15, col_offset=39, end_lineno=15, end_col_offset=52, value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=15, col_offset=68, end_lineno=15, end_col_offset=78, id='partner_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=104,
                                    targets=[Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=32, id='is_website_publisher', ctx=Store())],
                                    value=Call(
                                        lineno=16,
                                        col_offset=35,
                                        end_lineno=16,
                                        end_col_offset=104,
                                        func=Attribute(
                                            lineno=16,
                                            col_offset=35,
                                            end_lineno=16,
                                            end_col_offset=69,
                                            value=Subscript(
                                                lineno=16,
                                                col_offset=35,
                                                end_lineno=16,
                                                end_col_offset=59,
                                                value=Attribute(
                                                    lineno=16,
                                                    col_offset=35,
                                                    end_lineno=16,
                                                    end_col_offset=46,
                                                    value=Name(lineno=16, col_offset=35, end_lineno=16, end_col_offset=42, id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=16, col_offset=47, end_lineno=16, end_col_offset=58, value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=16, col_offset=70, end_lineno=16, end_col_offset=103, value='website.group_website_publisher', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=77,
                                    test=BoolOp(
                                        lineno=17,
                                        col_offset=15,
                                        end_lineno=17,
                                        end_col_offset=97,
                                        op=And(),
                                        values=[
                                            Call(
                                                lineno=17,
                                                col_offset=15,
                                                end_lineno=17,
                                                end_col_offset=36,
                                                func=Attribute(
                                                    lineno=17,
                                                    col_offset=15,
                                                    end_lineno=17,
                                                    end_col_offset=34,
                                                    value=Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=27, id='partner_sudo', ctx=Load()),
                                                    attr='exists',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                lineno=17,
                                                col_offset=42,
                                                end_lineno=17,
                                                end_col_offset=96,
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        lineno=17,
                                                        col_offset=42,
                                                        end_lineno=17,
                                                        end_col_offset=72,
                                                        value=Name(lineno=17, col_offset=42, end_lineno=17, end_col_offset=54, id='partner_sudo', ctx=Load()),
                                                        attr='website_published',
                                                        ctx=Load(),
                                                    ),
                                                    Name(lineno=17, col_offset=76, end_lineno=17, end_col_offset=96, id='is_website_publisher', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=18,
                                            col_offset=16,
                                            end_lineno=22,
                                            end_col_offset=17,
                                            targets=[Name(lineno=18, col_offset=16, end_lineno=18, end_col_offset=22, id='values', ctx=Store())],
                                            value=Dict(
                                                lineno=18,
                                                col_offset=25,
                                                end_lineno=22,
                                                end_col_offset=17,
                                                keys=[
                                                    Constant(lineno=19, col_offset=20, end_lineno=19, end_col_offset=33, value='main_object', kind=None),
                                                    Constant(lineno=20, col_offset=20, end_lineno=20, end_col_offset=29, value='partner', kind=None),
                                                    Constant(lineno=21, col_offset=20, end_lineno=21, end_col_offset=31, value='edit_page', kind=None),
                                                ],
                                                values=[
                                                    Name(lineno=19, col_offset=35, end_lineno=19, end_col_offset=47, id='partner_sudo', ctx=Load()),
                                                    Name(lineno=20, col_offset=31, end_lineno=20, end_col_offset=43, id='partner_sudo', ctx=Load()),
                                                    Constant(lineno=21, col_offset=33, end_lineno=21, end_col_offset=38, value=False, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            lineno=23,
                                            col_offset=16,
                                            end_lineno=23,
                                            end_col_offset=77,
                                            value=Call(
                                                lineno=23,
                                                col_offset=23,
                                                end_lineno=23,
                                                end_col_offset=77,
                                                func=Attribute(
                                                    lineno=23,
                                                    col_offset=23,
                                                    end_lineno=23,
                                                    end_col_offset=37,
                                                    value=Name(lineno=23, col_offset=23, end_lineno=23, end_col_offset=30, id='request', ctx=Load()),
                                                    attr='render',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(lineno=23, col_offset=38, end_lineno=23, end_col_offset=68, value='website_partner.partner_page', kind=None),
                                                    Name(lineno=23, col_offset=70, end_lineno=23, end_col_offset=76, id='values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=34,
                            value=Call(
                                lineno=24,
                                col_offset=15,
                                end_lineno=24,
                                end_col_offset=34,
                                func=Attribute(
                                    lineno=24,
                                    col_offset=15,
                                    end_lineno=24,
                                    end_col_offset=32,
                                    value=Name(lineno=24, col_offset=15, end_lineno=24, end_col_offset=22, id='request', ctx=Load()),
                                    attr='not_found',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=11,
                            col_offset=5,
                            end_lineno=11,
                            end_col_offset=85,
                            func=Attribute(
                                lineno=11,
                                col_offset=5,
                                end_lineno=11,
                                end_col_offset=15,
                                value=Name(lineno=11, col_offset=5, end_lineno=11, end_col_offset=9, id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    lineno=11,
                                    col_offset=16,
                                    end_lineno=11,
                                    end_col_offset=42,
                                    elts=[Constant(lineno=11, col_offset=17, end_lineno=11, end_col_offset=41, value='/partners/<partner_id>', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    lineno=11,
                                    col_offset=44,
                                    end_lineno=11,
                                    end_col_offset=55,
                                    arg='type',
                                    value=Constant(lineno=11, col_offset=49, end_lineno=11, end_col_offset=55, value='http', kind=None),
                                ),
                                keyword(
                                    lineno=11,
                                    col_offset=57,
                                    end_lineno=11,
                                    end_col_offset=70,
                                    arg='auth',
                                    value=Constant(lineno=11, col_offset=62, end_lineno=11, end_col_offset=70, value='public', kind=None),
                                ),
                                keyword(
                                    lineno=11,
                                    col_offset=72,
                                    end_lineno=11,
                                    end_col_offset=84,
                                    arg='website',
                                    value=Constant(lineno=11, col_offset=80, end_lineno=11, end_col_offset=84, value=True, kind=None),
                                ),
                            ],
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