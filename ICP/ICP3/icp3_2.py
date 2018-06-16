import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source_code = urllib.request.urlopen(url)
soup = BeautifulSoup(source_code, "html.parser")

#To find the title of the web page
body = soup.find('title')
print(soup.title.text)

#find all the anchor tags in html page
links = soup.find_all('a')
print(links);

#iterate through the anchor tags and get the corresponding href attribute
for link in soup.find_all('a'):
    print(link.get('href'))

#To get all the tables in the html page
all_table_data = soup.find('table')
print(all_table_data)

#to get the table with classes wikitable sortable plainrowheaders
table_data = soup.find('table', {'class': 'wikitable sortable plainrowheaders'})
statesList=[]
capitals=[]

#iterate through the tr tags in table_data
for row in table_data.findAll("tr"):
    cells = row.findAll('td') #store all the values of tr in cells list
    states = row.findAll('th') #tore all the values of th in states list
    if len(cells)==6: #Only extract table body not heading
        statesList.append(states[0].find(text=True)) #get the state name and store in statesList list
        capitals.append(cells[1].find(text=True)) #get the capital name and store it in capitals list

print(states)
print(capitals)

d = {'State': statesList,'Capital':capitals} #form a dictionary of states and capitals
df = pd.DataFrame.from_dict(d) #prepare a dataframe from the formed dictionary

print(df)