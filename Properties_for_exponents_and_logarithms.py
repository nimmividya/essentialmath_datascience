import math

# multiplications
# x^m + x^n = x^m + n

# Example
x = 2
m = 3
n = 4

exp_mult = x**m * x**n # 128
print(exp_mult)

exp_mult_alternative = x**(m + n)
print(exp_mult_alternative)

# multiplication with logarithm
# log(a x b) = log(a) + log(b)




log_a = math.log(m)
log_b = math.log(n)

# Calculate log(a * b) directly
log_ab_direct = math.log(m * n)
print(log_ab_direct)  # Output: 0.7781512503836436

# Calculate using the logarithm addition rule
log_ab_rule = log_a + log_b
print(log_ab_rule)  # Output: 0.7781512503836436
