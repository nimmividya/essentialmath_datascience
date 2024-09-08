import  math

# 2^x = 8
# If x is 3 -> 2^3 = 8

result1 = 2**3
print(f'2**3 : ',result1)

# how about 2^x = 1024?
# We have to find x.
# We use 'log' here

# log2 1024 = x

# What is the exponent of base 2 1024
# 2^x = 1024

x = math.log(1024, 2)

print(f"The exponent of 2^x is :  {x} which is 2^x = 1024 ")

print(f" 2^",x, "= 1024 ")