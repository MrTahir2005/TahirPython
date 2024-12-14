def check_age(age):
  if age<18:
    raise ValueError("Age cannot be less than 18")
  return True
try:
    check_age(16)
except ValueError as e:
    print(e)
