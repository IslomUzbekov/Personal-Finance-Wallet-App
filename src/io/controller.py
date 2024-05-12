# from datetime import datetime

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

    def search_records(
            self,
            category,
            start_date,
            end_date,
            min_amount,
            max_amount):

        """Поиск записей по категории, дате и/или сумме."""
        results: list = []

        for record in self.records:
            if (category is None or record.category == category) and \
               (start_date is None or record.date >= start_date) and \
               (end_date is None or record.date <= end_date) and \
               (min_amount is None or record.amount >= min_amount) and \
               (max_amount is None or record.amount <= max_amount):
                results.append(record)

        return results

    def calculate_balance(self) -> float:
        """Вычисление текущего баланса."""
        incomes: float = 0
        expenses: float = 0

        for record in self.records:
            if record.category == 'income':
                incomes = sum(record.amount)
            elif record.category == 'expense':
                expenses = sum(record.amount)

        balance = incomes - expenses
        return balance
