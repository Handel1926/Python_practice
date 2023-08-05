def prime_number(m):
    t=m+1
    y=0
    n=True
    for i in range(1,t):
        x=m/i
        if x==int(x):
            y=y+1
    if y==2:
        n=n
    else:
        n=not n
    return n
z=int(input("number: "))
d=prime_number(z)
print(d)
