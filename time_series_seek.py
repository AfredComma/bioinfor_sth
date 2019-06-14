#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/12 下午5:21
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : time_series_seek.py
# @Software: PyCharm

import os
import sys
import pandas as pd
import numpy as np


def deal_data_frame(infile):
    df = pd.read_csv(infile, sep='\t', index_col=0)
    print(df.head())
    a, b = df.shape
    dfre = pd.DataFrame(np.zeros((a * b, 4)))
    for i in range(b):
        dfre.iloc[list(range(i * a, (i + 1) * a)), 0] = df.iloc[:, i].tolist()
        dfre.iloc[list(range(i * a, (i + 1) * a)), 1] = df.index.to_list()
        dfre.iloc[list(range(i * a, (i + 1) * a)), 2] = [df.columns[i].split('_w')[0]] * a
        dfre.iloc[list(range(i * a, (i + 1) * a)), 3] = [df.columns[i].split('_w')[-1]] * a
    dfre.columns = ["value", "genus", "person", "period"]
    return dfre, df.index.to_list()


def seek_part(dfre, want_genus):
    df2 = dfre[dfre['genus'] == want_genus]
    return df2


def seek_run(dfre, want_genus="g__Abiotrophia"):
    right_path = '/'.join(os.path.abspath(__file__).split('/')[:-1])
    dfre2 = seek_part(dfre, want_genus)
    want_genus = want_genus.replace(' ', '_')
    want_genus = want_genus.replace('/', '_')
    want_genus = want_genus.replace('(', '_')
    want_genus = want_genus.replace(')', '_')
    want_genus = want_genus.replace(':', '_')
    dat_file = want_genus + ".tsv"
    lines_pdf = want_genus + '_lines'
    smooth_pdf = want_genus + "_smooth"
    dfre2.to_csv(dat_file, sep='\t')
    shs = "Rscript %s/draw_time_series_seek.R -i %s -o %s -s %s" % (right_path, dat_file, lines_pdf, smooth_pdf)
    print(shs)
    os.system(shs)


def main(infile):
    dfre, genus_list = deal_data_frame(infile)
    print(genus_list)
    for g in genus_list:
        seek_run(dfre, want_genus=g)


if __name__ == '__main__':
    main(sys.argv[1])
