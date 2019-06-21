import urllib.request as req

with req.urlopen('http://www.pythonchallenge.com/pc/def/banner.p') as page:
    pkl = page.read()

with open('level_05/banner.p', 'wb') as f:
    f.write(pkl)