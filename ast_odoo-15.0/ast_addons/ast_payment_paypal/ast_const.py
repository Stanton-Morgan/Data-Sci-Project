Module(
    body=[
        Assign(
            lineno=4,
            col_offset=0,
            end_lineno=30,
            end_col_offset=1,
            targets=[Name(lineno=4, col_offset=0, end_lineno=4, end_col_offset=20, id='SUPPORTED_CURRENCIES', ctx=Store())],
            value=Tuple(
                lineno=4,
                col_offset=23,
                end_lineno=30,
                end_col_offset=1,
                elts=[
                    Constant(lineno=5, col_offset=4, end_lineno=5, end_col_offset=9, value='AUD', kind=None),
                    Constant(lineno=6, col_offset=4, end_lineno=6, end_col_offset=9, value='BRL', kind=None),
                    Constant(lineno=7, col_offset=4, end_lineno=7, end_col_offset=9, value='CAD', kind=None),
                    Constant(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, value='CNY', kind=None),
                    Constant(lineno=9, col_offset=4, end_lineno=9, end_col_offset=9, value='CZK', kind=None),
                    Constant(lineno=10, col_offset=4, end_lineno=10, end_col_offset=9, value='DKK', kind=None),
                    Constant(lineno=11, col_offset=4, end_lineno=11, end_col_offset=9, value='EUR', kind=None),
                    Constant(lineno=12, col_offset=4, end_lineno=12, end_col_offset=9, value='HKD', kind=None),
                    Constant(lineno=13, col_offset=4, end_lineno=13, end_col_offset=9, value='HUF', kind=None),
                    Constant(lineno=14, col_offset=4, end_lineno=14, end_col_offset=9, value='ILS', kind=None),
                    Constant(lineno=15, col_offset=4, end_lineno=15, end_col_offset=9, value='JPY', kind=None),
                    Constant(lineno=16, col_offset=4, end_lineno=16, end_col_offset=9, value='MYR', kind=None),
                    Constant(lineno=17, col_offset=4, end_lineno=17, end_col_offset=9, value='MXN', kind=None),
                    Constant(lineno=18, col_offset=4, end_lineno=18, end_col_offset=9, value='TWD', kind=None),
                    Constant(lineno=19, col_offset=4, end_lineno=19, end_col_offset=9, value='NZD', kind=None),
                    Constant(lineno=20, col_offset=4, end_lineno=20, end_col_offset=9, value='NOK', kind=None),
                    Constant(lineno=21, col_offset=4, end_lineno=21, end_col_offset=9, value='PHP', kind=None),
                    Constant(lineno=22, col_offset=4, end_lineno=22, end_col_offset=9, value='PLN', kind=None),
                    Constant(lineno=23, col_offset=4, end_lineno=23, end_col_offset=9, value='GBP', kind=None),
                    Constant(lineno=24, col_offset=4, end_lineno=24, end_col_offset=9, value='RUB', kind=None),
                    Constant(lineno=25, col_offset=4, end_lineno=25, end_col_offset=9, value='SGD', kind=None),
                    Constant(lineno=26, col_offset=4, end_lineno=26, end_col_offset=9, value='SEK', kind=None),
                    Constant(lineno=27, col_offset=4, end_lineno=27, end_col_offset=9, value='CHF', kind=None),
                    Constant(lineno=28, col_offset=4, end_lineno=28, end_col_offset=9, value='THB', kind=None),
                    Constant(lineno=29, col_offset=4, end_lineno=29, end_col_offset=9, value='USD', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            lineno=34,
            col_offset=0,
            end_lineno=38,
            end_col_offset=1,
            targets=[Name(lineno=34, col_offset=0, end_lineno=34, end_col_offset=22, id='PAYMENT_STATUS_MAPPING', ctx=Store())],
            value=Dict(
                lineno=34,
                col_offset=25,
                end_lineno=38,
                end_col_offset=1,
                keys=[
                    Constant(lineno=35, col_offset=4, end_lineno=35, end_col_offset=13, value='pending', kind=None),
                    Constant(lineno=36, col_offset=4, end_lineno=36, end_col_offset=10, value='done', kind=None),
                    Constant(lineno=37, col_offset=4, end_lineno=37, end_col_offset=12, value='cancel', kind=None),
                ],
                values=[
                    Tuple(
                        lineno=35,
                        col_offset=15,
                        end_lineno=35,
                        end_col_offset=27,
                        elts=[Constant(lineno=35, col_offset=16, end_lineno=35, end_col_offset=25, value='Pending', kind=None)],
                        ctx=Load(),
                    ),
                    Tuple(
                        lineno=36,
                        col_offset=12,
                        end_lineno=36,
                        end_col_offset=38,
                        elts=[
                            Constant(lineno=36, col_offset=13, end_lineno=36, end_col_offset=24, value='Processed', kind=None),
                            Constant(lineno=36, col_offset=26, end_lineno=36, end_col_offset=37, value='Completed', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        lineno=37,
                        col_offset=14,
                        end_lineno=37,
                        end_col_offset=35,
                        elts=[
                            Constant(lineno=37, col_offset=15, end_lineno=37, end_col_offset=23, value='Voided', kind=None),
                            Constant(lineno=37, col_offset=25, end_lineno=37, end_col_offset=34, value='Expired', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
