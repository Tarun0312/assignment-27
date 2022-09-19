# 4. Write a python script to handle a ValueError

try:
    a=float(input("Enter a floating point number: "))
except ValueError:
    print("Only floating point,integer are allowed")
else:
    print(a)        
