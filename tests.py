import pytest
from main import BooksCollector

class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': '',
                                               'Что делать, если ваш кот хочет вас убить': ''}


    def test_add_new_book_already_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('Робинзон Крузо')
        collector.add_new_book('Робинзон Крузо')
        assert collector.get_books_genre() == {'Робинзон Крузо': ''}

    @pytest.mark.parametrize('name', ['',
                                      'Сказка о царе Салтане, о сыне его славном и могучем богат',
                                      'Сказка о царе Салтане, о сыне его славном и могучем богатыре Гвидоне Салтановиче и о прекрасной царевне Лебеди'])
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert len(books_collection.get_books_genre()) == 0   

    @pytest.mark.parametrize('name', ['Отверженные',
                                      'Над пропастью во ржи',
                                      'Оно'])
    def test_add_new_book_name_in_the_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre() 

    def test_set_book_genre_to_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Робинзон Крузо')
        collector.set_book_genre('Робинзон Крузо', 'Ужасы')
        assert collector.get_books_genre() == {'Робинзон Крузо': 'Ужасы'}      

    def test_set_book_genre_to_not_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Робинзон Крузо', 'Ужасы')
        assert collector.get_books_genre() == {}


    def test_set_book_genre_to_not_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Робинзон Крузо')
        collector.set_book_genre('Робинзон Крузо', 'Фэнтези')
        assert collector.get_books_genre() == {'Робинзон Крузо': ''}                

    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_book_genre_by_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre     

    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_books_with_specific_genre_by_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]     

    def test_get_books_with_specific_genre_by_wrong_genre(self, my_books_collection):
        assert len(my_books_collection.get_books_with_specific_genre('Фэнтези')) == 0    

    def test_get_books_for_children(self, my_books_collection):
        assert len(my_books_collection.get_books_for_children()) == 3 and my_books_collection.get_books_for_children() == ['Великий Гэтсби', 'Гарри Поттер', 'Джуманджи']  

    def test_add_book_in_favorites_not_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Великий Гэтсби')
        assert 'Великий Гэтсби' in my_books_collection.get_list_of_favorites_books() and len(my_books_collection.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Великий Гэтсби')
        my_books_collection.add_book_in_favorites('Великий Гэтсби')
        assert 'Великий Гэтсби' in my_books_collection.get_list_of_favorites_books() and len(my_books_collection.get_list_of_favorites_books()) == 1        