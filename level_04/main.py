# http://www.pythonchallenge.com/pc/def/linkedlist.php

from os import system
import urllib.request as req

nothing = '11877' # The last nothing is '66831'
template = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'

def extract(text):
    result = []
    for c in text:
        if c.isdigit():
            result.append(c)
    return ''.join(result)

while nothing:
    with req.urlopen(template.format(nothing)) as page:
       text = page.read().decode()
       print(text)
    if 'and the next nothing is ' in text and text.index('and') == 0:
        nothing = extract(text)
    else:
        nothing = input('Enter your judgement: ')