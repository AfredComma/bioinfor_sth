#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/27 下午6:26
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : grep_file_from_map.py
# @Software: PyCharm

import os
import sys
import pandas as pd


def main(infile, mapfile, outfile):
    df = pd.read_csv(infile, sep='\t', index_col=0)
    dfmap = pd.read_csv(mapfile, sep='\t')
    samples = dfmap['Sample'].to_list()
    dfuse = df[samples]
    dfuse.to_csv(outfile,sep = '\t')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
