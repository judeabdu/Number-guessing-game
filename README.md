# Number Guessing Game (Python)

This project is a command-line number guessing game written in Python.  
The program generates a random number between 1 and 50, and the player must guess the correct number within a limited number of attempts.

## Description

The game demonstrates the use of Python fundamentals together with standard libraries. It combines random number generation, loops, conditional statements, and user input to create an interactive terminal game.

The player is given five attempts to guess the correct number. After each guess, the program provides feedback to guide the player. If the guess is far from the correct number, the program indicates that the guess is "way too high" or "way too low". If the guess is closer, the program simply says "too high" or "too low".

If the player guesses the number correctly, the program congratulates them and ends the game. If all attempts are used without guessing the number, the program reveals the correct answer.

## Features

- Random number generation using Python's `random` library
- User input handling
- Input validation (numbers must be between 1 and 50)
- Five attempt limit
- Intelligent feedback based on distance from the correct number
- Game over message when attempts are exhausted

## Technologies Used

- Python 3
- `random` standard library

## How the Game Works

1. The program generates a secret number between 1 and 50.
2. The player is given 5 attempts to guess the number.
3. After each guess, the program tells the player whether the guess is:
   - Too high
   - Too low
   - Way too high (more than 10 away)
   - Way too low (more than 10 away)
4. If the player guesses correctly, the game ends with a success message.
5. If all attempts are used, the correct number is revealed.

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone the repository.
3. Run the program from the terminal:

```bash
python guessing_game.py
