import matplotlib.pyplot as plt


def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 5, 5, 2]

    plt.plot(x_coords, y_coords)

    plt.title("Sample Data")

    plt.xlabel("This is the X axis")
    plt.ylabel("This is the Y axis")

    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)

    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
