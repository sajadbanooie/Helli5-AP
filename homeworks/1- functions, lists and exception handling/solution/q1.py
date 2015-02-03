# question 1 solution

def avg(n):
    result = 0
    a = str(n)
    for ch in a:
        result += int(ch)
    return result//len(a)

#print avg(1234)
