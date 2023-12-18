import os 
import tkinter as tk
from tkinter import filedialog


def convert_numbers():
    filename = entry_filename.get()
    convert_from = int(entry_from.get())
    convert_to = int(entry_to.get())

    with open(filename, 'r+') as file:
        text = file.read()                                  
        numbers = text.split()
    
    converted_numbers = []

    for number in numbers:

        decimal_number = int(str(number) , convert_from)
        converted_number = ''
        
        while decimal_number > 0:
            remainder = decimal_number % convert_to
            if remainder < 10:
                converted_number = str(remainder) + converted_number
            else:
                converted_number = chr(remainder + 55) + converted_number  # для представления букв в системах счисления.
            
            decimal_number = decimal_number // convert_to

        converted_numbers.append(converted_number)

    with open('converted_numbers.txt', 'w') as file:
        
        width = max( max(len(word) for word in converted_numbers) , max(len(word) for word in numbers) ) + 2

        i = 0 
        j = 0

        for number in numbers:
            i += 1 
            
            if i % 10 == 0 or len(numbers) - i == 0:
                file.write("\n")

                for converted_number in converted_numbers:
                    converted_number = converted_numbers[j]
                    j += 1

                    if  j % 10 == 0 or len(converted_numbers) - j == 0:
                        file.write("\n\n")
                        break
                    file.write(converted_number.center(width))  

            else:
                file.write(number.center(width))

    label_result.config(text='Conversion completed')

    os.startfile("converted_numbers.txt")
        
def browse_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File")
    entry_filename.delete(0, tk.END)
    entry_filename.insert(tk.END, filename)

# Создание графического интерфейса
window = tk.Tk()
window.title("Конвертер")
window.geometry("300x350")

# Создание элементов интерфейса
label_filename = tk.Label(window, text="Имя файла:", font= 20,  pady=10)
entry_filename = tk.Entry(window, width= 37,font= 20)
button_browse = tk.Button(window, text="найти", command=browse_file, font= 20)

label_from = tk.Label(window, text="Из какой системы счисления:", font= 20, pady=10)
entry_from = tk.Entry(window, width= 37,font= 20)

label_to = tk.Label(window, text="В какую систему счисления:", font= 20, pady=10)
entry_to = tk.Entry(window, width= 37,font= 20)

button_convert = tk.Button(window, text="Конвертировать", command=convert_numbers, font= 20)

label_result = tk.Label(window, text="",font= 20)

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