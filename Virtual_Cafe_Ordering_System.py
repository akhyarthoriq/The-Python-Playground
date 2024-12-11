"""
Virtual Cafe Ordering System

Description:
This program simulates a cafe ordering experience, allowing users to browse a menu, add items 
to their cart, and view a detailed receipt at checkout.

Features:
- Displays a menu with items and prices.
- Allows users to select items and add them to the cart.
- Calculates subtotal, tax, and total cost.
- Generates a detailed receipt.

How to Use:
1. Run the program.
2. Browse the menu and select items by entering their corresponding numbers.
3. Add as many items as desired and view the running total.
4. Checkout to see the final receipt with tax and total cost.

"""


# Define constants
MENU = {
    1: ("Coffee", 3.00),
    2: ("Tea", 2.50),
    3: ("Sandwich", 5.00),
    4: ("Salad", 4.00),
    5: ("Cake", 4.50)
}
TAX_RATE = 0.10  # 10% tax

# Function to display the cafe menu
def display_menu(menu):
    print("\nMenu:")
    for number, (item, price) in menu.items():
        print(f"{number}. {item} - ${price:.2f}")
    print()

# Function to add an item to the cart
def add_to_cart(menu, cart):
    try:
        choice = int(input("Please enter the number of the item you'd like to order (or type '0' to finish): "))
        if choice == 0:  # Finish ordering
            return False
        elif choice in menu:
            item, price = menu[choice]
            cart.append((item, price))
            print(f"Added '{item}' - ${price:.2f}")
        else:
            print("Invalid choice, please select a valid item number.")
    except ValueError:
        print("Invalid input, please enter a number.")
    return True

# Function to calculate the subtotal of the cart
def calculate_total(cart):
    subtotal = sum(price for item, price in cart)
    return subtotal

# Function to calculate the tax on the subtotal
def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate

# Function to display the receipt
def show_receipt(cart, subtotal, tax, total):
    print("\n--- Order Summary ---")
    print("Items Ordered:")
    for item, price in cart:
        print(f"  {item} - ${price:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (10%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("\nThank you for your order!")

# Main function to run the Virtual Cafe Ordering System
def virtual_cafe_system():
    cart = []
    print("Welcome to the Virtual Cafe!")
    display_menu(MENU)

    # Ordering Loop
    while True:
        if not add_to_cart(MENU, cart):
            # Break = Exit if the user finishes ordering
            break
        # Show current total after each addition
        subtotal = calculate_total(cart)
        print(f"Current Total: ${subtotal:.2f}")
        another = input("Would you like to order another item? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    # Calculate subtotal, tax, and total
    subtotal = calculate_total(cart)
    tax = calculate_tax(subtotal, TAX_RATE)
    total = subtotal + tax

    # Show final receipt
    show_receipt(cart, subtotal, tax, total)

# Uncomment the following line to run the program:
virtual_cafe_system()
