from bs4 import BeautifulSoup
import requests
import xlsxwriter

total_pages = 50

workbook = xlsxwriter.Workbook('sampleData.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',80)
worksheet.set_column('B:B',30)
worksheet.set_column('C:C',20)
worksheet.set_column('D:D',30)

workbook = xlsxwriter.Workbook('sampleData.xlsx')
worksheet = workbook.add_worksheet()

titles = ['Title', 'Rating', 'Price', 'Stock']

for cl in range(4):
    worksheet.write(0, cl, titles[cl])

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
        # print(stock)
        price = price.split('Â')
        worksheet.write(row, col, title)
        worksheet.write(row, col+1, rating[-1])
        worksheet.write(row, col+2, price[1])
        worksheet.write(row, col+3, stock)
        row+=1
    print(f"page number : {page+1} done")

workbook.close()