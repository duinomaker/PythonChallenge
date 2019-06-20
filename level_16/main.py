# http://www.pythonchallenge.com/pc/return/mozart.html (huge:file)

from PIL import Image

def straighten(seq, x):
    return seq[x:] + seq[:x]

with Image.open('level_16/mozart.gif') as raw:
    seq = [[raw.getpixel((j, i)) for j in range(640)] for i in range(480)]

for i in range(480):
    for j in range(635):
        if seq[i][j] == seq[i][j + 1] == seq[i][j + 2] == seq[i][j + 3] == seq[i][j + 4] == 195:
            seq[i] = straighten(seq[i], j - 1)
            break

with Image.new('P', (640, 480)) as img:
    for i in range(480):
        for j in range(640):
            img.putpixel((j, i), seq[i][j])
    img.save('level_16/greyscale.gif')

with open('level_16/mozart.gif', 'rb') as f:
    header = f.read()[:781]

with open('level_16/greyscale.gif', 'rb') as f:
    body = f.read()[781:]

with open('level_16/result.gif', 'wb') as f:
    f.write(header + body)

with Image.open('level_16/result.gif') as img:
    img.show()