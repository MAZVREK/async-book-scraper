import requests

from pages.all_books_page import AllBooksPage


PAGE_CONTENT = requests.get('https://books.toscrape.com').content

page = AllBooksPage(PAGE_CONTENT)

books = page.books

for page_num in range(1, page.page_count):
    url = f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.extend(page.books)

