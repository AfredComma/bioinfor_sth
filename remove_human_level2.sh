#!/usr/bin/env bash
set -e

#files=cat *pca*sh|awk '{print()}'|sort|uniq|grep tsv|grep -v level4|grep -v level3

for f in $(cat *pca*sh|awk '{print($4)}'|sort|uniq|grep tsv|grep -v level4|grep -v level3)
do
    cat remove_human_level2.txt|xargs -I% echo "sed -i '/%/d' ${f}"|bash -
done
