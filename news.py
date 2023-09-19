import requests
from bs4 import BeautifulSoup

date = '2023.08.01'
headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
response = requests.get('https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=001&date=20230918&page=1',headers=headers)
soup = BeautifulSoup(response.text,'html.parser')


    

   