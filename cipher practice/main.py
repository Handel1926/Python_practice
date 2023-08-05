import random
x = "abcdef"
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
w = []
v = ""
z = []


while len(z) < len(b):
    m = random.choice(b)
    if m not in z:
        z.append(m)
    else:
        continue
z = z * 2
for i in x:
    y = z.index(i) + 3
    v += z[y]
print(v, z)



