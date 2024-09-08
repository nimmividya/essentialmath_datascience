
def find_euler():
    for n in range(1,1000):
        result = (1 + 1/n)**n
        print(result)

find_euler()