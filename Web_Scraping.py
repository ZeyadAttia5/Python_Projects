import requests


import bs4

quotes = requests.get("http://quotes.toscrape.com/")

quotes.text

all_Authors = {}
all_Authors = set(all_Authors)
soup = bs4.BeautifulSoup(quotes.text, 'lxml')
authors = soup.select('.author')

for author in authors:
    all_Authors.add(author.text)



quotes = []
quotes = set(quotes)
for quote in soup.select(".text"):
    quotes.add(quote.text)


topTenTags = []
for tag in soup.select('.tag-item'):
    topTenTags.append(tag.text)
for tag in topTenTags:
    print(tag)

