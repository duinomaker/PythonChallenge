# http://www.pythonchallenge.com/pc/return/evil.html (huge:file)

evil = [[], [], [], [], []]

with open('level_12/evil2.gfx', 'rb') as f:
    content = f.read()

for i, j in enumerate(content):
    evil[i % 5].append(j)

for i in range(5):
    evil[i] = bytes(evil[i])

with open('level_12/evil[0].jpeg', 'wb') as f:
    f.write(evil[0])

with open('level_12/evil[1].png', 'wb') as f:
    f.write(evil[1])

with open('level_12/evil[2].gif', 'wb') as f:
    f.write(evil[2])

with open('level_12/evil[3].png', 'wb') as f:
    f.write(evil[3])

with open('level_12/evil[4].jpeg', 'wb') as f:
    f.write(evil[4])