import random
import math

def vector2_length(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)

def estimate_pi(n):
    in_circle = 0
    for i in range(n):
        coords = [random.random(), random.random()]
        if vector2_length(coords) <= 1:
            in_circle += 1

    pi = (in_circle/n) * 4
    return pi

'''
estimate = estimate_pi(10000000)
print("Estimate PI =", estimate, "\nDifference =", abs(math.pi - estimate))
'''