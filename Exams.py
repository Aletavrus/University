import sqlite3
import Exams_Utills

db_connection = sqlite3.connect("university.db")
cursor = db_connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

def create():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Exams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATETIME NOT NULL,
        course_id INTEGER,
        max_score REAL,
        FOREIGN KEY (course_id) REFERENCES Courses(id)
    );
    """
    cursor.execute(create_table_query)
    db_connection.commit()
    print("Exams created successfully")

def show():
    select_query = "SELECT * FROM Exams"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Exams_Utills.Print(result)

def add():
    date = Exams_Utills.Get_Date()
    id = Exams_Utills.Get_Course()
    score = Exams_Utills.Get_Score()
    insert_query = "INSERT INTO Exams (date, course_id, max_score) VALUES (?, ?, ?)"
    data = (date, id, score)
    try:
        cursor.execute(insert_query, data)
        db_connection.commit()
        print("Добавлен новый экзамен")
    except sqlite3.IntegrityError as e:
        print("Указанного курса не существует")

def delete():
    print("Данные какого экзамена удалить? Напишите ID экзамена(первое число в строке)")
    select_query = "SELECT * FROM Exams"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Exams_Utills.Print(result)
    index = Exams_Utills.Get_Command(len(result))
    delete_query = "DELETE FROM Exams WHERE id = ?"
    cursor.execute(delete_query, (index, ))
    db_connection.commit()
    print("Экзамен успешно удален")