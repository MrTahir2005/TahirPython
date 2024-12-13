number=int(input("Enter a Number:"))
reverse=0
temp=number
while temp>0:
  digit=temp%10
  reverse=reverse*10+digit
  temp=temp//10
if reverse==number:
  print(f"{number} is Palindrome")
else:
  print(f"{number} is Not Palindrome")
