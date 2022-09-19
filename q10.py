# 10. Write a python script to implemented a nested Try Except block

from tkinter import E


a=7
try:
    b=int(input("Enter a number: "))
    c=a/b
    try:
        e=eval(input("Enter: "))
        d=c+e 
    except TypeError:
            print("Unsupported operand")
    else:
        print(d)         
except ZeroDivisionError:
    print("cannot divide with zero")
else:
    print(c)    
            


