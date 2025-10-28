# REMOVE DUPLICATES FROM SORTED ARRAY

num = [0,0,1,1,1,2,2,3,3,4]
k = 1
s, e = 0, 0
while s < len(num) or e < len(num):
    if num[s] == num[e]:
        num.append(num[e])
        num.remove(num[e])
        s += 1
        e += 1
    elif num[s] != num[e]:
        k += 1
        s += 1
        e += 1

print(k, num)
