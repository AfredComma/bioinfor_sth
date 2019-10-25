#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/10/25 0025 上午 10:35
# @Author  : HAOYU.Dou
# @Mail    : commadou@163.com
# @File    : get_kegg_pathway_pic_data.py
# @Software: PyCharm
# 这个程序会讲level3水平显著差异的kegg挑出来(从检验的文件），然后从level4里面挑出来对应的KO和检验差异水平

import os
import sys
import pandas as pd


def get_level3(pt_file):
    df = pd.read_csv(pt_file, sep='\t')
    id = df['ID'].tolist()
    # 这里选择的pt文件是经过挑选的，coverage>0.9，wilcox p<0.05
    return id


def get_relations(ab_file):
    df = pd.read_csv(ab_file, sep='\t', index_col=0)
    one_list = df['level4^level3^level2^level1']
    two_list = df.index.tolist()
    d = dict(zip(one_list, two_list))
    return d


def get_level4(pt_file):
    df = pd.read_csv(pt_file, sep='\t')
    d = dict()
    for i in range(df.shape[0]):
        if df.iloc[i, 1] > df.iloc[i, 2] and df.iloc[i, 9] < 0.05:
            # HEA组更大,p值检查
            d[df.iloc[i, 0]] = "green"
        elif df.iloc[i, 1] < df.iloc[i, 2] and df.iloc[i, 9] < 0.05:
            d[df.iloc[i, 0]] = "red"
        else:
            d[df.iloc[i, 0]] = "yellow"
    return d


def combines_result(relation_dict, l4_dict, use_id):
    for id in use_id:
        id_result = []
        for r in relation_dict:
            if id == r.split('^')[1]:
                id_result.append(relation_dict[r] + ":" + l4_dict[relation_dict[r]] + '\n')
        with open(id + '.txt', 'w') as f:
            f.writelines(id_result)


def main(ab_file, level3_pt_file, level4_pt_file):
    relation_dict = get_relations(ab_file)
    l4_dict = get_level4(level4_pt_file)
    id = get_level3(level3_pt_file)
    combines_result(relation_dict, l4_dict, id)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
