from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

# connecting with mongodb
cluster = MongoClient('your connection string')

# giving cluster name
db = cluster["localBookData"]

# giving collection name
collection = db["allBookDetails"]

total_pages = 50

# titles = ['Title', 'Rating', 'Price', 'Stock']


def individual_product(product_url, row):
    product_html_text = requests.get(f'https://books.toscrape.com/catalogue/{product_url}').content
    product_soup = BeautifulSoup(product_html_text, 'lxml')
    product_data = product_soup.find('article', class_='product_page')

    # extracting image url
    raw_img = product_data.find('img')['src']
    raw_img = raw_img.split('/')[2:]
    img = ''
    for char in raw_img:
        img = img + '/' + char
    img = 'https://books.toscrape.com' + img

    # extracting title
    title = product_data.find('div', class_='col-sm-6 product_main').h1.text

    # extracting price
    price = product_data.find('p',class_='price_color').text
    # print(price)

    # extracting rating
    rating = product_data.find('p','star-rating')['class'][1]

    # extracting description
    description = product_data.findAll('p')[3].text

    # extracting table content
    table = product_data.find('table' , class_='table table-striped').findAll('td')
    upc = table[0].text
    product_type = table[1].text
    price_excl_tax = table[2].text
    price_incl_tax = table[3].text
    tax = table[4].text
    availability = table[5].text
    num_reviews = table[6].text

    # print(row, upc, product_type, price_excl_tax, price_incl_tax, tax, availability, num_reviews)

    post = {"_id": row, "upc": upc, "Title": title, "description": description, "Rating": rating[-1], "price": price,
            "stock": availability, "product_type" : product_type, "price_excl_tax": price_excl_tax,
            "price_incl_tax": price_incl_tax, "tax": tax, "num_reviews": num_reviews}

    collection.insert_one(post)
    print(f'product {row} inserted into database')


row = 1
for page in range(total_pages):
    with open(f'./sampleWebpages/page-{page + 1}.html', 'rb') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    books_data = soup.findAll('article', class_='product_pod')


    for book in books_data:
        product_url = book.h3.a['href']


        # calling function to get individual product details
        individual_product(product_url,row)

        # print(product_url)
        row+=1
    print(f"page number : {page+1} done")

print("\nALl Books with details uploaded to the database")

