def pal(s): 
    return s[::-1] == s 

while True: 
    s = input("введите слово: ") 
    if pal(s):
        print('True')
    else:
        print('False')