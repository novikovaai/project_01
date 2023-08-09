class matrix:
    def __init__(self, row=1, col=1, value=None): #По умолчанию в матрице 1 столбец, 1 колонка и значение None
        if (isinstance(value, int) or value == None) and 0 < col < 100 and 0 < row < 100: #Принимается либо целое число, либо None, размер до 99 включительно
            self.matrix = [[value]*col for _ in range(row)]
            self.col = col
            self.row = row
        else:
            raise ValueError('Введенные данные некорректны')
    def set_value(self, value, row=0, col=0): #Изменение любой ячейки матрицы с заданием ее местоположения, по умолчанию - первой
        if (isinstance(value, int) or value == None) and col <= self.col and row <= self.row: #Проверка, что значение подходит и не выходит за границы индексов
            self.matrix[row][col] = value
        elif not isinstance(value, int) and value != None:
            raise ValueError('Введенные данные некорректны, value должно быть целым числом или None')
        elif col > self.col or row > self.row:
            raise ValueError('Неправильный индекс, размер матрицы меньше введенных значений')
        else:
            raise ValueError('Произошла ошибка при выполнении запроса')
    def set_row(self, spisok, row=0): #Изменение или добавление строчки в виде списка, по умолчанию изменяется первая
        if isinstance(spisok, list) and all(map(lambda x : type(x) == int or x == None, spisok)) and isinstance(row, int): #Проверка правильности данных
            if len(spisok) < self.col: #Если длина списка меньше, чем длина других строчек (количество колонок)
                diff = self.col - len(spisok)
                spisok_add = spisok[:] + [None]*diff #К списку добавляются None в недостающем количестве
            elif len(spisok) > self.col: #Если длина списка больше, чем длина других строчек (количество колонок)
                diff = len(spisok) - self.col
                spisok_add = spisok[0:len(spisok)-diff] #Список обрезается до необходимой длины
            else:
                spisok_add = spisok[:] #Копия списка во избежание случайного изменения
            if row <= self.row: #Если строчка в матрице есть
                self.matrix[row] = spisok_add #Строчка меняется на новую
            else: #Если строчки в матрице нет (любое значение больше, чем имеется)
                self.matrix.append(spisok_add) #Строчка добавляется в конец
                self.row += 1 #Увеличивается количество имеющихся строчек
        elif not isinstance(spisok, list):
            raise ValueError('Введенные данные некорректны, требуется объект класса list')
        elif not isinstance(row, int):
            raise ValueError('Введенные данные некорректны, row должен быть целым числом')
        elif not all(map(lambda x : type(x) == int or x == None, spisok)):
            raise ValueError('Все объекты в списке должны быть целыми числами либо None')
        else:
            raise ValueError('Произошла ошибка при выполнении запроса')
    def set_col(self, spisok, col=0): #Изменение или добавление колонки в виде списка, по умолчанию изменяется первая
        if isinstance(spisok, list) and all(map(lambda x : type(x) == int or x == None, spisok)) and isinstance(col, int): #Проверка правильности данных
            if len(spisok) < self.row: #Если длина списка меньше, чем длина других колонок (количество строчек)
                diff = self.row - len(spisok)
                spisok_add = spisok[:] + [None]*diff #К списку добавляются None в недостающем количестве
            elif len(spisok) > self.row: #Если длина списка больше, чем длина других колонок (количество строчек)
                diff = len(spisok) - self.row
                spisok_add = spisok[0:len(spisok)-diff] #Список обрезается до необходимой длины
            else:
                spisok_add = spisok[:] #Копия списка во избежание случайного изменения
            if col <= self.col: #Если колонка в матрице есть
                for i in range(self.row): #Колонка меняется на новую
                    self.matrix[i][col] = spisok_add[i]
            else: #Если колонки в матрице нет (любое значение больше, чем имеется)
                for i in range(self.row):
                    self.matrix[i].append(spisok_add[i]) #Колонка добавляется в конец
                self.col += 1 #Увеличивается количество имеющихся колонок
        elif not isinstance(spisok, list):
            raise ValueError('Введенные данные некорректны, требуется объект класса list')
        elif not isinstance(col, int):
            raise ValueError('Введенные данные некорректны, row должен быть целым числом')
        elif not all(map(lambda x : type(x) == int or x == None, spisok)):
            raise ValueError('Все объекты в списке должны быть целыми числами либо None')
        else:
            raise ValueError('Произошла ошибка при выполнении запроса')
    def print_matrix(self): #Вывод матрицы
        for i in range(self.row):
            for j in range(self.col):
                print(str(self.matrix[i][j]).center(4), end='') #На каждую ячейку по 4 символа, чтобы None отображалось красиво
            print()
    def stats(self):
        print(f'Число столбцов: {self.col}, число строк: {self.row}') #Вывод размерности матрицы

#Проверяем
print('Матрица 7x7 заполненная нулями')
matrix1 = matrix(7, 7, 0)
matrix1.print_matrix()
print()
print('Изменение ячейки')
matrix1.set_value(6, row=5, col=4)
matrix1.print_matrix()
print()
print('Вывод размера матрицы')
matrix1.stats()
print()
print('Изменение слишком короткой строчки')
matrix1.set_row([7, 4], 3)
matrix1.print_matrix()
print()
print('Изменение слишком длинной строчки')
matrix1.set_row([7, 4, 9, 8, 11, 23, 4, 9, 0], 3)
matrix1.print_matrix()
print()
print('Добавление строчки')
matrix1.set_row([7, 4, 9, 8, 11, 23, 4], 50)
matrix1.print_matrix()
print()
print('Изменение слишком короткой колонки')
matrix1.set_col([11, 12], 3)
matrix1.print_matrix()
print()
print('Изменение слишком длинной колонки')
matrix1.set_col([71, 41, 91, 81, 111, 213, 14, 91, 1], 3)
matrix1.print_matrix()
print()
print('Добавление колонки')
matrix1.set_col([71, 42, 39, 48, 111, 234, 44], 50)
matrix1.print_matrix()
print()
print('Вывод нового размера матрицы')
matrix1.stats()
print()