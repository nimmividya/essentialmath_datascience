import math


# P = Principles
# r = rate
# t = time

# A = P × e^(rt)

def find_interest(principle, rate, time ):
    amount = principle * math.e ** (rate * time)
    #A = P * math.e ** (r * t)

    print(f"The amount after {time} years is: ${amount:.2f}")


find_interest(1000, 0.05,3 )
