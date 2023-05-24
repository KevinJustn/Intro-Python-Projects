# This program sorts half of the list entered. This is done by splitting the list in half as it is entered. The first half is the same as the input, 
# but the second half is sorted in ascending order.  

HalfaSort = []
HalfbSort = []
i = 0
n = int(input("Please enter number of elements in list: " ))
        
while i < n:
    if i < n/2:
        element = int(input("Enter element: "))
        HalfaSort.append(element)
        i += 1
    else:
        element = int(input("Enter element: "))
        HalfbSort.append(element)
        i += 1

HalfaSort.extend(HalfbSort)
print("You entered:", HalfaSort)

i = 0
while i < n/2:
    HalfaSort.pop()
    i += 1

HalfbSort.sort()
HalfaSort.extend(HalfbSort)
print("Sorted:",HalfaSort)
