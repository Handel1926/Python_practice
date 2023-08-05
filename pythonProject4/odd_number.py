def perfect_number(w):
    n=True
    y=0
    for i in range(1,w):
        x=w%i
        if x == 0:
            y=y+i
            if y == w:
                a=n
            else:
                a= not n
    return a
b=perfect_number(28)
print(b)