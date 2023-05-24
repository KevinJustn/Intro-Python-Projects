# This program takes name and grade input from the user, and outputs the second lowest score from the inputs.

n = int(input("Enter number of students: "))

lowscore1 = 101
lowscore2 = 101
lowname1 = "Example"
i = 1

while i <= n:
    print("Please enter student",i, "name: ")
    name = str(input())
    print("Please enter student",i,"score:")
    x = int(input())

    
    if x < lowscore1:
        lowscore2 = lowscore1
        lowname2 = lowname1
        lowscore1 = x
        lowname1 = name
    elif x < lowscore2:
        lowscore2 = x
        lowname2 = name
        
    i += 1

print("The 2nd lowest student is:",lowname2,"with score:",lowscore2)

"""
print("Lowest score student:",lowname1)
print("Lowest score:",lowscore1)
print("2nd Lowest score student:",lowname2)
print("2nd Lowest score:", lowscore2)
"""
