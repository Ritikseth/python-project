import requests
from bs4 import BeautifulSoup
import pprint
import csv

csv_file = open('inshorts.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary'])

res = requests.get('https://inshorts.com/en/read')

soup = BeautifulSoup(res.text,'html.parser')
news = soup.find('div',class_= 'card-stack')

for i,card in enumerate(news.find_all('div',class_ = 'news-card z-depth-1')):
	Headline = card.find('div', class_ = 'news-card-title news-right-box')
	Headline = Headline.span.text
	print(f'{i+1}.  {Headline}')
	Summary= card.find('div', class_ = 'news-card-content news-right-box')
	Summary = Summary.div.text
	print(f'{Summary}\n\n')

	csv_writer.writerow([Headline,Summary])

csv_file.close()
