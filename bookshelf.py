class Book:
    def __init__(self, title: str, author: str, category: str):
        self.title = title
        self.author = author
        self.category = category

    def __repr__(self):
        return f'{self.title} by {self.author}, {self.category}'


class Shelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def sort_books(self):
        self.books.sort(key=lambda book: book.title)


class Room:
    def __init__(self):
        self.shelves = {}  # key: category, value: Shelf

    def add_book(self, book):
        if book.category not in self.shelves:
            self.shelves[book.category] = Shelf()
        self.shelves[book.category].add_book(book)

    def organize_books(self):
        for shelf in self.shelves.values():
            shelf.sort_books()


books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Classics"),
    Book("1984", "George Orwell", "Dystopian"),
    Book("Oliver Twist", "Charles Dickens", "Classics"),
    Book("Brave New World", "Aldous Huxley", "Dystopian"),
]

bob_room = Room()
for book in books:
    bob_room.add_book(book)
bob_room.organize_books()

for category, shelf in bob_room.shelves.items():
    print(f'Shelf {category}: {shelf.books}')
