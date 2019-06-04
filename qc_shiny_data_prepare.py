#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/4 上午9:54
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : qc_shiny_data_prepare.py
# @Software: PyCharm

import os
import sys
import pandas as pd


def p2f(x):
    return float(x.strip('%')) / 100


def read_seek(infile):
    df = pd.read_csv(infile, sep='\t',
                     converters={'covarage>1x': p2f, 'coverage>20x': p2f, 'coverage>30x': p2f, 'coverage>50x': p2f})
    use_col = "sample,total,dup,capture efficiency,alignment,covarage>1x,coverage>20x,coverage>30x,coverage>50x,depth,gender,time".split(
        ',')
    df_use = df[use_col]
    ids = df_use['sample'].to_list()
    groups_list = []
    for i in ids:
        if 'AS' in i:
            groups_list.append('production')
        else:
            groups_list.append('others')
    df_use['delete'] = 0
    df_use['group'] = groups_list
    df_use['gender'] = df_use['gender'].fillna('Uncertain')
    r = 'sample,total,dup,capture efficiency,alignment,covarage>1x,coverage>20x,coverage>30x,coverage>50x,depth,gender,time'.split(
        ',')
    s = 'sample,volume,dup_perc,specificity,align_rate,coverage>1,coverage>20,coverage>30,coverage>50,depth,gender,time'.split(
        ',')
    df_use.rename(columns=dict(zip(r, s)), inplace=True)
    right_sort = 'sample,volume,dup_perc,specificity,align_rate,delete,coverage>1,coverage>20,coverage>30,coverage>50,depth,gender,time,group'.split(',')
    df_use = df_use[right_sort]
    return df_use


def main(infile):
    df_use = read_seek(infile)
    df_use.to_csv("test.csv", index=False)


if __name__ == '__main__':
    main(sys.argv[1])
