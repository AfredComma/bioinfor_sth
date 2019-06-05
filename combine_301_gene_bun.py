#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/4 下午4:16
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : combine_301_gene_bun.py
# @Software: PyCharm

import os
import sys
import pandas as pd


def seek_read(in_dir):
    alist = os.listdir(in_dir)
    ulist = [i for i in alist if 'AG' in i]
    qlist = [os.path.join(j, 'humann2-bypass-translated-search', j + '_genefamilies.tsv') for j in ulist]
    dfre = pd.DataFrame()
    for q in qlist:
        dfq = pd.read_csv(q, sep='\t', index_col=0)
        dfre = pd.concat([dfre, dfq], axis=1)
    return dfre


def main():
    pass


if __name__ == '__main__':
    main()
