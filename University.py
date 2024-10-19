import sqlite3
import Courses
import Students
import Teachers
import Exams
import Grades

db_connection = sqlite3.connect("university.db")
cursor = db_connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")


def Get_Command(value):
    while True:
        try:
            index = int(input())
            if index<=value and index>0:
                return index
            print("Введенная команда не может быть выполнена (неправильный номер)")
        except Exception as e:
            print("Неправильный ввод(не целочисленное значение)")

def Sort_Department():
    print("Студентов какого факультета вывести? Введите ID этого курса")
    select_query = "SELECT * FROM Courses"
    cursor.execute(select_query)
    result = cursor.fetchall()
    if len(result)>0:
        Courses.show()
        index = int(input())
        select_query = "SELECT name, surname, date_of_birth FROM Courses INNER JOIN Students ON Courses.Title = Students.Department WHERE Courses.id=?"
        cursor.execute(select_query, (index, ))
        result = cursor.fetchall()
        for row in result:
            print(f"Имя: {row[0]}, Фамилия: {row[1]}, Дата рождения: {row[2]}")
    else:
        print("Невозможно выполнить операцию. Таблица Курсы явлется пустой")

def Teacher_Courses():
    print("Факультеты какого учителя вывести? Введите ID этого учителя")
    select_query = "SELECT * FROM Teachers"
    cursor.execute(select_query)
    result = cursor.fetchall()
    if len(result)>0:
        Teachers.show()
        index = int(input())
        select_query = "SELECT title, description FROM Courses INNER JOIN Teachers ON Courses.teacher_id = Teachers.id WHERE Teachers.id=?"
        cursor.execute(select_query, (index, ))
        result = cursor.fetchall()
        for row in result:
            print(f"Название: {row[0]}, Описание: {row[1]}")
    else:
        print("Невозможно выполнить операцию. Таблица Учителя явлется пустой")


def Grade_Courses():
    print("Оценки какого студента вывести? Введите ID этого студента")
    select_query = "SELECT * FROM Students"
    cursor.execute(select_query)
    result = cursor.fetchall()
    if len(result)>0:
        Students.show()
        index_student = int(input())
        print("Оценки какого факультета вывести? Введите название этого факультета")
        select_query = "SELECT department FROM Students WHERE id = ?"
        cursor.execute(select_query, (index_student,))
        result = cursor.fetchall()
        if len(result)>0:
            for row in result:
                print(row)
            index_course = input()
            select_query = """SELECT name, surname, title, score 
            FROM Students
            INNER JOIN Grades ON Students.id = Grades.student_id 
            INNER JOIN Courses ON Courses.Title = Students.Department
            WHERE title=? AND Students.id=?"""
            cursor.execute(select_query, (index_course, index_student))
            result = cursor.fetchall()
            for row in result:
                print(f"{row[0]} {row[1]} на факультете {row[2]} получил {row[3]}")
        else:
            print("Данного ID студента не существует")
    else:
        print("Невозможно выполнить операцию. Таблица Курсы явлется пустой")

def Average_In_Course():
    print("Оценки какого студента вы хотите увидеть? Введите ID этого студента")
    select_query = "SELECT * FROM Students"
    cursor.execute(select_query)
    result = cursor.fetchall()
    if len(result)>0:
        Students.show()
        index_student = int(input())
        print("По какому факультету рассчитать среднюю оценку? Введите ID этого факультета")
        select_query = "SELECT Courses.id, title, description, teacher_id FROM Courses INNER JOIN Students On Courses.title = Students.department WHERE Students.id = ?"
        cursor.execute(select_query, (index_student, ))
        result = cursor.fetchall()
        if len(result)>0:
            for row in result:
                print(f"ID: {row[0]}, Название: {row[1]}, Описание: {row[2]}, ID Учителя: {row[3]}")
            index_course = int(input())
            select_query = """SELECT name, surname, avg(score)
            FROM Students
            INNER JOIN Grades ON Grades.student_id = Students.id
            INNER JOIN Courses ON Courses.title = Students.department
            WHERE Students.id=? AND Courses.id = ?"""
            cursor.execute(select_query, (index_student, index_course))
            result = cursor.fetchall()
            for row in result:
                print(f"Имя: {row[0]}, Фамилия: {row[1]}, Средний балл: {row[2]}")
        else:
            print("Невозможно выполнить операцию. Данный ID курса не найден или таблица Курсы пустая")
    else:
        print("Невозможно выполнить операцию. Таблица Студенты явлется пустой")

