import sqlite3
import Student_Utills

db_connection = sqlite3.connect("university.db")
cursor = db_connection.cursor()

def create():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        surname VARCHAR NOT NULL,
        department VARCHAR NOT NULL,
        date_of_birth DATETIME NOT NULL
    )
    """
    cursor.execute(create_table_query)
    db_connection.commit()
    print("Students created successfully")

def show():
    select_query = "SELECT * FROM Students"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Student_Utills.Print(result)

def add():
    name = Student_Utills.Get_Name()
    surname = Student_Utills.Get_Surname()
    department = Student_Utills.Get_Department()
    date_of_birth = Student_Utills.Get_Date()

    insert_query = "INSERT INTO Students (name, surname, department, date_of_birth) VALUES (?, ?, ?, ?)"
    data = (name, surname, department, date_of_birth)
    cursor.execute(insert_query, data)
    db_connection.commit()
    print("Добавлен новый студент")


def change():
    print("Данные какого студента изменить? Напишите ID учащегося(первое число в строке)")
    select_query = "SELECT * FROM Students"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Student_Utills.Print(result)
    index = Student_Utills.Get_Command(len(result))
    print("Какой параметр вы хотите изменить? Введите соответствующие числа для изменения конкретного параметра")
    dic = {1: "Имя", 2: "Фамилия", 3: "Факультет", 4: "Дата рождения"}
    dic_english = {1: "name", 2: "surname", 3: "department", 4: "date_of_birth"}
    for i in dic.keys():
        print(f"{i} - {dic[i]}")
    param = Student_Utills.Get_Command(len(dic))
    print("Введите новые данные")
    param = dic_english[param]
    new_value = ""
    if param=="name":
        new_value = Student_Utills.Get_Name()
    elif param=="surname":
        new_value = Student_Utills.Get_Surname()
    elif param=="department":
        new_value = Student_Utills.Get_Department()
    else:
        new_value = Student_Utills.Get_Date()
    data_to_update = (new_value, index)
    cursor.execute("UPDATE Students SET (%s) = ? WHERE id = ?" % param, data_to_update)
    db_connection.commit()
    print("Параметры студента обновлены")

def delete():
    print("Данные какого студента удалить? Напишите ID учащегося(первое число в строке)")
    select_query = "SELECT * FROM Students"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Student_Utills.Print(result)
    index = Student_Utills.Get_Command(len(result))
    delete_query = "DELETE FROM Students WHERE id = ?"
    cursor.execute(delete_query, (index, ))
    db_connection.commit()
    print("Студент успешно удален")