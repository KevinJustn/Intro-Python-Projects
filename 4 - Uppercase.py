# This program uppercases a singular letter character inputted by the user.

letter = str(input("Please enter a character: "))

if ord(letter) >= 97 and ord(letter) <= 122:
    upper = ord(letter) - 32
    print("The uppercase is:",chr(upper))
    
elif ord(letter) >= 65 and ord(letter) <= 90: 
    print("The upper case is:",letter)

else:
    print("You didn't enter an alphabet")
