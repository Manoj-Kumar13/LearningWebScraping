from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests

# connecting with mongodb
cluster = MongoClient('your connection string')
# giving cluster name
db = cluster["localBookData"]
# giving collection name
collection = db["allBooks"]

total_pages = 50

# fetching saving webpages locally
for page in range(total_pages):
    html_text = requests.get(f'https://books.toscrape.com/catalogue/page-{page+1}.html').content

    open(f'./sampleWebpages/page-{page+1}.html', 'wb').write(html_text)
    print(f'saved page {page+1} !')

print("done saving all pages")


row = 1
for page in range(total_pages):
    #reading local file
    with open(f'./sampleWebpages/page-{page+1}.html', 'rb') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    books_data = soup.findAll('article', class_='product_pod')

    for book in books_data:
        col = 0
        title = book.h3.a['title']
        rating = book.p['class']
        price = book.find('div', class_='product_price').p.text
        stock = book.find('div', class_='product_price').find('p',class_='instock').contents[2].strip()
        print(price)

        # print(f'title = {title}, rating = {rating}, price = {price}, stock = {stock}\n')

        post = {"_id": row, "Title": title, "Rating": rating[-1], "price": price, "Stock": stock}

        collection.insert_one(post)

        row+=1
    print(f"page number : {page+1} done")

print("\nALl Books uploaded to the database")