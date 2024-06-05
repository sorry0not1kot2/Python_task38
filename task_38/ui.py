# ui.py
from logger import input_data, print_data
from rename_delete import update_data, delete_data

def interface():
    while True:
        print("\nДобро пожаловать в телефонный справочник!")
        print("1 - Записать новые данные")
        print("2 - Вывести существующие данные")
        print("3 - Изменить данные")
        print("4 - Удалить данные")
        print("5 - Выйти из программы")
        
        command = input("Введите номер команды: ")
        
        if command == "1":
            input_data()
        elif command == "2":
            print_data()
        elif command == "3":
            update_data()
        elif command == "4":
            delete_data()
        elif command == "5":
            print("Выход из программы...")
            break
        else:
            print("Неверная команда. Пожалуйста, попробуйте снова.")