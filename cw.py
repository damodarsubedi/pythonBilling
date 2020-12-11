l=[]
file=open("a.txt","r")
lines=file.readlines()
for line in lines:
    i=(line.replace("\n","").split(','))
    a=list(i)
    l.append(a)
for i in range (len(l)):
    for j in range (1,len(l[i])):
        l[i][j]=int(l[i][j])
file.close()
def List():
    for i in range (len(l)):
        for j in range (len(l[i])):
            print(" \nProduct available :  ",l[i][0])
            print(" \tPrice of product:   ",l[i][1])
            print(" \tAvailable  quantity:  ",l[i][2])
            break;

