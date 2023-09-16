

import requests
from bs4 import BeautifulSoup
URL = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=2'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
response = requests.get(URL,headers=headers)
bs = BeautifulSoup(response.text,'html.parser')
data = bs.select('th')
print(data)