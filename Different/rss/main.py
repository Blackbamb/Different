import urllib

from urllib import request
from urllib import parse

resp = request.urlopen('https://yandex.ru/')
dir(resp)
c = resp.code
v = resp.length
a = resp.peek()

data = resp.read()

html = data.decode("UTF-8")

# print(a)
# print(type(data))
# print(len(data))
# print(type(html))
# print(html)
# print(resp.read())
# qs = "v=" + "LosIGgon_KM" + "&" + "ab_channel=" + "Socratica"
params = {"v": "LosIGgon_KM", "ab_channel": "Socratica"}
querystring = parse.urlencode(params)
print(querystring)
url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)
close = resp.isclosed()
print(close)
print(resp.code)
html=resp.read().decode("UTF-8")
print(html[:500])
