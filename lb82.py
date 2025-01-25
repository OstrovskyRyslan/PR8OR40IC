import requests
url = "https://www.vodafone.ua/rates"
response = requests.get(url)
if response.status_code == 200:
    content = response.text
    def parse_tariffs(html):
        lines = html.split("\n")  
        for line in lines:
            if 'тариф' in line.lower():  
                yield line.strip()
    print("Результати без використання бібліотек для парсингу:")
    for tariff_info in parse_tariffs(content):
        print(tariff_info)
else:
    print("Не вдалося завантажити сторінку. Код відповіді:", response.status_code)
#Використання BeautifulSoup 
from bs4 import BeautifulSoup
import requests
url = "https://www.vodafone.ua/rates"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("\nРезультати з використанням BeautifulSoup (фільтровані):")
    for tariff_block in soup.find_all("div", class_="col"):
        print(tariff_block.text.strip())
else:
    print("Не вдалося завантажити сторінку. Код відповіді:", response.status_code)
    