import pandas as pd

netDB = pd.read_csv("netflix.csv")

Limitless = netDB[netDB["title"] == "Limitless"]

dirRobRod = (netDB["director"] == "Robert Rodriguez")
isMovie = (netDB["type"] == "Movie")
MovieRobRod = netDB[dirRobRod & isMovie]

date = netDB["date_added"] == "31-Jul-19"
diRobAlt = netDB["director"] == "Robert Altman"
dateRobAlt = netDB[date | diRobAlt]

Orson = (netDB["director"] == "Orson Welles")
Kri = (netDB["director"] == "Aditya Kripalani")
Raimi = (netDB["director"] == "Sam Raimi")
WelKriRai = netDB[Orson | Kri | Raimi]

mayMovies = netDB[netDB["date_added"].between("2019-05-01","2019-06-01")]

netDrop = netDB.dropna(subset="date_added")

singleAdd = netDB.drop_duplicates(subset=["date_added"],keep=False)