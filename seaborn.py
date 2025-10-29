import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [8, 8]
plt.rcParams["figure.autolayout"] = True
x = [1, 2, 3, 1, 2, 3, 4, 1, 3, 4, 5]
plt.hist(x, orientation="vertical")
plt.show()