# rename_delete.py
def read_data(file_path, delimiter):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
    if delimiter == 'n':
        records = [record.split(delimiter) for record in content.split('nn') if record]
    else:
        records = [record.split('; ') for record in content.split('n') if record]
    return records

def write_data(file_path, records, delimiter):
    with open(file_path, 'w', encoding='utf-8') as file:
        for record in records:
            if delimiter == 'n':
                file.write(delimiter.join(record).strip() + 'nn')
            else:
                file.write('; '.join(record).strip() + 'n')

def find_record(records, search_query):
    return [record for record in records if search_query.lower() in record[0].lower() or search_query.lower() in record[1].lower()]

def display_records(records):
    for index, record in enumerate(records):
        print(f"{index + 1}. {'; '.join(record)}")

def update_data():
    file_choice = input("В каком файле вы хотите изменить данные? (1 - первый вариант, 2 - второй вариант): ")
    delimiter = 'n' if file_choice == '1' else '; '
    file_path = 'data_first_variant.csv' if file_choice == '1' else 'data_second_variant.csv'

    search_query = input('Введите имя или фамилию для поиска: ')
    records = read_data(file_path, delimiter)
    matching_records = find_record(records, search_query)

    if matching_records:
        display_records(matching_records)
        record_number = int(input('Введите номер записи для изменения: ')) - 1
        if 0 <= record_number < len(matching_records):
            new_name = input('Введите новое имя: ')
            new_surname = input('Введите новую фамилию: ')
            new_phone = input('Введите новый телефон: ')
            new_address = input('Введите новый адрес: ')

            matching_records[record_number] = [new_name, new_surname, new_phone, new_address]
            write_data(file_path, records, delimiter)
            print('Данные успешно обновлены.')
        else:
            print('Неверный номер записи.')
    else:
        print('Запись не найдена.')

def delete_data():
    file_choice = input("Из какого файла вы хотите удалить данные? (1 - первый вариант, 2 - второй вариант): ")
    delimiter = 'n' if file_choice == '1' else '; '
    file_path = 'data_first_variant.csv' if file_choice == '1' else 'data_second_variant.csv'

    search_query = input('Введите имя или фамилию для поиска: ')
    records = read_data(file_path, delimiter)
    matching_records = find_record(records, search_query)

    if matching_records:
        display_records(matching_records)
        record_number = int(input('Введите номер записи для удаления: ')) - 1
        if 0 <= record_number < len(matching_records):
            records = [record for i, record in enumerate(records) if i != record_number]
            write_data(file_path, records, delimiter)
            print('Запись удалена.')
        else:
            print('Неверный номер записи.')
    else:
        print('Запись не найдена.')