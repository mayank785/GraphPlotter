import matplotlib.pyplot as plt

o = {}

for x in range(51):
    y = -(x + 2)
    o[x] = y
    x += 1
def graph_maker():
    """ Function to first seperate the dictionary values into x and y values and then use them to make the graph and show """
    x_values = []
    y_values = []
    for i in range(51):
        x_values.append(i)
        y_values.append(o[i])
        i += 1
    print(x_values)
    print(y_values)
    plt.plot(x_values, y_values)
    plt.show()

print(o)
graph_maker()