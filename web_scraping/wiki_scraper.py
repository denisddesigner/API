# import the library to query a website
import requests

# import pandas to convert list to data frame
import pandas as pd

# specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# query the website and return the html in the variable 'page'
page = requests.get(wiki)

# import the BeautifulSoup functions to parse the data returned from the website
from bs4 import BeautifulSoup

# parse the html in the 'page' variable & store it in a Beautiful Soup format
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

#all_links = soup.find_all('a')
#for link in all_links:
#	print(link.get("href"))

#all_tables = soup.find_all('table', class_='wikitable sortable plainrowheaders')

#print(all_tables)

# table
right_table = soup.find('table', class_="wikitable sortable plainrowheaders")


# Generate Lists

A = []
B = []
C = []
D = []
E = []
F = []
G = []

for row in right_table.findAll('tr'):
	cells = row.findAll('td')
	states = row.findAll('th') # To store second column data
	if len(cells) == 6: # Only extract table body not heading
		A.append(cells[0].find(text=True))
		B.append(states[0].find(text=True))
		C.append(cells[1].find(text=True))
		D.append(cells[2].find(text=True))
		E.append(cells[3].find(text=True))
		F.append(cells[4].find(text=True))
		G.append(cells[5].find(text=True))



df = pd.DataFrame(A, columns=['Number'])
df['State/UT'] = B
df['Admin_Capital'] = C
df['Legislative_Capital'] = D
df['Judiciary_Capital'] = E
df['Year_Capital'] = F
df['Former_Capital'] = G
print(df) 


































