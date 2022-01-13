import feedparser

def parseRSS(rss_url):
    return feedparser.parse(rss_url)


def getHeadLines(rss_url):
    headlines = []
    feed = parseRSS(rss_url)

    for newitem in feed['items']:
        headlines.append(newitem['title'])
    return headlines


allheadlines = []

news = {
    'yandex': 'https://yandex.ru/company/press_releases/news.rss'
}

for key, url in news.items():
    allheadlines.extend(getHeadLines(url))

for h in allheadlines:
    print(h)