import urllib.request
from bs4 import BeautifulSoup
import os
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
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
#for row in table_data.findAll("tr"):
 #   td = row.findAll('td')
  #  A.append(td[0].find(text=True))
   # for capitals in td:
    #    print(capitals.text);
    #th = row.find('th')
    #print('State Name')
   # print(th.text)

for row in table_data.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))

print(A)
print(B)
print(C)

import pandas as pd

d = {'Number': A, 'State': B,'Capital':C}
df = pd.DataFrame(data=d)
df

#df=pd.DataFrame(A,columns=['Number'])
#df['State/UT']=B
#df['Admin_Capital']=C
#df
print(df)