import urllib.request as req

with req.urlopen('http://www.pythonchallenge.com/pc/def/banner.p') as page:
    pkl = page.read()

with open('banner.p', 'wb') as f:
    f.write(pkl)