# Rotate array to right by k steps.

def rotate_array_by_right(arr, k):
    n = len(arr)
    ans_arr = [None] * n
    i = 0
    while i < k:
        ans_arr[i] = arr[n - k + i]
        i = i + 1
    
    while i < (n-k-1):
        ans_arr[n-k-1+i] = arr[i]
        i = i + 1
    return ans_arr

arr = [1,2,3,4,5,6,7]
k = 3
print(rotate_array_by_right(arr,k))
