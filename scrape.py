from bs4 import BeautifulSoup
import requests
import pandas as pd

url = f"https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

# Find all item containers
item_elements = soup.find_all('table')[0]
#print(item_elements)

#Extract data
#column names  
titles = item_elements.find_all('th')
items_title = [title.text.strip() for title in titles]
#print(items_title)
df = pd.DataFrame(columns = items_title)

#row data
data = item_elements.find_all('tr')
for row in data[1:]:
  row_data = row.find_all('td')
  column_data = [data.text.strip() for data in row_data]

#setting the data into the individual rows

  length =  len(df)
  df.loc[length] = column_data
print(df.set_index('Rank'))        

# df.to_csv(r'C:\Users\Admin\Desktop\Python_Practice\web-scrapper\Largest US companies.csv', index = False)







  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


