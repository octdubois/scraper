from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
import argparse

s = HTMLSession()
dealslist = []

searchterm = 'bluetooth+speaker'
url = f'https://www.amazon.ca/s?k={searchterm}'

def getdata(url):
    r=s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getdeals(soup):
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    for item in products:
        title = item.find('a', {'class': 'a-link-normal s-link-style a-text-normal'}).text.strip()
        short_title = item.find('a', {'class': 'a-link-normal s-link-style a-text-normal'}).text.strip()[:25]
        link = item.find('a', {'class': 'a-link-normal s-link-style a-text-normal'})['href']
        saleprice = (item.find('span', {'class':'a-price-whole'}))


        saleitem = {
            'title': title,
            'short_title': short_title,
            'link': link,
            'saleprice': saleprice,
            
            }
        dealslist.append(saleitem)
    return
        
def getnextpage(soup): 
    pages = soup.find('ul', {'class': 'a-pagination'})   
    if not pages.find('li', {'class': 'a-disabled a-last'}):
        url = 'https://www.amazon.ca' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return
    

while True:
    soup = getdata(url)
    getdeals(soup)
    url = getnextpage(soup)
    if not url:
        break
    else:
        print(url)
        print(len(dealslist))  


df = pd.DataFrame(dealslist)
#df['percentoff'] = 100 - ((df.saleprice / df.oldprice) * 100)
#df = df.sort_values(by=['percentoff'], ascending=False)
df.to_csv(searchterm + '-bfdeals.csv', index=False)
print('Fin.')


