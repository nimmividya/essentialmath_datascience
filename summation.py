# summation = sum(2* i for i in range(1,6))
# print(summation)


x = [1,4,6,8]
n = len(x)

# multiply members in x and add all the multipliers

summation = sum(((10*x[i])/2) for i in range(0,n))
print(summation)