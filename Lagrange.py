import matplotlib.pyplot as plot

# necessary data
x = [20, 21, 23, 24, 25, 27, 29, 30]
y = [346, 362, 343, 339, 347, 346, 339, 394]

degree = len(x) - 1
p = 0

# using lagrange interpolation formula over data
for i in range(degree + 1):
    product = 1
    for j in range(degree + 1):
        if j != i:
            product *= (26 - x[j]) / (x[i] - x[j])
    p += product * y[i]

print(p)

# data updated
y.insert(5, p)
x.insert(5, 26)

plot.plot(x, y)
plot.xlabel("April")
plot.ylabel("Number of Deaths")
plot.show()
