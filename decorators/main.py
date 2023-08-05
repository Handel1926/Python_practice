import time

def add(n,w):

    b = n + w
    c = time.time()
    time.sleep(2)
    d = n + w
    a = time.time()
    print(b, c, d, a)
add(3,4)