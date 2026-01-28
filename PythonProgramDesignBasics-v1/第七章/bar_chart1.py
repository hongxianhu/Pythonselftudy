import matplotlib.pyplot as plt


def main():
    left_edges = [0, 10, 20, 30, 40]

    height = [100, 200, 300, 400, 500]

    plt.bar(left_edges, height)

    plt.show()


if __name__ == "__main__":
    main()
