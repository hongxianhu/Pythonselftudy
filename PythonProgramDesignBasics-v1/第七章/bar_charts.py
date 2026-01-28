import matplotlib.pyplot as plt


def main():
    sales = [20, 60, 80, 40]

    slice_labels = ["1st Qtr", "2nd Qtr", "3rd Qtr", "4th Qtr"]

    plt.pie(sales, labels=slice_labels, colors=("r", "g", "b", "w", "k"))

    plt.title("Sales by Quarter")

    plt.show()


if __name__ == "__main__":
    main()
