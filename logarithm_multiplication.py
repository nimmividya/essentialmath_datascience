from math import log


exp1 = 2

base = 2  # You can set any base here

# Convert x to the chosen base
#x_base = 2^2
x_base = base ** exp1 # base ^ 2 -> 2^2

print(x_base) # 4

result = x_base**2 * x_base**3 # 4^2 x 4^3 -> 16 * 64 ->1024

print(result)


#----------------------------------------
def exp_mult(exp_1, exp_2, mybase):
    result2 = mybase ** exp_1 * mybase ** exp_2
    print(result2)

    result3 = mybase ** (exp_1 + exp_2)
    print(result3)


exp_mult(3,2,2)






