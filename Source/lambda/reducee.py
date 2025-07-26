from functools import reduce

lis = [1,2,3,4,5,6,7,8,9,10]
total = reduce(lambda a,b:a+b,lis)

# 3,3,4,5,6,7,8,9,10
# 6,4,5,6,7,8,9,10
# 10,5,6,7,8,9,10
# 15,6,7,8,9,10
# 21,7,8,9,10
# 28,8,9,10
# 36,9,10
# 45,10
# 55

print(total)