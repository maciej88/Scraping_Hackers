import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/newest')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

#def sort_stories_by_votes(hnlist):
#    return sorted(hnlist, key= lambda k:k['votes'] )
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            txt = (vote[0].getText().replace(' point', ''))
            print(txt)

            hn.append({'title': title, 'link': href})
    return hn

pprint.pprint(create_custom_hn(links, subtext))