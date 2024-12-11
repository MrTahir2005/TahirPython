SIMPLE PYTHON QUESTIONS BASED ON CONTROL FLOW AND LOOP

1.Write a program that checks if a character is a vowel or a consonant
letter=input("Enter a letter:")
if letter in 'aeiou':
  print(letter,  "is a vowel")
else:
  print(letter, "is a consonant")
  
2.Write a program to determine if a given number is divisible by 5 and 3
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 3 == 0:
    print(num, "is divisible by both 5 and 3")
else:
    print(num, "is not divisible by both 5 and 3")  
  
3.Write a program to print numbers from 1 to 10.
for i in range(1, 11):
  print(i)
  
4.Write a program to print the multiplication table of 5
number=5
for i in range(1, 11):
      product = number * i
      print(f"{number} x {i} = {product}")
  
5.Write a program to calculate the sum of the first 10 natural numbers
total_sum = 0
for i in range(1, 11):
    total_sum += i
print("The sum of the first 10 natural numbers is:", total_sum)
The sum of the first 10 natural numbers is: 55

6.Write a program to print all even numbers between 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
      
7.Write a program to print all odd numbers between 1 and 20
for i in range(1,21,2):
  print(i)

8.Write a program that stops printing numbers from 1 to 10 when it encounters the number 5
for i in range(1, 11):
     print(i)
     if i == 5:
       break
       
9.Write a program that skips printing the number 4 in a loop that goes from 1 to 5.
for i in range(1, 6):
  if i == 4:
    continue
  print(i)
  
10.Write a program to iterate through a list of fruits and print each fruit's name.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
     print(fruit)
  
11.Write a program to calculate the sum of numbers until the user enters 0
total_sum = 0
while True:
    number = int(input("Enter a number (enter 0 to stop): "))
    if number == 0:
        break
    total_sum += number
print("The sum of the numbers is:", total_sum)

12.Write a program to reverse a given number using a while loop
number = int(input("Enter a number: "))
reversed_number = 0
while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number //= 10
print("Reversed Number:", reversed_number)

13.Write a program to keep asking for a number until the user enters a negative number
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    print("You entered:", number)
print("You entered a negative number. Exiting.")

14.Write a program to count down from 10 to 1.
for i in range(10, 0, -1):
  print(i)
  
15.Write a program to print a 3x3 matrix of * symbols
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
