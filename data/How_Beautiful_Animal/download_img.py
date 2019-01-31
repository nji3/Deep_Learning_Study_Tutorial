import pandas as pd
import urllib.request

df = pd.read_csv('How-beautiful-animals-DFE.csv')
urls = df['url']

for t,url in enumerate(urls):
    urllib.request.urlretrieve(url,"img_%d.jpg"%t)