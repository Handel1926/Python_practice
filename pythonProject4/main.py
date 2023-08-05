def odd_number(x):
    y=0
    for i in x:
        if i%2==0:
            continue
         y=y+i
    return y
b=[1,2,3,4,5,6,7,8,9]
a=odd_number(b)
print(a)