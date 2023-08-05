def list(k,l):
    for i in l:
        k.append(i)
    s=k[:]
    l=0
    for i in k:
        l=l+1
        p=True
    while p:
        p= False
        for index in range(0,l-1):
            if s[index]<s[index+1]:
                d=s[index]
                s[index]=s[index+1]
                s[index+1]=d
                p=True
    return s
a=[2,1,3,4]
b=[5,9,7,6]
c=list(a,b)
print(c)