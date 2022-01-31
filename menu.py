from app import books


USER_CHOICE = '''Enter one of the following:

- 'b' to look at the best rated books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: '''

def print_best_books():
    print('---BEST---')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)

def print_cheapest_books():
    print('---CHEAPEST---')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

books_generator = (x for x in books)

def next_available_book():
    print('---NEXT---')
    print(next(books_generator))

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': next_available_book
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Wrong command! Please try again!')

        user_input = input(USER_CHOICE)

menu()
