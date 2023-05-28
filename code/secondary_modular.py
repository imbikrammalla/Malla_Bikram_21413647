city_data = {
    "Perth": {
        "Min Temp": 0.7,
        "Max Temp": 46,
        "Morning Temp": 18.2,
        "Evening Temp": 23.0
    },
    "Adelaide": {
        "Min Temp": -1,
        "Max Temp": 49,
        "Morning Temp": 16.5,
        "Evening Temp": 21.0
    }
}

def calculate_average_temperature(city):
    if city not in city_data:
        return None
    
    min_temp = city_data[city].get("Min Temp")
    max_temp = city_data[city].get("Max Temp")

    if min_temp is None or max_temp is None:
        return None

    average_temp = (min_temp + max_temp) / 2
    return average_temp

def compare_temperature(city, temperature, time_of_day):
    average_temp = calculate_average_temperature(city)

    if average_temp is None:
        return "Invalid city name. Please enter either Adelaide or Perth."

    if temperature > average_temp:
        return f"The temperature is above the average temperature of {city}."
    elif temperature < average_temp - 5:
        return f"The temperature is below the average temperature of {city}. The difference is more than 5°C."
    else:
        return f"The temperature is within 5°C of the average temperature of {city}."


if __name__ == "__main__":
    # Get user input
    city = input("Enter the city (Perth/Adelaide): ")
    temperature = float(input("Enter the temperature reading: "))
    time_of_day = input("Enter the time of day (morning/evening): ")

    # Check and display the result
    if city in city_data.keys():
        result = compare_temperature(city, temperature, time_of_day)
        print(result)
    else:
        print("Invalid city name. Please enter either Perth or Adelaide.")
