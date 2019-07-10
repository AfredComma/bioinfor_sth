#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/7/5 上午9:02
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : kegg_pathway_get.py
# @Software: PyCharm

import os
import sys
import pandas as pd
import numpy as np


def one(infile):
    df = pd.read_csv(infile, sep='\t', index_col=0)
    print(df.head())
    uselist = df.iloc[:, -1].to_list()
    aa, bb, cc, dd = ([], [], [], [])
    for j in uselist:
        try:
            a, b, c, d = j.split('^')
        except ValueError:
            a, b, c, d = ('', '', '', '')
        finally:
            aa.append(a)
            bb.append(b)
            cc.append(c)
            dd.append(d)
    df['l1'] = dd
    df['l2'] = cc
    df['l3'] = bb
    df['l4'] = aa
    return df


def two(df):
    cha = []
    print(df.head())
    for i in range(df.shape[0]):
        if df.iloc[i, 8] > 0.05:
            cha.append('#8DD3C7')  # normal
        else:
            if df.iloc[i, 0] < df.iloc[i, 1]:
                cha.append('#F98174')  # down
            elif df.iloc[i, 0] > df.iloc[i, 1]:
                cha.append('#80B1D3')  # up
            elif df.iloc[i, 0] == df.iloc[i, 1]:
                cha.append('#FDFDB4')  # equal
            else:
                cha.append('white')  # unknown
    df['sign'] = cha
    print(df.head())
    # df.to_csv('kegg_pt_draw_prepare.dat')
    return df


def three(df):
    three = list(set(df['l3'].to_list()))
    df_count = pd.DataFrame(df['l3'].value_counts())
    print(type(df_count))
    sigh_st_list = []
    for i in df_count.index.to_list():
        dd = df[df['l3'] == i]
        de = dict(zip(dd.index.to_list(), dd['sign'].to_list()))
        lali = ''
        for key in de:
            lai = key + '\t' + de[key] + '\n'
            lali += lai
        sigh_st_list.append(lali)
    df_count['sign'] = sigh_st_list
    print(df_count.head())
    df_count.to_csv("kegg_l3_count_short.csv")


def main(infile):
    df = one(infile)
    df2 = two(df)
    three(df2)


if __name__ == '__main__':
    main(sys.argv[1])
