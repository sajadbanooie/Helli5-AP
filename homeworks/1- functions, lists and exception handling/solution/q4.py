# question 4 solution

from q3 import compare

a = []
print "Enter 10 numbers"
for i in range(10):
    a.append(input())

for i in range(len(a)):
    for j in range(len(a)-1):
        if compare(a[j], a[j+1])==1:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t

print a


