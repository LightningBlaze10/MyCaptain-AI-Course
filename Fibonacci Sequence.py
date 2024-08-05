t1 = 0
t2 = 1
print(t1, t2, end = ", ", sep=", ")

for i in range(1,11):
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end = ", ")
