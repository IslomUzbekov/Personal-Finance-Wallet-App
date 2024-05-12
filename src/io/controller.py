from datetime import datetime

from .models import Record


class Controller:
    def __init__(self) -> None:
        self.records: list = []

    def add_record(self, record: Record) -> None:
        """Добавление новой записи."""
        self.records.append(record)

    def edit_record(self, index: int, new_record: Record) -> None:
        """Редактирование существующей записи по индексу."""
        if 0 <= index < len(self.records):
            self.records[index] = new_record
        else:
            raise IndexError("Invalid index")

    def search_records(self, category: str, date: datetime, amount: float):
        """Поиск записей по категории, дате и/или сумме."""
        results: list = []

        for r in self.records:
            if (category is None or r.category == category) and \
               (date is None or r.date == date) and \
               (amount is None or r.amount == amount):
                results.append(r)

        return results

    def calculate_balance(self) -> float:
        """Вычисление текущего баланса."""
        incomes: float = 0
        expenses: float = 0

        for r in self.records:
            if r.category == 'income':
                incomes = sum(r.amount)
            elif r.category == 'expense':
                expenses = sum(r.amount)

        balance = incomes - expenses
        return balance
