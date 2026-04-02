import requests 
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import utils as u

myHtml = None
myFile = "htmlFile.txt"
myLink = "https://www.scrapingcourse.com/button-click"

scrapeData = []

if Path(myFile).exists():
    print("Leggo")
    myHtml = u.useFile(myFile)
else:
    print("Scarico")
    myHtml = u.downloadHTML(myLink,myFile)

soup = BeautifulSoup(myHtml, "html.parser")