import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source_code = urllib.request.urlopen(url)
soup = BeautifulSoup(source_code, "html.parser")

body = soup.find('title')
print(soup.title.text)

links = soup.find_all('a')
print(links);


for link in soup.find_all('a'):
    print(link.get('href'))

all_table_data = soup.find('table')
print(all_table_data)

table_data = soup.find('table', {'class': 'wikitable sortable plainrowheaders'})
statesList=[]
capitals=[]


for row in table_data.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        statesList.append(states[0].find(text=True))
        capitals.append(cells[1].find(text=True))

print(states)
print(capitals)

d = {'State': statesList,'Capital':capitals}
df = pd.DataFrame.from_dict(d)
df

print(df)