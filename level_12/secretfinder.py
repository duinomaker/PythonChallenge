import urllib.request as req
import base64

def auth_req(url, auth):
    authorization = (b'Basic ' + base64.b64encode(auth.encode())).decode()
    request = req.Request(url)
    request.add_header('Authorization', authorization)
    return request

request = auth_req('http://www.pythonchallenge.com/pc/return/evil4.jpg', 'huge:file')

print(req.urlopen(request).read().decode())
# Bert is evil! go back!