#!/usr/bin/env python3
import requests
#import pprint
from pprint import pp
from re import match, split
from bs4 import BeautifulSoup

def get_text(url):
    req = requests.get(url, params='html_doc')
    return req.text

#pprint.PrettyPrinter(indent=2).pprint(get_text('https://toberge.github.io/startpage').split('\n'))
#pp(get_text('https://toberge.github.io/startpage').split('\n'))


# Decode A Web Page
soup = BeautifulSoup(get_text('https://www.nytimes.com/'), 'html.parser')

for article in soup.find_all('article'):
    #print(article.prettify() if article.find('h2').find('span') else 'nay')
    print(article.find('h2').get_text())

print('-----------------------------------------------')

# Decode A Web Page Two
# Disappointed that there was no multi-page stuff like in 2014 when the exercise was written
soup = BeautifulSoup(get_text('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'), 'html.parser')

for article in soup.find_all('div'):
    classes = article.get('class')
    if classes and 'article__body' in classes and not 'body__truncation-message' in classes:
        print(article.p.get_text())

print('-----------------------------------------------')

print(soup.find(class_='content-header__hed').get_text())
print()
print(soup.find(class_='content-header__dek').get_text())
print()

for article in soup.find_all(class_='article__body'):
    if not 'body__truncation-message' in article.get('class'):
        print(article.p.get_text())

# get text from next page (no, the buttons are just for the images!)

print('-----------------------------------------------')

# Custom stuffs
for line in get_text('https://toberge.github.io/startpage').split('\n'):
    if match(r'.+https://.*', line) and not 'stylesheet' in line:
        print(split(r'a href="|" target=', line))

soup = BeautifulSoup(get_text('https://toberge.github.io/startpage'), 'html.parser');
for link in soup.find_all('a'):
    print(link.get('href'))
