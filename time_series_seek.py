#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/12 下午5:21
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : time_series_seek.py
# @Software: PyCharm

import os
import sys
import pandas as pd
import numpy as np


def deal_data_frame(infile):
    df = pd.read_csv(infile, sep='\t', index_col=0)
    print(df.head())
    a, b = df.shape
    dfre = pd.DataFrame(np.zeros((a * b, 4)))
    for i in range(b):
        dfre.iloc[list(range(i * a, (i + 1) * a)), 0] = df.iloc[:, i].tolist()
        dfre.iloc[list(range(i * a, (i + 1) * a)), 1] = df.index.to_list()
        dfre.iloc[list(range(i * a, (i + 1) * a)), 2] = [df.columns[i].split('_w')[0]] * a
        dfre.iloc[list(range(i * a, (i + 1) * a)), 3] = [df.columns[i].split('_w')[-1]] * a
    dfre.columns = ["value", "genus", "person", "period"]
    return dfre


def main(infile):
    dfre = deal_data_frame(infile)
    print(dfre.head())


if __name__ == '__main__':
    os.chdir(sys.argv[1])
    main(sys.argv[2])
