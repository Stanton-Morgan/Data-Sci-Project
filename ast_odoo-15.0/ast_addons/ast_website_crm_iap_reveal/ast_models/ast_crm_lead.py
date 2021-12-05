Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=12,
            end_col_offset=98,
            name='Lead',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=11,
                    end_lineno=7,
                    end_col_offset=23,
                    value=Name(lineno=7, col_offset=11, end_lineno=7, end_col_offset=17, id='models', ctx=Load()),
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
                    end_col_offset=25,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=25, value='crm.lead', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=48,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=13, id='reveal_ip', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=16,
                        end_lineno=10,
                        end_col_offset=48,
                        func=Attribute(
                            lineno=10,
                            col_offset=16,
                            end_lineno=10,
                            end_col_offset=27,
                            value=Name(lineno=10, col_offset=16, end_lineno=10, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=28,
                                end_lineno=10,
                                end_col_offset=47,
                                arg='string',
                                value=Constant(lineno=10, col_offset=35, end_lineno=10, end_col_offset=47, value='IP Address', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=61,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=22, id='reveal_iap_credits', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=25,
                        end_lineno=11,
                        end_col_offset=61,
                        func=Attribute(
                            lineno=11,
                            col_offset=25,
                            end_lineno=11,
                            end_col_offset=39,
                            value=Name(lineno=11, col_offset=25, end_lineno=11, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=40,
                                end_lineno=11,
                                end_col_offset=60,
                                arg='string',
                                value=Constant(lineno=11, col_offset=47, end_lineno=11, end_col_offset=60, value='IAP Credits', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=98,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=18, id='reveal_rule_id', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=21,
                        end_lineno=12,
                        end_col_offset=98,
                        func=Attribute(
                            lineno=12,
                            col_offset=21,
                            end_lineno=12,
                            end_col_offset=36,
                            value=Name(lineno=12, col_offset=21, end_lineno=12, end_col_offset=27, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=12, col_offset=37, end_lineno=12, end_col_offset=54, value='crm.reveal.rule', kind=None)],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=56,
                                end_lineno=12,
                                end_col_offset=85,
                                arg='string',
                                value=Constant(lineno=12, col_offset=63, end_lineno=12, end_col_offset=85, value='Lead Generation Rule', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=87,
                                end_lineno=12,
                                end_col_offset=97,
                                arg='index',
                                value=Constant(lineno=12, col_offset=93, end_lineno=12, end_col_offset=97, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
