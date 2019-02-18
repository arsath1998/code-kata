low,upp=raw_input().split()
low=int(low)
upp=int(upp)
for n in range(low+1,upp):
    if n>1:
        for i in range(2,n):
         if(n%i==0):
          break
        else:
         print(n),
        
