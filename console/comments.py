                                                        # Программа Convert_base переводит числа из одной системы счисления в другую . 
                                                        # Читает цифры из file.txt заносит результат в result.txt

import os                                               # импорт библеотек

def convert_base(number, to_base = 10,from_base = 8):   # number - число, from_base - из какой системы счисления (2-16), to_base - в какую систему счисления (2-16)
    
    number = int(str(number), from_base)                # перевод number в десятичную 

    digits = '0123456789abcdef'                         # digits понадобится для составления символов переведенного числа на основании остатков.
    
    if to_base > len(digits): return None               # если to_base больше длины digits то возвращает None
    result = ''                                         
    
    while number > 0:                                   # цикл работает пока что number > 0 
        result = digits[number % to_base] + result      # остаток от деления numbers на to_base мы будем использовать как индекс для получения символа в строке digits
        number //= to_base                              # number = number // to_base
    return result

def file(file_name):                                    # file_name - имя файла
    file = open(file_name, 'r+')                        # открытие файла file_name
    file_result = open("result.txt", 'w')               # создание(открытие) файла result
    text = file.read()                                  # чтение файла

    numbers = text.split()                              # массив чисел numbers

    to_base = int(input("Введите в какую систему счисления переводить: "))           # ожидание ввода to_base
    from_base = int(input("Введите из какой системы счисления переводить: "))       # ожидание ввода from_base

    for num in numbers:                                 # перебор чисел в массиве
       print(num.center(6), end = "")                   # вывод чисел в консоль 
       file_result.write(num.center(6))                 # вывод чисел в файл result.txt

    print()                                             # переход на следующую строку в консоли
    file_result.write("    \n")                         # переход на следующую строку в файле

    for num in numbers:                                 # перебор чисел в массиве
        number = convert_base(num,to_base,from_base)    # nubber = вызов функции convert_base
        print(number.center(6),end = "")                # вывод конвертированых чисел в консоль 
        file_result.write(number.center(6))             # вывод конвертированых чисел в файл result.txt

    os.startfile("result.txt")                          # запуск result.txt

    file.close()                                        # закрытие файла
    file_result.close()

file_name = input("Введите название файла: ")           # ожидание ввода file_name

file(file_name)                                         # вызов функции file

