arr1 = [1, 16, 6, 3, 2]
arr2 = [1, 15, 16, 3, 20, 3, 5]
arr3 = [1, 4, 1, 4]
arr4 = [4, 10, 16, 6, 10, 16, 2, 15, 2, 1, 5, 2, 7, 1, 9, 3]
arr5 = [1, 15, 1, 3]
arr6 = [3, 19, 2, 16, 11, 5, 1, 2, 4, 3, 6, 3]
bigarr = arr1+arr2+arr3+arr4+arr5+arr6
n = len(bigarr)
print(n)
# a = dict()
# rev = reversed(bigarr)
# for i in rev:
#     a.append(i)
# b = []
# a[1] = 'R'
# a[16]='U'
# a[6] = 'T'
# a[3] = 'G'
# a[2] = 'E'
# a[15] = 'S'
a = []
for i in bigarr:
    if i %2 == 1:
        a.append(i)
# for i in range(n-2):
#     b.append((bigarr[i], bigarr[i+1], bigarr[i+2]))
# RUTGERS
# UG20G5R4R4410UT10UESER5E7R9GRSRGG19EU115RE4GTG
# for i in b:
#     a[i] = a.get(i, 0)+1
# c = []
# for i in a:
#     c.append(a[i])
# print("Eshaan")
# print(sorted(c))
# print(a)
# print()
# print(sorted(list(a)))
# for i in range(len(bigarr)-1):
#     b.append(bigarr[i]+bigarr[i+1])
# for i in range(0, 26):
#     b.append(chr(i+97))
# b = reversed(b)
# bt = []
# for i in b:
#     bt.append(i)
# print(bt)
# # print(rev)

for s in range(0, 26):
    for n in a:
        print(chr((n+s)%26+97), end="")
    print()

# freq = dict()

# for i in arr1+arr2+arr3+arr4+arr5+arr6:
#     print(chr(i+96), end="")
#     freq[chr(i+96)] = freq.get(chr(i+96), 0)+1
# print(freq)