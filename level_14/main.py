# http://www.pythonchallenge.com/pc/return/italy.html (huge:file)

from PIL import Image

wire = Image.open('level_14/wire.png')
block = Image.new('RGB', (100, 100))

pixels = tuple(wire.getpixel((i, 0)) for i in range(10000))

index = 0
span = 100
x, y = 0, 0
while span:
    for i in range(span):
        block.putpixel((x, y), pixels[index])
        x += 1
        index += 1
    span -= 1
    x -= 1
    for i in range(span):
        block.putpixel((x, y), pixels[index])
        y += 1
        index += 1
    y -= 1
    for i in range(span):
        block.putpixel((x, y), pixels[index])
        x -= 1
        index += 1
    span -= 1
    x += 1
    for i in range(span):
        block.putpixel((x, y), pixels[index])
        y -= 1
        index += 1
    y += 1

block.save('level_14/result.bmp')
block.show()