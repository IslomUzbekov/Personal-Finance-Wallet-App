import unittest
from datetime import datetime

from app.file_utils import FileUtils
from app.models import Record


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.file_path = 'data/records_test.txt'

    def test_read_records_from_file(self):
        expected_records = [
            Record(datetime(2024, 5, 12), 'доходы', 1000, 'Зарплата'),
            Record(datetime(2024, 5, 11), 'расходы', 50, 'Товары')
        ]
        records = FileUtils.read_records_from_file(self.file_path)
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0].date, expected_records[0].date)
        self.assertEqual(
            records[1].description,
            expected_records[1].description
            )

    def test_write_records_to_file(self):
        records = [
            Record(datetime(2024, 5, 12), 'доходы', 1000, 'Зарплата'),
            Record(datetime(2024, 5, 11), 'расходы', 50, 'Товары')
        ]
        FileUtils.write_records_to_file(records, self.file_path)
        read_records = FileUtils.read_records_from_file(self.file_path)
        self.assertEqual(len(read_records), 2)
        self.assertEqual(read_records[0].description, records[0].description)


if __name__ == '__main__':
    unittest.main()
