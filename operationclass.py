import numpy as np
import matplotlib.pyplot as plt


class IntArray:
    def __init__(self, int_array):
        # Input ko NumPy array me convert kar do
        int_array = np.array(int_array)

        # Ensure karo ki input valid NumPy array ho
        if not isinstance(int_array, np.ndarray):
            raise ValueError("Input must be a NumPy array")

        # Har value ko integer me convert karne ki koshish karo
        try:
            int_array = int_array.astype(int)
        except (ValueError, TypeError):
            raise ValueError("Input must contain only integer values")

        # Final cleaned integer array object me store kar do
        self.int_array = int_array

    def display(self):
        print("Employee productivity data:")
        print(self.int_array)

    def salary(self, rate_per_product=7):
        salaries = self.int_array * rate_per_product

        print(f"People made {self.int_array} products")
        print(f"Rate per product: {rate_per_product}")
        print(f"Salaries: {salaries}")

        return salaries

    def show_data(self):
        x = np.arange(1, len(self.int_array) + 1)

        plt.plot(x, self.int_array, marker='o')
        plt.title('Productivity of Employees')
        plt.xlabel('Employee Number')
        plt.ylabel('Products per Month')
        plt.xticks(x)
        plt.grid(True)
        plt.show()

    def total_products(self):
        return np.sum(self.int_array)

    def average_products(self):
        return np.mean(self.int_array)

    def max_products(self):
        return np.max(self.int_array)

    def min_products(self):
        return np.min(self.int_array)