def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

print(calculate(multiply, 2, 3))
