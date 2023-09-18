import requests
import pandas as pd
from bs4 import BeautifulSoup
URL = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=2'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
response = requests.get(URL,headers=headers)
bs = BeautifulSoup(response.text,'html.parser')

#column구하기 식
# list = bs.select('th')
# for title in list:
#     column = title.text

stock=[]
for i in range(2,5):
    url = f'https://finance.naver.com/item/sise_day.naver?code=005930&page={i}'
    headers= {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    items = soup.select('table.type2 tr')
    
    for item in items:
         if len(item.select('td .tah')) > 0:
              a0 = item.select('td .tah')[0].text
              a1 = item.select('td .tah')[1].text
              a2 = item.select('td .tah')[2].text.strip()
              a3 = item.select('td .tah')[3].text
              a4 = item.select('td .tah')[4].text
              a5 = item.select('td .tah')[5].text
              a6 = item.select('td .tah')[6].text

              stock.append({
                '날짜': a0,
                '종가': a1,
                '전일비': a2,
                '시가': a3,
                '고가':a4,
                '저가':a5,
                '거래량':a6
            })
print(stock)
df = pd.DataFrame(stock)
df.to_csv('stock.csv',encoding='utf-8-sig',index=False)

        



        
    


