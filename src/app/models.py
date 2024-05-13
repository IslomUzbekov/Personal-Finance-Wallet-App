import datetime


class Record:
    def __init__(
            self,
            date: datetime.date,
            category: str,
            amount: float,
            description: str) -> None:
        '''Инициализация объекта Record.

        Args:
            date (str): Дата записи в формате "гггг-мм-дд".
            category (str): Категория записи (Доход/Расход).
            amount (float): Сумма записи.
            description (str): Описание записи.
        '''
        self._date = date
        self._category = category
        self._amount = amount
        self._description = description

    # Декораторы getter для доступа к данным записи
    @property
    def date(self) -> datetime.date:
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
    def date(self, new_date: datetime.date) -> None:
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
        '''Представление объекта Record в виде строки.'''
        return f'Дата: {self._date}\n   Категория: {self._category}\n   Сумма: {self._amount}\n   Описание: {self._description}'
