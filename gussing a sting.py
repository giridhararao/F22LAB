import random
import string
def goto(linenum):
    line = linenum
rand=random.choices(string.ascii_uppercase, k=6)
line=1
while True:
 if(line==1):
    print("Give a string with size 6")
    a=input()
    c=list()
    atsame=0
    notsame=0
    for i in range(0,len(a)):
        c.append(a[i])
    if(rand==c):
        print("both the Strings are same")
        print("GAME OVER")
        break
    else:
        for i in range(0,6):
         for j in range(0,6):
            if(c[i]==rand[j]):
                if(i==j):
                   atsame=atsame+1
                else:
                   notsame=notsame+1
        print("The characters that are in the same place"+str(atsame))
        print("The characters that are same but not in the same place"+str(notsame))
    goto(1)    
