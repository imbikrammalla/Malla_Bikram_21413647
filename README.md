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


Different modularity concepts were applied in the code, such as:

- [Modularity Concept 1]: [Explanation of how this concept was applied]
- [Modularity Concept 2]: [Explanation of how this concept was applied]
- [Modularity Concept 3]: [Explanation of how this concept was applied]

Review Checklist:

1. [Checklist Item 1]
2. [Checklist Item 2]
3. [Checklist Item 3]

Results of the review using the checklist:

- [Checklist Item 1]: [Result]
- [Checklist Item 2]: [Result]
- [Checklist Item 3]: [Result]

Any identified issues were addressed by [Explanation of how the issues were addressed].

## E. Black-Box Test Cases

The following test cases were designed for Part 4 of the assessment:

| Test Case ID | Description | Input | Expected Output |
|--------------|-------------|-------|-----------------|
| 1            | [Description of Test Case 1] | [Input for Test Case 1] | [Expected Output for Test Case 1] |
| 2            | [Description of Test Case 2] | [Input for Test Case 2] | [Expected Output for Test Case 2] |
| 3            | [Description of Test Case 3] | [Input for Test Case 3] | [Expected Output for Test Case 3] |

Rationale behind the chosen test design: [Explanation of the rationale behind the test design]

Assumptions made during test design: [Assumptions, if any]

## F. White-Box Test Cases

The following test cases were designed for Part 5 of the assessment:

| Test Case ID | Description | Expected Output |
|--------------|-------------|-----------------|
| 1            | [Description of Test Case 1] | [Expected Output for Test Case 1] |
| 2            | [Description of Test Case 2] | [Expected Output for Test Case 2] |
| 3            | [Description of Test Case 3] | [Expected Output for Test Case 3] |

Brief explanation of the test design approach: [Explanation of the test design approach]

Assumptions made during test design: [Assumptions, if any]

## G. Test Implementation and Execution

To run the test code, use the following commands:


Results of test execution:

- [Test Case ID 1]: [Result]
- [Test Case ID 2]: [Result]
- [Test Case ID 3]: [Result]

Findings from Part 6 of the assessment: [Discussion of the findings]

Any attempts made to improve the code and new results, if applicable: [Explanation of any attempts to improve the code and the corresponding results]

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
