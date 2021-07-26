from bs4 import BeautifulSoup
import requests
import pandas as pd


def load_source(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_prices(source):
    dict = {}
    soup = BeautifulSoup(source, "html.parser")
    info = soup.find_all("a", class_='announcement-item')
    for i in info:
        try:
            modelis = i.find("div", class_='announcement-title')
            modelis_result = modelis.get_text().strip().split(',')[0]
            litrazas = modelis.get_text().strip().split(',')[1]
            kainos = i.find("div", class_='announcement-pricing-info')
            kainos_rezult = kainos.get_text().strip()
            informacija = i.find("div", class_='bottom-aligner')
            data = informacija.find(attrs={"title": "Pagaminimo data"}).get_text().strip()[:4]
            kuras = informacija.find(attrs={"title": "Kuro tipas"}).get_text().strip()
            deze = informacija.find(attrs={"title": "Pavarų dėžė"}).get_text().strip()
            galia = informacija.find(attrs={"title": "Galia"}).get_text().strip()
            rida = informacija.find(attrs={"title": "Rida"}).get_text().strip()
            miestas = informacija.find(attrs={"title": "Miestas"}).get_text().strip()
            masina = dict.update({"Modelis": modelis_result,
                         "Litrazas": litrazas,
                         "Kaina": kainos_rezult,
                         "Pagaminimo data": data,
                         "Kuro tipas": kuras,
                         "Pavarų dėžė": deze,
                         "Galia": galia,
                         "Rida": rida,
                         "Miestas": miestas
                         })
        except:
            pass
        print(dict)





if __name__ == '__main__':
    url_to_scrape = 'https://autoplius.lt/skelbimai/naudoti-automobiliai?make_id=103'
    source = load_source(url_to_scrape)
    tiltles = get_prices(source)
