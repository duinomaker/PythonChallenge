# http://www.pythonchallenge.com/pc/def/ocr.html

with open('level_3/mess') as f:
    mess = f.read()

characters = []

for c in mess:
    if c.isalnum():
        characters.append(c)

print(''.join(characters))