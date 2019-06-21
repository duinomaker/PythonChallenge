# http://www.pythonchallenge.com/pc/return/disproportional.html (huge:file)

import xmlrpc

uri = 'http://www.pythonchallenge.com/pc/phonebook.php'

with open('level_13/request.xml') as f:
    xmlrpc_request = f.read()

with xmlrpc.client.ServerProxy(uri) as proxy:
    print(proxy.phone('Bert'))

# Bert    -> 555-ITALY
# Leopold -> 555-VIOLIN