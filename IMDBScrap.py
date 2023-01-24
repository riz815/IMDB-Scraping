import requests, openpyxl
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

movies = soup.find('tbody', class_='lister-list').find_all('tr')

# print(movies)

movies_list = []
for movie in movies:
    dic={}
    dic["Movie_Name"] = movie.find('td', class_='titleColumn').a.text

    dic['Rating'] = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]

    dic['Year']  = movie.find('span',class_='secondaryInfo').text.strip('()')

    movies_list.append(dic)


df = pd.DataFrame(movies_list)
df.to_csv('IMDB RATING.csv', index=False)

    # print(rating, name, year)
    