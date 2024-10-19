import datetime

def get_value():
    while True:
        surname = input()
        if surname!="":
            return surname
        print("Строка не может быть пустой")

def Get_Name():
    print("Введите имя студента")
    return get_value()

def Get_Surname():
    print("Введите фамилию студента")
    return get_value()

def Get_Department():
    print("Введите факультет студента")
    return get_value()

def Get_Date():
    print("Введите дату рождения студента. Формат: YYYY-MM-DD")
    while True:
        try:
            date_of_birth = input()
            date = datetime.date(int(date_of_birth[:4]), int(date_of_birth[5:7]), int(date_of_birth[8:]))
            return date_of_birth
        except Exception as e:
            print("Неправильный формат даты, попробуйте еще раз")

def Get_Command(value):
    while True:
        try:
            index = int(input())
            if index<=value and index>=0:
                return index
            print("Введенная команда не может быть выполнена (неправильный номер)")
        except Exception as e:
            print("Неправильный ввод(не целочисленное значение)")

def Print(result):
    for row in result:
        print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Факультет: {row[3]}, Дата рождения: {row[4]}")