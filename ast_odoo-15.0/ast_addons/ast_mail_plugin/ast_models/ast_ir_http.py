Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=42,
            module='werkzeug.exceptions',
            names=[alias(name='BadRequest', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=26,
            end_col_offset=29,
            name='IrHttp',
            bases=[
                Attribute(
                    lineno=9,
                    col_offset=13,
                    end_lineno=9,
                    end_col_offset=33,
                    value=Name(lineno=9, col_offset=13, end_lineno=9, end_col_offset=19, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=24,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=10, col_offset=15, end_lineno=10, end_col_offset=24, value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=26,
                    end_col_offset=29,
                    name='_auth_method_outlook',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=29, end_lineno=13, end_col_offset=32, arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=71,
                            targets=[Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=20, id='access_token', ctx=Store())],
                            value=Call(
                                lineno=14,
                                col_offset=23,
                                end_lineno=14,
                                end_col_offset=71,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=23,
                                    end_lineno=14,
                                    end_col_offset=54,
                                    value=Attribute(
                                        lineno=14,
                                        col_offset=23,
                                        end_lineno=14,
                                        end_col_offset=50,
                                        value=Attribute(
                                            lineno=14,
                                            col_offset=23,
                                            end_lineno=14,
                                            end_col_offset=42,
                                            value=Name(lineno=14, col_offset=23, end_lineno=14, end_col_offset=30, id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=14, col_offset=55, end_lineno=14, end_col_offset=70, value='Authorization', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=15,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=52,
                            test=UnaryOp(
                                lineno=15,
                                col_offset=11,
                                end_lineno=15,
                                end_col_offset=27,
                                op=Not(),
                                operand=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=27, id='access_token', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=52,
                                    exc=Call(
                                        lineno=16,
                                        col_offset=18,
                                        end_lineno=16,
                                        end_col_offset=52,
                                        func=Name(lineno=16, col_offset=18, end_lineno=16, end_col_offset=28, id='BadRequest', ctx=Load()),
                                        args=[Constant(lineno=16, col_offset=29, end_lineno=16, end_col_offset=51, value='Access token missing', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            lineno=18,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=43,
                            test=Call(
                                lineno=18,
                                col_offset=11,
                                end_lineno=18,
                                end_col_offset=45,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=11,
                                    end_lineno=18,
                                    end_col_offset=34,
                                    value=Name(lineno=18, col_offset=11, end_lineno=18, end_col_offset=23, id='access_token', ctx=Load()),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=18, col_offset=35, end_lineno=18, end_col_offset=44, value='Bearer ', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=19,
                                    end_col_offset=43,
                                    targets=[Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=24, id='access_token', ctx=Store())],
                                    value=Subscript(
                                        lineno=19,
                                        col_offset=27,
                                        end_lineno=19,
                                        end_col_offset=43,
                                        value=Name(lineno=19, col_offset=27, end_lineno=19, end_col_offset=39, id='access_token', ctx=Load()),
                                        slice=Slice(
                                            lineno=19,
                                            col_offset=40,
                                            end_lineno=19,
                                            end_col_offset=42,
                                            lower=Constant(lineno=19, col_offset=40, end_lineno=19, end_col_offset=41, value=7, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=116,
                            targets=[Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=15, id='user_id', ctx=Store())],
                            value=Call(
                                lineno=21,
                                col_offset=18,
                                end_lineno=21,
                                end_col_offset=116,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=18,
                                    end_lineno=21,
                                    end_col_offset=69,
                                    value=Subscript(
                                        lineno=21,
                                        col_offset=18,
                                        end_lineno=21,
                                        end_col_offset=50,
                                        value=Attribute(
                                            lineno=21,
                                            col_offset=18,
                                            end_lineno=21,
                                            end_col_offset=29,
                                            value=Name(lineno=21, col_offset=18, end_lineno=21, end_col_offset=25, id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=21, col_offset=30, end_lineno=21, end_col_offset=49, value='res.users.apikeys', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_check_credentials',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        lineno=21,
                                        col_offset=70,
                                        end_lineno=21,
                                        end_col_offset=97,
                                        arg='scope',
                                        value=Constant(lineno=21, col_offset=76, end_lineno=21, end_col_offset=97, value='odoo.plugin.outlook', kind=None),
                                    ),
                                    keyword(
                                        lineno=21,
                                        col_offset=99,
                                        end_lineno=21,
                                        end_col_offset=115,
                                        arg='key',
                                        value=Name(lineno=21, col_offset=103, end_lineno=21, end_col_offset=115, id='access_token', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=22,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=52,
                            test=UnaryOp(
                                lineno=22,
                                col_offset=11,
                                end_lineno=22,
                                end_col_offset=22,
                                op=Not(),
                                operand=Name(lineno=22, col_offset=15, end_lineno=22, end_col_offset=22, id='user_id', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    lineno=23,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=52,
                                    exc=Call(
                                        lineno=23,
                                        col_offset=18,
                                        end_lineno=23,
                                        end_col_offset=52,
                                        func=Name(lineno=23, col_offset=18, end_lineno=23, end_col_offset=28, id='BadRequest', ctx=Load()),
                                        args=[Constant(lineno=23, col_offset=29, end_lineno=23, end_col_offset=51, value='Access token invalid', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=29,
                            targets=[
                                Attribute(
                                    lineno=26,
                                    col_offset=8,
                                    end_lineno=26,
                                    end_col_offset=19,
                                    value=Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=15, id='request', ctx=Load()),
                                    attr='uid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(lineno=26, col_offset=22, end_lineno=26, end_col_offset=29, id='user_id', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(lineno=12, col_offset=5, end_lineno=12, end_col_offset=16, id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
