from bs4 import BeautifulSoup
import pandas as pd
import requests

## Source of our data
url = 'https://liquipedia.net/valorant/VCT/2025/Stage_1/Masters/Statistics'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
# print(soup)

## Finding the data for table creation
table = soup.find('table', class_ = 'wikitable wikitable-striped sortable')

world_titles = table.find_all('th')

table_titles = [title.text for title in world_titles] # Use title.text.strip() if theres any cleaning required
# print(table_titles)

dataset = pd.DataFrame(columns = table_titles)
# print(dataset)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    inidividual_row_data = [data.text.strip() for data in row_data]
    
    length = len(dataset)
    dataset.loc[length] = inidividual_row_data

# print(dataset)
dataset = dataset.rename(columns={'#': 'Player_ID', 'Player': 'Player_Name'})
dataset.to_csv(r'D:\ML\VCT Champions ML Model\VCT_ChampionsWinnerPredictionModel\Data Scraping\2025\MastersBangkok2025_Players.csv', index = False)