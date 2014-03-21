"""
Objective: Import Walmart data and learn pandas.

Developer Notes: Be worried.
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH_GITHUB = 'E:/GitHub/'
PATH_RAW = os.path.join(PATH_GITHUB, 'Kaggle-Walmart/00_Raw_Data')


def wrap_read_csv(name_data, name_indices, name_dates=['Date']):
    """Decorate pd.read_csv() to remove duplication"""

    df = pd.read_csv(
        os.path.join(PATH_RAW, '{}.csv'.format(name_data)),
        index_col=name_indices,
        parse_dates=name_dates
        )

    assert df.index.is_unique, "{}'s index has dups.".format(name_data)

    df.index.names = map(str.lower, df.index.names)
    df.columns = map(str.lower, df.columns)

    print '\n\n==== {}.info() ====\n'.format(name_data)
    print 'Indices: {}\n'.format(df.index.names)
    print df.info()
    return df

train = wrap_read_csv('train', ['Store', 'Dept', 'Date'])
test = wrap_read_csv('test', ['Store', 'Dept', 'Date'])
features = wrap_read_csv('features', ['Store', 'Date'])
stores = wrap_read_csv('stores', ['Store'], False)
