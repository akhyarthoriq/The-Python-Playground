"""
Cinema Booking and Ticketing System

Description:
This program simulates a cinema seat booking system, allowing users to book available seats and 
view a summary of their bookings and total cost. 

Features:
- Displays a dynamic seating layout (3x5 grid).
- Ensures seat availability before booking.
- Calculates total ticket cost and provides a booking summary.

How to Use:
1. Run the program.
2. View the seating layout and select a seat by entering its row and column number.
3. Book additional seats if desired.
4. View the booking summary and total cost.

"""


# Define constants
ROWS = 3
COLS = 5
SEAT_PRICE = 10  # Price per ticket

# Function to display the current seating layout
def display_seating_layout(seats):
    print("\nCurrent Seating Layout:")
    for row in seats:
        print(" ".join(row))
    print()

# Function to book a seat if it's available
def book_seat(seats, row, col):
    if seats[row][col] == 'O':  # Check if the seat is available
        seats[row][col] = 'X'  # Mark seat as booked
        return True
    else:
        return False

# Function to get the price of a single seat
def get_seat_price():
    return SEAT_PRICE

# Function to calculate the total price for a given number of tickets
def calculate_total_price(num_tickets):
    return num_tickets * SEAT_PRICE

# Function to get seat choice from user with input validation
def get_seat_choice():
    while True:
        try:
            row = int(input(f"Please enter the row number (1-{ROWS}): ")) - 1
            col = int(input(f"Please enter the seat number (1-{COLS}): ")) - 1
            if 0 <= row < ROWS and 0 <= col < COLS:
                return row, col
            else:
                print(f"Invalid input. Please enter a row between 1 and {ROWS}, and a seat between 1 and {COLS}.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Function to show a summary of all booked seats and the total price
def show_booking_summary(booked_seats, total_price):
    print("\n--- Booking Summary ---")
    print("Booked Seats:")
    for seat in booked_seats:
        print(f"  Row {seat[0] + 1}, Seat {seat[1] + 1}")
    print(f"Total Tickets: {len(booked_seats)}")
    print(f"Total Price: ${total_price}")
    print("Thank you for using the Cinema Booking System!\n")

# Main function to handle the cinema booking system
def cinema_booking_system():
    # Initialize seating layout
    seats = [['O' for _ in range(COLS)] for _ in range(ROWS)]
    booked_seats = []  # To store the list of booked seats

    print("Welcome to the Cinema Booking System!")
    display_seating_layout(seats)

    while True:
        # Step 1: Get seat choice from user
        row, col = get_seat_choice()

        # Step 2: Attempt to book the chosen seat
        if book_seat(seats, row, col):
            print("Seat booked successfully!")
            booked_seats.append((row, col))
        else:
            print("Sorry, that seat is already booked. Please choose a different seat.")

        # Show updated seating layout
        display_seating_layout(seats)

        # Step 3: Ask if the user wants to book another seat
        another = input("Do you want to book another seat? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    # Calculate total price based on the number of booked seats
    total_price = calculate_total_price(len(booked_seats))

    # Show booking summary
    show_booking_summary(booked_seats, total_price)

# Uncomment the following line to run the program:
cinema_booking_system()
