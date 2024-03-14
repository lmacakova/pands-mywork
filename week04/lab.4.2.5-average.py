numbers = []
number = int(input("enter number (0 to quit): "))
while number != 0:
     numbers.append(number) 
     number = int(input("enter another (0 to quit): "))
for number in numbers:
    print (number)
average = float(sum(numbers)) / len(numbers) 
print (f"The average is {average}") 