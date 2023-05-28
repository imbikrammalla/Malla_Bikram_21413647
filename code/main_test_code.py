import unittest
from io import StringIO
from unittest.mock import patch
from main_modular import *

# White-box testing class
class WhiteBoxTestWeatherInformation(unittest.TestCase):
    def test_get_month_weather_map(self):
        expected_result = {
            "January": "Summer",
            "February": "Summer",
            "March": "Autumn",
            "April": "Autumn",
            "May": "Autumn",
            "June": "Winter",
            "July": "Winter",
            "August": "Winter",
            "September": "Spring",
            "October": "Spring",
            "November": "Spring",
            "December": "Summer"
        }
        result = get_month_weather_map("Australia", "Metrological")
        self.assertEqual(result, expected_result)

    def test_get_weather(self):
        month_weather_map = {
            "January": "Summer",
            "February": "Summer",
            "March": "Autumn",
            "April": "Autumn",
            "May": "Autumn",
            "June": "Winter",
            "July": "Winter",
            "August": "Winter",
            "September": "Spring",
            "October": "Spring",
            "November": "Spring",
            "December": "Summer"
        }
        expected_result = "Summer"
        result = get_weather(month_weather_map, "January")
        self.assertEqual(result, expected_result)

    def test_get_weather_photo(self):
        expected_result = ""
        result = get_weather_photo("Winter")
        self.assertEqual(result, expected_result)


# Black-box testing class
class BlackBoxTestWeatherInformation(unittest.TestCase):
    def setUp(self):
        self.input_values = []
        self.output_values = []
        self.print_values = []

    def mock_input(self):
        return self.input_values.pop(0)

    def mock_print(self, *args, **kwargs):
        self.print_values.append(" ".join(map(str, args)))

    def test_user_input_flow(self):
        self.input_values = ["Australia", "Metrological", "January"]
        expected_output = "Summer "
        with patch('builtins.input', self.mock_input), patch('builtins.print', self.mock_print):
            month_weather_map = get_month_weather_map("Australia", "Metrological")
            month = "January"
            weather = get_weather(month_weather_map, month)
            photo = get_weather_photo(weather)
            print(weather, photo, end="")
        self.assertEqual("".join(self.print_values), expected_output)


if __name__ == "__main__":
    unittest.main()
