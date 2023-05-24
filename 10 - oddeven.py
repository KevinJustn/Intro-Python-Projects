# This program works by checking to see if a number is odd with an even amount of digits. For example, 1111 returns "valid" but 1112 returns "invalid".

num = int(input("Please enter a number: "))
lst = list(str(num))
i = 0
lstO = []
lstE = []

def oddEvenSame():
    for i in range(0,len(lst),2):
        lstO.append(int(lst[i]))

    for i in range(1,len(lst),2):
        lstE.append(int(lst[i]))

    global oddEvenSame
    if sum(lstE) == sum(lstO):
        oddEvenSame = True
    else:
        oddEvenSame = False

def main():
    oddEvenSame()
    if oddEvenSame == True:
        print("Valid")
    else:
        print("Invalid")

main()
