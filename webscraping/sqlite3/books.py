import requests, sqlite3
from bs4 import BeautifulSoup

base_url = 'http://books.toscrape.com/catalogue/category/books/history_32/index.html'

response = requests.get(base_url)

data = BeautifulSoup(response.text, 'html.parser')

books = data.find_all(class_='product_pod')
conn = sqlite3.connect('books.db')
c = conn.cursor()

# query = '''
#     CREATE TABLE books(
#         title TEXT,
#         price REAL,
#         star INTEGER
#     )
# '''

# c.execute(query)

star_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}


for book in books:
    title = book.find('h3').find('a')['title']
    price = book.select('.price_color')[0].get_text()
    price = float(price.replace('Â', '').replace('£', ''))
    star = book.find(class_='star-rating')['class'][-1]
    # star = book.find(class_='star-rating').attrs['class'][-1]
    # star = book.find(class_='star-rating').get_attribute_list('class')[-1]
    # print(star)
    query = 'INSERT INTO books VALUES (?,?,?)'
    c.execute(query, (title, price, star_dict[star]))


conn.commit()
conn.close()

