Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=36,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=22,
            end_col_offset=9,
            name='ReportAccountHashIntegrity',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=33,
                    end_lineno=7,
                    end_col_offset=53,
                    value=Name(lineno=7, col_offset=33, end_lineno=7, end_col_offset=39, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=50,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=50, value='report.account.report_hash_integrity', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=54,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=54, value='Get hash integrity result as PDF.', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=9,
                    name='_get_report_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=12, col_offset=27, end_lineno=12, end_col_offset=31, arg='self', annotation=None, type_comment=None),
                            arg(lineno=12, col_offset=33, end_lineno=12, end_col_offset=39, arg='docids', annotation=None, type_comment=None),
                            arg(lineno=12, col_offset=41, end_lineno=12, end_col_offset=45, arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(lineno=12, col_offset=46, end_lineno=12, end_col_offset=50, value=None, kind=None)],
                    ),
                    body=[
                        If(
                            lineno=13,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=59,
                            test=Name(lineno=13, col_offset=11, end_lineno=13, end_col_offset=15, id='data', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=14,
                                    end_col_offset=65,
                                    value=Call(
                                        lineno=14,
                                        col_offset=12,
                                        end_lineno=14,
                                        end_col_offset=65,
                                        func=Attribute(
                                            lineno=14,
                                            col_offset=12,
                                            end_lineno=14,
                                            end_col_offset=23,
                                            value=Name(lineno=14, col_offset=12, end_lineno=14, end_col_offset=16, id='data', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                lineno=14,
                                                col_offset=24,
                                                end_lineno=14,
                                                end_col_offset=64,
                                                func=Attribute(
                                                    lineno=14,
                                                    col_offset=24,
                                                    end_lineno=14,
                                                    end_col_offset=62,
                                                    value=Attribute(
                                                        lineno=14,
                                                        col_offset=24,
                                                        end_lineno=14,
                                                        end_col_offset=40,
                                                        value=Attribute(
                                                            lineno=14,
                                                            col_offset=24,
                                                            end_lineno=14,
                                                            end_col_offset=32,
                                                            value=Name(lineno=14, col_offset=24, end_lineno=14, end_col_offset=28, id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_check_hash_integrity',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=59,
                                    targets=[Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=16, id='data', ctx=Store())],
                                    value=Call(
                                        lineno=16,
                                        col_offset=19,
                                        end_lineno=16,
                                        end_col_offset=59,
                                        func=Attribute(
                                            lineno=16,
                                            col_offset=19,
                                            end_lineno=16,
                                            end_col_offset=57,
                                            value=Attribute(
                                                lineno=16,
                                                col_offset=19,
                                                end_lineno=16,
                                                end_col_offset=35,
                                                value=Attribute(
                                                    lineno=16,
                                                    col_offset=19,
                                                    end_lineno=16,
                                                    end_col_offset=27,
                                                    value=Name(lineno=16, col_offset=19, end_lineno=16, end_col_offset=23, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='_check_hash_integrity',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
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
                                    Constant(lineno=20, col_offset=12, end_lineno=20, end_col_offset=18, value='data', kind=None),
                                    Constant(lineno=21, col_offset=12, end_lineno=21, end_col_offset=18, value='docs', kind=None),
                                ],
                                values=[
                                    Name(lineno=18, col_offset=24, end_lineno=18, end_col_offset=30, id='docids', ctx=Load()),
                                    Subscript(
                                        lineno=19,
                                        col_offset=26,
                                        end_lineno=19,
                                        end_col_offset=49,
                                        value=Attribute(
                                            lineno=19,
                                            col_offset=26,
                                            end_lineno=19,
                                            end_col_offset=34,
                                            value=Name(lineno=19, col_offset=26, end_lineno=19, end_col_offset=30, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=19, col_offset=35, end_lineno=19, end_col_offset=48, value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(lineno=20, col_offset=21, end_lineno=20, end_col_offset=25, id='data', ctx=Load()),
                                    Call(
                                        lineno=21,
                                        col_offset=21,
                                        end_lineno=21,
                                        end_col_offset=72,
                                        func=Attribute(
                                            lineno=21,
                                            col_offset=21,
                                            end_lineno=21,
                                            end_col_offset=51,
                                            value=Subscript(
                                                lineno=21,
                                                col_offset=21,
                                                end_lineno=21,
                                                end_col_offset=44,
                                                value=Attribute(
                                                    lineno=21,
                                                    col_offset=21,
                                                    end_lineno=21,
                                                    end_col_offset=29,
                                                    value=Name(lineno=21, col_offset=21, end_lineno=21, end_col_offset=25, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=21, col_offset=30, end_lineno=21, end_col_offset=43, value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=21,
                                                col_offset=52,
                                                end_lineno=21,
                                                end_col_offset=71,
                                                value=Attribute(
                                                    lineno=21,
                                                    col_offset=52,
                                                    end_lineno=21,
                                                    end_col_offset=68,
                                                    value=Attribute(
                                                        lineno=21,
                                                        col_offset=52,
                                                        end_lineno=21,
                                                        end_col_offset=60,
                                                        value=Name(lineno=21, col_offset=52, end_lineno=21, end_col_offset=56, id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=11,
                            col_offset=5,
                            end_lineno=11,
                            end_col_offset=14,
                            value=Name(lineno=11, col_offset=5, end_lineno=11, end_col_offset=8, id='api', ctx=Load()),
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
