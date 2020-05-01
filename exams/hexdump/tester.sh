#!/usr/bin/env bash

for f in hexdump-data/*.bin.hex
do
    python dumper.py "${f}" | diff --color=always -c -s "${f%%.hex}-expanded.hex" -
done

