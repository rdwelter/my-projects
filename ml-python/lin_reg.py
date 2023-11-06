# based on https://www.youtube.com/watch?v=uwwWVAgJBcM
# not my own work, largely just a way for me to start ml

import numpy as np
import matplotlib.pyplot as plt

# Takes partial derivatives of m and b
# Adjusts m and b based on partials scaled by a learning rate
def gradient_descent(points, m, b, learning_rate):
    partial_m = 0
    partial_b = 0
    for i in range(len(points)):
        partial_m += -points[i][0] * (points[i][1] - (m * points[i][0] + b))
        partial_b += -(points[i][1] - (m * points[i][0] + b))
    partial_m *= float(2) / float(len(points))
    partial_b *= float(2) / float(len(points))
    new_m = m - (partial_m * learning_rate)
    new_b = b - (partial_b * learning_rate)
    return [new_m, new_b]

# Simple error calculation for the line at the end
def error_for_line(points, m, b):
    err = 0
    for i in range(len(points)):
        err += np.float_power(points[i][1] - (m * points[i][0] + b), 2)
    err /= float(len(points))
    return err

# Main function, runs iters iterations of gradient_descent()
def run():
    points = np.genfromtxt("data/data.csv", delimiter=',') # nparray of nparrays
    for point in points:
        plt.plot(point[0], point[1], 'o')
    m = b = 0
    learning_rate = 0.0001 # can't make too big or else theres overflow, or too small or else the program takes forever
    iters = 1000 # relatively arbitrary, but should be large
    xvals = np.linspace(0, 100, 101) # x coords for plotting lines
    for _ in range(iters):
        m, b = gradient_descent(points, m, b, learning_rate)
        if (_ < 50): # graphs progress of linear regression
            plt.plot(xvals, m * xvals + b, linestyle='dashed')
    print(f'Final line of best fit:\nm = {m}\nb = {b}\nError = {error_for_line(points, m, b)}')
    plt.plot(xvals, m * xvals + b, linestyle='solid')
    plt.show()
    

if __name__ == "__main__":
    run()
