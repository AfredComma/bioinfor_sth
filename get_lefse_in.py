#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/25 下午4:34
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : get_lefse_in.py
# @Software: PyCharm

import os
import sys
import pandas as pd


def main(in_file, map_file):
    df = pd.read_csv(in_file, sep='\t', index_col=0)
    dfmap = pd.read_csv(map_file, sep='\t', index_col=0)
    dfmap2 = dfmap.T
    w = dfmap.index.to_list()
    df2 = df[w]
    dfre = pd.concat([dfmap2, df2])
    return dfre


if __name__ == '__main__':
    dfre = main(sys.argv[1], sys.argv[2])
    dfre.to_csv(sys.argv[3], sep='\t')
