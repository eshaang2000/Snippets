# You have a 6 faced die and you roll it repeadetly (excuse my spelling, I am using vim and there is no autocorrect installed). What is the probabilty that you roll all the even numbers atleast once before rolling an odd number. 

#Just did it empirically


import random
ans = 0
m1= 100000
for m in range(m1):
	a = [1, 2, 3, 4, 5, 6]
#print(random.choice(a))
	b = set()
	#print(m)
	while(True):
		c=random.choice(a)
		if c%2!=0:
			if 6 in b and 2 in b and 4 in b:
				ans+=1
			break
		b.add(c)
print(ans/ (m1))
