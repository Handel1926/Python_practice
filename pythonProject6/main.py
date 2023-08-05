def number(x,y):
    if x > y:
        h=x
    else:
        h=y
    u=h
    while True:
        if h%x==0 and h%y==0:
            h=h
            break
        else:
            h=h+u
    return h
n=number(5,12)A
print(n)


