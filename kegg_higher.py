#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/27 下午6:11
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : kegg_higher.py
# @Software: PyCharm

import os
import sys
import pandas as pd
import numpy as np


def main(infile, outfile, level='level2'):
    df = pd.read_csv(infile, sep='\t', index_col=0)
    df = df[df['level4^level3^level2^level1'] != 'None']
    ulist = df['level4^level3^level2^level1'].to_list()
    level_n = 'level4^level3^level2^level1'.split('^').index(level)
    level_list = [i.split('^')[level_n] for i in ulist]
    df.index = level_list
    df = df.drop(['level4^level3^level2^level1'], axis=1)
    df2 = df[:]
    df3 = df2.sum(level=0)
    df3.to_csv(outfile, sep='\t')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
