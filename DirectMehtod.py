import numpy as np
import matplotlib.pyplot as plot

# necessary data
data = [346, 362, 343, 339, 347, 346, 339, 394]
days = [20, 21, 23, 24, 25, 27, 29, 30]

row, col = (8, 8)

# creating the matrix of equation and filling part
A = [[0 for i in range(col)] for j in range(col)]

for i in range(0, 8):
    for j in range(0, 8):
        A[i][j] = days[i] ** j

# solving with numpy
X = np.linalg.inv(A).dot(data)
day = 26
solution = 0
for i in range(0, 8):
    solution += X[i] * day ** i

print(solution)

# data updated
data.insert(5, solution)
days.insert(5, 26)

plot.plot(days, data)
plot.xlabel("April")
plot.ylabel("Number of Deaths")
plot.show()
