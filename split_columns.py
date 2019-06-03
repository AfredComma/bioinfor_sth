#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/3 上午11:25
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : split_columns.py
# @Software: PyCharm

import os
import sys
import pandas as pd


def ss(df, k):
    inlist = df.columns.to_list()
    n = len(inlist)
    a = list(range(n))
    b = a[::k]
    c = [i for i in b[1:]]
    c.append(a[-1] + 1)
    nn = len(b)
    for i in range(nn):
        w = inlist[b[i]:c[i]]
        dfone = df[w]
        print(dfone.head())
        out_file = str(i) + '_gene_count.tsv'
        dfone.to_csv(out_file, sep='\t')


def relative_abundance(df):
    return df / df.sum(axis=0)


def split_trans_abun(df, k):
    in_list = df.columns.to_list()
    n = len(in_list)
    a = list(range(n))
    b = a[::k]
    c = [i for i in b[1:]]
    c.append(a[-1] + 1)
    nn = len(b)
    for i in range(nn):
        w = in_list[b[i]:c[i]]
        df_two = relative_abundance(df[w])
        print(df_two.head())
        out_file = str(i) + '_gene_relative_abun.tsv'
        df_two.to_csv(out_file, sep='\t')


def main(infile):
    df = pd.read_csv(infile, sep='\t', index_col=0)
    split_trans_abun(df, 10)


if __name__ == '__main__':
    main(sys.argv[1])
