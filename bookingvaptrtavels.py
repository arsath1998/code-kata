print("************WELCOME TO VAP TRAVELS**********")
startinglocation=("Central")
destinationlocation=["OMR","ECR","Avadi"]
distance=[35,30,25]
car=["nano","micro","mini","prime"]
stat=["confirmed","not confirmed"]
nano=5
micro=7
mini=8
prime=10
print("please select your destination\n1.OMR 2.ECR 3.Avadi")
pchoice=int(input())
print(destinationlocation[pchoice-1],"is your destination")
if pchoice==1:
    a=distance[0]
elif pchoice==2:
    a=distance[1]
else:
    a=distance[2]
print("distance of the destination is:",a,"KM")
print("********************************************")
print("please select your car type\n1.nano 2.micro 3.mini 4.prime")
cchoice=int(input())
print(car[cchoice-1],"is your selected car type")
if cchoice==1:
    b=a*nano
elif cchoice==2:
    b=a*micro
elif cchoice==3:
    b=a*mini
else:
    b=a*prime
print("amount for your travel is:",b,"Rupees")
print("**********************************************")
print("do you confirm your travel\n1.yes 2.no")
bchoice=int(input())
if bchoice==1:
    print("your booking is",stat[bchoice-1] )
else:
    print("your booking was",stat[bchoice-1],", please confim again")
print("************************************************")
print("your desination is",destinationlocation[pchoice-1])
print("total distance is",a,"KM")
print("selected car type is",car[cchoice-1])
print("amount for your travel is",b)
print("current status:",stat[bchoice-1])



