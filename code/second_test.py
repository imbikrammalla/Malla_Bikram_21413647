import unittest
from unittest.mock import patch
from secondary_modular import calculate_average_temperature, compare_temperature


#White-box testing class

class WhiteBoxTestTemperatureInformation(unittest.TestCase):
    def setUp(self):
        self.print_values = [] # Initialize print_values as an empty list

    def tearDown(self):
        self.print_values = None  # Clean up print_values after each test

    def mock_print(self, text):
        self.print_values.append(text)  # Append printed values to print_values list

    def test_calculate_average_temperature(self):
        city = "Perth"
        expected_average_temp = 23.4
        average_temp = calculate_average_temperature(city)
        self.assertAlmostEqual(average_temp, expected_average_temp, places=1)

    def test_compare_temperature_above(self):
        city = "Adelaide"
        temperature = 30.5
        expected_result = "The temperature is above the average temperature of Adelaide."
        result = compare_temperature(city, temperature, "morning")
        self.assertEqual(result, expected_result)

    def test_compare_temperature_below(self):
        city = "Perth"
        temperature = 15.8
        expected_result = "The temperature is below the average temperature of Perth. The difference is more than 5°C."
        result = compare_temperature(city, temperature, "evening")
        self.assertEqual(result, expected_result)

    def test_compare_temperature_large_difference(self):
        city = "Adelaide"
        temperature = 5.0
        expected_result = "The temperature is below the average temperature of Adelaide. The difference is more than 5°C."
        result = compare_temperature(city, temperature , "morning")
        self.assertEqual(result, expected_result)

#Black-box testing class

class BlackBoxTestTemperatureInformation(unittest.TestCase):
    def setUp(self):
        self.input_values = []
        self.print_values = []
        self.expected_output = ""


    def mock_input(self):
        return self.input_values.pop(0)

    def mock_print(self, text):
        self.print_values.append(text)

    @patch("builtins.input", mock_input)
    @patch("builtins.print", mock_print)
    def test_user_input_flow_perth(self):
        self.input_values = ["Perth", "25.0", "morning"]
        self.expected_output = "The temperature is above the average temperature of Perth."
        calculate_average_temperature("Perth")  # Pre-compute average temperature
        result = compare_temperature("Perth", 25.0, "morning")
        self.assertEqual(result, self.expected_output)

    @patch("builtins.input", mock_input)
    @patch("builtins.print", mock_print)
    def test_user_input_flow_adelaide(self):
        self.input_values = ["Adelaide", "10.0", "evening"]
        self.expected_output = 'The temperature is below the average temperature of Adelaide. The difference is more than 5°C.'
        calculate_average_temperature("Adelaide")  # Pre-compute average temperature
        result = compare_temperature("Adelaide", 10.0, "evening")
        self.assertEqual(result, self.expected_output)

    @patch("builtins.input", mock_input)
    @patch("builtins.print", mock_print)
    def test_user_input_flow_invalid_city(self):
        self.print_values = []  # Initialize print_values as an empty list
        self.input_values = ["Sydney", "20.0", "morning"]
        self.expected_output = "Invalid city name. Please enter either Adelaide or Perth."
        result = compare_temperature("Sydney", 20.0, "morning")
        self.assertEqual(result, self.expected_output)

    
    # boundary value test cases
    @patch("builtins.input", mock_input)
    @patch("builtins.print", mock_print)
    def test_user_input_flow_perth_boundary(self):
        self.input_values = ["Perth", "-50.0", "morning"]
        self.expected_output = "The temperature is below the average temperature of Perth. The difference is more than 5°C."
        calculate_average_temperature("Perth")  # Pre-compute average temperature
        result = compare_temperature("Perth", -50.0, "morning")
        self.assertEqual(result, self.expected_output)

    @patch("builtins.input", mock_input)
    @patch("builtins.print", mock_print)
    def test_user_input_flow_adelaide_boundary(self):
        self.input_values = ["Adelaide", "60.0", "evening"]
        self.expected_output = "The temperature is above the average temperature of Adelaide."
        calculate_average_temperature("Adelaide")  # Pre-compute average temperature
        result = compare_temperature("Adelaide", 60.0, "evening")
        self.assertEqual(result, self.expected_output)

if __name__ == "__main__":
    unittest.main()