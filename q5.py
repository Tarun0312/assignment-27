# 5. Write a python script to handle multiple Exception in one try

a=1
try:
    b=int(input("Enter an integer: "))
    c=a/b
except ZeroDivisionError:
    print("cannot divide with zero")
except ValueError:
    print("Gadhe integer enter kr")
except Exception:
    print("Kuch toh gadbad hai")
else:
    print(c)                