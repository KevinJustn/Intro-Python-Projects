# This program takes a three digit input and splits the three numbers accordingly.

threeDigit = int(input("Enter a three digit number: "))
firsttwo = threeDigit//10
first = firsttwo//10
second=firsttwo%10
third = threeDigit%10

print("The first digit is:",first) 
print("The second digit is:",second) 
print("The third digit is:",third) 
