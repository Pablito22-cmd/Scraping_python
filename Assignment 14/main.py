import requests 
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import utils as u

myHtml = None
myFile = "htmlWiki.txt"
myLink = "https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes#Season_1_(2011)"

scrapeData = []

if Path(myFile).exists():
    print("Leggo")
    myHtml = u.useFile(myFile)
else:
    print("Scarico")
    myHtml = u.downloadHTML(myLink,myFile)

soup = BeautifulSoup(myHtml, "html.parser")
epTables = soup.find_all("table",class_="wikitable plainrowheaders wikiepisodetable")
epTables.pop(8)

season = 1
for table in epTables:
    episodes = table.find_all("tr",class_="vevent module-episode-list-row")
    for episode in episodes:
        info = episode.find_all("td")
        data = {
            "Stagione": season,
            "NumEpisodio": info[0].contents[0],
            "Titolo": info[1].find("a").get("title"),
            #"Visualizzazioni": episode.find()
        }
        
        director = info[2].find("a")
        if director:
            data["Regista"] = director.get("title")
        else:
            data["Regista"] = info[2].contents[0]

        writer = info[3].find("a")
        if writer:
            data["Sceneggiatore"] = writer.get("title")
        else:
            data["Sceneggiatore"] = info[3].contents[0]

        data["DataRilascio"] = info[4].contents[0]
        data["Visualizzazioni (mil)"] = info[5].contents[0]
        scrapeData.append(data)

    season += 1

df = pd.DataFrame(scrapeData)
df.to_csv('GOT_episodes.csv', index=False)
print(df.head())