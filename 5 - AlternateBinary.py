# This program prints out alternating binary (1,0,1...) based on the inputed integer. 

n = int(input("Enter n: "))

i = 0

while i < n:
    if i%2 == 0:
        print("1", end=" ")
    elif i%2 == 1:
        print("0", end=" ")
    i += 1
