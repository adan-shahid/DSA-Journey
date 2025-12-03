# Rotate array to right by k steps.

def rotate_array_by_right(arr, k):
    n = len(arr)
    ans_arr = [None] * n
    i = 0
    while i < k:
        ans_arr[i] = arr[n - k + i]
        i = i + 1
   

    j = 0
    while j < (n-k):
        ans_arr[k + j] = arr[j]
        j = j + 1
    return ans_arr
arr = [-1,-100,3,99]
k = 2
print(rotate_array_by_right(arr,k))


# Optimized code :
arr = [1,2]
k = 7
n = len(arr)

k = k % n
arr[n-k:n], arr[0:n-k] = arr[0:n-k], arr[n-k:n]
print(arr)