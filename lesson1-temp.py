# C to F = (0°C × 9/5) + 32 = 32°F
# F to C = (32°F − 32) × 5/9 = 0°C
# K to F = (0K − 273.15) × 9/5 + 32 = -459,7°F
# F to K = 	(32°F − 32) × 5/9 + 273.15 = 273,15K
# C to K = 0°C + 273.15 = 273,15K
# K to C = 273,15K - 273.15 = 0°C

temp_unit_set = {"C", "F", "K"}

while True:
    temp_input = input(
        "Enter a temperature with unit to convert (e.g., 25C, 98.6F, 300K) or 'q' to quit: "
    ).strip()
    # Q or q to quit
    if temp_input.lower() == "q":
        break
    temp_output = (
        input("Enter the unit you want to get (C/F/K): ").strip().upper()
    )  # yeah yeah, always uppercase this shit

    # If unit is NOT included tell the user to input the letter too ;)
    if len(temp_input) < 2:
        print("Please enter a valid temperature and unit (e.g., 25C).\n")
        continue

    # Uppercase the last token; and put it in its own var
    unit = temp_input[-1].upper()
    value_str = temp_input[:-1]

    # If it's not Celsius, Fahrenheit or Kelvin - error!
    if (unit not in temp_unit_set) or (temp_output not in temp_unit_set):
        print("Invalid unit. Please use C, F, or K.\n")
        continue

    # Ensure it's an actual number, not a char ;)
    try:
        temp = float(value_str)
    except ValueError:
        print("Invalid number. Please enter a valid temperature value.\n")
        continue

    if unit == "C":
        if temp_output == "F":
            f = (temp * 9 / 5) + 32
            print(f"Result: {temp}°C = {f:.2f}°F\n")
        elif temp_output == "K":
            k = temp + 273.15
            print(f"Result: {temp}°C = {k:.2f}K\n")
        else:
            print(
                "You asked for Celsius and gave Celsius. So yeah, you know your answer ;)"
            )
            break
    elif unit == "F":
        if temp_output == "C":
            c = (temp - 32) * 5 / 9
            print(f"Result: {temp}°F = {c:.2f}°C\n")
        elif temp_output == "K":
            k = temp + 273.15
            print(f"Result: {temp}°F = {k:.2f}K\n")
        else:
            print(
                "You asked for Fahrenheit and gave Fahrenheit. So yeah, you know your answer ;)"
            )
            # break
    elif unit == "K":
        if temp_output == "C":
            c = temp - 273.15
            print(f"Result: {temp}K = {c:.2f}°C\n")
        elif temp_output == "F":
            f = (temp - 273.15) * 9 / 5 + 32
            print(f"Result: {temp}K = {f:.2f}°F\n")
        else:
            print(
                "You asked for Kelvin and gave Kelvin. So yeah, you know your answer ;)"
            )
    else:
        print("Invalid unit. Please use C, F, or K.\n")
