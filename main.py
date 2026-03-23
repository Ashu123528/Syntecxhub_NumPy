import numpy as np
from operationclass import IntArray


file_path = 'company.txt'


def productivity_of_company(order, data_frame):
    return np.sum(data_frame[order])


def max_productivity(data_frame):
    best_company = 1
    num_of_products = productivity_of_company(0, data_frame)

    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        if result > num_of_products:
            num_of_products = result
            best_company = i + 1

    print(f"The best company is company {best_company} with {num_of_products} products made")


def min_productivity(data_frame):
    worst_company = 1
    num_of_products = productivity_of_company(0, data_frame)

    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        if result < num_of_products:
            num_of_products = result
            worst_company = i + 1

    print(f"The worst company is company {worst_company} with {num_of_products} products made")


def mean_products(data_frame):
    for i in range(len(data_frame)):
        average = np.mean(data_frame[i])
        print(f"On average, one employee from company {i + 1} produced {average:.2f} products")

    total_sum = 0
    num_elements = 0

    for row in data_frame:
        for element in row:
            total_sum += element
            num_elements += 1

    total_mean = total_sum / num_elements
    print(f"Mean productivity of the entire monopoly is {total_mean:.2f} per employee")


def file_handling():
    lines = []

    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            int_values = [int(val) for val in values]
            lines.append(np.array(int_values, dtype=int))

    data_frame = np.array(lines, dtype=object)
    return data_frame


def main():
    data_frame = file_handling()

    print("Complete company data:")
    print(data_frame)
    print()

    first_branch = IntArray(data_frame[0])
    first_branch.display()
    print()

    first_branch.salary()
    print()

    first_branch.show_data()

    print(f"Total products of first company: {first_branch.total_products()}")
    print(f"Average products of first company: {first_branch.average_products():.2f}")
    print(f"Maximum products by one employee in first company: {first_branch.max_products()}")
    print(f"Minimum products by one employee in first company: {first_branch.min_products()}")
    print()

    max_productivity(data_frame)
    min_productivity(data_frame)
    mean_products(data_frame)


if __name__ == "__main__":
    main()