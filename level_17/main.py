# http://www.pythonchallenge.com/pc/return/romance.html (huge:file)

from urllib import request as req, parse
from http import cookiejar
import bz2

nothing = '12345'
template = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'

def extract(text):
    result = []
    for c in text:
        if c.isdigit():
            result.append(c)
    return ''.join(result)

data = []

jar = cookiejar.CookieJar()
handler = req.HTTPCookieProcessor(jar)
opener = req.build_opener(handler)
while nothing:
    with opener.open(template.format(nothing)) as page:
        text = page.read().decode()
        char = list(jar)[0].value
        data.append(char)
        print(text, char)
    jar.clear()
    if 'and the next busynothing is ' in text and text.index('and') == 0:
        nothing = extract(text)
    else:
        nothing = input('Enter your judgement: ')

data = parse.unquote_to_bytes((''.join(data)).replace('+', ' '))
print(data)
print(bz2.decompress(data).decode())
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.