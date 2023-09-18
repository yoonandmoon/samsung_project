import requests
from bs4 import BeautifulSoup

date = '2023.08.01'
url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=001&date=20230918&page=1'
headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'html.parser')

for news_item in soup.select('div.list_body ul li'):
    response = requests.get(news_item.select('dt')[1].select_one('a').attrs['href'],headers=headers)
    news_soup = BeautifulSoup(response.text,'html.parser')

    print(news_soup.select('h2#title_area').text)
    print('')
    # print(news_soup.select('div.end_body_wrp #articlebody').text)


    break
    # print(news_item.select('dt')[1].select_one('a').text.strip())
    

   