import aiohttp
import async_timeout
import asyncio
import requests

from pages.all_books_page import AllBooksPage


PAGE_CONTENT = requests.get('https://books.toscrape.com').content

page = AllBooksPage(PAGE_CONTENT)

loop = asyncio.get_event_loop()

books = page.books

async def fetch_page(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url, ssl=False) as response:
            return await response.text()

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = [f'https://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(1, page.page_count)]
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))

for page_content in pages:
    page = AllBooksPage(page_content)
    books.extend(page.books)

