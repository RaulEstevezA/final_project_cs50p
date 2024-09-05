# Anglo-Saxon system converter to decimal metric and vice versa
#### Video Demo:  <https://youtu.be/gQ491b5lro0>
### __Description:__
#### It is a program for converting units from the Anglo-Saxon system to the metric system and vice versa.
#### It first presents the program and prompts you to enter *exit* any time you want to exit. Then it will ask you what measurement you want to make the conversion, the choices being length, weight, volume or temperature. If the user does not enter the choice correctly, it will ask you again until you enter it correctly or enter *exit*. Once you have chosen one of the four options, it asks you to enter the data to convert. In this step, you are also asked to enter either the measurement to be converted or its acronym. If it is not entered correctly, it will be requested again until it is written correctly or *exit* is inserted. Once the measurement to be converted has been correctly inserted, the program prints the conversion in the most common measurement of the opposite system.
#### For example, if we want to convert **4 miles** the program will return **6.44 km**. Another example would be to convert **33º F**, the program will return **0.67º C**. In volume, for example, if we enter **4 gallons** it will return **15.14 l** but if you enter **30 fluid onze** it will return **88.72 cl**.
#### Project structure:
- project.py
- test_project.py
- README.md
### A small description of each of the files that compose it:
#### project.py
##### Contains the complete program. I did not see it necessary to resort to more files to complete the program.
#### test_project.py
##### Contains various tests to test the definitions in the main program.
### __Development process__
#### When I started the project I thought of some type of program that only used Python, since this course is exclusive to Python, so I thought of one that used a large part of the lessons learned. Among the ideas I was considering, a measurement system converter seemed the most appropriate. Additionally, I wanted the user to be able to exit at any time using the word *“exit”*, instead of forcing them to close using *“ctrl+c”*. I also thought that the user could make a mistake when entering data, so instead of exiting the program and having to run it again, I thought that the best way to approach this was through *“while”* loops together with some words accepted in each loop. Each *“while”* loop calls a definition and if the data entered is correct, returns the conversion and closes the program.
### __Usage__
```python project.py```
```
Welcome to the conversion system between the Metric system and the Anglo-Saxon system.
If you want to exit the program, enter "exit" at any time
What would you like to convert, temperature, length, weight or volume ?
```
#### At this point you will have to choose between temperature, length, weight or volume and enter it. Let's choose *temperature*, for example.
```
Write the temperature you would like to convert (example: 33 ºF):
```
#### We will insert, for example, `40º C`, although the program accepts some variants, such as not putting the space between the numbers and the measurement system (celsius or fahrenheit) putting the numbers followed by the system (40f).
#### Once the option we want has been inserted, in this case the one mentioned, the program returns the conversion with a decimal:
```
104.0º F
```
## Autor: Raul Estevez
### GitHub profile: [RaulEstevezA](https://github.com/RaulEstevezA)
### LinkedIn: [Raul Estevez](https://www.linkedin.com/in/raul-estevez-abella-9a2a1687/)
