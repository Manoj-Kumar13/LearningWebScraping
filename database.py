from bs4 import BeautifulSoup
import requests
import pymongo
from pymongo import MongoClient

# connecting with mongodb
cluster = MongoClient('your connection string')
# giving cluster name
db = cluster["booksData"]
# giving collection name
collection = db["allBooks"]

# creating the post data
# post1 = {"_id": 0, "name": "Chris", "score": 5}
# post2 = {"_id": 1, "name": "Brad", "score": 7}
#
# collection.insert_one(post1)
# collection.insert_one(post2)

total_pages = 50

titles = ['Title', 'Rating', 'Price', 'Stock']

row = 1
for page in range(total_pages):
    html_text = requests.get(f'https://books.toscrape.com/catalogue/page-{page+1}.html').text

    soup = BeautifulSoup(html_text,'lxml')
    books_data = soup.findAll('article', class_='product_pod')

    for book in books_data:
        col = 0
        title = book.h3.a['title']
        rating = book.p['class']
        price = book.find('div', class_='product_price').p.string
        stock = book.find('div', class_='product_price').find('p',class_='instock').contents[2].strip()
        price = price.split('Â')

        post = {"_id": row, "Title": title, "Rating": rating[-1], "price": price[1], "Stock": stock}

        collection.insert_one(post)

        row+=1
    print(f"page number : {page+1} done")

print("\nALl Books uploaded to the database")