#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/7/8 下午4:13
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : grep_name_from_ncbi_names.py
# @Software: PyCharm

import os
import sys
import pandas as pd


def one(names_file, nodes_file, level):
    df_names = pd.read_csv(names_file, sep='|', header=None)
    df_nodes = pd.read_csv(nodes_file, sep='|', header=None)
    df_names = df_names.dropna(axis=1, how='all')
    df_nodes = df_nodes.dropna(axis=1, how='all')
    df_names = df_names.applymap(lambda x: str(x).replace('\t', ''))
    df_nodes = df_nodes.applymap(lambda x: str(x).replace('\t', ''))

    df_level = df_nodes[df_nodes[2] == level]
    id_list = df_level[0].to_list()
    df_use = df_names[df_names[0].isin(id_list)]

    df_use = df_use[~(df_use[2].str.contains("type strain"))]
    df_use = df_use[~(df_use[2].str.contains("type material"))]
    df_use = df_use[~(df_use[2].str.contains("culture from"))]
    df_use = df_use[~(df_use[3].str.contains("authority"))]
    df_use = df_use[~(df_use[3].str.contains("type material"))]
    df_use = df_use.drop_duplicates(subset=0, keep='first')
    print(df_use.head())
    df_use.to_csv("pick_name.csv", index=False)


def main(names_file, nodes_file, level):
    one(names_file, nodes_file, level)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
