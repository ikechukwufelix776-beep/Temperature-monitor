# Temperature Monitor and Alarm Checker
#f/ND/25/3450094
# Function to collect and analyze temperature readings
def monitor_temperature():

    temperatures = []

    print("WELCOME TO THE TEMPERATURE MONITOR")
    print("-----------------------------------")

    # Collect the safe temperature limit
    try:
        safe_limit = float(input("Enter the safe temperature limit: "))

        # Collect five temperature readings
        for i in range(5):
            reading = float(input(f"Enter temperature reading {i + 1}: "))
            temperatures.append(reading)

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    # Calculate highest, lowest and average temperatures
    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)

    print("\n----- TEMPERATURE REPORT -----")

    print("All readings:", temperatures)
    print("Highest temperature:", highest)
    print("Lowest temperature:", lowest)
    print("Average temperature:", round(average, 2))

    # Check whether any temperature exceeds the safe limit
    if highest > safe_limit:
        print("WARNING! Machine temperature is above the safe limit.")
    else:
        print("Machine temperature is within the safe limit.")

    # Extra feature: Detect temperature trend
    if all(temperatures[i] < temperatures[i + 1] for i in range(4)):
        print("Temperature trend: Increasing!")

    elif all(temperatures[i] > temperatures[i + 1] for i in range(4)):
        print("Temperature trend: Decreasing!")

    else:
        print("Temperature trend: Fluctuating or stable.")

    print("-----------------------------------")
    print("Temperature monitoring completed.")


# Run the program
monitor_temperature()