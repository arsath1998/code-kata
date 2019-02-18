w=int(raw_input())
x=0
y=w
while w!=0:
    z=w%10
    x=x*10+z
    w=w/10
if x==y:
    print('yes')
else:
    print('no')
