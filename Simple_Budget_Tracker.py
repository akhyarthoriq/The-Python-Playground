"""
Simple Budget Tracker

Description:
This program helps users track their monthly income and expenses, providing a detailed budget summary. 
It calculates remaining balance and classifies the budget as "Over Budget", "On Target", or "Within Budget".

Features:
- User input for monthly income and categorized expenses.
- Calculates total expenses and remaining balance.
- Option to set a spending goal for budget classification.

How to Use:
1. Run the program.
2. Input your monthly income when prompted.
3. Enter expenses for each category.
4. Optionally, set a spending goal.
5. View the summary of your budget.

"""

# Function to get monthly income from the user
def get_income():
    income = float(input("Enter your total monthly income: "))
    return income

# Function to get expenses from various categories
def get_expenses():
    categories = ["Rent/Mortgage", "Utilities", "Groceries", "Transportation", "Entertainment", "Others"]
    total_expenses = 0
    expenses = {}  # Dictionary to store individual expenses by category

    for category in categories:
        expense = float(input(f"Enter your {category} expense: "))
        expenses[category] = expense
        total_expenses += expense

    return total_expenses, expenses

# Function to get the user's spending goal, if they choose to set one
def get_spending_goal():
    choice = input("Do you want to set a spending goal? (yes/no): ").strip().lower()
    if choice == "yes":
        goal = float(input("Enter your monthly spending goal: "))
    else:
        goal = None
    return goal

# Function to calculate remaining balance
def calculate_balance(income, expenses):
    balance = income - expenses
    return balance

# Function to classify budget status based on expenses and goal
def classify_budget(expenses, goal):
    if goal is None:
        return "No spending goal set"
    if expenses > goal:
        return "OVER BUDGET"
    elif expenses <= goal * 0.95:
        return "WITHIN BUDGET"
    else:
        return "ON TARGET"

# Main function to run the program
def budget_tracker():
    # Step 1: Get income, expenses, and spending goal
    income = get_income()
    total_expenses, expense_details = get_expenses()
    goal = get_spending_goal()

    # Step 2: Calculate balance
    balance = calculate_balance(income, total_expenses)

    # Step 3: Classify budget status
    status = classify_budget(total_expenses, goal)

    # Step 4: Display the summary
    print("\nMonthly Budget Summary:")
    print("------------------------")
    print(f"Income: ${income:.2f}")
    print("Expense Breakdown:")
    for category, expense in expense_details.items():
        print(f"  {category}: ${expense:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")
    if goal is not None:
        print(f"Budget Goal: ${goal:.2f}")
    print(f"Classification: {status}")
    print(f"You are {status} with your spending this month.")

# Uncomment the following line to run the program:
budget_tracker()
