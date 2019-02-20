print('welcome to doublequeue')
l=[]
while True:
    print('please select the operation you want to use\n1.enque 2.deque 3.size of stack 4.emptiness 5.exit')
    a=input()
    a=int(a)
    b=len(l)
    if a==1:
        print('where do you want to enter\n 1.front 2.rear')
        c=input()
        c=int(c)
        element=input()
        if c==1:
          l.insert(0,element)
          print(l)
        elif c==2:
          l.append(element)
          print(l)
    elif a==2:
        if b==0:
            print('cannot pop element because queue is empty')
        else:
            print('where you want to remove\n 1.front 2.rear')
            d=input()
            d=int(d)
            if d==1:
               l.pop(0)
               print(l)
            elif d==2:
               l.pop()
               print(l)
    elif a==3:
        print('the size of stack is')
        print(len(l))
        print(l)
    elif a==4:
        if b==0:
            print('stack is empty')
        else:
            print('stack is not empty')
    elif a==5:
        print('You have exited the stack')
        break;
    elif a>=6:
        print('We have only five operations\nPlease choose the above options')
