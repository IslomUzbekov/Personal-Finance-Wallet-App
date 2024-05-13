from datetime import datetime

from app.controller import Controller
from app.file_utils import FileUtils
from app.models import Record


def main():
    # Создаем экземпляр контроллера
    controller = Controller()

    # Загружаем данные из файла
    file_path = '../data/records.csv'
    controller._records = FileUtils.read_records_from_file(file_path)

    print('Добро пожаловать!')

    while True:
        print('\n1. Вывод баланса')
        print('2. Добавление записи')
        print('3. Редактирование записи')
        print('4. Удалить запись')
        print('5. Поиск по записям')
        print('6. Выход')

        choice = input('\nВыберите действие: ')

        if choice == '1':
            # Вывод текущего баланса
            print(f'\nТекущий баланс: {controller.get_balance()}')
            print(f'Доходы: {controller.get_incomes()}')
            print(f'Расходы: {controller.get_expenses()}')

        elif choice == '2':
            # Добавление новой записи
            # date = str(datetime.now().date())
            date = datetime.now()
            while True:
                cat_str = input('Выберите категорию: Доход [д]/Расход [р]: ')
                if cat_str == 'д':
                    category = 'Доход'
                    break
                elif cat_str == 'р':
                    category = 'Расход'
                    break
            amount = float(input('Введите сумму: '))
            description = input('Введите описание: ')
            new_record = Record(date, category, amount, description)
            controller.add_record(new_record)
            FileUtils.write_records_to_file(controller._records, file_path)
            print('Запись успешно добавлена!')

        elif choice == '3':
            # Редактирование записи
            index = int(input('Введите индекс записи для редактирования: '))
            date_str = input('Введите дату (гггг-мм-дд) для редактирования: ')
            # date = date_str if date_str else str(datetime.now().date())
            date = datetime.strptime(date_str, '%Y-%m-%d').date() \
                if date_str else datetime.now()
            while True:
                cat_str = input('Выберите категорию: Доход [д]/Расход [р]: ')
                if cat_str == 'д':
                    category = 'Доход'
                    break
                elif cat_str == 'р':
                    category = 'Расход'
                    break
            amount = float(input('Введите сумму: '))
            description = input('Введите описание: ')
            new_record = Record(date, category, amount, description)
            controller.edit_record(index, new_record)
            FileUtils.write_records_to_file(controller._records, file_path)
            print('Запись успешно отредактирована!')

        elif choice == '4':
            # Удаление записи
            index = int(input('Введите индекс записи для удаления: '))
            controller.delete_record(index)
            FileUtils.write_records_to_file(controller._records, file_path)
            print('Запись удалена!')

        elif choice == '5':
            # Поиск записей
            cat_str = input('Выберите категорию: Доход [д]/Расход [р]: ')
            date_str = input('Введите дату (гггг-мм-дд) для поиска '
                             '(оставьте пустой для любой): ')
            amount_str = input('Введите сумму для поиска '
                               '(оставьте пустым для любого): ')

            category = 'Доход' if cat_str == 'д' else \
                'Расход' if cat_str == 'р' else None
            date = datetime.strptime(date_str, '%Y-%m-%d').date() \
                if date_str else None
            amount = float(amount_str) \
                if date_str else None
            results = controller.search_records(category, date, amount)

            if results:
                print('\nРезультаты поиска:')
                for id, record in enumerate(results):
                    print(f'{id+1}. {record}')
            else:
                print('\nНичего не найдено. \n'
                      'Пожалуйста попробуйте изменить параметры поиска.')

        elif choice == '6':
            # Сохраняем записи в файл перед выходом
            FileUtils.write_records_to_file(controller._records, file_path)
            print('Выход... \nВсего хорошего!')
            break

        else:
            print('Неверный выбор!!!\nПожалуйста, попробуйте еще раз.')


if __name__ == '__main__':
    main()
