
v = [7, 4, 2, 1, 8, 3, 6, 5]

n = len(v)

for i in range(n -1):
    ok = True
    for j in range(n-1 - i):
        if v[j] > v[j +1]:
            v[j],v[j+1] = v[j +1] , v[j]
            ok = False
    if ok:
        break

print(v)