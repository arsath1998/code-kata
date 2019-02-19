n=int(input())
lis=[]
for i in range(n):
    lis.append(input())
vowels=['a','e','i','o','u'] 
for i in range (0,len(lis)):
    if lis[i] in vowels:
        print(lis[i])
