# The introduction just performs actions to take an input from the user
def introduction():
    global l
    global m
    global n
    l = input("Please eneter a number: ")
    m = list(l)
    n = []
    for i in range(len(m)):
        n.append((m[i]))


# END OF PART 0 - - - - - - - - - - - - - - - - - - - - - - - - introduction()


# Part 1 checks to see if the inputted number is a palindrome (a number that is the same forwards and backwards)

def palindrome():
    global a1
    a1 = []
    global a2
    a2 = []
    if len(n)%2 == 0:
        a = len(n)//2
        for i in range(a):
            a1.append((n[i]))
            a2.append(n[i + a])
        fragments()
    if len(n)%2 != 0:
        a = 1 + len(n)//2
        for i in range(a):
            a1.append((n[i]))
            a2.append(n[i + a - 1])
        fragments() 

def fragments():
    global valid
    valid = False
    a2.reverse()
    a1a = "".join(a1)
    a2a = "".join(a2)
    if a1a == a2a:
        valid = True
        
# END OF PART 1 - - - - - - - - - - - - - - - - - - introduction() + palindrome()


# Part 2 checks to see if a number is a "near prime" which are divisible by 1, itself, and one other number. Ex: 49 is near prime as it is only divisible by 1, 7, and 49.

def NearPrime():
    global valid2
    p = int(l)
    valid2 = False
    q = 0
    for i in range(1,p+1):
        if p%i == 0:
            q += 1
    if q <= 4:
        valid2 = True

# END OF PART 2 - - - - - - - - - - - - - - - - - - introduction() + NearPrime()


# Part 3 checks several things: 
# Up numbers are numbers that increase or stay the same as we read them (123, 1223, 157 is an up number)
# Down numbers are numbers that decrease or stay the same as we read them (321, 221, 951 is an down number)
# An up-down number is a number that initially increases but then decreases as we read it. (12351, 156742 is a down number)
# A nice number is a number that is any of the above three categories.

def upnum():
    global up
    u = 1
    up = False
    for i in range(len(n)-1):
        if n[i] <= n[i+1]:
            u += 1
    if u == len(n):
        up = True

def downnum():
    global down
    u = 1
    down = False
    for i in range(len(n)-1):
        if n[i] >= n[i+1]:
            u += 1
    if u == len(n):
        down = True

def updown():
    global ud
    u = 1
    i = 0
    ud = False
    while i+1 <= len(n)-1 and n[i] <= n[i+1]:
        u += 1
        i += 1
    while i+1 <= len(n)-1 and n[i] >= n[i+1]:
        u += 1
        i += 1
    if i+1 <= len(n)-1 and n[i] < n[i+1]:
        u -= 10
        i += 1
    if u == len(n):
        ud = True
    else:
        ud = False

def nice():
    global valid3
    valid3 = False
    upnum()
    downnum()
    updown()
    if up == True or down == True or ud == True:
        valid3 = True
    
# END OF PART 3 - - - - - - - - - - - - - - - - - - introduction() + nice()


# Part 4 ranks the score of an inputted number
# Palindrome inputs are doubled.
# Near prime inputs are doubled. If it has been doubled already, double it again.
# Nice numbers are tripled. If it has been doubled before (once or twice), triple it. 

def score():
    global l
    global m
    global n
    j = input("Please enter a list of numbers (separated by spaces): ")
    t = j.split(" ")
    s = []
    o = []
    for i in range(len(t)):
        l = t[i]
        m = list(l)
        n = []
        p = int(l)
        for i in range(len(m)):
            n.append(m[i])
        palindrome()
        NearPrime()
        nice()
        score2 = p
        if valid == True:
            score2 = 2 * score2
        if valid2 == True:
            score2 = 2 * score2
        if valid3 == True:
            score2 = 3 * score2
        s.append(score2)
        o.append(p)
    zipped = zip(s,o)
    sort = sorted(zipped)
    print("The order of inputted number scores (score, input) is:",sort)
        

# END OF PART 4 - - - - - - - - - - - - - - - - - - - - - - - - score()

# Use for Parts 0 through 3

# The Function calls for all parts: 

introduction()
palindrome()
print("Palindrome:",valid)
NearPrime()
print("Near Prime:",valid2)
nice()
print("Nice:",valid3)

# Use for Part 4

score()

