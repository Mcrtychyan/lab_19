class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if not title or not author:
            raise ValueError("Название и автор обязательны")
        if title in self.books:
            raise ValueError(f"Книга '{title}' уже есть")
        self.books[title] = {'author': author, 'available': 1, 'issued': 0}

    def issue_book(self, title):
        if title not in self.books:
            raise ValueError(f"Книга '{title}' не найдена")
        if self.books[title]['available'] == 0:
            raise ValueError(f"Нет доступных '{title}'")
        self.books[title]['available'] -= 1
        self.books[title]['issued'] += 1

    def return_book(self, title):
        if title not in self.books:
            raise ValueError(f"Книга '{title}' не найдена")
        if self.books[title]['issued'] == 0:
            raise ValueError(f"Нет выданных '{title}'")
        self.books[title]['issued'] -= 1
        self.books[title]['available'] += 1

    def get_available_count(self):
        return sum(b['available'] for b in self.books.values())

    def get_issued_count(self):
        return sum(b['issued'] for b in self.books.values())

    def get_book_info(self, title):
        return self.books.get(title)
