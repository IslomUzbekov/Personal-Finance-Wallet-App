from datetime import datetime
from typing import List

from .models import Record


class FileUtils:
    @staticmethod
    def read_records_from_file(file_path: str) -> List[Record]:
        """Чтение записей из файла."""
        records = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    date = datetime.strptime(data[0], '%Y-%m-%d')
                    category = data[1]
                    amount = float(data[2])
                    description = data[3]
                    records.append(Record(date, category, amount, description))
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        return records

    @staticmethod
    def write_records_to_file(records: List[Record], file_path: str):
        """Запись записей в файл."""
        with open(file_path, 'w') as file:
            for record in records:
                file.write(f"{record.date.strftime('%Y-%m-%d')},\
                           {record.category},{record.amount},\
                            {record.description}\n")


def log_function_call(func):
    """Декоратор для логирования вызовов функций."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
