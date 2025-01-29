import pytest


from main import BooksCollector


class TestBooksCollector:


    @pytest.mark.parametrize('book_names', ['', 'Название_книги_на_сорок_один_символ_отриц',
                                            'Название_книги_на_сорок_два_символаа_отриц'])
    def test_add_new_book_add_negative_book(self, collector, book_names):
        collector = BooksCollector()
        collector.add_new_book(book_names)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_added_genre_book_positive_result(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холм')
        collector.set_book_genre('Шерлок Холм', 'Детективы')
        assert collector.books_genre.get('Шерлок Холм') == 'Детективы'

    def test_set_book_genre_add_genre_is_not_list(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холм')
        collector.set_book_genre('Шерлок Холм', 'Жанр_которого_нет')
        assert collector.books_genre.get('Шерлок Холм') == ''

    def test_get_book_genre_for_name_positive_result(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холм')
        collector.set_book_genre('Шерлок Холм', 'Детективы')
        assert collector.get_book_genre('Шерлок Холм') == 'Детективы'

    def test_get_books_with_specific_genre_get_two_books_detectiv(self, collector):
        collector = BooksCollector()
        collector.books_genre = {'Шерлок Холмс': 'Детективы', 'Шерлок Холмс_1': 'Детективы', 'Шерлок Холмс_2': 'Ужасы',
                               'Шерлок Холмс_3': 'Мультфильмы'}
        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_for_children_two_books(self, collector):
        collector = BooksCollector()
        collector.books_genre = {'Шерлок Холмс': 'Мультфильмы', 'Шерлок Холмс_1': 'Детективы', 'Шерлок Холмс_2': 'Ужасы',
                               'Шерлок Холмс_3': 'Комедии'}
        assert len(collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_one_book(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холм')
        collector.add_book_in_favorites('Шерлок Холм')
        assert len(collector.get_list_of_favorites_books()) == 1 and collector.favorites[0] == 'Шерлок Холм'

    def test_add_book_in_favorites_add_two_double_book(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холм')
        collector.add_book_in_favorites('Шерлок Холм')
        collector.add_book_in_favorites('Шерлок Холм')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холм')
        collector.add_book_in_favorites('Шерлок Холм')
        collector.delete_book_from_favorites('Шерлок Холм')
        assert len(collector.favorites) == 0
