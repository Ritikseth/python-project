import requests
from bs4 import BeautifulSoup
import pprint

'''This is a script written for scraping the HackerNews website and displaying the title and links for the stories having score greater than 99'''

pages=int(input('Enter how many pages to scrape: '))
#instead of the for loop,we could have used another res named res2 similarly for soup,links and subtexts and then merge them into one.Like ------>    mega_link =links + links2
for i in range(0,pages+1):
	res = requests.get(f'https://news.ycombinator.com/news?p={i}')
#   print(res),The response status_code can be verified in the developer tools network column
#   print(res.text),returns the html file

	soup = BeautifulSoup(res.text,'html.parser')
	links = soup.select('.storylink')
	subtext = soup.select('.subtext')

	def sort_stories_by_votes(hnlist):
		return sorted(hnlist,key= lambda k:k['votes'],reverse = True)

	def create_custom_hn(links,subtext):
		hn = []
		for idx,item in enumerate(links):

			title = links[idx].getText()
			href = links[idx].get('href',None)
			vote = subtext[idx].select('.score')
			if len(vote):
				points = int(vote[0].getText().replace(' points',''))
				if points > 99:
					hn.append({'title': title,'link':href,'votes': points})
		return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))