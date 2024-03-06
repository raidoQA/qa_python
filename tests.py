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

    @pytest.mark.parametrize("book, genre", [
        ('Дракула', 'Ужасы'),
        ('Метро 2033', 'Фантастика'),
        ('Внутри убийцы', 'Детективы'),
        ('Институт', 'Ужасы'),
        ('Чебурашка', 'Мультфильмы'),
        ('Финт', 'Комедии')
        ])
    def test_get_books_with_specific_genre(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_with_specific_genre(genre) == [book]
    
    @pytest.mark.parametrize("book, genre", [
        ('Жребий', 'Ужасы'),
        ('Метро 2033', 'Фантастика'),
        ('Внутри убийцы', 'Детективы')
        ])
    def test_get_books_with_specific_genre_not_have(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_with_specific_genre('Роман') == []

    def test_get_books_genre(self, collector):
        collector.add_new_book('Порог')
        collector.set_book_genre('Порог', 'Фантастика')
        assert collector.get_books_genre() == {'Порог': 'Фантастика'}

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Сияние')
        collector.add_new_book('Чебурашка')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Чебурашка', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Чебурашка']
    
    def test_get_books_not_for_children(self, collector):
        collector.add_new_book('Воскреситель')
        collector.add_new_book('Чебурашка')
        collector.set_book_genre('Воскреситель', 'Ужасы')
        collector.set_book_genre('Чебурашка', 'Мультфильмы')
        assert collector.get_books_for_children() != ['Воскреситель']

    @pytest.mark.parametrize("book", ['Питер Пен', 'Лед и Пламя'])
    def test_add_book_in_favorites(self, collector, book):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

    @pytest.mark.parametrize("book", ['Зеленая миля', 'Король лев'])
    def test_delete_book_from_favorites(self, collector, book):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize("books", [['Винни Пух'], ['Дядя Федор']])
    def test_get_list_of_favorites_books(self, collector, books):
        favorites = []
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
            favorites.append(book)
        assert collector.get_list_of_favorites_books() == favorites