import requests
import json

favourite = input("Ievadi savu mīļāko TV šovu: ")
if not favourite:
    favourite = "Viņas Melo Labāk" #Friends, Big Bang Theory, Suits

def get_tv_show_information_json():
    url = f"http://api.tvmaze.com/search/shows?q={favourite}"
    response = requests.get(url)
    data_from_json = response.json()
    return data_from_json

def output():
    z = get_tv_show_information_json()
    show_name = z[0]["show"]["name"]
    show_year = z[0]["show"]["premiered"][:4]
    print(f'Tavu mīļāko šovu "{show_name}" sāka pārraidīt {show_year}.gadā!')
    with open("your_favourite_show.json", mode="w", encoding="UTF8") as write_file:
        json.dump(get_tv_show_information_json(), write_file, indent=4, ensure_ascii=False)

output()
