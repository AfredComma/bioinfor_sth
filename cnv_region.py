#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/7/10 下午2:45
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : cnv_region.py
# @Software: PyCharm

import os
import sys
import pandas as pd


def main(infile):
    df = pd.read_csv(infile, sep='\t', header=None)
    chr_list = set(df[0].to_list())
    dfre = df
    for chr in chr_list:
        df_chrx = df[df[0] == chr]
        chrx_p_list = set(df_chrx[3].to_list())
        p_set = set([i.split('.')[0] for i in chrx_p_list])

        for p in p_set:
            p_list = [j for j in chrx_p_list if p in j]
            low_list = df_chrx[df_chrx[3].isin(p_list)][1].to_list()
            high_list = df_chrx[df_chrx[3].isin(p_list)][2].to_list()
            dfre = dfre.append({0: chr, 1: min(low_list), 2: max(high_list), 3: p, 4: 'new'}, ignore_index=True)
    dfre.to_csv("hg19_cytoBand_update.txt", sep='\t', index=False)


if __name__ == '__main__':
    main(sys.argv[1])
