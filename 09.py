import math
import random
import numpy as np
def coding_problem_09(n = 100000):
	#The area of a circle is defined as $\pi r^2$. Estimate $\pi$ to 3 decimal places using a Monte Carlo method.
    m = 0
    for i in range(n):
        x, y = random.uniform(0, 1), random.uniform(0,1)
        if  y**2 + x**2 < 1:
            m += 1
    return     4 * m / n 

print(coding_problem_09())