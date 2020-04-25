#!/usr/bin/env bash

rm -r sorted
mkdir sorted

files=$(ls files)
cp files/* .

echo Running the script:
python identifier.py ${files[@]}
echo

echo Resulting tree:
tree sorted
