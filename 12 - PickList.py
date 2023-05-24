# This program asks the user to enter a sequence of numbers. Let's call this sequence A. Thereafter ask the user to enter a sequence of numbers 
# B which indicates positions which are most important. We generate a sequence as follows: 
# The important numbers specified by B must be at the beginning and in the same order as they were in A.
# The remaining number from A are to be sorted in descending order.

lsta = input("Please enter A: ")
lstb = input("Please enter B: ")
lstA = lsta.split(" ")
lstB = lstb.split(" ")
lstC = []
lstD = []
lstA2 = []

def sequencer():
    for i in range(len(lstB)):
        lstC.append(int(lstA[int(lstB[i]) - 1]))
    for i in range(len(lstB)):
        lstA.remove(str(lstC[i]))
    for i in range(len(lstA)):
        lstA2.append(int(lstA[i]))
    lstA2.sort(reverse=True)
    for i in range(len(lstC)):
        lstD.append(int(lstC[i]))
    for i in range(len(lstA2)):
        lstD.append(int(lstA2[i]))
    print("The sequence you want is:",lstD)
    
sequencer()
