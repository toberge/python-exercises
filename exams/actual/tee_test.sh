#!/usr/bin/env bash

ls | python tee.py | tr -d '\n'
echo
ls | python tee.py web_content/file.txt
echo
echo this is the last line | python tee.py -a web_content/file.txt
tail -n 1 web_content/file.txt
echo
rm web_content/file.txt
echo this is the only line | python tee.py -a web_content/file.txt

echo this will never be written | python tee.py /etc/conf.d/sensord
echo this will never be written | python tee.py /baluba/nope

