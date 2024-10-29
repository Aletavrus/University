import sqlite3
import Teachers_Utills

db_connection = sqlite3.connect("university.db")
cursor = db_connection.cursor()

def create():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Teachers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        surname VARCHAR NOT NULL,
        department VARCHAR NOT NULL
    )
    """
    cursor.execute(create_table_query)
    db_connection.commit()
    print("Teachers created successfully")

def show():
    select_query = "SELECT * FROM Teachers"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Teachers_Utills.Print(result)

def add():
    name = Teachers_Utills.Get_Name()
    surname = Teachers_Utills.Get_Surname()
    department = Teachers_Utills.Get_Department()

    insert_query = "INSERT INTO Teachers(name, surname, department) VALUES (?, ?, ?)"
    data = (name, surname, department)
    cursor.execute(insert_query, data)
    db_connection.commit()
    print("Добавлен новый учитель")

def change():
    print("Данные какого учителя изменить? Напишите ID учителя(первое число в строке)")
    select_query = "SELECT * FROM Teachers"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Teachers_Utills.Print(result)
    index = Teachers_Utills.Get_Command(len(result))
    print("Какой параметр вы хотите изменить? Введите соответствующие числа для изменения конкретного параметра")
    dic = {1: "Имя", 2: "Фамилия", 3: "Факультет"}
    dic_english = {1: "name", 2: "surname", 3: "department"}
    for i in dic.keys():
        print(f"{i} - {dic[i]}")
    param = Teachers_Utills.Get_Command(len(dic))
    print("Введите новые данные")
    param = dic_english[param]
    new_value = ""
    if param=="name":
        new_value = Teachers_Utills.Get_Name()
    elif param=="surname":
        new_value = Teachers_Utills.Get_Surname()
    elif param=="department":
        new_value = Teachers_Utills.Get_Department()
    data_to_update = (new_value, (index, ))
    cursor.execute("UPDATE Teachers SET (%s) = ? WHERE id = ?" % param, data_to_update)
    db_connection.commit()
    print("Параметры учителя обновлены")

def delete():
    print("Данные какого учителя удалить? Напишите ID учителя(первое число в строке)")
    select_query = "SELECT * FROM Teachers"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Teachers_Utills.Print(result)
    index = Teachers_Utills.Get_Command(len(result))
    delete_query = "DELETE FROM Teachers WHERE id = ?"
    cursor.execute(delete_query, (index, ))
    db_connection.commit()
    print("Учитель успешно удален")