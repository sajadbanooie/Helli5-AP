# question 5 solution

def add_list(a, b):
    c = a[:]
    for i in range(len(a)):
        c[i] = a[i] + b[i]
    return c

x = [1, 2, 3]
y = [4, 5, 6]
z = add_list(x, y)

print z
