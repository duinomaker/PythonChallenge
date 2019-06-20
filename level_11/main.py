# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image

img = Image.open('level_11/cave.jpg')
odd = Image.new('RGB', (640, 480))

for i in range(0, 480):
    for j in range(i % 2, 640, 2):
        odd.putpixel((j, i), img.getpixel((j, i)))

odd.save('level_11/odd.bmp')
odd.show()