import matplotlib.pyplot as plt


def main():
    left_edges = [0, 10, 20, 30, 40]

    height = [100, 200, 300, 400, 500]

    bar_width = 5

    plt.bar(left_edges, height, bar_width, color=('r','g','b','c','k'))

    plt.show()


if __name__ == "__main__":
    main()
