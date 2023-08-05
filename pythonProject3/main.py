n=int(input("number:",))
for x in range(n):
    for y in range(x):
        print("*",end="")
    print()
for x in range(n):
    for z in range(x,n):
        print("*",end="")
    print()




