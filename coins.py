a = []
ans = 0
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1,7):
            for l in range(1, 7):
                s = i+j+k+l
                if s == 4 or s == 5 or s == 6:
                    ans+=1

print(ans)