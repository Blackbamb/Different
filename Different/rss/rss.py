from urllib import request


resp = request.urlopen('https://yandex.ru/company/press_releases/news.rss')
data = resp.read()
html = data.decode("UTF-8")

for i in range(len(html)):
    if (html[i] == '>') and (html[i + 1] != ' '):
        html = html[:i + 1] + ' ' + html[i + 1:]
    if (html[i] + html[i + 1] == '</') and (html[i + 1] != ' '):
        html = html[:i] + ' ' + html[i + 1:]

a = html.split()
u1 = []
u2 = []
new = []
for i in range(len(a)):
    if a[i] == '<title>':
        u1.append(i)
    if a[i] == '/title>':
        u2.append(i)
for i in range(len(a)):
    for j in range(len(u1)):
        if (i > u1[j]) and (i < u2[j]):
            new.append(a[i] + ' ')
        if i == u2[j] + 1:
            new.append("." + "\n ")

str1 = ''.join(new)
print(str1)
