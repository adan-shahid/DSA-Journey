# REMOVE DUPLICATES FROM THE SORTED ARRAY. IN_PLACE.

arr = [0, 0, 1, 1, 1, 1, 2, 3, 4]
count = 1
total_count = 1
ans = 0
i = 1
while i < len(arr):
    if arr[i-1] == arr[i]:
        count += 1
        total_count += count
        if count == 2:
            i = i + 1
            count = 1
    elif arr[i-1] != arr[i]:
        i = i + 1
        total_count = total_count + count
print(total_count)