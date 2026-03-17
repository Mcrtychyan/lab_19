import pytest

@pytest.mark.parametrize("title,author", [
    ("Книга А", "Автор А"),
    ("Книга Б", "Автор Б"),
    ("Книга В", "Автор В"),
    ("Книга Г", "Автор Г"),
])

def test_add_book_valid(empty_library, title, author):
    empty_library.add_book(title, author)
    info = empty_library.get_book_info(title)
    assert info is not None
    assert info['author'] == author
    assert info['available'] == 1

@pytest.mark.parametrize("title,author,expected", [
    ("", "Автор", "Название и автор обязательны"),
    (None, "Автор", "Название и автор обязательны"),
    ("Книга", "", "Название и автор обязательны"),
    ("Книга", None, "Название и автор обязательны"),
])
def test_add_book_invalid(empty_library, title, author, expected):
    with pytest.raises(ValueError, match=expected):
        empty_library.add_book(title, author)

@pytest.mark.parametrize("books_count,expected", [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
])
def test_get_available_count(empty_library, books_count, expected):
    for i in range(books_count):
        empty_library.add_book(f"Книга{i}", f"Автор{i}")
    assert empty_library.get_available_count() == expected

def test_library_readonly_scope_module(library_readonly):
    print(f"ID: {id(library_readonly)}")
    assert len(library_readonly.books) == 5
    assert library_readonly.get_available_count() == 5

def test_library_readonly_scope_module_2(library_readonly):
    print(f"ID: {id(library_readonly)}")
    assert len(library_readonly.books) == 5
    assert library_readonly.get_available_count() == 5

def test_empty_library_scope_function(empty_library):
    print(f"ID: {id(empty_library)}")
    assert len(empty_library.books) == 0
    assert empty_library.get_available_count() == 0

def test_empty_library_scope_function_2(empty_library):
    print(f"ID: {id(empty_library)}")
    assert len(empty_library.books) == 0
    assert empty_library.get_available_count() == 0



def test_issue_return_book(library):
    title = "Война и мир"
    library.issue_book(title)
    assert library.get_available_count() == 2  # 3-1=2
    assert library.get_issued_count() == 1
    library.return_book(title)
    assert library.get_available_count() == 3

def test_issue_return_book_2(library):
    title = "1984"
    library.issue_book(title)
    info = library.get_book_info(title)
    assert info['available'] == 0
    assert library.get_available_count() == 2
    library.return_book(title)
    assert library.get_book_info(title)['available'] == 1

def test_issue_return_book_3(library):
    title = "Гарри Поттер и отсутствие Фролова"
    library.issue_book(title)
    assert library.get_available_count() == 2
    library.return_book(title)
    assert library.get_available_count() == 3