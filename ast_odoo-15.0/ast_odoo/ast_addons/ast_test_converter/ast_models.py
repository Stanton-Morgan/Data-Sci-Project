Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=50,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='api', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=34,
            end_col_offset=35,
            name='test_model',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=17,
                    end_lineno=6,
                    end_col_offset=29,
                    value=Name(lineno=6, col_offset=17, end_lineno=6, end_col_offset=23, id='models', ctx=Load()),
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
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=7, col_offset=12, end_lineno=7, end_col_offset=39, value='test_converter.test_model', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=41,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=8, col_offset=19, end_lineno=8, end_col_offset=41, value='Test Converter Model', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=24,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=8, id='char', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=11,
                        end_lineno=10,
                        end_col_offset=24,
                        func=Attribute(
                            lineno=10,
                            col_offset=11,
                            end_lineno=10,
                            end_col_offset=22,
                            value=Name(lineno=10, col_offset=11, end_lineno=10, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=30,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=11, id='integer', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=14,
                        end_lineno=11,
                        end_col_offset=30,
                        func=Attribute(
                            lineno=11,
                            col_offset=14,
                            end_lineno=11,
                            end_col_offset=28,
                            value=Name(lineno=11, col_offset=14, end_lineno=11, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=26,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=9, id='float', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=12,
                        end_lineno=12,
                        end_col_offset=26,
                        func=Attribute(
                            lineno=12,
                            col_offset=12,
                            end_lineno=12,
                            end_col_offset=24,
                            value=Name(lineno=12, col_offset=12, end_lineno=12, end_col_offset=18, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=42,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=11, id='numeric', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=14,
                        end_lineno=13,
                        end_col_offset=42,
                        func=Attribute(
                            lineno=13,
                            col_offset=14,
                            end_lineno=13,
                            end_col_offset=26,
                            value=Name(lineno=13, col_offset=14, end_lineno=13, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=27,
                                end_lineno=13,
                                end_col_offset=41,
                                arg='digits',
                                value=Tuple(
                                    lineno=13,
                                    col_offset=34,
                                    end_lineno=13,
                                    end_col_offset=41,
                                    elts=[
                                        Constant(lineno=13, col_offset=35, end_lineno=13, end_col_offset=37, value=16, kind=None),
                                        Constant(lineno=13, col_offset=39, end_lineno=13, end_col_offset=40, value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=88,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=12, id='many2one', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=15,
                        end_lineno=14,
                        end_col_offset=88,
                        func=Attribute(
                            lineno=14,
                            col_offset=15,
                            end_lineno=14,
                            end_col_offset=30,
                            value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=14, col_offset=31, end_lineno=14, end_col_offset=62, value='test_converter.test_model.sub', kind=None)],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=64,
                                end_lineno=14,
                                end_col_offset=87,
                                arg='group_expand',
                                value=Constant(lineno=14, col_offset=77, end_lineno=14, end_col_offset=87, value='_gbf_m2o', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=44,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=10, id='binary', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=13,
                        end_lineno=15,
                        end_col_offset=44,
                        func=Attribute(
                            lineno=15,
                            col_offset=13,
                            end_lineno=15,
                            end_col_offset=26,
                            value=Name(lineno=15, col_offset=13, end_lineno=15, end_col_offset=19, id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=27,
                                end_lineno=15,
                                end_col_offset=43,
                                arg='attachment',
                                value=Constant(lineno=15, col_offset=38, end_lineno=15, end_col_offset=43, value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=24,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=8, id='date', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=11,
                        end_lineno=16,
                        end_col_offset=24,
                        func=Attribute(
                            lineno=16,
                            col_offset=11,
                            end_lineno=16,
                            end_col_offset=22,
                            value=Name(lineno=16, col_offset=11, end_lineno=16, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=32,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=12, id='datetime', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=15,
                        end_lineno=17,
                        end_col_offset=32,
                        func=Attribute(
                            lineno=17,
                            col_offset=15,
                            end_lineno=17,
                            end_col_offset=30,
                            value=Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=71,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=17, id='selection_str', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=20,
                        end_lineno=24,
                        end_col_offset=71,
                        func=Attribute(
                            lineno=18,
                            col_offset=20,
                            end_lineno=18,
                            end_col_offset=36,
                            value=Name(lineno=18, col_offset=20, end_lineno=18, end_col_offset=26, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                lineno=18,
                                col_offset=37,
                                end_lineno=23,
                                end_col_offset=5,
                                elts=[
                                    Tuple(
                                        lineno=19,
                                        col_offset=8,
                                        end_lineno=19,
                                        end_col_offset=52,
                                        elts=[
                                            Constant(lineno=19, col_offset=9, end_lineno=19, end_col_offset=12, value='A', kind=None),
                                            Constant(lineno=19, col_offset=14, end_lineno=19, end_col_offset=51, value="Qu'il n'est pas arrivé à Toronto", kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=20,
                                        col_offset=8,
                                        end_lineno=20,
                                        end_col_offset=58,
                                        elts=[
                                            Constant(lineno=20, col_offset=9, end_lineno=20, end_col_offset=12, value='B', kind=None),
                                            Constant(lineno=20, col_offset=14, end_lineno=20, end_col_offset=57, value="Qu'il était supposé arriver à Toronto", kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=21,
                                        col_offset=8,
                                        end_lineno=21,
                                        end_col_offset=70,
                                        elts=[
                                            Constant(lineno=21, col_offset=9, end_lineno=21, end_col_offset=12, value='C', kind=None),
                                            Constant(lineno=21, col_offset=14, end_lineno=21, end_col_offset=69, value="Qu'est-ce qu'il fout ce maudit pancake, tabernacle ?", kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=22,
                                        col_offset=8,
                                        end_lineno=22,
                                        end_col_offset=31,
                                        elts=[
                                            Constant(lineno=22, col_offset=9, end_lineno=22, end_col_offset=12, value='D', kind=None),
                                            Constant(lineno=22, col_offset=14, end_lineno=22, end_col_offset=30, value='La réponse D', kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                lineno=23,
                                col_offset=7,
                                end_lineno=24,
                                end_col_offset=70,
                                arg='string',
                                value=Constant(lineno=23, col_offset=14, end_lineno=24, end_col_offset=70, value="Lorsqu'un pancake prend l'avion à destination de Toronto et qu'il fait une escale technique à St Claude, on dit:", kind='u'),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=25,
                    col_offset=4,
                    end_lineno=25,
                    end_col_offset=24,
                    targets=[Name(lineno=25, col_offset=4, end_lineno=25, end_col_offset=8, id='html', ctx=Store())],
                    value=Call(
                        lineno=25,
                        col_offset=11,
                        end_lineno=25,
                        end_col_offset=24,
                        func=Attribute(
                            lineno=25,
                            col_offset=11,
                            end_lineno=25,
                            end_col_offset=22,
                            value=Name(lineno=25, col_offset=11, end_lineno=25, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=26,
                    col_offset=4,
                    end_lineno=26,
                    end_col_offset=24,
                    targets=[Name(lineno=26, col_offset=4, end_lineno=26, end_col_offset=8, id='text', ctx=Store())],
                    value=Call(
                        lineno=26,
                        col_offset=11,
                        end_lineno=26,
                        end_col_offset=24,
                        func=Attribute(
                            lineno=26,
                            col_offset=11,
                            end_lineno=26,
                            end_col_offset=22,
                            value=Name(lineno=26, col_offset=11, end_lineno=26, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=32,
                    col_offset=4,
                    end_lineno=34,
                    end_col_offset=35,
                    name='_gbf_m2o',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=32, col_offset=17, end_lineno=32, end_col_offset=21, arg='self', annotation=None, type_comment=None),
                            arg(lineno=32, col_offset=23, end_lineno=32, end_col_offset=27, arg='subs', annotation=None, type_comment=None),
                            arg(lineno=32, col_offset=29, end_lineno=32, end_col_offset=35, arg='domain', annotation=None, type_comment=None),
                            arg(lineno=32, col_offset=37, end_lineno=32, end_col_offset=42, arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=33,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=79,
                            targets=[Name(lineno=33, col_offset=8, end_lineno=33, end_col_offset=15, id='sub_ids', ctx=Store())],
                            value=Call(
                                lineno=33,
                                col_offset=18,
                                end_lineno=33,
                                end_col_offset=79,
                                func=Attribute(
                                    lineno=33,
                                    col_offset=18,
                                    end_lineno=33,
                                    end_col_offset=30,
                                    value=Name(lineno=33, col_offset=18, end_lineno=33, end_col_offset=22, id='subs', ctx=Load()),
                                    attr='_search',
                                    ctx=Load(),
                                ),
                                args=[List(lineno=33, col_offset=31, end_lineno=33, end_col_offset=33, elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        lineno=33,
                                        col_offset=35,
                                        end_lineno=33,
                                        end_col_offset=46,
                                        arg='order',
                                        value=Name(lineno=33, col_offset=41, end_lineno=33, end_col_offset=46, id='order', ctx=Load()),
                                    ),
                                    keyword(
                                        lineno=33,
                                        col_offset=48,
                                        end_lineno=33,
                                        end_col_offset=78,
                                        arg='access_rights_uid',
                                        value=Name(lineno=33, col_offset=66, end_lineno=33, end_col_offset=78, id='SUPERUSER_ID', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=35,
                            value=Call(
                                lineno=34,
                                col_offset=15,
                                end_lineno=34,
                                end_col_offset=35,
                                func=Attribute(
                                    lineno=34,
                                    col_offset=15,
                                    end_lineno=34,
                                    end_col_offset=26,
                                    value=Name(lineno=34, col_offset=15, end_lineno=34, end_col_offset=19, id='subs', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=34, col_offset=27, end_lineno=34, end_col_offset=34, id='sub_ids', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            lineno=31,
                            col_offset=5,
                            end_lineno=31,
                            end_col_offset=14,
                            value=Name(lineno=31, col_offset=5, end_lineno=31, end_col_offset=8, id='api', ctx=Load()),
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
        ClassDef(
            lineno=37,
            col_offset=0,
            end_lineno=40,
            end_col_offset=24,
            name='test_model_sub',
            bases=[
                Attribute(
                    lineno=37,
                    col_offset=21,
                    end_lineno=37,
                    end_col_offset=33,
                    value=Name(lineno=37, col_offset=21, end_lineno=37, end_col_offset=27, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=38,
                    col_offset=4,
                    end_lineno=38,
                    end_col_offset=43,
                    targets=[Name(lineno=38, col_offset=4, end_lineno=38, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=38, col_offset=12, end_lineno=38, end_col_offset=43, value='test_converter.test_model.sub', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=39,
                    col_offset=4,
                    end_lineno=39,
                    end_col_offset=64,
                    targets=[Name(lineno=39, col_offset=4, end_lineno=39, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=39, col_offset=19, end_lineno=39, end_col_offset=64, value='Subtraction For Test Model & Test Converter', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=40,
                    col_offset=4,
                    end_lineno=40,
                    end_col_offset=24,
                    targets=[Name(lineno=40, col_offset=4, end_lineno=40, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=40,
                        col_offset=11,
                        end_lineno=40,
                        end_col_offset=24,
                        func=Attribute(
                            lineno=40,
                            col_offset=11,
                            end_lineno=40,
                            end_col_offset=22,
                            value=Name(lineno=40, col_offset=11, end_lineno=40, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            lineno=43,
            col_offset=0,
            end_lineno=46,
            end_col_offset=41,
            name='test_model_monetary',
            bases=[
                Attribute(
                    lineno=43,
                    col_offset=26,
                    end_lineno=43,
                    end_col_offset=38,
                    value=Name(lineno=43, col_offset=26, end_lineno=43, end_col_offset=32, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=44,
                    col_offset=4,
                    end_lineno=44,
                    end_col_offset=37,
                    targets=[Name(lineno=44, col_offset=4, end_lineno=44, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=44, col_offset=12, end_lineno=44, end_col_offset=37, value='test_converter.monetary', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=45,
                    col_offset=4,
                    end_lineno=45,
                    end_col_offset=44,
                    targets=[Name(lineno=45, col_offset=4, end_lineno=45, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=45, col_offset=19, end_lineno=45, end_col_offset=44, value='Test Converter Monetary', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=46,
                    col_offset=4,
                    end_lineno=46,
                    end_col_offset=41,
                    targets=[Name(lineno=46, col_offset=4, end_lineno=46, end_col_offset=9, id='value', ctx=Store())],
                    value=Call(
                        lineno=46,
                        col_offset=12,
                        end_lineno=46,
                        end_col_offset=41,
                        func=Attribute(
                            lineno=46,
                            col_offset=12,
                            end_lineno=46,
                            end_col_offset=24,
                            value=Name(lineno=46, col_offset=12, end_lineno=46, end_col_offset=18, id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=46,
                                col_offset=25,
                                end_lineno=46,
                                end_col_offset=40,
                                arg='digits',
                                value=Tuple(
                                    lineno=46,
                                    col_offset=32,
                                    end_lineno=46,
                                    end_col_offset=40,
                                    elts=[
                                        Constant(lineno=46, col_offset=33, end_lineno=46, end_col_offset=35, value=16, kind=None),
                                        Constant(lineno=46, col_offset=37, end_lineno=46, end_col_offset=39, value=55, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
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
