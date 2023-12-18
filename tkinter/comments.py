import os   # Импортируется модуль os, который предоставляет функциональность для работы с операционной системой.
import tkinter as tk # Импортируется модуль tkinter под псевдонимом tk, который используется для создания графического интерфейса.
from tkinter import filedialog # Импортируется класс filedialog из модуля tkinter, который позволяет выбирать файлы через диалоговое окно.

def convert_numbers():
# Определяется функция convert_numbers, которая будет вызываться при нажатии 
# на кнопку "Конвертировать". Функция получает значение из поля ввода имени файла
# (entry_filename) и двух полей ввода для системы счисления
# (entry_from и entry_to) и выполняет преобразование чисел.
    
    filename = entry_filename.get()
    convert_from = int(entry_from.get())
    convert_to = int(entry_to.get())


    with open(filename, 'r') as file:
    # В блоке with открывается файл с именем, полученным из поля ввода имени файла,
    # в режиме чтения ('r'). Содержимое файла читается в переменную text, 
    # а затем разбивается на числа с помощью метода split().

        text = file.read()                                  
        numbers = text.split()
    
    converted_numbers = [] # Создается пустой список converted_numbers для хранения преобразованных чисел.

    for number in numbers: # Происходит итерация по списку numbers, содержащему числа из файла.

        decimal_number = int(str(number) , convert_from) # Каждое число преобразуется в десятичное число.
        converted_number = ''
        
        while decimal_number > 0: # Пока decimal_number больше 0, выполняется следующее:
            remainder = decimal_number % convert_to # Получается остаток от деления decimal_number на основание convert_to.
            if remainder < 10: # Если остаток меньше 10, он добавляется в начало преобразованного числа converted_number.
                converted_number = str(remainder) + converted_number
            else:
                converted_number = chr(remainder + 55) + converted_number  # Иначе, остаток преобразуется в символ (A-F) с помощью функции chr() и добавляется в начало converted_number. 
            
            decimal_number = decimal_number // convert_to #Decimal_number делится на основание convert_to с округлением в меньшую сторону.
 
        converted_numbers.append(converted_number) # Преобразованное число converted_number добавляется в список converted_numbers.

    with open('converted_numbers.txt', 'w') as file: #Открывается(создаeм) файл 'converted_numbers.txt' в режиме записи, используя блок with.
        
        if convert_from == 2:
            width = 6
        else:
            width = max(len(word) for word in converted_numbers)  #Высота вывода определяется как максимальная длина слова из списка converted_numbers.

        i = 0 # переременные i,g - сщётчики
        j = 0

        for number in numbers: # По очереди каждое число из списка numbers записывается в файл file, выровненное по центру с использованием метода center().
            i += 1 
            
            if i % 15 == 0 or len(numbers) - i == 0: # проверка на 15 слово или на последнее слово
                file.write("\n")

                for converted_number in converted_numbers:  # По очереди каждое преобразованное число из списка converted_numbers записывается в файл file, выровненное по центру.
                    converted_number = converted_numbers[j] # Сохранения прогресса цикла при выходе.
                    j += 1

                    if  j % 15 == 0 or len(converted_numbers) - j == 0: # проверка на 15 слово или на последнее слово
                        file.write("\n\n")
                        break
                    file.write(converted_number.center(width + 2))  

            else:
                file.write(number.center(width + 2))

    label_result.config(text='Conversion completed') #Метка label_result обновляется текстом "Conversion completed".

    os.startfile("converted_numbers.txt") # Функция os.startfile() открывает файл "converted_numbers.txt".
        
def browse_file():
# Определяется функция browse_file, которая будет вызываться при нажатии на кнопку "найти".
# Функция открывает диалоговое окно для выбора файла и вставляет выбранный файл в поле ввода entry_filename.
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File")
    entry_filename.delete(0, tk.END)
    entry_filename.insert(tk.END, filename)

# Создание графического интерфейса
window = tk.Tk()
window.title("Конвертер")
window.geometry("350x375")

# Создание элементов интерфейса
label_filename = tk.Label(window, text="Имя файла:", font=("Arial", 15), pady=10)
entry_filename = tk.Entry(window, width= 26,font=("Arial", 15))
button_browse = tk.Button(window, text="найти", command=browse_file, font=("Arial", 15))

label_from = tk.Label(window, text="Из какой системы счисления:", font=("Arial", 15), pady=10)
entry_from = tk.Entry(window, width= 26,font=("Arial", 15))

label_to = tk.Label(window, text="В какую систему счисления:", font=("Arial", 15), pady=10)
entry_to = tk.Entry(window, width= 26,font=("Arial", 15))

button_convert = tk.Button(window, text="Конвертировать", command=convert_numbers, font=("Arial", 15))

label_result = tk.Label(window, text="",font=("Arial", 15))

# Размещение элементов на экране
label_filename.pack()
entry_filename.pack()
button_browse.pack(padx=10, pady=10)

label_from.pack()
entry_from.pack()

label_to.pack()
entry_to.pack()

button_convert.pack(padx=10, pady=10)
label_result.pack()

# Запуск основного цикла интерфейса
window.mainloop()