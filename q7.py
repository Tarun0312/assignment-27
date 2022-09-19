# 7. Write a python script to add a finally block for the above script

class Calculator:
    
    @staticmethod
    def add(x,y):
        try:
            z=x+y
        except TypeError:
            print("addition not possible,Unsupported operands")
        else:
            print(z)
        finally:
            print("File closed")        

    @staticmethod
    def sub(x,y):
        try:
            z=x-y
        except TypeError:
            print("subtarction not possible unsuuported operands")
        else:
            print(z)
        finally:
            print("File closed")     
    
    @staticmethod   
    def multiply(x,y):
            try:
                z=x*y
            except TypeError:
                 print("multiplication not possible unsuuported operands")
            else:
                print(z)
            finally:
                print("In final")     

    @staticmethod
    def divide(x,y):
        try:
            z=x%y
        except TypeError:
                 print("Divsion not possible unsuuported operands")
        except ZeroDivisionError:
                print("cannot divide with zero")
        except FloatingPointError:
                print("Floating point error") 
        else:
            print(z)
        finally:
            print("In final")                            

Calculator().add(eval(input("enter num1 and num2: ")),eval(input()))
Calculator().sub(eval(input("enter num1 and num2: ")),eval(input()))
Calculator().multiply(eval(input("enter num1 and num2: ")),eval(input()))
Calculator().divide(eval(input("enter num1 and num2: ")),eval(input()))


