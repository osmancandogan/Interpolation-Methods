import numpy as np
import matplotlib.pyplot as plot

# necessary data
x = [20, 21, 23, 24, 25, 27, 29, 30]
y = [346, 362, 343, 339, 347, 346, 339, 394]

coeffs = np.zeros([8, 8])

# finding coefficients
coeffs[:, 0] = y
for i in range(1, 8):
    for j in range(8 - i):
        coeffs[j][i] = (coeffs[j + 1][i - 1] - coeffs[j][i - 1]) / (x[i + j] - x[j])

coeffs = coeffs[0]
degree = len(x)
sum = 0
product = 1
a = 0

# using Newton's polynomial with coefficients
for i in coeffs:
    product = i
    for j in range(a):
        product *= (26 - x[j])
    a += 1
    sum += product

print(sum)

# data updated
y.insert(5, sum)
x.insert(5, 26)

plot.plot(x, y)
plot.xlabel("April")
plot.ylabel("Number of Deaths")
plot.show()
