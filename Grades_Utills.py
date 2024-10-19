import datetime
import Students
import Exams

def get_value():
    while True:
        surname = input()
        if surname!="":
            return surname
        print("Строка не может быть пустой")

def Print(result):
    for row in result:
        print(f"ID: {row[0]}, student_id: {row[1]}, exam_id: {row[2]}, оценка: {row[3]}")

def Get_Score():
    print("Введите оценку студента")
    while True:
        try:
            index = float(input())
            if index>=0:
                return index
            print("Значение должно быть больше нуля")
        except Exception as e:
            print("Неправильный ввод(не целочисленное значение)")

def Get_Exam():
    print("Введите ID экзамена")
    Exams.show()
    while True:
        try:
            index = int(input())
            if index>=0:
                return index
            print("Число должно быть положительным")
        except Exception as e:
            print("Неправильный формат данных (не целочисленное значение)")

def Get_Student():
    print("Введите ID студента")
    Students.show()
    while True:
        try:
            index = int(input())
            if index>=0:
                return index
            print("Число должно быть положительным")
        except Exception as e:
            print("Неправильный формат данных (не целочисленное значение)")