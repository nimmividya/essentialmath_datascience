import math

x = 2
m = 3
n = 2

result = (x**m)**n # (x^3)^2
print(f'(x^3)^2 = ', result)  # Output: 64

# Alternatively, using the exponent multiplication rule:
result_alternative = x**(m * n)
print(result_alternative)  # Output: 64

print("---------------------------------")

a = 8
n = 3

log_a = math.log2(a) # 3 , 2^3 = 8
print(log_a)

log_n = math.log2(n) # 3 , 2^3 = 8
print(log_n) # 1.6 , 2^1.6 = 3


# Calculate log(a^n) directly
log_exp_direct = math.log2(a**n)
print(log_exp_direct)  #

# Calculate using the logarithm multiplication rule
log_exp_rule = log_a * n
print(log_exp_rule)  #



