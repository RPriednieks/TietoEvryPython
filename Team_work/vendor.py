from bs4 import BeautifulSoup
import requests

fuel_types = ["95", "95 Premium", "98", "DD", "DD Premium", "LPG", "CNG", "85"]
vendors = ("Neste", "Circle K", "Virši", "Viada")

def get_fuel_types(types):
    """
    Input arguments for function = list
    Returns dictionary with empty values.
    Input example:
        get_fuel_types(["95", "95 Premium"])
    Output example:
        {'95': None, '95 Premium': None}
    """
    fuel_types = dict.fromkeys(types)
    return fuel_types


def get_vendors(ven):
    """
    Input arguments for function = tuple
    Coverts tuple into a list. I know, it is silly.
    Input example:
        get_vendors(("Neste", "Circle K"))
    Output example:
        ['Neste', 'Circle K']
    """
    vendors_list = list(ven)
    return vendors_list


def get_prices(vendor):
    """
    Input arguments for function = string
    Returns dictionary of prices.
    Input example:
        get_prices("Neste")
    Output example:
        {'95': 1.487, '95 Premium': None, '98': 1.527, 'DD': 1.367, 'DD Premium': 1.457, 'LPG': None,
        'CNG': None, '85': None}
    """
    if vendor == "Neste":
        neste_response = requests.get("https://www.neste.lv/lv/content/degvielas-cenas")
        neste_webpage = neste_response.text
        neste_soup = BeautifulSoup(neste_webpage, "lxml")
        data = neste_soup.find_all("p")
        fuel_dict = get_fuel_types(fuel_types)
        fuel_dict["95"] = float(data[3].string)
        fuel_dict["98"] = float(data[6].string)
        fuel_dict["DD"] = float(data[9].string)
        fuel_dict["DD Premium"] = float(data[12].string)
        return fuel_dict
    elif vendor == "Circle K":
        circlek_response = requests.get("https://www.circlek.lv/degvielas-cenas")
        circlek_webpage = circlek_response.text
        neste_soup = BeautifulSoup(circlek_webpage, "lxml")
        data = neste_soup.find_all("td")
        fuel_dict = get_fuel_types(fuel_types)
        fuel_dict["95"] = float(data[1].string[:5])
        fuel_dict["98"] = float(data[4].string[:5])
        fuel_dict["DD"] = float(data[7].string[:5])
        fuel_dict["DD Premium"] = float(data[10].string[:5])
        fuel_dict["LPG"] = float(data[13].string[:5])
        return fuel_dict
    elif vendor == "Virši":
        virsi_response = requests.get("https://www.virsi.lv/lv/degvielas-cena")
        virsi_webpage = virsi_response.text
        virsi_soup = BeautifulSoup(virsi_webpage, "lxml")
        data = virsi_soup.find_all("p")
        fuel_dict = get_fuel_types(fuel_types)
        fuel_dict["95"] = float(data[4].string)
        fuel_dict["98"] = float(data[6].string)
        fuel_dict["DD"] = float(data[2].string)
        fuel_dict["CNG"] = float(data[8].string)
        fuel_dict["LPG"] = float(data[10].string)
        return fuel_dict
    elif vendor == "Viada":
        viada_response = requests.get("https://www.viada.lv/zemakas-degvielas-cenas/")
        viada_webpage = viada_response.text
        viada_soup = BeautifulSoup(viada_webpage, "lxml")
        data = viada_soup.find_all("td")
        fuel_dict = get_fuel_types(fuel_types)
        fuel_dict["95"] = float(data[1].string[:5])
        fuel_dict["95 Premium"] = float(data[4].string[:5])
        fuel_dict["98"] = float(data[7].string[:5])
        fuel_dict["DD"] = float(data[10].string[:5])
        fuel_dict["DD Premium"] = float(data[13].string[:5])
        fuel_dict["LPG"] = float(data[16].string[:5])
        fuel_dict["85"] = float(data[19].string[:5])
        return fuel_dict
