# logger.py
from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = input("Выберите вариант формата для сохранения данных (1 или 2): ")
    if var == "1":
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == "2":
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {address}\n\n")
    else:
        print("Неверный вариант формата.")

def print_data():
    var = input("Выберите вариант формата для вывода данных (1 или 2): ")
    if var == "1":
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            print(f.read())
    elif var == "2":
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print("Неверный вариант формата.")