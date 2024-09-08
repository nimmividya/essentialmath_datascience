import math

# Division

# x^m/x^n = x^ m - n

x = 2
m = 5
n = 3

division1 = x**5 / x**3

print(division1) # 4
print("-------------------------------------")

a = 8
b = 2

log_a = math.log2(a)
print(f"value of x  of 2^x = 8 : ",log_a)
log_b = math.log2(b)
print(f"value of x  of 2^x = 2 : ",log_b)

# Calculate log(a / b) directly
log_div_direct = math.log2(a / b)
print(log_div_direct)  #

# Calculate using the logarithm subtraction rule
log_div_rule = log_a - log_b
print(log_div_rule)  #