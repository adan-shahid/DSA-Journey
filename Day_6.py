
# MAJORITY ELEMENT IN AN ARRAY, which appers more than floor of n/2 times.

# THIS IS IMPLEMETED USING HASHMAP. TAKES O(N) SPACE. WE CAN ALSO DO IT IN O(1) SPACE.
def majorityElement(arr):
    count = {}
    res, maxCount = 0, 0

    for n in arr:
        count[n] = 1 + count.get(n, 0)
        res = n if count[n] > maxCount else res
        maxCount = max(count[n], maxCount)
    return res

arr = [3,3,4]
[print(majorityElement(arr))]