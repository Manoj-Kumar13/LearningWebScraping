import requests
import os
import datetime
from bs4 import BeautifulSoup

date = datetime.datetime.now()
date = date.strftime("%d-%m-%Y")
# print(date)

total_pages = 50
path = "C:\MyFolder\Rough\learningWebScraping"


# creating directory for webpages
# try:
#     os.makedirs(f"{path}\historicalData\{date}\webpages")
#     print(f"directory created successfully at {path}")
# except FileExistsError:
#     print("Directory already exists")
#
# # saving webpages locally
# for page in range(total_pages):
#     html_text = requests.get(f'https://books.toscrape.com/catalogue/page-{page+1}.html').content
# #
#     open(f'{path}\historicalData\{date}\webpages\page-{page+1}.html', 'wb').write(html_text)
#     print(f'saved page {page+1} !')
# #
# print("done saving all webpages pages")
# print("\nALl Books uploaded to the database")


# saving products locally

total_pages = 50

# creating directory for products
try:
    os.makedirs(f"{path}\historicalData\{date}\products")
    print(f"directory created successfully at {path}")
except FileExistsError:
    print("Directory already exists")
def individual_product(product_url, row):
    product_html_text = requests.get(f'https://books.toscrape.com/catalogue/{product_url}').content

    # saving product page
    open(f'{path}\historicalData\{date}\products\product-{row}.html', 'wb').write(product_html_text)

    print(f'product {product_url} saved to directory!')


row = 1
for page in range(total_pages):
    with open(f'{path}\historicalData\{date}\webpages\page-{page+1}.html', 'rb') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    books_data = soup.findAll('article', class_='product_pod')


    for book in books_data:
        product_url = book.h3.a['href']
        title = book.h3.a['title']


        # calling function to get individual product details
        individual_product(product_url, row)

        # print(product_url)
        row+=1
    print(f"page number : {page+1} done")

print(f"\nALl Books with details saved to the directory {path}")


