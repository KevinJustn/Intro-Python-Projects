f = open("dobA.txt","r")
g = open("dobB.txt","w")

i=0

s = f.readline()
s = s.rstrip("\n")
while s != "":
    a = s.split(" ")
    i = len(a)
    b = a[i-1].split("/")
    lstR = [b[1],b[0],b[2]]
    a[i-1] = "/".join(lstR)
    s = " ".join(a)
    g.write(s+"\n")
    s = f.readline()
    s = s.rstrip("\n")
    
f.close()
g.close()
