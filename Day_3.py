def remove_element(num1, val):
    k = 0
    n = len(num1)
    for i in range(0, n, 1):
        if num1[i] != val:
            k += 1
    for j in range(0, n-1, 1):
        if num1[j] == val:
            num1.remove(num1[j])

    return (k, num1)



num1 = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element(num1, val))