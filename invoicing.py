from main import *
import datetime
from random import randint
filename=str(randint(0,100000))
file=open("invoice "+filename+".txt","w")
now=datetime.datetime.now()
now=now.strftime("%d-%m-%Y  %I:%M %p ")
file.write(".*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*\t\tINVOICE\t\t.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
file.write("\n\t\t\t\tInvoice number is: "+filename)
file.write("\t\t\t\tDate of purchased  :"+now)
file.write("\n Name of Buyer: "+str(a))
for i in range(len(q)):
    file.write("\n\n Product brought :\t\t"+str(q[i]))
    file.write("\n Number of product:\t\t"+str(r[i]))
    file.write("\n given Discount:\t\t"+str(o[i]))
    file.write("\n Cost of product\t\t"+str(m[i]))
file.write("\n\n\n\t\t\t\t Total Amount: Rs."+str(sum(m)))
file.write("\n\n\n\.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*\t\tINVOICE\t\t.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
file.close()

