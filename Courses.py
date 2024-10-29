import sqlite3
import Courses_Utills

db_connection = sqlite3.connect("university.db")
cursor = db_connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

def create():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR NOT NULL,
        description TEXT NOT NULL,
        teacher_id INTEGER, 
        FOREIGN KEY (teacher_id) REFERENCES Teachers(id) ON DELETE CASCADE
    )
    """
    cursor.execute(create_table_query)
    db_connection.commit()
    print("Courses created successfully")

def show():
    select_query = "SELECT * FROM Courses"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Courses_Utills.Print(result)

def add():
    title = Courses_Utills.Get_Title()
    description = Courses_Utills.Get_Description()
    id = Courses_Utills.Get_Teacher()
    insert_query = "INSERT INTO Courses(title, description, teacher_id) VALUES (?, ?, ?)"
    data = (title, description, id)
    try:
        cursor.execute(insert_query, data)
        db_connection.commit()
        print("Добавлен новый курс")
    except sqlite3.IntegrityError as e:
        print("Указанного учителя не существует")

def change():
    print("Данные какого курса изменить? Напишите ID курса(первое число в строке)")
    select_query = "SELECT * FROM Courses"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Courses_Utills.Print(result)
    index = Courses_Utills.Get_Command(len(result))
    print("Какой параметр вы хотите изменить? Введите соответствующие числа для изменения конкретного параметра")
    dic = {1: "Название", 2: "Описание", 3: "teacher_id"}
    dic_english = {1: "title", 2: "description", 3: "teacher_id"}
    for i in dic.keys():
        print(f"{i} - {dic[i]}")
    param = Courses_Utills.Get_Command(len(dic))
    param = dic_english[param]
    print("Введите новые данные")
    new_value = ""
    if param=="title":
        new_value = Courses_Utills.Get_Title()
    elif param=="description":
        new_value = Courses_Utills.Get_Description()
    else:
        new_value = Courses_Utills.Get_Teacher()
    data_to_update = (new_value, index)
    try:
        cursor.execute("UPDATE Courses SET (%s) = ? WHERE id = ?" % param, data_to_update)
        db_connection.commit()
        print("Параметры курса обновлены")
    except sqlite3.IntegrityError as e:
        print("Ошибка при добавлении данных")

def delete():
    print("Данные какого курса удалить? Напишите ID курса(первое число в строке)")
    select_query = "SELECT * FROM Courses"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Courses_Utills.Print(result)
    index = Courses_Utills.Get_Command(len(result))
    cursor.execute("PRAGMA foreign_keys = OFF;")
    delete_query = "DELETE FROM Courses WHERE id = ?"
    cursor.execute(delete_query, (index,))
    db_connection.commit()
    cursor.execute("PRAGMA foreign_keys = ON;")
    print("Курс успешно удален")