age = 20
price = 19.5

print(age, price)
print("hello")

name = input("what is your name? ")
print("Welcome "+name)

birth_year = input("Enter your birth year? ")
age = 2020 - int(birth_year)
print("Your age is "+ str(age)) 

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

sum = float(first_number) + float(second_number)
print("Sum is "+ str(sum))

x = 3 > 2
print(x)
temperature = 25

#if elif else statement
if temperature > 30:
    print("It is a hot day get water")
elif temperature > 20:
    print('It is a nice day')
else:
    print("it's cold")


#while-loop
i=0;
while i<=5:
    print(i)
    i+=1


#list
names = ["John", "Bob", "Mosh","Sam","Mary"]
print(names)
print(names[0])
#to return the lsit of an array from 0 to 3
print(names[0:3])
names.append("Robi")
names.insert(0,"Fafo")
print(len(names))
for x in names:
    print(x)

#tuples
numbers = (1, 2, 3, 4)
numbers.count(3) #returns the number of threes in the tuples