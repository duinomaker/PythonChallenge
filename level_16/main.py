# http://www.pythonchallenge.com/pc/return/mozart.html (huge:file)

from PIL import Image

def straighten(seq, x):
    return seq[x:] + seq[:x]

raw = Image.open('level_16/mozart.gif')
seq = [[raw.getpixel((j, i)) for j in range(640)] for i in range(480)]

for i in range(480):
    for j in range(635):
        if seq[i][j] == seq[i][j + 1] == seq[i][j + 2] == seq[i][j + 3] == seq[i][j + 4] == 195:
            seq[i] = straighten(seq[i], j - 1)
            break

img = Image.new('L', (640, 480))

for i in range(480):
    for j in range(640):
        img.putpixel((j, i), seq[i][j])

img.save('level_16/result.bmp')
img.show()