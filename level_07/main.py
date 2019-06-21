# http://www.pythonchallenge.com/pc/def/oxygen.html

import PIL.Image as Image
img = Image.open('level_07/oxygen.png')

pixels = []

last_index = 0
for i in range(0, 629, 7):
    r, g, b, a = img.getpixel((i, 47))
    if not (r == g == b):
        break
    pixels.append(r)

text_1 = ''.join(chr(i) for i in pixels)
print(text_1)

text_2 = ''.join(chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121])
print(text_2)