from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://books.toscrape.com/').text

soup = BeautifulSoup(html_text,'lxml')
books_data = soup.findAll('article', class_='product_pod')

for book in books_data:
    print(book.h3.a['title'])
