import random
a = 0
for i in range(1000000):
	b = (random.randint(1, 6), random.randint(1, 6))
	a+=max(b)

print(a/1000000)
print(161/36)
