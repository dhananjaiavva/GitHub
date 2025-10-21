def main():
    """  Main function to run the calorie tracking program.  """
    meal_names = []
    calorie_amounts = []

    try:
        num_meals = int(input("How many meals do you want to enter? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for i in range(num_meals):
        meal_name = input(f"Enter the name of meal {i + 1}: ")
        while True:
            try:
                calorie_amount = float(input(f"Enter calorie amount for {meal_name}: "))
                if calorie_amount < 0:
                    print("Calorie amount cannot be negative. Please enter a valid number.")
                else:
                    meal_names.append(meal_name)
                    calorie_amounts.append(calorie_amount)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for calories.")

    if calorie_amounts:
        total_calories = sum(calorie_amounts)
        average_calories = total_calories / len(calorie_amounts)
    else:
        total_calories = 0
        average_calories = 0

    while True:
        try:
            daily_limit = float(input("Enter your daily calorie limit: "))
            if daily_limit < 0:
                print("Calorie limit cannot be negative. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for the calorie limit.")

    if total_calories > daily_limit:
        warning_message = "Warning: Your total calorie intake exceeded your daily limit."
    else:
        warning_message = "Success: You stayed within your daily calorie limit."

    print("\n" + "=" * 40)
    print("DAILY CALORIE SUMMARY")
    print("=" * 40)

    print(f"{'Meal Name':<15}{'Calories':>15}")
    print("-" * 40)

    for name, calories in zip(meal_names, calorie_amounts):
        print(f"{name:<15}{calories:>15.2f}")

    print("-" * 40)
    print(f"{'Total:':<15}{total_calories:>15.2f}")
    print(f"{'Average:':<15}{average_calories:>15.2f}")
    print("=" * 40)

    print(f"\n{warning_message}")
    print("=" * 40)


if __name__ == "__main__":
    main()
