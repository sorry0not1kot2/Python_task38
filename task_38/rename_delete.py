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

def display_records(records):
    for index, record in enumerate(records):
        print(f"{index + 1}. {'; '.join(record)}")

def update_data():
    file_choice = input("В каком файле вы хотите изменить данные? (1 - первый вариант, 2 - второй вариант): ")
    delimiter = 'n' if file_choice == '1' else '; '
    file_path = 'data_first_variant.csv' if file_choice == '1' else 'data_second_variant.csv'

    records = read_data(file_path, delimiter)
    display_records(records)

    try:
        record_number = int(input('Введите номер записи для изменения: ')) - 1
        if 0 <= record_number < len(records):
            new_name = input('Введите новое имя: ')
            new_surname = input('Введите новую фамилию: ')
            new_phone = input('Введите новый телефон: ')
            new_address = input('Введите новый адрес: ')

            records[record_number] = [new_name, new_surname, new_phone, new_address]
            write_data(file_path, records, delimiter)
            print('Данные успешно обновлены.')
        else:
            raise IndexError
    except ValueError:
        print("Пожалуйста, введите корректный номер.")
    except IndexError:
        print("Несуществующий номер записи.")

def delete_data():
    file_choice = input("Из какого файла вы хотите удалить данные? (1 - первый вариант, 2 - второй вариант): ")
    delimiter = 'n' if file_choice == '1' else '; '
    file_path = 'data_first_variant.csv' if file_choice == '1' else 'data_second_variant.csv'

    records = read_data(file_path, delimiter)
    display_records(records)

    try:
        record_number = int(input('Введите номер записи для удаления: ')) - 1
        if 0 <= record_number < len(records):
            del records[record_number]
            write_data(file_path, records, delimiter)
            print('Запись удалена.')
        else:
            raise IndexError
    except ValueError:
        print("Пожалуйста, введите корректный номер.")
    except IndexError:
        print("Несуществующий номер записи.")