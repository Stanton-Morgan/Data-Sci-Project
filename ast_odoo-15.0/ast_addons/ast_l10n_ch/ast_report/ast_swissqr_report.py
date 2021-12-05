Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=28,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=22,
            end_col_offset=9,
            name='ReportSwissQR',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=20,
                    end_lineno=5,
                    end_col_offset=40,
                    value=Name(lineno=5, col_offset=20, end_lineno=5, end_col_offset=26, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=6,
                    col_offset=4,
                    end_lineno=6,
                    end_col_offset=43,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=6, col_offset=12, end_lineno=6, end_col_offset=43, value='report.l10n_ch.qr_report_main', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=41,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=7, col_offset=19, end_lineno=7, end_col_offset=41, value='Swiss QR-bill report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=9,
                    name='_get_report_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=10, col_offset=27, end_lineno=10, end_col_offset=31, arg='self', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=33, end_lineno=10, end_col_offset=39, arg='docids', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=41, end_lineno=10, end_col_offset=45, arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=10, col_offset=46, end_lineno=10, end_col_offset=50, value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=54,
                            targets=[Name(lineno=11, col_offset=8, end_lineno=11, end_col_offset=12, id='docs', ctx=Store())],
                            value=Call(
                                lineno=11,
                                col_offset=15,
                                end_lineno=11,
                                end_col_offset=54,
                                func=Attribute(
                                    lineno=11,
                                    col_offset=15,
                                    end_lineno=11,
                                    end_col_offset=46,
                                    value=Subscript(
                                        lineno=11,
                                        col_offset=15,
                                        end_lineno=11,
                                        end_col_offset=39,
                                        value=Attribute(
                                            lineno=11,
                                            col_offset=15,
                                            end_lineno=11,
                                            end_col_offset=23,
                                            value=Name(lineno=11, col_offset=15, end_lineno=11, end_col_offset=19, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=11, col_offset=24, end_lineno=11, end_col_offset=38, value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=11, col_offset=47, end_lineno=11, end_col_offset=53, id='docids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=25,
                            targets=[Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=20, id='qr_code_urls', ctx=Store())],
                            value=Dict(lineno=13, col_offset=23, end_lineno=13, end_col_offset=25, keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            lineno=14,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=245,
                            target=Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=19, id='invoice', ctx=Store()),
                            iter=Name(lineno=14, col_offset=23, end_lineno=14, end_col_offset=27, id='docs', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=15,
                                    col_offset=12,
                                    end_lineno=15,
                                    end_col_offset=245,
                                    targets=[
                                        Subscript(
                                            lineno=15,
                                            col_offset=12,
                                            end_lineno=15,
                                            end_col_offset=36,
                                            value=Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=24, id='qr_code_urls', ctx=Load()),
                                            slice=Attribute(
                                                lineno=15,
                                                col_offset=25,
                                                end_lineno=15,
                                                end_col_offset=35,
                                                value=Name(lineno=15, col_offset=25, end_lineno=15, end_col_offset=32, id='invoice', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=15,
                                        col_offset=39,
                                        end_lineno=15,
                                        end_col_offset=245,
                                        func=Attribute(
                                            lineno=15,
                                            col_offset=39,
                                            end_lineno=15,
                                            end_col_offset=83,
                                            value=Attribute(
                                                lineno=15,
                                                col_offset=39,
                                                end_lineno=15,
                                                end_col_offset=62,
                                                value=Name(lineno=15, col_offset=39, end_lineno=15, end_col_offset=46, id='invoice', ctx=Load()),
                                                attr='partner_bank_id',
                                                ctx=Load(),
                                            ),
                                            attr='build_qr_code_base64',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=15,
                                                col_offset=84,
                                                end_lineno=15,
                                                end_col_offset=107,
                                                value=Name(lineno=15, col_offset=84, end_lineno=15, end_col_offset=91, id='invoice', ctx=Load()),
                                                attr='amount_residual',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                lineno=15,
                                                col_offset=109,
                                                end_lineno=15,
                                                end_col_offset=136,
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        lineno=15,
                                                        col_offset=109,
                                                        end_lineno=15,
                                                        end_col_offset=120,
                                                        value=Name(lineno=15, col_offset=109, end_lineno=15, end_col_offset=116, id='invoice', ctx=Load()),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        lineno=15,
                                                        col_offset=124,
                                                        end_lineno=15,
                                                        end_col_offset=136,
                                                        value=Name(lineno=15, col_offset=124, end_lineno=15, end_col_offset=131, id='invoice', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                lineno=15,
                                                col_offset=138,
                                                end_lineno=15,
                                                end_col_offset=163,
                                                value=Name(lineno=15, col_offset=138, end_lineno=15, end_col_offset=145, id='invoice', ctx=Load()),
                                                attr='payment_reference',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=15,
                                                col_offset=165,
                                                end_lineno=15,
                                                end_col_offset=184,
                                                value=Name(lineno=15, col_offset=165, end_lineno=15, end_col_offset=172, id='invoice', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=15,
                                                col_offset=186,
                                                end_lineno=15,
                                                end_col_offset=204,
                                                value=Name(lineno=15, col_offset=186, end_lineno=15, end_col_offset=193, id='invoice', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                lineno=15,
                                                col_offset=206,
                                                end_lineno=15,
                                                end_col_offset=223,
                                                arg='qr_method',
                                                value=Constant(lineno=15, col_offset=216, end_lineno=15, end_col_offset=223, value='ch_qr', kind=None),
                                            ),
                                            keyword(
                                                lineno=15,
                                                col_offset=225,
                                                end_lineno=15,
                                                end_col_offset=244,
                                                arg='silent_errors',
                                                value=Constant(lineno=15, col_offset=239, end_lineno=15, end_col_offset=244, value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=17,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=9,
                            value=Dict(
                                lineno=17,
                                col_offset=15,
                                end_lineno=22,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=18, col_offset=12, end_lineno=18, end_col_offset=21, value='doc_ids', kind=None),
                                    Constant(lineno=19, col_offset=12, end_lineno=19, end_col_offset=23, value='doc_model', kind=None),
                                    Constant(lineno=20, col_offset=12, end_lineno=20, end_col_offset=18, value='docs', kind=None),
                                    Constant(lineno=21, col_offset=12, end_lineno=21, end_col_offset=26, value='qr_code_urls', kind=None),
                                ],
                                values=[
                                    Name(lineno=18, col_offset=23, end_lineno=18, end_col_offset=29, id='docids', ctx=Load()),
                                    Constant(lineno=19, col_offset=25, end_lineno=19, end_col_offset=39, value='account.move', kind=None),
                                    Name(lineno=20, col_offset=20, end_lineno=20, end_col_offset=24, id='docs', ctx=Load()),
                                    Name(lineno=21, col_offset=28, end_lineno=21, end_col_offset=40, id='qr_code_urls', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=9,
                            col_offset=5,
                            end_lineno=9,
                            end_col_offset=14,
                            value=Name(lineno=9, col_offset=5, end_lineno=9, end_col_offset=8, id='api', ctx=Load()),
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