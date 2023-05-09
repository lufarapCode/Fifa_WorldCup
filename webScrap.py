
from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962,1966, 1970, 1974, 1978,1982,
         1986, 1990, 1994, 1998, 2002,2006, 2010, 2014, 2018]

# Se crea la funcion para trer toda la data necesaria
def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    #Mandar solicitud
    response = requests.get(web)
    #respuesta en formtato html
    content = response.text
    # permite leer el texto de content
    soup = BeautifulSoup(content, 'lxml')

    # inspecciono la pagina y encuentro que el tag que necesito es div y la clase se llama footballbox
    matches = soup.find_all('div', class_='footballbox')
    # creamos la variable de la lista
    home = []
    score = []
    away = []
    # extraemos unicamente el equipo local, visitante y marcador
    for match in matches:
        home.append(match.find('th',class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())

    dict_soccer = {'home':home, 'score':score, 'away':away }
    df_soccer = pd.DataFrame(dict_soccer)
    df_soccer['year'] = year
    
    return df_soccer

# Lista de comprencion
fifa = [get_matches(year) for year in years]

print(fifa)
# concatenar los dataframes 
df_fifa = pd.concat(fifa, ignore_index=True)

# indix=false, para no importar en el dataframe el index inicial
df_fifa.to_csv('fifa_worldCup_historical.csv', index=False)

df_fixture = get_matches(2022)
df_fixture.to_csv('fifa_fixture_2022.csv', index=False)


