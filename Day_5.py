# REMOVE DUPLICATES FROM THE SORTED ARRAY. IN_PLACE.

num = [0,0,1,1,1,1,2,3,3]

i = 0
for n in num:
    if i < 2 or n > num[i-2]:
        num[i] = n
        i += 1
print(i, num)

# l, r = 0, 0
# while r < len(num):
#     count = 1
#     while r + 1 < len(num) and num[r] == num[r + 1]:
#         r += 1
#         count += 1
    
#     for i in range(min(2, count)):
#         num[l] = num[r]
#         l += 1
#     r += 1
# print(l, num)