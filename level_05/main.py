# http://www.pythonchallenge.com/pc/def/peak.html

import pickle

with open('level_05/banner.p', 'rb') as f:
    data = pickle.load(f)

for line in data:
    print(''.join(i * j for i, j in line))