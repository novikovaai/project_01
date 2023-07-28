# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

# Подключение базы
conn = sqlite3.connect("teatchers.db")
cursor = conn.cursor()

#Удаление таблицы, если она уже есть
cursor.execute('''
DROP TABLE IF EXISTS Students
''')
# Создание таблицы Students
cursor.execute('''
CREATE TABLE Students (
Student_Id INT, 
Student_Name VARCHAR(255),
School_Id INT PRIMARY KEY);
''')

# Наполнение таблицы данными
cursor.execute('''
INSERT INTO Students (Student_Id, Student_Name, School_Id)
    VALUES (201, 'Иван', 1),
           (202, 'Петр', 2),
           (203, 'Анастасия', 3),
           (204, 'Игорь', 4);
''')

conn.commit()

# Выборка нужных строк в кортеж
students = cursor.execute('''
SELECT Students.Student_Id AS 'ID Студента', 
Students.Student_Name AS 'Имя студента', 
Students.School_Id AS 'ID школы', 
School.School_Name AS 'Название школы' 
FROM Students 
JOIN School 
ON School.School_Id  = Students.School_Id; 
''').fetchall()

#Функция для получения нужного индекса кортежа
def get_id(num, l):
    for i in range(len(l)):
        if l[i][0] == num:
            return i


id_st = int(input('Введите ID студента... '))
iden = get_id(id_st, students)
print(f'ID Студента: {id_st}\nИмя студента: {students[iden][1]}\nID школы: {students[iden][2]}\nНазвание школы: {students[iden][3]}') if iden != None else print('ID студента не найден')