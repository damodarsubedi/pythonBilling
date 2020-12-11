from cw import *
from sty import*
List()
a=input("Your Name please?\n")
c=input("Is the coustomer purchasing then \n \t input y for yes and n for no\n")
m=[]
q=[]
r=[]
o=[]
while c=="y":
    b=input("Please say your item to be purchased\n")
    q.append(b)
    for i in range (len(l)):
        for j in range (len(l[i])):
            if l[i][0]==b.lower():
                print("Product Price is",l[i][1])
                print("Number of Product available",l[i][2])
                check=False
                while check==False:
                    try:
                        n=int(input("Enter number of item to be purchase:"))
                        r.append(n)
                        check=True
                    except:
                        print("error")
                if ((int (l[i][2]))<=0 or (n> int (l[i][2]))) :
                            print("sorry the item is out of stock")
                            reduce_num=input("Do you want to reduce number?\t input y or yes and n for no:")
                            if reduce_num=="y":
                                l[i][0]==b.lower()
                            elif reduce_num=="n":
                                break
                elif (n==0):
                    print("Sory number of items cant be zero")
                    l[i][0]==b.lower()
                else:       
                    check=False
                    while check ==False:
                        try:
                            discount=int(input("Enter the discount you are giving in Rs.:>"))
                            if(discount>l[i][2]):
                                print("Sorry we cant provide such discounnt")
                                discount=int(input("Please reenter eligible discount"))
                            check=True
                            o.append(discount)
                        except:
                            print("error")
                    l[i][2]=int(l[i][2])-n
                    total=l[i][1]-discount
                    print("After giving Discount your total cost of total product is Rs. ",total)
                    bill=total*n
                    m.append(bill)
                    print("Your bill for current product is: ",bill)
                    c= input("Do you want to purchase more than this than y for yes and n for no:")
                    print("Your Total bill is",sum(m))
                    break
                        
if c=="n":
    print("Thank you! :) ")
    List()
f=open("a.txt","w")
for i in (l):
        i = str(i)
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        f.write(i)
        f.write("\n")
f.close()

