#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2019/7/13 下午3:45
# @Author  : commadou
# @Mail    : commadou@163.com
# @File    : download_virus_protein_from_ncbi.py
# @Software: PyCharm

import os
import sys
import time
from Bio import Entrez


def get_count(search_text="viridae[Organism]", email='commadou@163.com'):
    Entrez.email = email
    bandle = Entrez.esearch(db="protein", term=search_text, idtype="acc")
    brecord = Entrez.read(bandle)
    bandle.close()
    return int(brecord["Count"])


def main(seq_num=100000, search_text="viridae[Organism]"):
    number = get_count()
    all_id = []
    for i in range(0, number, seq_num):
        handle = Entrez.esearch(db="protein", term=search_text, rettype="fasta",
                                retmax=seq_num, retstart=i)
        records = Entrez.read(handle)
        handle.close()
        all_id.extend(records["IdList"])
        # time.sleep(1)
    right_now = time.strftime("%d_%b_%Y_%H_%M_%S", time.localtime())
    all_id = [str(j) + "\n" for j in all_id]
    outfile = 'Virus_protein_ncbi' + right_now + '.txt'
    with open(outfile, 'w') as f:
        f.writelines(all_id)


def download_dfata(infile):
    Entrez.email = "commadou@163.com"
    with open(infile, 'r') as f:
        ids = f.readlines()
    ids = [i.replace('\n', '') for i in ids]
    for seq_id in ids:
        outfile = str(seq_id) + ".fasta"
        handle = Entrez.efetch(db="protein", id=seq_id, rettype="fasta", retmode="text")
        record = handle.read()
        re_string = record.rstrip('\n')
        with open(outfile, 'w') as g:
            g.write(re_string)
        time.sleep(0.3)


if __name__ == '__main__':
    # main()
    download_dfata("Virus_protein_ncbi13_Jul_2019_17_30_46.txt")