import requests
from bs4 import BeautifulSoup

url = 'https://www.rsssf.org/tables/2006f.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')

rows = table.find_all('tr')[1:] # Excluimos la primera fila que contiene las cabeceras de la tabla

for row in rows:
    columns = row.find_all('td')
    if len(columns) == 11: # Excluimos las filas que no contienen datos de partidos
        date = columns[0].text
        team1 = columns[2].text
        team2 = columns[4].text
        score = columns[6].text
        print(f'{date} - {team1} vs. {team2}: {score}')
