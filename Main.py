import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL du site à scraper
url = "http://quotes.toscrape.com/"

# Récupérer le contenu de la page
response = requests.get(url)
html_content = response.text

# Analyser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver toutes les citations sur la page
quotes = soup.find_all('span', class_='text')

# Trouver les auteurs associés à chaque citation
authors = soup.find_all('small', class_='author')

# Trouver les tags associés aux citations
tags = soup.find_all('a', class_='tag')

# Créer une liste pour stocker les données
data = []

# Extraire les citations, auteurs et tags
for i in range(len(quotes)):
    quote = quotes[i].text
    author = authors[i].text
    tag = tags[i % len(tags)].text  # Répéter les tags si nécessaire
    data.append({'quote': quote, 'author': author, 'tag': tag})

# Sauvegarder les données dans un fichier CSV
df = pd.DataFrame(data)
df.to_csv('quotes.csv', index=False)

# Afficher les 5 premières lignes pour vérifier
print(df.head())