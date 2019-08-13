import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep

boilerplate = 'https://www.rithmschool.com'
response = requests.get('https://www.rithmschool.com/blog')
data = BeautifulSoup(response.text, 'html.parser')

# find current page
current = data.find(class_='pagination').find(class_='current').get_text()
count = 1

# find last page
last = data.find(class_='pagination').find(class_='last').find('a')['href']
url_format = boilerplate + last[:-1]
last_num = int(last[-1])


# prepare csv file
with open('article.csv', 'w', newline='') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['title', 'link', 'date'])

# crawl and scrape
for i in range(count, last_num+1):
    # 2 second delay
    sleep(2)
    if i != current:
        response = requests.get(url_format+str(i))
        data = BeautifulSoup(response.text, 'html.parser')
        articles = data.find_all('article')

        with open('article.csv', 'a', newline='') as file:
            csv_writer = writer(file)
            for article in articles:
                a_tag = article.find('a')
                title = a_tag.get_text()
                link = a_tag['href']
                date = article.find('time')['datetime']
                csv_writer.writerow([title, link, date])
