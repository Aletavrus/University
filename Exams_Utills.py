import datetime
import Courses

def get_value():
    while True:
        surname = input()
        if surname!="":
            return surname
        print("Строка не может быть пустой")

def Print(result):
    for row in result:
        print(f"ID: {row[0]}, Дата: {row[1]}, Course_ID: {row[2]}, Лучшая оценка: {row[3]}")

def Get_Date():
    print("Введите дату проведения экзамена. Формат: YYYY-MM-DD")
    while True:
        try:
            date_of_birth = input()
            date = datetime.date(int(date_of_birth[:4]), int(date_of_birth[5:7]), int(date_of_birth[8:]))
            return date_of_birth
        except Exception as e:
            print("Неправильный формат даты, попробуйте еще раз")

def Get_Score():
    print("Введите лучшую оценку по данному экзамену")
    while True:
        try:
            index = float(input())
            if index>=0:
                return index
            print("Значение должно быть больше нуля")
        except Exception as e:
            print("Неправильный ввод(не целочисленное значение)")

def Get_Command(value):
    while True:
        try:
            index = int(input())
            if index<=value and index>0:
                return index
            print("Введенная команда не может быть выполнена (неправильный номер)")
        except Exception as e:
            print("Неправильный ввод(не целочисленное значение)")

def Get_Course():
    print("Введите ID факультета")
    Courses.show()
    while True:
        try:
            index = int(input())
            if index>=0:
                return index
            print("Число должно быть положительным")
        except Exception as e:
            print("Неправильный формат данных (не целочисленное значение)")