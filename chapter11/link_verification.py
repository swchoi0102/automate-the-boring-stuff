import requests
import bs4

url = "http://imgur.com"
res = requests.get(url)

soup = bs4.BeautifulSoup(res.text, 'html.parser')

for link in soup.find_all('a', href=True):
    url = link['href']
    if not url.startswith("http:") and not url.startswith("https:"):
        url2 = "http:" + url
    try:
        res = requests.get(url2)
    except Exception:
        print("broken link: {}".format(url))
