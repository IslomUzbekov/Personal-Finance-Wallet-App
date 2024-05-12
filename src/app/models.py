from datetime import datetime


class Record:
    def __init__(
            self,
            date: datetime,
            category: str,
            amount: float,
            description: str) -> None:

        self._date = date
        self._category = category
        self._amount = amount
        self._description = description

    # Декораторы getter для доступа к данным записи
    @property
    def date(self) -> datetime:
        return self._date

    @property
    def category(self) -> str:
        return self._category

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def description(self) -> str:
        return self._description

    # Декораторы setter для изменения данных записи
    @date.setter
    def date(self, new_date: datetime) -> None:
        self._date = new_date

    @category.setter
    def category(self, new_cat: str) -> None:
        self._category = new_cat

    @amount.setter
    def amount(self, new_amount: float) -> None:
        self._amount = new_amount

    @description.setter
    def description(self, new_desc: str) -> None:
        self._description = new_desc

    def __str__(self):
        return f'Дата: {self._date}, Категория: {self._category}, \
            Сумма: {self._amount}, Описание: {self._description}'
