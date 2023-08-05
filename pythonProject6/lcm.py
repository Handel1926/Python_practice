x=[4,6]

if x[0]>x[1]:
    t= x[0]
else:
    t=x[1]
for i in x:
    for j in range(1,t):
        if j!=i:
           h=i/j
           if h==int(h):
              print(j)


