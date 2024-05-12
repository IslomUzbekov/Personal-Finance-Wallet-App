import unittest
from datetime import datetime

from app.controller import Controller
from app.models import Record


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_add_record(self):
        record = Record(datetime.now(), 'доходы', 100, 'Тестирование: доходы')
        self.controller.add_record(record)
        self.assertEqual(len(self.controller._records), 1)

    def test_edit_record(self):
        record = Record(datetime.now(), 'расходы', 50, 'Тестирование: расходы')
        self.controller.add_record(record)
        new_record = Record(datetime.now(), 'доходы', 200, 'Обновленный доход')
        self.controller.edit_record(0, new_record)
        self.assertEqual(self.controller._records[0].category, 'Доходы')
        self.assertEqual(self.controller._records[0].amount, 200)


if __name__ == '__main__':
    unittest.main()
