import requests
import bs4

base_url = 'https://quotes.toscrape.com/'
result = requests.get(base_url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup)

tags = set()
for tag in soup.select('.tag-item'):
    tags.add(tag.text.strip())
print(tags)

authors = set()
for author in soup.select('.author'):
    authors.add(author.text)
print(authors)

texts = []
for text in soup.select('.text'):
    texts.append(text.text)
print(texts)

