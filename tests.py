import pytest

from main import BooksCollector


class TestBooksCollector:

    # 1 test verifies 2 books are added to books collection
    def test_add_new_book_name_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление')
        collector.add_new_book('Наказание')
        assert collector.books_genre == {'Преступление': '', 'Наказание': ''}

    # 2 test verifies that books are not added to books collection when book names are out of range
    @pytest.mark.parametrize('book_name', ['', 'очень_длинное_название_книги_очень_длинное'])
    def test_add_new_book_name_len_out_of_range(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.books_genre == {}

    # 3 test verifies that book names duplicates are not saved in books collection
    def test_add_new_book_name_add_books_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление')
        collector.add_new_book('Наказание')
        collector.add_new_book('Преступление')
        collector.add_new_book('Наказание')
        assert collector.books_genre == {'Преступление': '', 'Наказание': ''}

    # 4 test verifies that get_book_genre method return selected book genre - added 20.11
    def test_get_book_genre_return_book_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Преступление': 'Фантастика'}
        assert collector.get_book_genre('Преступление') == 'Фантастика'

    # 5 test verifies that genre is not updated when parameters are not existing
    @pytest.mark.parametrize('book_name, genre', [['Не_название', 'Фантастика'], ['Преступление', 'Не_жанр']])
    def test_set_book_genre_genre_not_updated(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book('Преступление')
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre('Преступление') == ''

    # 6 test verifies that books list corresponds to selected genre
    def test_get_books_with_specific_genre_books_correspond_to_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Преступление': 'Детективы', 'Наказание': 'Детективы', 'Пони': 'Комедии'}
        assert collector.get_books_with_specific_genre('Детективы') == ['Преступление', 'Наказание']

    # 7 test verifies that adult genre books don't get in children books list
    @pytest.mark.parametrize('book_name, genre', [['Преступление', 'Не_жанр'], ['Пони для взрослых', 'Ужасы'],
                                                  ['Преступление единорога', 'Детективы'], ['', '']])
    def test_get_books_for_children_books_list_not_updated(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_for_children() == []

    # 8 test verifies that book is added to favorites books list and uses get_list_of_favorites_books method
    def test_add_book_in_favorites_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая_книга')
        collector.add_new_book('Нелюбимая_книга')
        collector.add_book_in_favorites('Любимая_книга')
        assert collector.get_list_of_favorites_books() == ['Любимая_книга']

    # 9 test verifies that method get_list_of_favorites_books returs expected list of favorite books  - added 20.11
    def test_get_list_of_favorites_books_return_list(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая_книга')
        collector.add_new_book('Тоже_любимая_книга')
        collector.add_book_in_favorites('Любимая_книга')
        collector.add_book_in_favorites('Тоже_любимая_книга')
        assert collector.get_list_of_favorites_books() == ['Любимая_книга', 'Тоже_любимая_книга']

    # 10 test verifies that book is deleted from favorites books list and uses get_list_of_favorites_books method
    def test_delete_book_from_favorites_book_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая_книга')
        collector.add_new_book('Нелюбимая_книга')
        collector.add_book_in_favorites('Любимая_книга')
        collector.add_book_in_favorites('Нелюбимая_книга')
        collector.delete_book_from_favorites('Нелюбимая_книга')
        assert collector.get_list_of_favorites_books() == ['Любимая_книга']

    # 11 test verifies that books collection returned
    def test_get_books_genre_collection_returned(self):
        collector = BooksCollector()
        collector.books_genre = {'Преступление': 'Детективы', 'Наказание': 'Детективы', 'Пони': 'Комедии'}
        assert collector.get_books_genre() == {'Преступление': 'Детективы', 'Наказание': 'Детективы', 'Пони': 'Комедии'}