#!/usr/bin/env bash

set -e

cd examFiles_43590097_1556880827788

exts=(eps tif png jpg)
ext="($(echo ${exts[@]} | tr ' ' '|'))"
echo "${ext}"

# all graphics files
grafix=$(find . -type f -print | grep -E "\.${ext}" | cut -d '/' -f 2)
echo "${grafix[@]}"

# all references to graphics in latex
latex=$(grep -E "\s*[^%].+\.$ext.*" GSGradientFromColor.tex | awk -F'{' '{print $NF}' | tr -d '}')
echo LATEX
echo "${latex[@]}"

declare -A counts

# take complement to ./dump
todump=$(echo ${grafix[@]} ${latex[@]} | tr ' ' '\n' | sort | uniq -u)
counts[dump]=$(echo "${todump[@]}" | wc -w)

mkdir dump
mv -f ${todump[@]} dump || true

# make ext dirs
for e in "${exts[@]}"
do
    counts[$e]=0
done

# take the rest to file ext
for f in $(echo ${latex[@]})
do
    e=$(echo $f | cut -d '.' -f 2)
    echo $f
    mkdir -p $e
    mv $f "$e/$f" && ((counts[$e]+=1)) || true
    #(( counts[$e]++))
done

# print counts
echo ${counts[dump]} dumped files
for e in "${exts[@]}"
do
    echo ${counts[$e]} $e files
done

