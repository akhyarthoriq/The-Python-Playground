"""
InventoryManager - Interactive Inventory Management System

Description:
This program provides a command-line interface for managing an inventory of products.
Users can add, remove, and view products, as well as perform basic analytics such as
calculating the total inventory value, average product price, and identifying the most
expensive item in the inventory.

Features:
- Add new products with a name, price, and quantity.
- Remove products from the inventory by name.
- View all products in the inventory.
- Calculate the total value of the inventory.
- Compute the average price of products.
- Identify the most expensive product in the inventory.

Usage:
1. Run the program in a Python environment.
2. Follow the menu prompts to interact with the inventory system.

Requirements:
- Python 3.8 or higher.
- No additional dependencies are required.

File Structure:
- This script contains both the main program and the Inventory/Product classes.

Author:
- Your Name (your-email@example.com)

License:
- This project is licensed under the MIT License.

"""

class Product:
    """Represents a product with a name, price, and quantity."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}, Quantity: {self.quantity}"

class Inventory:
    """Manages a collection of products."""
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"Added: {new_product}")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Removed: {name}")
                return
        print(f"Product '{name}' not found.")

    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product)

    def calculate_total_value(self):
        total_value = sum(p.price * p.quantity for p in self.products)
        print(f"Total inventory value: ${total_value:.2f}")

    def calculate_average_price(self):
        if not self.products:
            print("No products to calculate an average price.")
            return
        average = sum(p.price for p in self.products) / len(self.products)
        print(f"Average product price: ${average:.2f}")

    def find_most_expensive(self):
        if not self.products:
            print("No products available.")
            return
        most_expensive = max(self.products, key=lambda p: p.price)
        print(f"Most expensive product: {most_expensive}")

def main():
    inventory = Inventory()

    menu = (
        "\nOptions:\n"
        "1. Add Product\n"
        "2. Remove Product\n"
        "3. View Products\n"
        "4. Total Inventory Value\n"
        "5. Average Product Price\n"
        "6. Most Expensive Product\n"
        "7. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            inventory.add_product(name, price, quantity)

        elif choice == "2":
            name = input("Enter product name to remove: ")
            inventory.remove_product(name)

        elif choice == "3":
            inventory.view_products()

        elif choice == "4":
            inventory.calculate_total_value()

        elif choice == "5":
            inventory.calculate_average_price()

        elif choice == "6":
            inventory.find_most_expensive()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()
