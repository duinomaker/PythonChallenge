# http://www.pythonchallenge.com/pc/return/good.html (huge:file)

from PIL import Image, ImageDraw
import pickle

with open('level_09/first', 'rb') as f:
    first = pickle.load(f)

with open('level_09/second', 'rb') as f:
    second = pickle.load(f)

img = Image.new('L', (480, 480))
drawer = ImageDraw.Draw(img)

drawer.polygon(first, fill=210)
drawer.polygon(second, fill=230)

img.save('level_09/result.bmp')
img.show()