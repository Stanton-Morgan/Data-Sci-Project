Module(
    body=[
        Import(
            lineno=14,
            col_offset=0,
            end_lineno=14,
            end_col_offset=14,
            names=[
                alias(name='sys', asname=None),
                alias(name='os', asname=None),
            ],
        ),
        Assign(
            lineno=28,
            col_offset=0,
            end_lineno=28,
            end_col_offset=32,
            targets=[Name(lineno=28, col_offset=0, end_lineno=28, end_col_offset=10, id='extensions', ctx=Store())],
            value=List(
                lineno=28,
                col_offset=13,
                end_lineno=28,
                end_col_offset=32,
                elts=[Constant(lineno=28, col_offset=14, end_lineno=28, end_col_offset=31, value='sphinx.ext.todo', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            lineno=31,
            col_offset=0,
            end_lineno=31,
            end_col_offset=31,
            targets=[Name(lineno=31, col_offset=0, end_lineno=31, end_col_offset=14, id='templates_path', ctx=Store())],
            value=List(
                lineno=31,
                col_offset=17,
                end_lineno=31,
                end_col_offset=31,
                elts=[Constant(lineno=31, col_offset=18, end_lineno=31, end_col_offset=30, value='_templates', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            lineno=34,
            col_offset=0,
            end_lineno=34,
            end_col_offset=22,
            targets=[Name(lineno=34, col_offset=0, end_lineno=34, end_col_offset=13, id='source_suffix', ctx=Store())],
            value=Constant(lineno=34, col_offset=16, end_lineno=34, end_col_offset=22, value='.rst', kind=None),
            type_comment=None,
        ),
        Assign(
            lineno=40,
            col_offset=0,
            end_lineno=40,
            end_col_offset=20,
            targets=[Name(lineno=40, col_offset=0, end_lineno=40, end_col_offset=10, id='master_doc', ctx=Store())],
            value=Constant(lineno=40, col_offset=13, end_lineno=40, end_col_offset=20, value='index', kind=None),
            type_comment=None,
        ),
        Assign(
            lineno=43,
            col_offset=0,
            end_lineno=43,
            end_col_offset=18,
            targets=[Name(lineno=43, col_offset=0, end_lineno=43, end_col_offset=7, id='project', ctx=Store())],
            value=Constant(lineno=43, col_offset=10, end_lineno=43, end_col_offset=18, value='py.js', kind='u'),
            type_comment=None,
        ),
        Assign(
            lineno=44,
            col_offset=0,
            end_lineno=44,
            end_col_offset=33,
            targets=[Name(lineno=44, col_offset=0, end_lineno=44, end_col_offset=9, id='copyright', ctx=Store())],
            value=Constant(lineno=44, col_offset=12, end_lineno=44, end_col_offset=33, value='2012, Xavier Morel', kind='u'),
            type_comment=None,
        ),
        Assign(
            lineno=51,
            col_offset=0,
            end_lineno=51,
            end_col_offset=15,
            targets=[Name(lineno=51, col_offset=0, end_lineno=51, end_col_offset=7, id='version', ctx=Store())],
            value=Constant(lineno=51, col_offset=10, end_lineno=51, end_col_offset=15, value='0.6', kind=None),
            type_comment=None,
        ),
        Assign(
            lineno=53,
            col_offset=0,
            end_lineno=53,
            end_col_offset=15,
            targets=[Name(lineno=53, col_offset=0, end_lineno=53, end_col_offset=7, id='release', ctx=Store())],
            value=Constant(lineno=53, col_offset=10, end_lineno=53, end_col_offset=15, value='0.6', kind=None),
            type_comment=None,
        ),
        Assign(
            lineno=67,
            col_offset=0,
            end_lineno=67,
            end_col_offset=29,
            targets=[Name(lineno=67, col_offset=0, end_lineno=67, end_col_offset=16, id='exclude_patterns', ctx=Store())],
            value=List(
                lineno=67,
                col_offset=19,
                end_lineno=67,
                end_col_offset=29,
                elts=[Constant(lineno=67, col_offset=20, end_lineno=67, end_col_offset=28, value='_build', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            lineno=73,
            col_offset=0,
            end_lineno=73,
            end_col_offset=21,
            targets=[Name(lineno=73, col_offset=0, end_lineno=73, end_col_offset=14, id='default_domain', ctx=Store())],
            value=Constant(lineno=73, col_offset=17, end_lineno=73, end_col_offset=21, value='js', kind=None),
            type_comment=None,
        ),
        Assign(
            lineno=87,
            col_offset=0,
            end_lineno=87,
            end_col_offset=25,
            targets=[Name(lineno=87, col_offset=0, end_lineno=87, end_col_offset=14, id='pygments_style', ctx=Store())],
            value=Constant(lineno=87, col_offset=17, end_lineno=87, end_col_offset=25, value='sphinx', kind=None),
            type_comment=None,
        ),
        Assign(
            lineno=89,
            col_offset=0,
            end_lineno=89,
            end_col_offset=33,
            targets=[Name(lineno=89, col_offset=0, end_lineno=89, end_col_offset=18, id='highlight_language', ctx=Store())],
            value=Constant(lineno=89, col_offset=21, end_lineno=89, end_col_offset=33, value='javascript', kind=None),
            type_comment=None,
        ),
        Assign(
            lineno=99,
            col_offset=0,
            end_lineno=99,
            end_col_offset=22,
            targets=[Name(lineno=99, col_offset=0, end_lineno=99, end_col_offset=10, id='html_theme', ctx=Store())],
            value=Constant(lineno=99, col_offset=13, end_lineno=99, end_col_offset=22, value='default', kind=None),
            type_comment=None,
        ),
        Assign(
            lineno=128,
            col_offset=0,
            end_lineno=128,
            end_col_offset=30,
            targets=[Name(lineno=128, col_offset=0, end_lineno=128, end_col_offset=16, id='html_static_path', ctx=Store())],
            value=List(
                lineno=128,
                col_offset=19,
                end_lineno=128,
                end_col_offset=30,
                elts=[Constant(lineno=128, col_offset=20, end_lineno=128, end_col_offset=29, value='_static', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            lineno=172,
            col_offset=0,
            end_lineno=172,
            end_col_offset=29,
            targets=[Name(lineno=172, col_offset=0, end_lineno=172, end_col_offset=17, id='htmlhelp_basename', ctx=Store())],
            value=Constant(lineno=172, col_offset=20, end_lineno=172, end_col_offset=29, value='pyjsdoc', kind=None),
            type_comment=None,
        ),
        Assign(
            lineno=177,
            col_offset=0,
            end_lineno=186,
            end_col_offset=1,
            targets=[Name(lineno=177, col_offset=0, end_lineno=177, end_col_offset=14, id='latex_elements', ctx=Store())],
            value=Dict(lineno=177, col_offset=17, end_lineno=186, end_col_offset=1, keys=[], values=[]),
            type_comment=None,
        ),
        Assign(
            lineno=190,
            col_offset=0,
            end_lineno=193,
            end_col_offset=1,
            targets=[Name(lineno=190, col_offset=0, end_lineno=190, end_col_offset=15, id='latex_documents', ctx=Store())],
            value=List(
                lineno=190,
                col_offset=18,
                end_lineno=193,
                end_col_offset=1,
                elts=[
                    Tuple(
                        lineno=191,
                        col_offset=2,
                        end_lineno=192,
                        end_col_offset=29,
                        elts=[
                            Constant(lineno=191, col_offset=3, end_lineno=191, end_col_offset=10, value='index', kind=None),
                            Constant(lineno=191, col_offset=12, end_lineno=191, end_col_offset=22, value='pyjs.tex', kind=None),
                            Constant(lineno=191, col_offset=24, end_lineno=191, end_col_offset=46, value='py.js Documentation', kind='u'),
                            Constant(lineno=192, col_offset=3, end_lineno=192, end_col_offset=18, value='Xavier Morel', kind='u'),
                            Constant(lineno=192, col_offset=20, end_lineno=192, end_col_offset=28, value='manual', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            lineno=220,
            col_offset=0,
            end_lineno=223,
            end_col_offset=1,
            targets=[Name(lineno=220, col_offset=0, end_lineno=220, end_col_offset=9, id='man_pages', ctx=Store())],
            value=List(
                lineno=220,
                col_offset=12,
                end_lineno=223,
                end_col_offset=1,
                elts=[
                    Tuple(
                        lineno=221,
                        col_offset=4,
                        end_lineno=222,
                        end_col_offset=26,
                        elts=[
                            Constant(lineno=221, col_offset=5, end_lineno=221, end_col_offset=12, value='index', kind=None),
                            Constant(lineno=221, col_offset=14, end_lineno=221, end_col_offset=20, value='pyjs', kind=None),
                            Constant(lineno=221, col_offset=22, end_lineno=221, end_col_offset=44, value='py.js Documentation', kind='u'),
                            List(
                                lineno=222,
                                col_offset=5,
                                end_lineno=222,
                                end_col_offset=22,
                                elts=[Constant(lineno=222, col_offset=6, end_lineno=222, end_col_offset=21, value='Xavier Morel', kind='u')],
                                ctx=Load(),
                            ),
                            Constant(lineno=222, col_offset=24, end_lineno=222, end_col_offset=25, value=1, kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            lineno=234,
            col_offset=0,
            end_lineno=238,
            end_col_offset=1,
            targets=[Name(lineno=234, col_offset=0, end_lineno=234, end_col_offset=17, id='texinfo_documents', ctx=Store())],
            value=List(
                lineno=234,
                col_offset=20,
                end_lineno=238,
                end_col_offset=1,
                elts=[
                    Tuple(
                        lineno=235,
                        col_offset=2,
                        end_lineno=237,
                        end_col_offset=19,
                        elts=[
                            Constant(lineno=235, col_offset=3, end_lineno=235, end_col_offset=10, value='index', kind=None),
                            Constant(lineno=235, col_offset=12, end_lineno=235, end_col_offset=18, value='pyjs', kind=None),
                            Constant(lineno=235, col_offset=20, end_lineno=235, end_col_offset=42, value='py.js Documentation', kind='u'),
                            Constant(lineno=236, col_offset=3, end_lineno=236, end_col_offset=18, value='Xavier Morel', kind='u'),
                            Constant(lineno=236, col_offset=20, end_lineno=236, end_col_offset=26, value='pyjs', kind=None),
                            Constant(lineno=236, col_offset=28, end_lineno=236, end_col_offset=62, value='One line description of project.', kind=None),
                            Constant(lineno=237, col_offset=3, end_lineno=237, end_col_offset=18, value='Miscellaneous', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)