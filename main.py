import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/newest')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)