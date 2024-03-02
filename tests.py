import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
        
    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book_add_three_books(self, collector):
        books = ['Дюна', 'Маугли', 'Зеленая миля']
        for book in books:
            collector.add_new_book(book)
        assert len(collector.get_books_genre()), 3
    
    def test_set_book_genre_with_true_genre(self, collector):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион', 'Фантастика')
        assert collector.get_book_genre('Гиперион') == 'Фантастика'

    def test_set_book_genre_with_other_genre(self, collector):
        collector.add_new_book('Темный лес')
        collector.set_book_genre('Темный лес', 'Фантастика')
        assert collector.get_book_genre('Темный лес') != 'Детективы'

    @pytest.mark.parametrize("genre", ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre(self, collector, genre):
        books = ['Дракула', 'Институт', 'Метро 2033', 'Внутри убийцы', 'Чебурашка', 'Финт']
        for book in books:
            collector.add_new_book(book)
        if book == 'Дракула' and 'Институт':
            collector.set_book_genre(book, 'Ужасы')
        collector.set_book_genre('Метро 2033', 'Фантастика')
        collector.set_book_genre('Внутри убийцы', 'Детективы')
        collector.set_book_genre('Чебурашка', 'Мультфильмы')
        collector.set_book_genre('Финт', 'Комедии')
        assert (collector.get_books_with_specific_genre(genre) == 
        ['Метро 2033'] if genre == 'Фантастика' else 
        ['Дракула', 'Институт'] if genre == 'Ужасы' else 
        ['Внутри убийцы'] if genre == 'Детективы' else 
        ['Чебурашка'] if genre == 'Мультфильмы' else 
        ['Финт'] if genre == 'Комедии' 
        else [])
    
    def test_get_books_with_specific_genre_not_have(self, collector):
        assert len(collector.get_books_with_specific_genre('Роман')) == 0

    def test_get_books_genre(self, collector):
        collector.add_new_book('Порог')
        collector.set_book_genre('Порог', 'Фантастика')
        assert collector.get_books_genre() == {'Порог': 'Фантастика'}

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Дракула')
        collector.add_new_book('Чебурашка')
        collector.set_book_genre('Дракула', 'Ужасы')
        collector.set_book_genre('Чебурашка', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Чебурашка']
    
    def test_get_books_not_for_children(self, collector):
        collector.add_new_book('Дракула')
        collector.add_new_book('Чебурашка')
        collector.set_book_genre('Дракула', 'Ужасы')
        collector.set_book_genre('Чебурашка', 'Мультфильмы')
        assert collector.get_books_for_children() != ['Дракула']

    @pytest.mark.parametrize("book", ['Дракула', 'Чебурашка'])
    def test_add_book_in_favorites(self, collector, book):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

    @pytest.mark.parametrize("book", ['Дракула', 'Чебурашка'])
    def test_delete_book_from_favorites(self, collector, book):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize("books, favorites", [(['Дракула', 'Чебурашка'], ['Дракула', 'Чебурашка'])])
    def test_get_list_of_favorites_books(self, collector, books, favorites):
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == favorites