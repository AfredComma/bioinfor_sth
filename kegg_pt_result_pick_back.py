#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/7/4 上午11:30
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : kegg_pt_result_pick_back.py
# @Software: PyCharm

import os
import sys
import pandas as pd


def get_pt(pt_file, big_file):
    df = pd.read_csv(pt_file, sep='\t', index_col=0)
    dfbig = pd.read_csv(big_file, sep='\t', index_col=0)
    real_list = dfbig.iloc[:, -1].to_list()

    dfre = pd.DataFrame()
    index_list = df.index.to_list()
    for i in range(df.shape[0] - 1):
        for j in real_list:
            if index_list[i] in j:
                ci = df.iloc[i, :]
                ci['anno'] = j
                ci = pd.DataFrame(ci).T
                dfre = pd.concat([dfre, ci])

    print(df.head())
    dfre.to_csv("pt_anno.csv")
    # print(real_list)


def main(pt_file, big_file):
    get_pt(pt_file, big_file)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
