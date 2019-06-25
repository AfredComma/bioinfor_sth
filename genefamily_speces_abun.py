#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/24 下午6:27
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : genefamily_speces_abun.py
# @Software: PyCharm

import os
import sys
import pandas as pd


def getfile(indir):
    a = os.listdir(indir)
    b = [i for i in a if i.endswith('tsv')]
    return b


def begin_grep(file_list):
    result_file = []
    for i in file_list:
        outfile = i.replace("_genefamilies.tsv", "_speces.tsv")
        shs = '''grep -E "Abundance-RPKs|s__" %s > %s''' % (i, outfile)
        result_file.append(outfile)

        print(shs)
        os.system(shs)
    return result_file


def get_only(file_list):
    dfre = pd.DataFrame()
    for i in file_list:
        dd = pd.read_csv(i, sep='\t', index_col=0)
        print(dd.head())
        dd.index = [i.split('|')[-1] for i in dd.index]
        dd2 = dd.sum(level=0)
        dd3 = dd2 / dd2.sum()
        dfre = pd.concat([dfre, dd3], axis=1)
    a = dfre.columns.to_list()
    b = [j.replace('_Abundance-RPKs', '') for j in a]
    dfre.columns = b
    dfre = dfre.fillna(0)
    dfre.to_csv("species_relative_abundance.tsv", sep='\t')


def main(indir):
    b = getfile(indir)
    reusl = begin_grep(b)
    get_only(reusl)


if __name__ == '__main__':
    main(sys.argv[1])
