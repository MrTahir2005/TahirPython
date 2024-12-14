class NegativeNumberError(Exception):
    pass
def check_positive(num):
    if num<0:
        raise NegativeNumberError("Number cannot be negative")
    return True
try:
    num=int(input("Enter a number: "))
    check_positive(num)
    print("The number is positive")
except NegativeNumberError as e:
    print(e)
