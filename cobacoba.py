from functools import cache
@cache

def f(n):
    if n == 1:
        return 1
    else:
        k = int(n/2)
        o = n-k
        return f(k) + f(o) + 1
    

n = int(input())
isian = []

for i in range(n):
    isian.append(int(input()))
for i in isian:
    print(f(i))
