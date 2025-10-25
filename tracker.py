# ---------------------------------------------------------
# Name: Anurag Mishra
# Date: October 24, 2025
# Project Title: Daily Calorie Tracker (CLI App)
# Description:
# A simple Python command-line tool that allows users to
# log their meals, calculate total and average calories,
# compare intake with a daily limit, and optionally save
# the session log to a text file.
# ---------------------------------------------------------

# Task 1: Setup & Introduction
print("==========================================")
print("   Welcome to the Daily Calorie Tracker!   ")
print("==========================================")
print("This tool helps you log your meals, calculate your total")
print("and average calories, and check if you're within your daily limit.\n")

# Task 2: Input & Data Collection
meals = []
calories = []

# Ask how many meals to enter
num_meals = int(input("How many meals would you like to log today? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal_name = input("Enter meal name (e.g., Breakfast): ")
    calorie_amount = float(input("Enter calorie amount: "))
    
    meals.append(meal_name)
    calories.append(calorie_amount)

# Task 3: Calorie Calculations
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    status = "⚠ Warning: You have exceeded your daily calorie limit!"
else:
    status = "✅ Great job! You are within your daily calorie limit."

# Task 5: Neatly Formatted Output
print("\n\n========= DAILY CALORIE SUMMARY =========")
print("Meal Name\tCalories")
print("------------------------------------------")

for meal, cal in zip(meals, calories):
    print(f"{meal:<12}\t{cal}")

print("------------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("------------------------------------------")
print(status)
print("==========================================\n")

# Task 6 (Bonus): Save Session Log to File

s = input("\nDo you want to save this session log to a file? (y/n): ")
if s.lower() == "y":
    from datetime import datetime
    timestamp = datetime.now()
    
    with open("calorie_log.txt", "a") as file:
        file.write("\n=========================================\n")
        file.write(f"Calorie Tracker Session - {timestamp}\n")
        file.write("-----------------------------------------\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:<20}{calories[i]}\n")
        file.write(f"Total calories: {total_calories}\n")
        file.write(f"Average calories: {average_calories:.2f}\n")
        if total_calories > daily_limit:
            file.write("Status: Exceeded daily limit\n")
        else:
            file.write("Status: Within daily limit\n")
    print("✅ Session log saved to calorie_log.txt")