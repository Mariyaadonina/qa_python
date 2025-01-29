
4 спринт
Финальный проект
Файлы:
conftest.py - (фикстура)
main.py - класс BooksCollector
tests.py - тестовый класс TestBooksCollector

Тестовые методы класса TestBooksCollector:
test_add_new_book_add_incorrect_name_failed: добавление некорректных наименований
test_set_book_genre_incorrect_genre_failed: установка некорректного жанра для книги
test_get_book_genre_success: получение жанра книги
test_get_books_with_specific_genre_add_dict_success: получение книг по жанру
test_get_books_with_specific_genre_wrong_genre_failed: получение книг по некорреткному жанру
test_get_books_genre_success: получение всей коллекции книг с жанрами
test_get_books_for_children_success: получение детских книг
test_add_book_in_favorites_correct_name_success: добавление книг в избранное
test_add_book_in_favorites_incorrect_failed: добавление книг в избранное
test_delete_book_from_favorites_one_book_success: удаление книги из избранного
test_delete_book_from_favorites_wrong_book_failed: Удаление книги из избранного
test_get_list_of_favorites_books_success: получение списка избранных книг
Запуск тестов
pytest -v
# qa_python