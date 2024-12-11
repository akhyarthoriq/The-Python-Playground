"""
BMI and Calorie Needs Calculator

Description:
This program calculates BMI (Body Mass Index) and daily calorie needs based on user inputs such as 
weight, height, age, gender, and activity level. It provides BMI classification and estimated calorie 
requirements for maintenance, weight loss, or gain.

Features:
- Calculates BMI and provides a WHO-based classification.
- Calculates Basal Metabolic Rate (BMR) and daily calorie needs.
- Adjusts calorie estimates based on activity level and user goal.

How to Use:
1. Run the program.
2. Input your weight, height, age, and gender.
3. Select your activity level from the menu.
4. Choose your goal (maintenance, gain, or loss).
5. View your BMI and daily calorie needs.

"""


# Function to calculate BMI and classify it based on WHO standards
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    # WHO classification based on BMI
    if bmi < 18.5:
        classification = "UNDERWEIGHT"
    elif 18.5 <= bmi < 24.9:
        classification = "NORMAL"
    elif 25 <= bmi < 29.9:
        classification = "OVERWEIGHT"
    else:
        classification = "OBESE"

    return bmi, classification

# Function to calculate BMR based on gender
def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161
    return bmr

# Function to get the activity multiplier based on user input
def get_activity_multiplier(activity_level):
    activity_multipliers = {
        1: 1.2,   # Sedentary
        2: 1.375, # Lightly active
        3: 1.55,  # Moderately active
        4: 1.725, # Very active
        5: 1.9    # Super active
    }
    return activity_multipliers.get(activity_level, 1.2)  # Default to 1.2 if invalid input

# Function to calculate daily calorie needs based on BMR, activity level, and goal
def calculate_daily_calories(bmr, activity_level, goal):
    # Adjust BMR based on activity multiplier
    daily_calories = bmr * get_activity_multiplier(activity_level)

    # Adjust daily calories based on goal
    if goal.lower() == 'gain':
        daily_calories += 500  # Additional 500 calories for weight gain
    elif goal.lower() == 'loss':
        daily_calories -= 500  # Reduce 500 calories for weight loss

    return daily_calories

# Main function to run the BMI and Calorie Needs Calculator
def bmi_calories_calculator():
    # Step 1: Gather user inputs
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").strip().lower()

    # Step 2: Calculate BMI and display classification
    bmi, classification = calculate_bmi(weight, height)
    print(f"\nYour BMI is {bmi:.2f}, which is classified as {classification}.")

    # Step 3: Gather additional inputs for calorie needs
    print("\nSelect Activity Level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise/sports 1-3 days/week)")
    print("3. Moderately active (moderate exercise/sports 3-5 days/week)")
    print("4. Very active (hard exercise/sports 6-7 days a week)")
    print("5. Super active (very hard exercise, physical job)")

    activity_level = int(input("Enter the number corresponding to your activity level: "))
    goal = input("Enter your goal (maintenance/gain/loss): ").strip().lower()

    # Step 4: Calculate BMR
    bmr = calculate_bmr(weight, height, age, gender)

    # Step 5: Calculate daily calories based on activity and goal
    daily_calories = calculate_daily_calories(bmr, activity_level, goal)

    # Step 6: Display the calorie needs
    print(f"\nYour estimated daily calorie needs for {goal} are: {daily_calories:.0f} calories.")

# Uncomment the following line to run the program:
bmi_calories_calculator()