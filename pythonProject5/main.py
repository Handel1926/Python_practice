def prime_number(m):
    t=m+1
    y=0
    for i in range(1, t):
        x = m / i
        if x == int(x):
            y = y + 1
    print(y)
    return(y)
c=int(input("number:"))
b=prime_number(c)
n=True
if b == 2:
    n=n
else:
    n=not n
print(n)
