#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/29 下午2:06
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : kegg_anno3.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import os


def getlines_list(infile):
    with open(infile, 'r') as f:
        a = f.readlines()
    return a


def get_dict(txt):
    re_d = dict()
    A = ''
    B = ''
    C = ''
    for i in txt:
        if i.startswith('A'):
            A = i[7:].replace('\n', '')
        elif i.startswith('B'):
            if len(i) > 5:
                B = i[9:].replace('\n', '')
        elif i.startswith('C'):
            C = i[11:].replace('\n', '')
        elif i.startswith('D'):
            s = i.replace('D      ', '')
            D = s[:6]
            D_des = '^'.join([s[8:].replace('\n', ''), C, B, A])
            if D in re_d:
                print("************")
                print(re_d[D])
                if isinstance(re_d[D], str):
                    re_d[D] = [re_d[D]]
                    re_d[D].append(D_des)
                elif isinstance(re_d[D], list):
                    re_d[D].append(D_des)
                # None?
            else:
                re_d[D] = '^'.join([s[8:].replace('\n', ''), C, B, A])
    return re_d


a = getlines_list('ko00001.keg')
re_d = get_dict(a)


# print(re_d)


def extend_df(re_d):
    df = pd.read_csv("kegg_use_abundance.tsv", sep='\t', index_col=0)
    df2 = df[:]
    cc = []
    rr = []
    for h in range(len(df.index)):
        i = df.index[h]
        if i not in re_d.keys():
            cc.append("None")
            print(i + "has not level!")
            rr.append(h)
        else:
            site = re_d[i]
            if isinstance(site, str):
                cc.append(site)
                rr.append(h)
            elif isinstance(site, list):
                print(site)
                cc.extend(site)
                rr.extend([h] * len(site))
            else:
                cc.append(site)
                rr.append(h)
    print(len(rr))
    dfr = df.iloc[rr, :]
    dfr['level4^level3^level2^level1'] = cc
    # df['des^level4^level3^level2^level1'] = [re_d[i] for i in df.index]
    dfr.to_csv("uniq_kegg_relative_abundance_table_explain_updateJune27", sep='\t')


extend_df(re_d)


def main():
    pass


if __name__ == '__main__':
    main()
