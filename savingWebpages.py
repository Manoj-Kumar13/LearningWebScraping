import requests

total_pages = 50

for page in range(total_pages):
    html_text = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html').content

    open(f'./sampleWebpages/page-{page+1}.html', 'wb').write(html_text)
    print(f'saved page {page} !')

print("done saving all pages")