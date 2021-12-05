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
            end_lineno=21,
            end_col_offset=5,
            name='ResConfigSettings',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=24,
                    end_lineno=7,
                    end_col_offset=45,
                    value=Name(lineno=7, col_offset=24, end_lineno=7, end_col_offset=30, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=36,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=36, value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=5,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=22, id='geoloc_provider_id', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=25,
                        end_lineno=15,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=10,
                            col_offset=25,
                            end_lineno=10,
                            end_col_offset=40,
                            value=Name(lineno=10, col_offset=25, end_lineno=10, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=11, col_offset=8, end_lineno=11, end_col_offset=27, value='base.geo_provider', kind=None)],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=20,
                                arg='string',
                                value=Constant(lineno=12, col_offset=15, end_lineno=12, end_col_offset=20, value='API', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=56,
                                arg='config_parameter',
                                value=Constant(lineno=13, col_offset=25, end_lineno=13, end_col_offset=56, value='base_geolocalize.geo_provider', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=8,
                                end_lineno=14,
                                end_col_offset=64,
                                arg='default',
                                value=Lambda(
                                    lineno=14,
                                    col_offset=16,
                                    end_lineno=14,
                                    end_col_offset=64,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=14, col_offset=23, end_lineno=14, end_col_offset=24, arg='x', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        lineno=14,
                                        col_offset=26,
                                        end_lineno=14,
                                        end_col_offset=64,
                                        func=Attribute(
                                            lineno=14,
                                            col_offset=26,
                                            end_lineno=14,
                                            end_col_offset=62,
                                            value=Subscript(
                                                lineno=14,
                                                col_offset=26,
                                                end_lineno=14,
                                                end_col_offset=48,
                                                value=Attribute(
                                                    lineno=14,
                                                    col_offset=26,
                                                    end_lineno=14,
                                                    end_col_offset=31,
                                                    value=Name(lineno=14, col_offset=26, end_lineno=14, end_col_offset=27, id='x', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=14, col_offset=32, end_lineno=14, end_col_offset=47, value='base.geocoder', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_provider',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=94,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=28, id='geoloc_provider_techname', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=31,
                        end_lineno=16,
                        end_col_offset=94,
                        func=Attribute(
                            lineno=16,
                            col_offset=31,
                            end_lineno=16,
                            end_col_offset=42,
                            value=Name(lineno=16, col_offset=31, end_lineno=16, end_col_offset=37, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=43,
                                end_lineno=16,
                                end_col_offset=81,
                                arg='related',
                                value=Constant(lineno=16, col_offset=51, end_lineno=16, end_col_offset=81, value='geoloc_provider_id.tech_name', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=83,
                                end_lineno=16,
                                end_col_offset=93,
                                arg='readonly',
                                value=Constant(lineno=16, col_offset=92, end_lineno=16, end_col_offset=93, value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=5,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=33, id='geoloc_provider_googlemap_key', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=36,
                        end_lineno=21,
                        end_col_offset=5,
                        func=Attribute(
                            lineno=17,
                            col_offset=36,
                            end_lineno=17,
                            end_col_offset=47,
                            value=Name(lineno=17, col_offset=36, end_lineno=17, end_col_offset=42, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=18,
                                col_offset=8,
                                end_lineno=18,
                                end_col_offset=35,
                                arg='string',
                                value=Constant(lineno=18, col_offset=15, end_lineno=18, end_col_offset=35, value='Google Map API Key', kind=None),
                            ),
                            keyword(
                                lineno=19,
                                col_offset=8,
                                end_lineno=19,
                                end_col_offset=62,
                                arg='config_parameter',
                                value=Constant(lineno=19, col_offset=25, end_lineno=19, end_col_offset=62, value='base_geolocalize.google_map_api_key', kind=None),
                            ),
                            keyword(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=113,
                                arg='help',
                                value=Constant(lineno=20, col_offset=13, end_lineno=20, end_col_offset=113, value='Visit https://developers.google.com/maps/documentation/geocoding/get-api-key for more information.', kind=None),
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
