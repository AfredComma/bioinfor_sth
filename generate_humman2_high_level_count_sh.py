#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/6/20 上午10:36
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : generate_humman2_high_level_count_sh.py
# @Software: PyCharm

import os
import sys


def one(activate_path, sample_id, Type='Phylum'):
    shs = '. %s && conda activate humann2&&humann2_infer_taxonomy -i %s_genefamilies.tsv  --level %s -o %s_%s.tsv ' \
          '-r uniref90 && humann2_renorm_table --input %s_%s.tsv --output %s_relabun_%s.tsv --units relab' % (
              activate_path, sample_id, Type, sample_id, Type, sample_id, Type, sample_id, Type)
    return shs


def main(activate_path, Type):
    a = os.listdir('.')
    gene_f = [i for i in a if i.endswith('genefamilies.tsv')]
    names = [j.split('_')[0] for j in gene_f]
    re_list = []
    for n in names:
        re_list.append(one(activate_path, n, Type=Type))
    re_str = '\n'.join(re_list)
    out_file = 'get_' + Type + '_abun.sh'

    with open(out_file, 'w') as f:
        f.write(re_str)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
