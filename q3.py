# 3. Write a python script to handle the ArithmeticError

a=1

    
try:
    b=int(input("Enter a number: "))
    c=a/b
except ArithmeticError:
    print("You cannot divide by zero\nAgain input values")
    b=int(input("Enter a number: "))
    c=a/b
except Exception as e:
    print(e)
    b=int(input("Enter a number: "))
    c=a/b    
finally:
    print(c)

    
        