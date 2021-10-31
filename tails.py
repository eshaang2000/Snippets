import random
ans = 0
for i in range(10000):
    a = []
    for i in range(10):
        a.append(random.randint(1, 2))

    for i in range(1, len(a)):
        if a[i-1]==1 and a[i] == 1:
            ans+=1
            break
print(ans)
