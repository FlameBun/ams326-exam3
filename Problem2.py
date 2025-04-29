import matplotlib.pyplot as plot
import numpy
import math

num_needles = 100000 # Number of needles to toss
cross_prob = {} # Dictionary of each needle's probability to cross the rose curve
lengths = [1/10, 1/5, 1/4, 1/3, 1/2, 1] # Needle lengths

# Given two points, return True if sampled line between two points crosses the rose curve.
# Otherwise, return False. 
def crosses_rose(x1, y1, x2, y2, steps=1000, tolerance=1e-2):
    t_vals = numpy.linspace(0, 1, steps)
    x_vals = x1 + t_vals * (x2 - x1)
    y_vals = y1 + t_vals * (y2 - y1)

    left_side = (x_vals**2 + y_vals**2)**3
    right_side = 4 * x_vals**2 * y_vals**2

    # Check where the difference is near zero (crosses the curve)
    difference = numpy.abs(left_side - right_side)
    return numpy.any(difference < tolerance)

for length in lengths:
    # Randomly pick first points
    x0 = numpy.random.uniform(-1, 1, num_needles)
    y0 = numpy.random.uniform(-1, 1, num_needles)

    # Randomly pick angles second point is at from first points
    angle = numpy.random.uniform(0, 2 * numpy.pi, num_needles)

    # Compute second points given the needle length and corresponding angles
    x1 = x0 + length * numpy.cos(angle)
    y1 = y0 + length * numpy.sin(angle)

    # Determine percentage of set of points (x0, y0) and (x1, y1) form a line that crosses the rose curve
    num_crosses = 0
    for i in range(num_needles):
        crosses = crosses_rose(x0[i], y0[i], x1[i], y1[i])
        if crosses == True:
            num_crosses += 1

    cross_prob[length] = num_crosses / num_needles
    print(f"Needle Length L ({length}) Cross Probability: {cross_prob[length]}")
