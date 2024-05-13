
# Учет личных доходов и расходов

Это консольное приложение, которое помогает пользователям отслеживать и управлять своими финансами путем записи доходов и расходов.

## Основные возможности

1. **Вывод баланса**: Показывает текущий баланс пользователя, разделяя доходы и расходы для удобства анализа.

2. **Добавление записи**: Позволяет пользователю добавлять новые записи о доходах или расходах. Каждая запись содержит дату, категорию (доход/расход), сумму и описание.

3. **Редактирование записи**: Дает возможность изменять существующие записи о доходах и расходах. Пользователь может обновлять дату, категорию, сумму и описание.

4. **Удаление записи**: Дает возможность удалять существующие записи о доходах и расходах.

5. **Поиск по записям**: Позволяет пользователю осуществлять поиск записей по категории, дате или сумме. Пользователь может найти все записи, удовлетворяющие заданным критериям.

## Требования к программе

- Программа структурирована на основе принципов ООП.
- Данные хранятся в текстовом файле в формате CSV.
- Реализация осуществляется через консольный интерфейс (CLI).
- Программа должна содержать тесты для проверки корректности работы основных функций.
- Весь код должен быть аннотирован для облегчения чтения и понимания.

## Как использовать

1. Установите Python (если не установлен).
2. Скачайте репозиторий с приложением.
3. Запустите программу из командной строки.
4. Следуйте инструкциям по добавлению, редактированию и поиску записей о доходах и расходах.

## Пример использования

```bash
$ python main.py
Выберите действие:
1. Вывод баланса
2. Добавление записи
3. Редактирование записи
4. Поиск записей
5. Выход
Выберите номер действия: 2

Введите дату (ГГГГ-ММ-ДД): 2024-05-15
Выберите категорию (доход/расход): расход
Введите сумму: 50.00
Введите описание: Покупка продуктов
Запись успешно добавлена.

Выберите действие:
1. Вывод баланса
2. Добавление записи
3. Редактирование записи
4. Поиск записей
5. Выход
Выберите номер действия: 1

Текущий баланс:
- Расходы: 50.00
- Доходы: 0.00
- Баланс: -50.00
```

## Зависимости

Это приложение использует следующие библиотеки Python:

- `datetime`: для работы с датами и временем.
- `csv`: для работы с данными в соответствующем формате.
