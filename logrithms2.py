import math

a = 8
b = 4

log_a = math.log2(a)
print(f"exponent of 8 in base 2 is", log_a)

log_b = math.log2(b)
print(f"exponent of 4 in base 2 is", log_b)

print("--------------------")
# Calculate log(a * b) directly
log_ab_direct = math.log2(a * b)
print(log_ab_direct)  # 

# Calculate using the logarithm addition rule
log_ab_rule = log_a + log_b
print(log_ab_rule)  #
