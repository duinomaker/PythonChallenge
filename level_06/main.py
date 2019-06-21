# http://www.pythonchallenge.com/pc/def/channel.html
# Please extract archive 'channel.zip' before running this

import os
import zipfile

def extract(text):
    result = []
    for c in text:
        if c.isdigit():
            result.append(c)
    return ''.join(result)

os.chdir('level_06/channel')
nothing = '90052'

zfile = zipfile.ZipFile('../channel.zip')
comments = b''

while nothing:
    filename = '%s.txt' % (nothing,)
    comments += zfile.getinfo(filename).comment
    with open(filename) as f:
       text = f.read()
       print(text)
    if 'Next nothing is ' in text and text.index('Next') == 0:
        nothing = extract(text)
    else:
        nothing = input('Enter your judgement: ')

print(comments.decode())