from datetime import datetime
from typing import List

from .models import Record


class Controller:
    def __init__(self) -> None:
        self._records: list = []

    def add_record(self, record: Record) -> None:
        '''Добавление новой записи.'''
        self._records.append(record)

    def edit_record(self, index: int, new_record: Record) -> None:
        '''Редактирование существующей записи по индексу.'''
        if 0 <= index < len(self._records):
            self._records[index] = new_record
        else:
            raise IndexError('Некорректный индекс записи')

    def delete_record(self, index: int):
        if 0 <= index < len(self._records):
            del self._records[index]
        else:
            raise IndexError('Некорректный индекс записи')

    def search_records(
            self,
            category: str | None,
            date: datetime | None,
            amount: float | None) -> List[Record]:

        '''Поиск записей по категории, дате и/или сумме.'''
        results = []
        for record in self._records:
            if (category is None or record.category == category) and \
               (date is None or record.date == date) and \
               (amount is None or record.amount == amount):
                results.append(record)
        return results

    def get_incomes(self) -> float:
        '''Вычисление доходов'''
        incomes: float = 0
        for record in self._records:
            if record.category == 'доходы':
                incomes += record.amount
        return incomes

    def get_expenses(self) -> float:
        '''Вычисление расходов'''
        expenses: float = 0
        for record in self._records:
            if record.category == 'расходы':
                expenses += record.amount
        return expenses

    def get_balance(self) -> float:
        return self.get_incomes() - self.get_expenses()
