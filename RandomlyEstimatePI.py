import random
import math

def vector2_length(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)

def randomly_estimate_pi(n):
    in_circle = 0
    for i in range(n):
        coords = [random.random(), random.random()]
        if vector2_length(coords) <= 1:
            in_circle += 1

    pi = (in_circle/n) * 4
    return pi

estimate = randomly_estimate_pi(10000000)
print("Estimate PI =", estimate, "\nDifference =", abs(math.pi - estimate))
