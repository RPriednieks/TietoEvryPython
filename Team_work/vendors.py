import requests
from bs4 import BeautifulSoup

class Neste:
    neste_response = requests.get("https://www.neste.lv/lv/content/degvielas-cenas")
    neste_webpage = neste_response.text
    neste_soup = BeautifulSoup(neste_webpage, "lxml")
    data = neste_soup.find_all("p")

    def get_95(self):
        return float(Neste.data[3].string)

    def get_98(self):
        return float(Neste.data[6].string)

    def get_DD(self):
        return float(Neste.data[9].string)

neste = Neste()
print(neste.get_DD())
