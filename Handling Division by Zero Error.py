try:
    num1=int(input("Enter a numerator: "))
    num2=int(input("Enter a denominator2: "))
    result=num1/num2
    print("The result is:",result)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:    
    print("Enter a valid number")
