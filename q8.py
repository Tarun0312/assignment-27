# 8. Write a python script to implement try except and else block for division

a=7
try:
    b=int(input("Enter a number: "))
    c=a/b
except ZeroDivisionError:
        print("you cannot divide with zero")
else:
    print(c)            