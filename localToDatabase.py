from bs4 import BeautifulSoup
from pymongo import MongoClient

# connecting with mongodb
cluster = MongoClient('your connection string')
# giving cluster name
db = cluster["localBookData"]
# giving collection name
collection = db["allBooks"]

total_pages = 5

titles = ['Title', 'Rating', 'Price', 'Stock']

row = 1
for page in range(total_pages):
    #reading local file
    with open(f'./sampleWebpages/page{page+1}.html', 'r') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    books_data = soup.findAll('article', class_='product_pod')

    for book in books_data:
        col = 0
        title = book.h3.a['title']
        rating = book.p['class']
        price = book.find('div', class_='product_price').p.string
        stock = book.find('div', class_='product_price').find('p',class_='instock').contents[2].strip()
        price = price.split('Â')

        # print(f'title = {title}, rating = {rating}, price = {price}, stock = {stock}\n')

        post = {"_id": row, "Title": title, "Rating": rating[-1], "price": price[1], "Stock": stock}

        collection.insert_one(post)

        row+=1
    print(f"page number : {page+1} done")

print("\nALl Books uploaded to the database")