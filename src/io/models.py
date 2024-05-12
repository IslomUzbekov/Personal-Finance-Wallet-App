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

    @property
    def date(self) -> datetime:
        return self._date

    @date.setter
    def date(self, value: datetime) -> None:
        self._date = value

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str) -> None:
        self._category = value

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value: float) -> None:
        self._amount = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    def __str__(self):
        return f"Дата: {self._date}, Категория: {self._category}, \
            Сумма: {self._amount}, Описание: {self._description}"
