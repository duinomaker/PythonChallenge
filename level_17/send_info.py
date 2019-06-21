# http://www.pythonchallenge.com/pc/stuff/violin.php (huge:file)
#
# At first, I solved this just typing
# >> document.cookie = 'info=the flowers are on their way'
# in the Web Console, and then refreshed the page.
#
# In salute to the *PYTHON* challenge, I'll do it using python.

from urllib import request as req

request = req.Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
request.add_header('Cookie', 'info=the flowers are on their way')

with req.urlopen(request) as page:
    print(page.read().decode())