# This program checks for the nearest prime number for the number entered by the user. 

n = int(input("Enter n: "))
Base = [1,2,3,5,7]
Prime = False
Prime2 = False
Prime3 = False
x = n
y = n
xz = 0
yz = 0

if n not in Base:
    if n%2==0 or n%3==0 or n%5==0 or n%7==0:
        Prime = False
    else:
        Prime = True
        
    while Prime2 == False:
        x -= 1
        if x not in Base:
            if x%2==0 or x%3==0 or x%5==0 or x%7==0:
                Prime2 = False
            else:
                Prime2 = True
        else:
            Prime2 = True
        xz += 1

    while Prime3 == False:
        y += 1
        if y not in Base:
            if y%2==0 or y%3==0 or y%5==0 or y%7==0:
                Prime3 = False
            else:
                Prime3 = True
        else:
            Prime3 = True
        yz += 1
    
if n in Base:
    Prime = True

if yz >= 2 and xz >= 2:
    print("The prime number closes to",n,"is:",n)

else:
    if xz <= yz:
        print("The prime number closes to",n,"is:",x)
    if yz < xz: 
        print("The prime number closes to",n,"is:",y)


