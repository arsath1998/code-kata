a=int(raw_input())
b=0
for i in range(2,a//3):
    if(a%i==0):
        b=b+1
if(b<=0):
    print('yes')
else:
    print('no')
