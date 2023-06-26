def pal(s): 
    return s[::-1] == s 
#сравниваем конец и начало строки
while True: 
    s = input("введите слово: ") 
    if pal(s):
        print('True')
    else:
        print('False')
#если слово палиндром выводим 'True',если нет- 'False'
