from bs4 import BeautifulSoup
import requests
import json


def main():
   
    response = requests.get("https://souhrada.github.io/bsoup-exam/")

    soup = BeautifulSoup(response.content, "html.parser")
    ingredience = soup.select("h2")

    ingredience = { # chybí rovnítko
        ingredience[0]. text,
        ingredience[1]. text,
        ingredience[2]. text,
        ingredience[3]. text
    }
    if not ingredience:
        print("nenasel jsem zadne")
    
    # proč chybí print ingrediencí?
       
   
    # response = requests.get(url)

    # BeautifulSoup(response.content, "html.parser") <--- Úkol: popiš krátce, co tohle dělá
    # zacne zpracovavat stazena data


if __name__ == "__main__":
    main()
