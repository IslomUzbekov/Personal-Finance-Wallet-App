import datetime
from typing import List, Optional

from .models import Record


class Controller:
    def __init__(self) -> None:
        '''Инициализация контроллера.'''
        self._records: list = []

    def add_record(self, record: Record) -> None:
        '''Добавление новой записи.

        Args:
            record (Record): Новая запись о доходе или расходе
        '''
        self._records.append(record)

    def edit_record(self, index: int, new_record: Record) -> None:
        '''Редактирование существующей записи по индексу.

        Args:
            index (int): Индекс записи для редактирования.
            new_record (Record): Новая запись для замены существующей.
        '''
        if 0 <= index < len(self._records):
            self._records[index] = new_record
        else:
            raise IndexError('Некорректный индекс записи')

    def delete_record(self, index: int):
        '''Удаление существующей записи по индексу.

        Args:
            index (int): Индекс записи для редактирования.
        '''
        if 0 <= index < len(self._records):
            del self._records[index]
        else:
            raise IndexError('Некорректный индекс записи')

    def search_records(
            self,
            category: Optional[str] = None,
            date: Optional[datetime.date] = None,
            amount: Optional[float] = None) -> List[Record]:

        '''Поиск записей по заданным критериям.

        Args:
            category (str, optional): Категория записи (Доход/Расход).
                Defaults to None.
            date (str, optional): Дата записи. Defaults to None.
            amount (float, optional): Сумма записи. Defaults to None.

        Returns:
            List[Record]: Список найденных записей.
        '''
        results = []
        for record in self._records:
            if (category is None or record.category == category) and \
               (date is None or record.date == date) and \
               (amount is None or record.amount == amount):
                results.append(record)
        return results

    def get_incomes(self) -> float:
        '''Вычисление и отображение сумму доходов

        Returns:
            incomes (float): Сумма доходов
        '''
        incomes: float = 0
        for record in self._records:
            if record.category == 'Доход':
                incomes += record.amount
        return incomes

    def get_expenses(self) -> float:
        '''Вычисление и отображение сумму расходов

        Returns:
            expenses (float): Сумма расходов
        '''
        expenses: float = 0
        for record in self._records:
            if record.category == 'Расход':
                expenses += record.amount
        return expenses

    def get_balance(self) -> float:
        '''Отображение текущего баланса.

        Returns:
            balance (float): Общая сумма
        '''
        balance: float = self.get_incomes() - self.get_expenses()
        return balance
