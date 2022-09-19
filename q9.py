# 9. Write a python script to raise a ValueError.
1
try:
    a=eval(input("Enter an integer or floating point number: "))
    if(type(a)!=float):
        raise ValueError
    
except ValueError:
    print(type(a),"value error")
except Exception:
    print("kuch toh gadbad hai")    
else:
    print(a)        