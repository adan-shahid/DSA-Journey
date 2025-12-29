# n = 44
# if n % 2 == 0:
#     print(True)
# else:
#     print(False)

# the last bit of odd number is always 1. and of even number is 0.
#taking the bitwise AND operation with 1

n = 100
if (n & 1) == 1:
    print(False)
else:
    print(True)