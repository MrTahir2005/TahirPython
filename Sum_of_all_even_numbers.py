# SUM OF ALL EVEN NUMBERS
start=int(input("Enter the start of the range:"))
end=int(input("Enter the end of the range:"))
sum_even=0
for i in range(start,end+1):
  if i%2==0:
    sum_even+=i
print("The sum of even numbers from",start,"to",end,"is",sum_even)
