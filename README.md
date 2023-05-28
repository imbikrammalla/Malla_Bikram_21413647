# Malla_Bikram_21413647

## A. Cover Page/Identity Information

- Assessment Name: Introduction to Software Engineering
- Your Name: Bikram Malla
- Curtin Student ID: 21413647
- Practical Class (Date/Time/Venue):

## B. Introduction
This assessment involved the development and testing of a software system focusing on weather information and temperature comparison. The objective was to design and implement modules that would allow users to retrieve weather data for a specific location and type of weather, as well as compare the temperature of a given city with its average temperature.

The assessment was divided into several parts, each addressing different aspects of software engineering. It began with creating module descriptions for the weather information and temperature comparison modules. These descriptions outlined the functionality and purpose of each module, providing a clear understanding of their roles within the software system.

Following the module descriptions, the focus shifted to implementing modularity in the code. Modularity concepts, such as encapsulation and separation of concerns, were applied to ensure that the system was organized into cohesive and reusable modules. This approach promoted code maintainability and scalability.

To ensure the reliability and correctness of the software system, black-box and white-box test cases were designed and executed. Black-box testing focused on validating the system's behavior based on external inputs and expected outputs. White-box testing delved into the internal structure of the code, verifying its logic and ensuring thorough coverage of different code paths.

Version control played a crucial role in managing the development process. A version control system was used to track changes, collaborate with team members, and maintain a history of the codebase. This facilitated efficient teamwork and provided a safety net for code modifications.

Ethical considerations were also taken into account throughout the assessment. The impact of the software system on users' privacy, data security, and potential biases was considered. Measures were taken to ensure data protection and fairness in the temperature comparison process.

This report will delve into the details of each section, including the module descriptions, modularity implementation, test case design and execution, version control usage, and ethical considerations. Additionally, a reflective discussion will be provided to highlight areas of improvement and share personal insights gained from completing the assessment.

## C. Module Descriptions

### Original Module Descriptions
The original module descriptions created for Part 2 of the assessment are as follows:

1. Module Name: Main Modular
- Description: This module handles the retrieval of weather data for a specific location.
- Reason for Implementation: It is essential to fetch accurate weather information to provide relevant insights to the users.
- Assumptions Made: The weather data API will provide the required information in the expected format.

2. Module Name: Secondary Modular
- Description: This module calculates the average temperature for a given city.
- Reason for Implementation: The average temperature is a crucial metric to compare against the current temperature and determine if it is above or below average.
- Assumptions Made: The city's temperature data is available and reliable for calculation purposes.

### Revised Module Descriptions (After Refactoring)

After conducting the refactoring process in Part 3, several improvements were made to the original module descriptions. The refactoring aimed to enhance code readability, maintainability, and adherence to software engineering best practices. The following are the revised module descriptions:

1. Module Name: calculate_average_temperature
- Description: This module calculates the average temperature for a given city based on the minimum and maximum temperatures.
- Reason for Implementation: This module is essential for providing users with an accurate representation of the average temperature for a specific city.
- Assumptions Made: The module assumes that the city's temperature data is available in the city_data dictionary with the keys "Min Temp" and "Max Temp".

1.Module Name: compare_temperature
- Description: This module compares the temperature reading with the average temperature of a city and provides a corresponding message based on the comparison.
- Reason for Implementation: This module allows users to determine if the temperature reading is above, below, or within 5°C of the average temperature for a specific city.
- Assumptions Made: The module assumes that the average temperature for the city is calculated using the calculate_average_temperature module and that the temperature reading and time of day inputs are provided by the user.

By refactoring the original code, these modules were optimized for readability and maintainability. The module descriptions were updated to provide clearer explanations of their purposes and assumptions. This refactoring process ensures that the codebase is more robust and easier to understand, facilitating future modifications and improvements.

## D. Modularity

To run the production code, use the following commands:
- `python3 main_modular.py` to run the first main_modular code.
- `python3 secondary_modular.py` to run the second code.


Different modularity concepts were applied in the code, such as:

- **Encapsulation**: The code is organized into separate modules, each encapsulating a specific functionality. This promotes modular design and allows for independent development and maintenance of different components.

- **Abstraction**: The modules provide an abstraction layer that hides the internal implementation details. Users can interact with the modules using well-defined interfaces, without needing to understand the underlying complexities.

