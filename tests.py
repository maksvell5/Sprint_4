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
        #тут ошибка, у класса нету метода get_books_rating
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
  
    #Проверка установки жанра книги
    @pytest.mark.parametrize(
            'book_name, ganre',
            [
                ['Гордость и предубеждение и зомби','Ужасы'],
             ['Что делать, если ваш кот хочет вас убить','Комедии']
             ]
    )
    def test_set_book_ganre(self,book_name, ganre):
        collector=BooksCollector()
        collector.add_new_book(book_name)
        

        collector.set_book_genre(book_name,ganre)
       

        assert collector.books_genre[book_name]==ganre
        


    #Проверка получение жанра книги по названию
    def test_get_book_ganre(self):
        collector=BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Комедии')

        assert collector.get_book_genre('Гордость и предубеждение и зомби')=='Ужасы'
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить')=='Комедии'


    #Проверка метода выводящего книги с определенным жанром 
    def test_get_books_specifical_ganre(self):
        collector=BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Комедии')

        assert len(collector.get_books_with_specific_genre('Ужасы')) == 1
    

    #Проверка получение словаря books_genre
    def test_check_books_ganre(self):
        collector=BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Комедии')

        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби':'Ужасы', 'Что делать, если ваш кот хочет вас убить':'Комедии'}



    #Проверка метода возвращающего книги подходящие детям
    def test_get_book_for_children(self):
        collector=BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Комедии')

        assert len(collector.get_books_for_children()) == 1


    #Проверка добавления книг в избранное
    def test_add_book_in_favorit(self):
        collector=BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Комедии')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.favorites) == 1


    #Проверка удалении книги из избраного
    def test_remove_book_in_favorit(self):
        collector=BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Комедии')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert collector.favorites == []

    
    #Проверка получения списка избранных книг
    def test_get_favorit_list(self):
        collector=BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Комедии')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) == 2
        assert collector.favorites == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']


    #Проверить что книги с возрастным рейтингом не попадают в список для детей
    def test_age_rating_check(self):
        collector=BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Смерть на Ниле','Детектив')

        assert len(collector.get_books_for_children()) == 0




    


        

        
        