from bs4 import BeautifulSoup
import requests


url = input("Website to be scraped: ")
r = requests.get("https://" + url)

def link_counter(url):
	data = r.text
	soup = BeautifulSoup(data, 'lxml')

	count = 0
	for link in soup.find_all('a'):
		count += 1
	return count

print(link_counter(url))