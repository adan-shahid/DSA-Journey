def mergesorted(num1, num2, m, n):
    # get last index of num1
    last = m + n - 1
    # merge in reverse order
    while m > 0 and n > 0:
        if num1[m - 1] > num2[n - 1]:
            num1[last] = num1[m - 1]
            m -=1
        else:
            num1[last] = num2[n - 1]
            n -=1
        last -= 1

    #fills num1 with leftover num2 elements
    while n > 0:
        num1[last] = num2[n - 1]
        n, last = n-1, last - 1
    
    return num1

num1 = [1,2,3,0,0,0]
num2 = [2,5,6]
m = 3
n = 3
print(mergesorted(num1, num2, m, m))


# OTHER PEOPLE CODE 
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	a, b, write_index = m-1, n-1, m + n - 1

	while b >= 0:
		if a >= 0 and nums1[a] > nums2[b]:
			nums1[write_index] = nums1[a]
			a -= 1
		else:
			nums1[write_index] = nums2[b]
			b -= 1

		write_index -= 1
