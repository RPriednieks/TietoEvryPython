from bs4 import BeautifulSoup
import requests

def get_prices(vendor):
    if vendor == "Neste":
        neste_response = requests.get("https://www.neste.lv/lv/content/degvielas-cenas")
        neste_webpage = neste_response.text
        neste_soup = BeautifulSoup(neste_webpage, "lxml")
        data = neste_soup.find_all("p")
        gasoline_95 = float(data[3].string)
        gasoline_98 = float(data[6].string)
        diesel = float(data[9].string)
        diesel_premium = float(data[12].string)
        print(gasoline_95)
        print(gasoline_98)
        print(diesel)
        print(diesel_premium)
    elif vendor == "Circle K":
        circlek_response = requests.get("https://www.circlek.lv/degvielas-cenas")
        circlek_webpage = circlek_response.text
        neste_soup = BeautifulSoup(circlek_webpage, "lxml")
        data = neste_soup.find_all("td")
        gasoline_95 = float(data[1].string[:5])
        gasoline_98 = float(data[4].string[:5])
        diesel = float(data[7].string[:5])
        diesel_premium = float(data[10].string[:5])
        LPG = float(data[13].string[:5])
        print(gasoline_95)
        print(gasoline_98)
        print(diesel)
        print(diesel_premium)
        print(LPG)
    elif vendor == "Virši":
        virsi_response = requests.get("https://www.virsi.lv/lv/degvielas-cena")
        virsi_webpage = virsi_response.text
        virsi_soup = BeautifulSoup(virsi_webpage, "lxml")
        data = virsi_soup.find_all("p")
        gasoline_95 = float(data[4].string)
        gasoline_98 = float(data[6].string)
        diesel = float(data[2].string)
        CNG = float(data[8].string)
        LPG = float(data[10].string)
        print(gasoline_95)
        print(gasoline_98)
        print(diesel)
        print(CNG)
        print(LPG)
    elif vendor == "Viada":
        viada_response = requests.get("https://www.viada.lv/zemakas-degvielas-cenas/")
        viada_webpage = viada_response.text
        viada_soup = BeautifulSoup(viada_webpage, "lxml")
        data = viada_soup.find_all("td")
        gasoline_95 = float(data[1].string[:5])
        gasoline_95_premium = float(data[4].string[:5])
        gasoline_98 = float(data[7].string[:5])
        diesel = float(data[10].string[:5])
        diesel_premium = float(data[13].string[:5])
        LPG = float(data[16].string[:5])
        gasoline_85 = float(data[19].string[:5])
        print(gasoline_95)
        print(gasoline_95_premium)
        print(gasoline_98)
        print(diesel)
        print(diesel_premium)
        print(LPG)
        print(gasoline_85)

# get_prices("Neste")
# get_prices("Circle K")
# get_prices("Virši")
get_prices("Viada")

# for i in data:
#     print(i.string)