# -*- coding: utf-8 -*-
import os
import pandas as pd
from pyEX import Client, PyEXception


def _get_data(symbol, start, end, client=None):
    if client is None and not os.environ.get('IEX_TOKEN'):
        raise PyEXception('Must provide pyEX client or set IEX_TOKEN environment variable')
    elif client is None:
        client = Client()

    df = client.chartDF(symbol, '5y')
    if start:
        df = df[df.index > start]
    if end:
        df = df[df.index < end]

    return df


def load_from_iex(symbols, start=None, end=None, client=None):

    data = {}
    for symbol in symbols:
        data[symbol] = _get_data(symbol, start, end, client)
    mi_data = pd.concat(data, axis=1)
    return mi_data
