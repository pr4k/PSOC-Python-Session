import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
i = 0
last_links = soup.find(class_='dyk-footer hlist noprint')
last_links.decompose()
did_you_know_list = soup.find(id ='mp-dyk')
print('Did You Know ...')
while i<8 :
    print(did_you_know_list.find_all('li')[i].get_text())
    i = i + 1
