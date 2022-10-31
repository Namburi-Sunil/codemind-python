a=int(input())
n=int(input())
for i in range(a,n+1):
    b=str(i)
    c=len(b)
    d=0
    f=i
    while i!=0:
        e=i%10
        if e==0:
         break
        else:
            if f%e!=0:
                break
            else:
                i=i//10
                d+=1
    if d==c:
        print(f,end=' ')