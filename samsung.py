import csv

new_file = open('samsung.csv','w',encoding="utf-8")




with open('news.csv','r',encoding="utf-8") as file:
    rdr = csv.reader(file)
    
    for data in rdr:
        print(data)

text = '삼성전자 안녕하세요.'
print(text.find('삼성전자'))