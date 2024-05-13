import csv
import os
from datetime import datetime
from typing import List

from .models import Record


class FileUtils:
    @staticmethod
    def read_records_from_file(file_path: str) -> List[Record]:
        '''Чтение записей из файла.

        Args:
            file_path (str): Путь к файлу с записями.

        Returns:
            List[Record]: Список объектов Record,
                представляющих собой данные из файла.
        '''
        records = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for data in reader:
                    # Преобразование строк в объекты Record
                    date = datetime.strptime(data[0], '%Y-%m-%d').date()
                    # date = data[0]
                    category = data[1]
                    amount = float(data[2])
                    description = data[3]
                    record = Record(date, category, amount, description)
                    records.append(record)
        except FileNotFoundError:
            print(f'Файл \'{file_path}\' не найден.')
        return records

    @staticmethod
    def write_records_to_file(records: List[Record], file_path: str) -> None:
        '''Запись записей в файл в формате CSV.

        Args:
            records (List[Record]): Список объектов Record для записи.
            file_path (str): Путь к файлу, в который будут записаны данные.
        '''
        try:
            # Создаем каталог, если он не существует
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for record in records:
                    writer.writerow([record.date,
                                     record.category,
                                     record.amount,
                                     record.description])
        except Exception as e:
            print(f'Возникла ошибка при записи в файл \'{file_path}\': {e}')


def log_function_call(func):
    '''Декоратор для логирования вызовов функций.'''
    def wrapper(*args, **kwargs):
        print(f'Вызов функции {func.__name__} \
              с args: {args} и kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper
