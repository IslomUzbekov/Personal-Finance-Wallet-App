import unittest
from datetime import date

from app.controller import Controller
from app.models import Record


class TestController(unittest.TestCase):
    def setUp(self):
        '''Настройка тестовых данных.'''
        self.controller = Controller()

    def test_add_record(self):
        '''Тест добавления записи.'''
        # Добавляем несколько записей для тестирования
        record = Record(date.today(), 'Доход',
                        100, 'Тест: доход')
        self.controller.add_record(record)
        self.assertEqual(len(self.controller._records), 1)

    def test_edit_record(self):
        '''Тест редактирования записи.'''
        record = Record(date.today(), 'Дасход',
                        50, 'Тест: расход')
        self.controller.add_record(record)
        new_record = Record(date.today(), 'Доход',
                            200, 'Обновленный доход')
        self.controller.edit_record(0, new_record)
        self.assertEqual(self.controller._records[0].category, 'Доход')
        self.assertEqual(self.controller._records[0].amount, 200)

    def test_search_record(self):
        '''Тест поиск записией.'''
        self.controller.add_record(Record(date(2024, 5, 1), 'Доход',
                                          100.0, 'Зарплата'))
        self.controller.add_record(Record(date(2024, 5, 2), 'Расход',
                                          50.0, 'Товары'))
        self.controller.add_record(Record(date(2024, 5, 3), 'Расход',
                                          30.0, 'Ресторан'))

        search_results = self.controller.search_records(category='Расход')
        self.assertEqual(len(search_results), 2)
        self.assertEqual(search_results[0].date, date(2024, 5, 2))
        self.assertEqual(search_results[1].amount, 30.0)


if __name__ == '__main__':
    unittest.main()
