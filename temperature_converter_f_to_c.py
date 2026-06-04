def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9

# Example usage for testing:
if __name__ == "__main__":
    test_temperatures = [32, 50, 70, 90, 212, 10, 40]
    for temp in test_temperatures:
        c_temp = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is equal to {c_temp:.2f}°C")