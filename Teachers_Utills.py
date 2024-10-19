def get_value():
    while True:
        surname = input()
        if surname!="":
            return surname
        print("Строка не может быть пустой")

def Get_Name():
    print("Введите имя учителя")
    return get_value()

def Get_Surname():
    print("Введите фамилию учителя")
    return get_value()

def Get_Department():
    print("Введите курс, который ведет учитель")
    return get_value()

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
        print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Факультет: {row[3]}")