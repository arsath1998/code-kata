N=int(input())
length=[]
length=input().split()
for i in range(0,len(length)):
    length[i]=int(length[i])
print(max(length))    
