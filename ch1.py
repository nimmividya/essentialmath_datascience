from sympy import *

# my_value = (2 * (((3+2)**2)/5)) - 4
#
# print(f'my_value: ',my_value)
#
# x =(int(input('Enter a number')))
#
# print(2 * x)

# f(x) 2x + 1

# def f(x):
#     return 2 * x + 1
#
# x_values = [0,1,2,3]
#
# for x in x_values:
#     y = f(x)
#     print(y)


from sympy import symbols, plot

# Step 1: Define the symbolic variable
x = symbols('x')

# Step 2: Define the function f(x) = 2x + 1
f = 2 * x + 1

# Step 3: Plot the function
plot(f, (x, 1, 10),
     title='Graph of f(x) = 2x + 1',
     xlabel='x', ylabel='f(x)',
     line_color='blue')
