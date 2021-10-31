import random
b = 0
x1 = 0
for i in range(10000):
    a = []
    n = 0
    for j in range(3):
        # a.append(random.randint(1,6))
        c = random.randint(1, 6)
        d = random.randint(1, 6)
        if c > d:
            n+=c-d
    if n > 12:
        x1+=1
    n = 0
    
    # a = []

print(x1/10000*100)