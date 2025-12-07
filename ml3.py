
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(x)


sum_x = sum(x)
sum_y = sum(y)

sum_xy = sum([x[i] * y[i] for i in range(n)])
sum_x2 = sum([x[i] ** 2 for i in range(n)])


m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - m * sum_x) / n

print("Slope (m):", m)
print("Intercept (b):", b)


def predict(x_new):
    return m * x_new + b


print("\nPrediction for x=6:", predict(6))
