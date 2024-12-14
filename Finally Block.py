try:
  num=int(input("Enter a number: "))
  print(10/num)
except ZeroDivisionError:
  print("You can't divide by zero")
  print("Enter a valid number")
except ValueError:
  print("Invalid input")
finally:
  print("code executed")
