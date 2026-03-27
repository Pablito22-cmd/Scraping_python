import requests 
from bs4 import BeautifulSoup

def downloadHTML(link,myFile):
    headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}

    file = open(myFile,"w")
    try:
        response = requests.get(link,headers=headers)
        response.raise_for_status()
        file.write(response.text)
    except requests.exceptions.Timeout:
        print("Richiesta scaduta")
    except requests.exceptions.HTTPError:
        print("Errore HTTP")
    except requests.exceptions.RequestException as e:
        print("Errore generico")
        print("Errore GET:", e)

    file.close()
    return response.text

def useFile(fileName):
    file = open(fileName,"r")
    return file.read()

