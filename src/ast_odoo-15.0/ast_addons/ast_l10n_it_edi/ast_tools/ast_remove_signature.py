Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=14,
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=15,
            names=[alias(name='warnings', asname=None)],
        ),
        Assign(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=37,
            targets=[Name(lineno=7, col_offset=0, end_lineno=7, end_col_offset=7, id='_logger', ctx=Store())],
            value=Call(
                lineno=7,
                col_offset=10,
                end_lineno=7,
                end_col_offset=37,
                func=Attribute(
                    lineno=7,
                    col_offset=10,
                    end_lineno=7,
                    end_col_offset=27,
                    value=Name(lineno=7, col_offset=10, end_lineno=7, end_col_offset=17, id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(lineno=7, col_offset=28, end_lineno=7, end_col_offset=36, id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Try(
            lineno=9,
            col_offset=0,
            end_lineno=14,
            end_col_offset=86,
            body=[
                ImportFrom(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=44,
                    module='OpenSSL',
                    names=[alias(name='crypto', asname='ssl_crypto')],
                    level=0,
                ),
                Import(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=36,
                    names=[alias(name='OpenSSL._util', asname='ssl_util')],
                ),
            ],
            handlers=[
                ExceptHandler(
                    lineno=12,
                    col_offset=0,
                    end_lineno=14,
                    end_col_offset=86,
                    type=Name(lineno=12, col_offset=7, end_lineno=12, end_col_offset=18, id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            lineno=13,
                            col_offset=4,
                            end_lineno=13,
                            end_col_offset=21,
                            targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=14, id='ssl_crypto', ctx=Store())],
                            value=Constant(lineno=13, col_offset=17, end_lineno=13, end_col_offset=21, value=None, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=14,
                            col_offset=4,
                            end_lineno=14,
                            end_col_offset=86,
                            value=Call(
                                lineno=14,
                                col_offset=4,
                                end_lineno=14,
                                end_col_offset=86,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=4,
                                    end_lineno=14,
                                    end_col_offset=19,
                                    value=Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=11, id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=14, col_offset=20, end_lineno=14, end_col_offset=85, value="Cannot import library 'OpenSSL' for PKCS#7 envelope extraction.", kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        FunctionDef(
            lineno=17,
            col_offset=0,
            end_lineno=47,
            end_col_offset=26,
            name='remove_signature',
            args=arguments(
                posonlyargs=[],
                args=[arg(lineno=17, col_offset=21, end_lineno=17, end_col_offset=28, arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    lineno=18,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=99,
                    value=Constant(lineno=18, col_offset=4, end_lineno=19, end_col_offset=99, value=" Remove the PKCS#7 envelope from given content, making a '.xml.p7m' file content readable as it was '.xml'.\n        As OpenSSL may not be installed, in that case a warning is issued and None is returned. ", kind=None),
                ),
                If(
                    lineno=22,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=19,
                    test=UnaryOp(
                        lineno=22,
                        col_offset=7,
                        end_lineno=22,
                        end_col_offset=21,
                        op=Not(),
                        operand=Name(lineno=22, col_offset=11, end_lineno=22, end_col_offset=21, id='ssl_crypto', ctx=Load()),
                    ),
                    body=[
                        Expr(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=131,
                            value=Call(
                                lineno=23,
                                col_offset=8,
                                end_lineno=23,
                                end_col_offset=131,
                                func=Attribute(
                                    lineno=23,
                                    col_offset=8,
                                    end_lineno=23,
                                    end_col_offset=23,
                                    value=Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=15, id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=23, col_offset=24, end_lineno=23, end_col_offset=130, value='Error reading the content, check if the OpenSSL library is installed for for PKCS#7 envelope extraction.', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=19,
                            value=Constant(lineno=24, col_offset=15, end_lineno=24, end_col_offset=19, value=None, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=27,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=28,
                    targets=[Name(lineno=27, col_offset=4, end_lineno=27, end_col_offset=8, id='null', ctx=Store())],
                    value=Attribute(
                        lineno=27,
                        col_offset=11,
                        end_lineno=27,
                        end_col_offset=28,
                        value=Attribute(
                            lineno=27,
                            col_offset=11,
                            end_lineno=27,
                            end_col_offset=23,
                            value=Name(lineno=27, col_offset=11, end_lineno=27, end_col_offset=19, id='ssl_util', ctx=Load()),
                            attr='ffi',
                            ctx=Load(),
                        ),
                        attr='NULL',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=28,
                    col_offset=4,
                    end_lineno=28,
                    end_col_offset=38,
                    targets=[Name(lineno=28, col_offset=4, end_lineno=28, end_col_offset=10, id='verify', ctx=Store())],
                    value=Attribute(
                        lineno=28,
                        col_offset=13,
                        end_lineno=28,
                        end_col_offset=38,
                        value=Attribute(
                            lineno=28,
                            col_offset=13,
                            end_lineno=28,
                            end_col_offset=25,
                            value=Name(lineno=28, col_offset=13, end_lineno=28, end_col_offset=21, id='ssl_util', ctx=Load()),
                            attr='lib',
                            ctx=Load(),
                        ),
                        attr='PKCS7_verify',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=31,
                    col_offset=4,
                    end_lineno=31,
                    end_col_offset=67,
                    targets=[Name(lineno=31, col_offset=4, end_lineno=31, end_col_offset=9, id='flags', ctx=Store())],
                    value=BinOp(
                        lineno=31,
                        col_offset=12,
                        end_lineno=31,
                        end_col_offset=67,
                        left=Attribute(
                            lineno=31,
                            col_offset=12,
                            end_lineno=31,
                            end_col_offset=39,
                            value=Attribute(
                                lineno=31,
                                col_offset=12,
                                end_lineno=31,
                                end_col_offset=24,
                                value=Name(lineno=31, col_offset=12, end_lineno=31, end_col_offset=20, id='ssl_util', ctx=Load()),
                                attr='lib',
                                ctx=Load(),
                            ),
                            attr='PKCS7_NOVERIFY',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            lineno=31,
                            col_offset=42,
                            end_lineno=31,
                            end_col_offset=67,
                            value=Attribute(
                                lineno=31,
                                col_offset=42,
                                end_lineno=31,
                                end_col_offset=54,
                                value=Name(lineno=31, col_offset=42, end_lineno=31, end_col_offset=50, id='ssl_util', ctx=Load()),
                                attr='lib',
                                ctx=Load(),
                            ),
                            attr='PKCS7_NOSIGS',
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=34,
                    col_offset=4,
                    end_lineno=34,
                    end_col_offset=42,
                    targets=[Name(lineno=34, col_offset=4, end_lineno=34, end_col_offset=14, id='out_buffer', ctx=Store())],
                    value=Call(
                        lineno=34,
                        col_offset=17,
                        end_lineno=34,
                        end_col_offset=42,
                        func=Attribute(
                            lineno=34,
                            col_offset=17,
                            end_lineno=34,
                            end_col_offset=40,
                            value=Name(lineno=34, col_offset=17, end_lineno=34, end_col_offset=27, id='ssl_crypto', ctx=Load()),
                            attr='_new_mem_buf',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                With(
                    lineno=37,
                    col_offset=4,
                    end_lineno=39,
                    end_col_offset=83,
                    items=[
                        withitem(
                            context_expr=Call(
                                lineno=37,
                                col_offset=9,
                                end_lineno=37,
                                end_col_offset=34,
                                func=Attribute(
                                    lineno=37,
                                    col_offset=9,
                                    end_lineno=37,
                                    end_col_offset=32,
                                    value=Name(lineno=37, col_offset=9, end_lineno=37, end_col_offset=17, id='warnings', ctx=Load()),
                                    attr='catch_warnings',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=None,
                        ),
                    ],
                    body=[
                        Expr(
                            lineno=38,
                            col_offset=8,
                            end_lineno=38,
                            end_col_offset=70,
                            value=Call(
                                lineno=38,
                                col_offset=8,
                                end_lineno=38,
                                end_col_offset=70,
                                func=Attribute(
                                    lineno=38,
                                    col_offset=8,
                                    end_lineno=38,
                                    end_col_offset=31,
                                    value=Name(lineno=38, col_offset=8, end_lineno=38, end_col_offset=16, id='warnings', ctx=Load()),
                                    attr='filterwarnings',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=38, col_offset=32, end_lineno=38, end_col_offset=40, value='ignore', kind=None)],
                                keywords=[
                                    keyword(
                                        lineno=38,
                                        col_offset=42,
                                        end_lineno=38,
                                        end_col_offset=69,
                                        arg='category',
                                        value=Name(lineno=38, col_offset=51, end_lineno=38, end_col_offset=69, id='DeprecationWarning', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            lineno=39,
                            col_offset=8,
                            end_lineno=39,
                            end_col_offset=83,
                            targets=[Name(lineno=39, col_offset=8, end_lineno=39, end_col_offset=19, id='loaded_data', ctx=Store())],
                            value=Call(
                                lineno=39,
                                col_offset=22,
                                end_lineno=39,
                                end_col_offset=83,
                                func=Attribute(
                                    lineno=39,
                                    col_offset=22,
                                    end_lineno=39,
                                    end_col_offset=48,
                                    value=Name(lineno=39, col_offset=22, end_lineno=39, end_col_offset=32, id='ssl_crypto', ctx=Load()),
                                    attr='load_pkcs7_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=39,
                                        col_offset=49,
                                        end_lineno=39,
                                        end_col_offset=73,
                                        value=Name(lineno=39, col_offset=49, end_lineno=39, end_col_offset=59, id='ssl_crypto', ctx=Load()),
                                        attr='FILETYPE_ASN1',
                                        ctx=Load(),
                                    ),
                                    Name(lineno=39, col_offset=75, end_lineno=39, end_col_offset=82, id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    type_comment=None,
                ),
                If(
                    lineno=42,
                    col_offset=4,
                    end_lineno=43,
                    end_col_offset=41,
                    test=Compare(
                        lineno=42,
                        col_offset=7,
                        end_lineno=42,
                        end_col_offset=75,
                        left=Call(
                            lineno=42,
                            col_offset=7,
                            end_lineno=42,
                            end_col_offset=70,
                            func=Name(lineno=42, col_offset=7, end_lineno=42, end_col_offset=13, id='verify', ctx=Load()),
                            args=[
                                Attribute(
                                    lineno=42,
                                    col_offset=14,
                                    end_lineno=42,
                                    end_col_offset=32,
                                    value=Name(lineno=42, col_offset=14, end_lineno=42, end_col_offset=25, id='loaded_data', ctx=Load()),
                                    attr='_pkcs7',
                                    ctx=Load(),
                                ),
                                Name(lineno=42, col_offset=34, end_lineno=42, end_col_offset=38, id='null', ctx=Load()),
                                Name(lineno=42, col_offset=40, end_lineno=42, end_col_offset=44, id='null', ctx=Load()),
                                Name(lineno=42, col_offset=46, end_lineno=42, end_col_offset=50, id='null', ctx=Load()),
                                Name(lineno=42, col_offset=52, end_lineno=42, end_col_offset=62, id='out_buffer', ctx=Load()),
                                Name(lineno=42, col_offset=64, end_lineno=42, end_col_offset=69, id='flags', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                        ops=[NotEq()],
                        comparators=[Constant(lineno=42, col_offset=74, end_lineno=42, end_col_offset=75, value=1, kind=None)],
                    ),
                    body=[
                        Expr(
                            lineno=43,
                            col_offset=8,
                            end_lineno=43,
                            end_col_offset=41,
                            value=Call(
                                lineno=43,
                                col_offset=8,
                                end_lineno=43,
                                end_col_offset=41,
                                func=Attribute(
                                    lineno=43,
                                    col_offset=8,
                                    end_lineno=43,
                                    end_col_offset=39,
                                    value=Name(lineno=43, col_offset=8, end_lineno=43, end_col_offset=18, id='ssl_crypto', ctx=Load()),
                                    attr='_raise_current_error',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=46,
                    col_offset=4,
                    end_lineno=46,
                    end_col_offset=59,
                    targets=[Name(lineno=46, col_offset=4, end_lineno=46, end_col_offset=19, id='decoded_content', ctx=Store())],
                    value=Call(
                        lineno=46,
                        col_offset=22,
                        end_lineno=46,
                        end_col_offset=59,
                        func=Attribute(
                            lineno=46,
                            col_offset=22,
                            end_lineno=46,
                            end_col_offset=47,
                            value=Name(lineno=46, col_offset=22, end_lineno=46, end_col_offset=32, id='ssl_crypto', ctx=Load()),
                            attr='_bio_to_string',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=46, col_offset=48, end_lineno=46, end_col_offset=58, id='out_buffer', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    lineno=47,
                    col_offset=4,
                    end_lineno=47,
                    end_col_offset=26,
                    value=Name(lineno=47, col_offset=11, end_lineno=47, end_col_offset=26, id='decoded_content', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)