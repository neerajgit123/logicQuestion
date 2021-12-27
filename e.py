n=int(input('enter number'))
l=[]
for i in range(n):
    x=input().strip().split()
    if x[0]=='insert':
        l.insert(int(x[1]),int(x[2]))
    elif x[0]=='print':
        print(l)
    elif x[0]=='sort':
        l.sort()
