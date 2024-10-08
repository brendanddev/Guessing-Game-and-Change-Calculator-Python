# Python Guessing Game and Change Calculation

This repository contains two Python assignments that implement a guessing game and a store change calculator. The purpose of these assignments is to demonstrate skills in Python programming, including the use of conditional statements, loops, and modular code design.

## Project Structure

- `design.pdf` or `design.docx`: Contains the design documentation for the guessing game in the form of an IPO chart, flow chart, and/or pseudocode. Includes a certification statement with the student’s name and student number.
- `guessing_game.txt`: Text file with the Python code for the guessing game module, `checkGuess`, and the main program that utilizes it.
- `guessing_game.zip`: Contains the `guessing_game.py` file with the full implementation of the guessing game.
- `change_calculation.py`: Python file implementing the store change calculator, based on the provided flow chart.

## Assignment Details

### Question 1: Guessing Game

The guessing game consists of a module named `checkGuess` that accepts two string inputs. The first input is the user’s guess, and the second is a secret letter chosen at random. The module checks whether the user’s guess is alphabetically before, after, or equal to the secret letter, returning -1, 1, or 0, respectively.

- **Game Rules**:
  - The user has three attempts to guess the secret letter.
  - Scoring is based on which attempt the user guesses correctly:
    - First attempt: 26 points
    - Second attempt: 13 points
    - Third attempt: 7 points
  - If all three attempts are incorrect, the user scores 0 points.
  - After each incorrect guess, the program will indicate whether the guess is too high or too low.

### Question 2: Store Change Calculation

This script calculates the correct change for a customer’s purchase using the fewest coins possible, in the denominations of dollars, quarters, dimes, and nickels. The total change is rounded to the nearest nickel, as pennies are no longer in use in Canada.

- **Implementation**:
  - Calculates the amount owed using random values.
  - Accepts the amount of money given by the customer.
  - Determines the correct amount of change and provides the fewest coins necessary.

## How to Run

1. Download or clone the repository.
2. Open the desired `.py` file (`guessing_game.py` or `change_calculation.py`) in a Python IDE or execute it from the command line.
3. Ensure that Python is installed on your system.
