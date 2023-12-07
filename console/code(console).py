import os                                              

def convert_base(number, to_base = 10,from_base = 8):   
    
    
    number = int(str(number), from_base)                
    digits = '0123456789abcdef'                         
    
    
    if to_base > len(digits): return None              
    result = ''                                         
    
    while number > 0:                                   
        result = digits[number % to_base] + result      
        number //= to_base                              
    return result

def file(file_name):                                    
    file = open(file_name, 'r+')                        
    file_result = open("result.txt", 'w')              
    text = file.read()                                  

    numbers = text.split()                              

    to_base = int(input("Введите в какую систему счисления переводить: "))           
    from_base = int(input("Введите из какой системы счисления переводить: "))       

    for num in numbers:                                
        print(num.center(6), end = "")                 
        file_result.write(num.center(6))                 

    print()                                             
    file_result.write("    \n")                         

    for num in numbers:                                
        number = convert_base(num,to_base,from_base)    
        print(number.center(6),end = "")                
        file_result.write(number.center(6))             

    os.startfile("result.txt")                          
    file.close()                                       
    file_result.close()

file_name = input("Введите название файла: ")                

file(file_name)