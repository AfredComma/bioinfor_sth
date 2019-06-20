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


def get_file(infile):
    sample_id = infile.split('/')[-1].replace('_genefamilies.tsv', '')
    out_file = os.path.join('gene_count', sample_id + "_genefamilies_remove_repeat.tsv")
    shs = 'grep -v -e "g__" %s > %s' % (
        infile, out_file)
    os.system(shs)
    return sample_id, out_file


def main():
    infile = sys.argv[1]
    sample_id, out_file = get_file(infile)
    a, b = con(out_file)
    relist = [a, b]
    relist.insert(0, sample_id)
    relist = [str(i) for i in relist]
    re_str = '\t'.join(relist)
    print(re_str)


if __name__ == '__main__':
    main()
