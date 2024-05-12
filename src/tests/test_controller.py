import unittest
from datetime import datetime

from finance.io.controller import Controller
from finance.io.models import Record


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_add_record(self):
        record = Record(datetime.now(), 'income', 100, 'Test income')
        self.controller.add_record(record)
        self.assertEqual(len(self.controller.records), 1)

    def test_edit_record(self):
        record = Record(datetime.now(), 'expense', 50, 'Test expense')
        self.controller.add_record(record)
        new_record = Record(datetime.now(), 'income', 200, 'Updated income')
        self.controller.edit_record(0, new_record)
        self.assertEqual(self.controller.records[0].category, 'income')
        self.assertEqual(self.controller.records[0].amount, 200)


if __name__ == '__main__':
    unittest.main()
