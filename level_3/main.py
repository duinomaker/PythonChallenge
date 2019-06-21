# http://www.pythonchallenge.com/pc/def/equality.html

import re

pattern = re.compile(r'(?:^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?:[^A-Z]|$)')

with open('level_3/mess') as f:
    mess = f.read().replace('\n', '')

result = pattern.findall(mess)
print(''.join(result))