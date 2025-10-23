num1 = [1,2,3,0,0,0]
m = 6
num2 = [2,5,6]
n = 3
if num1[0] == 1:
    for i in range(1, m-n+1, 1):
        if num1[i] == num2[i-1]:
            num1.insert(i+1, num2[i-1])
        elif num1[i] < num2[i-1]:
            num1.insert(i+1, num2[i-1])
        elif num1[i] > num2[i-1]:
            num1.insert(i-1, num2[i-1])


z = len(num1)
for j in range(m+n, z, 1):
    if num1[j] == 0:
        num1.remove(num1[j])
    else:
        pass
    
print(num1)

# print(num1)