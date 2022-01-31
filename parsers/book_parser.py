import re

from locators.books_locators import BookLocators


class BookParser:


    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price}, Rating: {self.rating}/5 stars>'

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator).attrs.get('title')
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs.get('href')
        return item_link

    @property
    def price(self):
        regex = '£([0-9]+\.[0-9]+)'
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        prices = re.search(regex, item_price)
        item_price = float(prices.group(1))
        return item_price

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs.get('class', [])
        classes = [i for i in classes if i != 'star-rating']
        return BookParser.RATINGS.get(classes[0])
