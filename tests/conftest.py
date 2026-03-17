import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.library import Library
import pytest

@pytest.fixture
def library():
    lib = Library()
    lib.add_book("Война и мир", "Толстой")
    lib.add_book("1984", "Оруэлл")
    lib.add_book("Гарри Поттер и отсутствие Фролова", "Роулинг")
    print("Setup: библиотека готова")
    yield lib
    lib.books.clear()
    print("Teardown: библиотека очищена")

@pytest.fixture(scope="function")
def empty_library():
    return Library()

@pytest.fixture(scope="module")
def library_readonly():
    lib = Library()
    books = [
        ("Книга1", "Автор1"),
        ("Книга2", "Автор2"),
        ("Книга3", "Автор3"),
        ("Книга4", "Автор4"),
        ("Книга5", "Автор5")
    ]
    for title, author in books:
        lib.add_book(title, author)
    return lib

@pytest.fixture(autouse=True)
def log_tests(request):
    print("=" * 50 + request.node.name)
    yield
    print("Завершён")

