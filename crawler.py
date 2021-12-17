import requests
from bs4 import BeautifulSoup
from utils import *
import json
import pandas as pd

urls_to_scrape = [base_url+domain.lower() for domain in domains]

quotes_metadata = []

for url in urls_to_scrape:
    
    content = requests.get(url, verify=True).content
    soup = BeautifulSoup(content, "html.parser")
    quotes_divs = soup.find_all('div', {'class': 'border-bottom my-2'})
    print('fetching this domain : ',url[45:])
    for quote_div in quotes_divs:
        quotes_metadata_tmp = {}

        domain = url[45:]
        quotes_metadata_tmp['domain'] = domain

        article_title = quote_div.find('h4').get_text()        
        quotes_metadata_tmp['article_title'] = article_title

        date = quote_div.find('h5').get_text()
        quotes_metadata_tmp['date'] = date

        quote = quote_div.find('p').get_text()
        quotes_metadata_tmp['quote'] = quote
    
        quotes_metadata.append(quotes_metadata_tmp)

print(type(quotes_metadata))
with open('quotes.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write(str(quotes_metadata))

df = pd.DataFrame(quotes_metadata)
# Let's do some preprocessing
df['date'] = df['date'].map(lambda x:x.replace(' - Link','')) # remove some text added from scraping

df.to_csv('satoshi_quotes.csv')