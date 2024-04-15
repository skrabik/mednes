import matplotlib.pyplot as plt


def build_graph(x, y, xlabel, ylabel, title):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(f'main.jpg')

# build_graph([1, 2, 3], [1, 2, 3], 'x', 'y', 'title')