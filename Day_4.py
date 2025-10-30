# REMOVE DUPLICATES FROM SORTED ARRAY

num = [0,0,1,1,1,2,2,3,3,4]
ans = 0
i = 1
count = 1
while i < (len(num)):
    if num[ans] == num[i]:
        i += 1
    else:
        ans = ans + 1
        num[ans] = num[i]
        i += 1
        count += 1
    

print(num, count)
