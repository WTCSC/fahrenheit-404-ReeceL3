#Starting the program

def convert_temperature():
    print("Welcome to the Temperature Converter!")
    print("This program allows you to convert temperatures between Fahrenheit and Celsius.")
    print("You can convert as many temperatures as you want. Type 'exit' at any time to quit.\n")

    while True:
        starting_temp_unit = input("Enter the unit of your current temperature (F for Fahrenheit, C for Celsius): ").strip().upper()

        if starting_temp_unit == "EXIT":
            break

        if starting_temp_unit not in ["F", "C"]:
            print("Invalid unit. Please enter 'F' or 'C'. Try again.\n")
            continue

        temp_input = input("Enter the numeric value of the temperature you want to convert: ").strip()

        if temp_input.lower() == "exit":
            break

        try:
            temp_value = float(temp_input)
        except ValueError:
            print("Invalid temperature value. Please enter a number.\n")
            continue

        if starting_temp_unit == "F":
            converted_temp = (temp_value - 32) * 5 / 9
            print(f"{temp_value:.2f}°F is equal to {converted_temp:.2f}°C\n")
        elif starting_temp_unit == "C":
            converted_temp = (temp_value * 9 / 5) + 32
            print(f"{temp_value:.2f}°C is equal to {converted_temp:.2f}°F\n")

        repeat = input("Would you like to convert another temperature? (yes/no): ").strip().lower()
        if repeat not in ["yes", "y"]:
            print("\n Thank you for using the Temperature Converter I hope that you need to convert temps again")
            break

convert_temperature()
