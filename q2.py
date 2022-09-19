# 2. Write a python script to create a ValueError

try:
    b=int(input("Enter an integer: "))
    if(b==str or b==float or b==complex or b==bool):
        raise ValueError()
except ValueError:
    print("b is of int type")
else:
    print(b)
finally:
    print("File closed")            
