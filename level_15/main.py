# http://www.pythonchallenge.com/pc/return/uzi.html (huge:file)

import datetime

eligible = []
for i in range(1006, 1997):
    if i % 10 == 6 and (i % 400 == 0 or (i % 4 == 0 and i % 100 != 0)):
        if datetime.datetime(i, 1, 1).isoweekday() == 4:
            eligible.append(i)

print(eligible)
# Wolfgang Amadeus Mozart, born in 26/1/1756