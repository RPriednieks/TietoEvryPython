import requests

webpage_response = requests.get("https://www.neste.lv/lv/content/degvielas-cenas")

webpage = webpage_response.text
print(webpage)

