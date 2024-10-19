import sqlite3
import Grades_Utills

db_connection = sqlite3.connect("university.db")
cursor = db_connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

def create():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        exam_id INTEGER,
        score REAL,
        FOREIGN KEY (exam_id) REFERENCES Exams(id),
        FOREIGN KEY (student_id) REFERENCES Students(id)
    );
    """
    cursor.execute(create_table_query)
    db_connection.commit()
    print("Grades created successfully")

def show():
    select_query = "SELECT * FROM Grades"
    cursor.execute(select_query)
    result = cursor.fetchall()
    Grades_Utills.Print(result)

def add():
    student = Grades_Utills.Get_Student()
    exam = Grades_Utills.Get_Exam()
    score = Grades_Utills.Get_Score()
    insert_query = "INSERT INTO Grades (student_id, exam_id, score) VALUES (?, ?, ?)"
    data = (student, exam, score)
    try:
        cursor.execute(insert_query, data)
        db_connection.commit()
        print("Добавлена новая оценка")
    except sqlite3.IntegrityError as e:
        print("Указанного студента или экзамена не существует")