def Average_General():
    print("Оценки какого студента вы хотите увидеть? Введите ID этого студента")
    select_query = "SELECT * FROM Students"
    cursor.execute(select_query)
    result = cursor.fetchall()
    if len(result)>0:
        Students.show()
        index_student = int(input())
        select_query = """SELECT name, surname, avg(score)
        FROM Students
        INNER JOIN Grades ON Grades.student_id = Students.id
        WHERE Students.id=?"""
        cursor.execute(select_query, (index_student, ))
        result = cursor.fetchall()
        for row in result:
            print(f"Имя: {row[0]}, Фамилия: {row[1]}, Средний балл: {row[2]}")
    else:
        print("Невозможно выполнить операцию. Таблица Студенты явлется пустой")

def Average_Department():
    print("Средний балл учеников какого факультета вы хотите посмотреть? Введите ID факультета")
    select_query = "SELECT * FROM Courses"
    cursor.execute(select_query)
    result = cursor.fetchall()
    if len(result)>0:
        Courses.show()
        index_course = int(input())
        select_query = """SELECT title, avg(score)
        FROM Courses
        INNER JOIN Exams ON Courses.id = Exams.course_id 
        INNER JOIN Grades ON Grades.exam_id = Exams.id
        WHERE Courses.id=?"""
        cursor.execute(select_query, (index_course,))
        result = cursor.fetchall()
        for row in result:
            print(f"Средний балл студентов на факультете {row[0]} равен {row[1]}")
    else:
        print("Невозможно выполнить операцию. Таблица Курсы явлется пустой")

def Drop_DB():
    cursor.execute("PRAGMA foreign_keys = OFF;")
    db_connection.commit()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_sequence';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        drop_query = f"DROP TABLE IF EXISTS {table_name};"
        cursor.execute(drop_query)
    cursor.execute("PRAGMA foreign_keys = ON;")
    db_connection.commit()
    Students.create()
    Teachers.create()
    Courses.create()
    Exams.create()
    Grades.create()

Students.create()
Teachers.create()
Courses.create()
Exams.create()
Grades.create()
while True:
    dic = {1: "Добавить", 2:"Изменить", 3:"Удалить", 4:"Студенты факультета", 5:"Курсы учителей", 6:"Оценки студента по курсу", 7:"Средний балл студента по курсу", 8:"Средний балл студента в целом", 9:"Средний балл по факультету", 10:"Показать таблицы", 11:"Удалить базу данных", 12:"Закрыть программу"}
    for i in dic.keys():
        print(f"{i} - {dic[i]}")
    command = Get_Command(len(dic))
    if command<=3:
        users = {"1": "Students", "2":"Teachers", "3":"Courses", "4":"Exams", "5":"Grades"} 
        for i in users.keys():
            print(f"{i} - {users[i]}")
        user = Get_Command(len(users))
        cursor.execute(f"SELECT * FROM {users[str(user)]}")
        result = cursor.fetchall()
        if len(result)==0 and command!=1:
            print("Невозможно выполнить операцию. Данная таблица является пустой")
        else:
            if user==1:
                if command==1:
                    Students.add()
                elif command==2:
                    Students.change()
                else:
                    Students.delete()
            elif user==2:
                if command==1:
                    Teachers.add()
                elif command==2:
                    Teachers.change()
                else:
                    Teachers.delete()
            elif user==3:
                if command==1:
                    Courses.add()
                elif command==2:
                    Courses.change()
                else:
                    Courses.delete()
            elif user==4:
                if command==1:
                    Exams.add()
            else:
                if command==1:
                    Grades.add()
    elif command == 4:
        Sort_Department()
    elif command == 5:
        Teacher_Courses()
    elif command == 6:
        Grade_Courses()
    elif command == 7:
        Average_In_Course()
    elif command == 8:
        Average_General()
    elif command ==9:
        Average_Department()
    elif command == 10:
        print("Студенты")
        Students.show()
        print("Учителя")
        Teachers.show()
        print("Курсы")
        Courses.show()
        print("Экзамены")
        Exams.show()
        print("Оценки")
        Grades.show()
    elif command == 11:
        Drop_DB()
    elif command == 12:
        break
print("Завершение работы")
db_connection.close()