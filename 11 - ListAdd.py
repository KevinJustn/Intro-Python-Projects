# This program intakes a list separated by spaces, then checks to see if the second input is equal to the list added together.

elist = input("Plese enter the list: ")
n = int(input("Please enter n: "))
lst = []
lst = elist.split(" ")
a = 0
b = 0


def sumup():
    for i in range(0,len(lst)):
        for j in range(1,len(lst)):
            for k in range(2,len(lst)):
                m = int(lst[i]) + int(lst[j]) + int(lst[k])
                if m == n:
                    global a
                    a = 2
                if m != n:
                    global b
                    b = 1
    if a > b:
        print("Yes")
    elif b > a:
        print("No")


sumup()
