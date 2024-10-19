import Teachers

def Get_Title():
    print("Введите название курса")
    while True:
        title = input()
        if title!="":
            return title
        print("Название курса не может быть пустым")

def Get_Description():
    print("Введите описание курса")
    while True:
        description = input()
        if description!="":
            return description
        print("Описание курса не может быть пустым")

def Get_Teacher():
    print("Введите ID учителя")
    Teachers.show()
    while True:
        try:
            index = int(input())
            if index>=0:
                return index
            print("Число должно быть положительным")
        except Exception as e:
            print("Неправильный формат данных (не целочисленное значение)")
        

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
        print(f"ID: {row[0]}, Название: {row[1]}, Описание: {row[2]}, ID Учителя: {row[3]}")