- **Reusability**: The code promotes reusability by modularizing common functionalities. For example, the `calculate_average_temperature` module can be reused to calculate the average temperature for different cities.

Review Checklist:

1. **Code Clarity**: The code was reviewed to ensure clarity and readability. Variable names, function names, and comments were descriptive and followed appropriate naming conventions.
2. **Code Structure**: The code structure was reviewed to ensure it followed modular design principles and was organized in a logical and coherent manner.
3. **Error Handling**: The code was reviewed to ensure proper error handling techniques were implemented, such as exception handling and appropriate error messages.

Results of the review using the checklist:

- **Code Clarity**: Passed. The code was well-documented with clear and meaningful variable and function names.
- **Code Structure**: Passed. The code followed a modular structure, with separate functions and modules for different tasks.
- **Error Handling**: Passed. The code implemented proper error handling techniques, ensuring robustness and graceful handling of exceptions.

Any identified issues were addressed by refactoring the code and making necessary improvements to meet the modularity requirements.


## E. Black-Box Test Cases

The following test cases were designed for Part 4 of the assessment:

| Test Case ID | Description | Input | Expected Output |
|--------------|-------------|-------|-----------------|
| 1            | Verify the calculation of average temperature | City: Perth | Expected Average Temperature: 23.4 |
| 2            | Compare temperature above the average | City: Adelaide, Temperature: 30.5, Time: Morning | Expected Result: "The temperature is above the average temperature of Adelaide." |
| 3            | Compare temperature below the average with a large difference | City: Perth, Temperature: 15.8, Time: Evening | Expected Result: "The temperature is below the average temperature of Perth. The difference is more than 5°C." |
| 4            | Compare temperature below the average with a small difference | City: Adelaide, Temperature: 5.0, Time: Morning | Expected Result: "The temperature is below the average temperature of Adelaide. The difference is more than 5°C." |

Rationale behind the chosen test design: The test cases were designed to cover different scenarios and verify the correctness of the implemented functions. They include cases for calculating the average temperature, comparing temperatures above and below the average, and checking for large and small differences.

Assumptions made during test design: The assumptions include the availability of temperature data for the specified cities and times, and the correct implementation of the average temperature calculation and comparison functions.

## F. White-Box Test Cases

The following test cases were designed for Part 5 of the assessment:

| Test Case ID | Description | Expected Output |
|--------------|-------------|-----------------|
| 1            | Verify the calculate_average_temperature function | Expected Average Temperature: 23.4 |
| 2            | Verify the compare_temperature function for temperature above the average | Expected Result: "The temperature is above the average temperature of Adelaide." |
| 3            | Verify the compare_temperature function for temperature below the average with a large difference | Expected Result: "The temperature is below the average temperature of Adelaide. The difference is more than 5°C." |

Brief explanation of the test design approach: The test cases were designed to focus on the individual functions in the code. Test Case 1 verifies the correctness of the calculate_average_temperature function by comparing the expected average temperature. Test Case 2 checks the compare_temperature function for temperatures above the average, validating the expected result. Test Case 3 examines the compare_temperature function for temperatures below the average with a large difference, ensuring the expected result is returned.

Assumptions made during test design: The assumptions include the availability of temperature data for the specified cities and times, and the correct implementation of the calculate_average_temperature and compare_temperature functions.

## G. Test Implementation and Execution

To run the test code, use the following commands:
`python main_test_code.py` to run the test cases for first module
`python main_test.py` to run the test cases for second module


Results of test execution of first module: 

- Test Case ID 1: Passed
- Test Case ID 2: Passed
- Test Case ID 3: Passed

Results of test execution of first module: 

- Test Case ID 1: Passed
- Test Case ID 2: Passed
- Test Case ID 3: Passed

Findings from Part 6 of the assessment: All test cases passed successfully, indicating that the code implementation is functioning correctly according to the specified requirements.

Any attempts made to improve the code and new results, if applicable: Since all test cases passed, no specific attempts were made to improve the code in this case.

## H. Version Control

The version control system was used as follows:

[Provide a log of the use of your version control system]

Relevant points or observations regarding version control: [Discussion of relevant points or observations]

## I. Ethics

Part 7 of the assessment regarding ethics:

[Answer the ethics-related questions]

## J. Discussion

Reflection on your own work and discussion of areas for improvement:

[Reflect on your work and discuss areas for improvement]

Any other relevant thoughts or points: [Share any other relevant thoughts or points]
