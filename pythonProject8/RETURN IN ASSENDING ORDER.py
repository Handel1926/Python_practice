def list(k):
    s=k[:]
    l=0
    for i in k:
        l=l+1
        p=True
    while p:
        p= False
        for index in range(0,l-1):
            if s[index]>s[index+1]:
                d=s[index]
                s[index]=s[index+1]
                s[index+1]=d
                p=True
    return s

b=[5,9,7,6]
c=list(b)
print(c)