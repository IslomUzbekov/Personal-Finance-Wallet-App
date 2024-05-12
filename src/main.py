from datetime import datetime

from src.io.controller import Controller
from src.io.file_utils import FileUtils
from src.io.models import Record


def main():
    # Создаем экземпляр контроллера
    controller = Controller()

    # Загружаем данные из файла
    file_path = 'data/transactions.txt'
    controller.records = FileUtils.read_records_from_file(file_path)

    while True:
        print('\nДобро пожаловать!')
        print('1. Вывод баланса')
        print('2. Добавление записи')
        print('3. Редактирование записи')
        print('4. Поиск по записям')
        print('5. Выход')

        choice = input('Выберите действие: ')

        if choice == '1':
            # Вывод текущего баланса
            balance = controller.calculate_balance()
            print(f'\nТекущий баланс: {balance}')

        elif choice == '2':
            # Добавление новой записи
            date = datetime.now()
            category_id = input('Выберите категорию\
                                \n\t1. Доходы\n\t2. Расходы\n: ')
            if category_id == '1':
                category = 'income'
            else:
                category = 'expense'
            amount = float(input('Введите сумму: '))
            description = input('Введите описание: ')
            new_record = Record(date, category, amount, description)
            controller.add_record(new_record)
            print('Запись успешно добавлена!')

        elif choice == '3':
            # Редактирование записи
            index = int(input('Введите индекс записи для редактирования: '))
            date = datetime.now()
            category_id = input('Выберите категорию\
                                \n\t1. Доходы\n\t2. Расходы\n: ')
            if category_id == '1':
                category = 'income'
            else:
                category = 'expense'
            amount = float(input('Введите сумму: '))
            description = input('Введите описание: ')
            new_record = Record(date, category, amount, description)
            controller.edit_record(index, new_record)
            print('Запись успешно отредактирована!')

        elif choice == '4':
            # Поиск записей
            category_id = input('Введите категорию для поиска\
                             \n\t1. Доходы\n\t2. Расходы\n: ')
            if category_id == '1':
                category = 'income'
            else:
                category = 'expense'
            date_str = input('Введите дату (ГГГГ-ММ-ДД) для \
                             поиска (оставьте пустой для любой): ')
            amount_str = input('Введите сумму для поиска \
                               (оставьте пустым для любого): ')
            # start_date_str = input('Введите начальную дату (ГГГГ-ММ-ДД) для \
            #     поиска (оставьте пустой для любой): ')
            # end_date_str = input('Введите конечную  дату (ГГГГ-ММ-ДД) для \
            #     поиска (оставьте пустой для любой): ')
            # min_amount_str = input('Введите минимальную сумму для поиска \
            #     (оставьте пустым для любого): ')
            # max_amount_str = input('Введите максимальную сумму для поиска \
            #     (оставьте пустым для любого): ')

            date = datetime.strptime(date_str, '%Y-%m-%d')
            amount = float(amount_str)

            # start_date = datetime.strptime(start_date_str, '%Y-%m-%d')\
            #     if start_date_str else None
            # end_date = datetime.strptime(end_date_str, '%Y-%m-%d')\
            #     if end_date_str else None
            # min_amount = float(min_amount_str)\
            #     if min_amount_str else None
            # max_amount = float(max_amount_str)\
            #     if max_amount_str else None
            results = controller.search_records(category, date, amount)
            print('\nРезультаты поиска:')

            for idx, record in enumerate(results):
                print(f'{idx+1}. {record}')

        elif choice == '5':
            # Сохраняем записи в файл перед выходом
            FileUtils.write_records_to_file(controller.records, file_path)
            print('Выход... Всего хорошего!')
            break

        else:
            print('Неверный выбор!!!\nПожалуйста, попробуйте еще раз.')


if __name__ == '__main__':
    main()
