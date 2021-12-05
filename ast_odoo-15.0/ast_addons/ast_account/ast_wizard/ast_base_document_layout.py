Module(
    body=[
        ImportFrom(
            lineno=1,
            col_offset=0,
            end_lineno=1,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=4,
            col_offset=0,
            end_lineno=11,
            end_col_offset=18,
            name='BaseDocumentLayout',
            bases=[
                Attribute(
                    lineno=4,
                    col_offset=25,
                    end_lineno=4,
                    end_col_offset=46,
                    value=Name(lineno=4, col_offset=25, end_lineno=4, end_col_offset=31, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=5,
                    col_offset=4,
                    end_lineno=5,
                    end_col_offset=37,
                    targets=[Name(lineno=5, col_offset=4, end_lineno=5, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=5, col_offset=15, end_lineno=5, end_col_offset=37, value='base.document.layout', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=7,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=18,
                    name='document_layout_save',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=7, col_offset=29, end_lineno=7, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=8,
                            col_offset=8,
                            end_lineno=8,
                            end_col_offset=68,
                            targets=[Name(lineno=8, col_offset=8, end_lineno=8, end_col_offset=11, id='res', ctx=Store())],
                            value=Call(
                                lineno=8,
                                col_offset=14,
                                end_lineno=8,
                                end_col_offset=68,
                                func=Attribute(
                                    lineno=8,
                                    col_offset=14,
                                    end_lineno=8,
                                    end_col_offset=66,
                                    value=Call(
                                        lineno=8,
                                        col_offset=14,
                                        end_lineno=8,
                                        end_col_offset=45,
                                        func=Name(lineno=8, col_offset=14, end_lineno=8, end_col_offset=19, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=8, col_offset=20, end_lineno=8, end_col_offset=38, id='BaseDocumentLayout', ctx=Load()),
                                            Name(lineno=8, col_offset=40, end_lineno=8, end_col_offset=44, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='document_layout_save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=9,
                            col_offset=8,
                            end_lineno=10,
                            end_col_offset=69,
                            target=Name(lineno=9, col_offset=12, end_lineno=9, end_col_offset=18, id='wizard', ctx=Store()),
                            iter=Name(lineno=9, col_offset=22, end_lineno=9, end_col_offset=26, id='self', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=10,
                                    col_offset=12,
                                    end_lineno=10,
                                    end_col_offset=69,
                                    value=Call(
                                        lineno=10,
                                        col_offset=12,
                                        end_lineno=10,
                                        end_col_offset=69,
                                        func=Attribute(
                                            lineno=10,
                                            col_offset=12,
                                            end_lineno=10,
                                            end_col_offset=67,
                                            value=Attribute(
                                                lineno=10,
                                                col_offset=12,
                                                end_lineno=10,
                                                end_col_offset=29,
                                                value=Name(lineno=10, col_offset=12, end_lineno=10, end_col_offset=18, id='wizard', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='action_save_onboarding_invoice_layout',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=18,
                            value=Name(lineno=11, col_offset=15, end_lineno=11, end_col_offset=18, id='res', ctx=Load()),
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
