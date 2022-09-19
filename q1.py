# 1. Write a python script to create a ArithmeticError

a=1
try:
    b=0
    if(b==0):
        raise ArithmeticError()
except ArithmeticError:
    print("you cannot divide by 0")    
else:
    print(a/b)