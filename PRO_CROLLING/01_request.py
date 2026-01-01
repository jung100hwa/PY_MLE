import requests
from bs4 import BeautifulSoup

codes = "005930"
url = f"https://finance.naver.com/item/sise.naver?code={codes}"
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('#_nowVal')
for link in links:
    title = link.text
    print(title)

# for link in links:
#     title = link.text
#     url   = link.attrs['href']
#     print(title)
#     print(url)
#     print("#" * 100)