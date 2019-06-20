#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/20 上午8:56
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : count_gene_number.py
# @Software: PyCharm

import os
import sys
import pandas as pd
import sys


def con(infile):
    df = pd.read_csv(infile, sep='\t')
    a = df.iloc[:, 1].sum()
    b = a - df.iloc[0, 1] - df.iloc[1, 1]
    return a, b


infile = sys.argv[1]
a, b = con(infile)
relist = [a, b]
relist.insert(0, infile.split('/')[-1].replace('_genefamilies.tsv', ''))
relist = [str(i) for i in relist]
re_str = '\t'.join(relist)
print(re_str)


def main():
    pass


if __name__ == '__main__':
    main()
