# SA Assignment 1

This project contains the solution for the Software Architecture Assignment 1, exercises: 1. Document Editor, 2. Car Configuration, as well as a combination between the two (Car Management System) and unit tests.

## Project Structure

The project is split into separate files for better organization:

* main.py: The main script. Run this to see a demonstration of the code working in the terminal.
* tests.py: Contains the unit tests. Run this to verify that the code works as expected.
* document_editor.py: Contains the Document class and the Factory logic (Exercise 1).
* car_configurator.py: Contains the Car class and the Builder logic (Exercise 2).
* car_management.py: Contains the integration logic that combines the Builder and Factory (Bonus Task).

## How to Run

1. To run the demonstration:
   Run the following command:
   python main.py

   This will print the results of creating documents and cars to the console. It will also create sample text files in the folder to simulate saving documents.

2. To run the tests:
   Run the following command:
   python tests.py

   This will check if the logic is correct and print "OK" if all tests pass.

## Implementation Details

### Exercise 1: Document Editor (Factory Pattern)
I used the Factory Method pattern to handle different document formats. The DocumentFactory class takes a string input (like "pdf", "word", or "html") and returns the correct document object. This makes it easy to add new formats later without changing the main code.

### Exercise 2: Car Configuration (Builder Pattern)
I used the Builder pattern to construct complex Car objects. The CarBuilder class allows you to set engine types, transmission, and optional features step-by-step. It also includes validation to ensure the car has an engine and transmission before it is built.

### Bonus Tasks
* Integration: I created a CarManagementSystem class that takes a configured car and generates an order document using the Factory.
* Unit Tests: I added tests using the unittest library to cover the main functionality and edge cases (like trying to build a car without an engine).
* File Output: The document classes actually write text files to the disk to simulate a real save operation.