# Ensure that you have both beautifulsoup and requests installed:
#   pip install beautifulsoup4
#   pip install requests

import requests
from bs4 import BeautifulSoup
import pprint

def main():

	'''Goal: Extract all of the links on the page'''

	# Using the requests module, we use the "get" function provided to access the webpage 
	# which is provided as an argument to this function:
	page = input('Enter the page url to scrape: ')

	try:
		res = requests.get(page)

		# To make sure that the website is accessible, we can ensure that we obtain a 200 OK response to indicate
		# that the page is indeed present:
		print(f'Status code={res.status_code}')

		# Now, let us store the page content of the website accessed
		# from requests to a variable:
		src = res.content

		# Now that we have the page source stored, we will use the BeautifulSoup module to parse and process the source.
		# To do so, we create a BeautifulSoup object based on the source variable we created above:
		soup = BeautifulSoup(src,'lxml')

		#Now that the page source has been processed via Beautifulsoup we can access specific information directly from it.
		links = soup.find_all('a')
		all_urls = []

		for link in links:
			url = link.attrs['href']
			
			if 'http' in url:
				all_urls.append(url)
			else:
				all_urls.append(page+url)

		my_dict={k:all_urls.count(k) for k in all_urls}

		for i,j in my_dict.items():
			print(f'link=  {i}  ,count={j}')
		print('Done')


	except:
		pprint.pprint('Incorrect url please Check')
	


if __name__ == '__main__':
	help(main)
	main()
