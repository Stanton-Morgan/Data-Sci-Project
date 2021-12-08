Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=13,
            end_col_offset=102,
            name='AccountInvoiceReport',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=27,
                    end_lineno=5,
                    end_col_offset=39,
                    value=Name(lineno=5, col_offset=27, end_lineno=5, end_col_offset=33, id='models', ctx=Load()),
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
                    end_col_offset=39,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=39, value='account.invoice.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=106,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=31, id='l10n_latam_document_type_id', ctx=Store())],
                    value=Call(
                        lineno=9,
                        col_offset=34,
                        end_lineno=9,
                        end_col_offset=106,
                        func=Attribute(
                            lineno=9,
                            col_offset=34,
                            end_lineno=9,
                            end_col_offset=49,
                            value=Name(lineno=9, col_offset=34, end_lineno=9, end_col_offset=40, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=9, col_offset=50, end_lineno=9, end_col_offset=76, value='l10n_latam.document.type', kind=None),
                            Constant(lineno=9, col_offset=78, end_lineno=9, end_col_offset=93, value='Document Type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=9,
                                col_offset=95,
                                end_lineno=9,
                                end_col_offset=105,
                                arg='index',
                                value=Constant(lineno=9, col_offset=101, end_lineno=9, end_col_offset=105, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=65,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=12, id='_depends', ctx=Store())],
                    value=Dict(
                        lineno=10,
                        col_offset=15,
                        end_lineno=10,
                        end_col_offset=65,
                        keys=[Constant(lineno=10, col_offset=16, end_lineno=10, end_col_offset=30, value='account.move', kind=None)],
                        values=[
                            List(
                                lineno=10,
                                col_offset=32,
                                end_lineno=10,
                                end_col_offset=63,
                                elts=[Constant(lineno=10, col_offset=33, end_lineno=10, end_col_offset=62, value='l10n_latam_document_type_id', kind=None)],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=102,
                    name='_select',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=12, col_offset=16, end_lineno=12, end_col_offset=20, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=102,
                            value=BinOp(
                                lineno=13,
                                col_offset=15,
                                end_lineno=13,
                                end_col_offset=102,
                                left=Call(
                                    lineno=13,
                                    col_offset=15,
                                    end_lineno=13,
                                    end_col_offset=32,
                                    func=Attribute(
                                        lineno=13,
                                        col_offset=15,
                                        end_lineno=13,
                                        end_col_offset=30,
                                        value=Call(
                                            lineno=13,
                                            col_offset=15,
                                            end_lineno=13,
                                            end_col_offset=22,
                                            func=Name(lineno=13, col_offset=15, end_lineno=13, end_col_offset=20, id='super', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='_select',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Constant(lineno=13, col_offset=35, end_lineno=13, end_col_offset=102, value=', move.l10n_latam_document_type_id as l10n_latam_document_type_id', kind=None),
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