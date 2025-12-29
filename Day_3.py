def remove_element(num1, val):
    k = 0
    for i in range(len(num1)):
        if num1[i] != val:
            num1[k] = num1[i]
            k += 1
    return k, num1
    
num1 = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element(num1, val))

# Replacing the values
# num = [1,2,3,4,5]
# num[0], num[0+1] = num[0+1], num[0]
# print(num)