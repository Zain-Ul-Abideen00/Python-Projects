# Python Projects Collection

This repository contains a collection of Python projects as part of the AI-101 course requirements. Each project demonstrates different Python programming concepts and features.

## Projects List

### Basic Python Projects
1. **Mad Libs** (`mad_libs.py`) - A word game where players fill in blanks in a story with their own words
2. **Guess the Number (Computer)** (`guess_number_computer.py`) - A game where the computer tries to guess a number you're thinking of
3. **Guess the Number (User)** (`guess_number_user.py`) - A game where you try to guess a number the computer has chosen
4. **Rock, Paper, Scissors** (`rock_paper_scissors.py`) - The classic hand game implemented in Python
5. **Hangman** (`hangman.py`) - A word guessing game where players try to guess a hidden word
6. **Countdown Timer** (`countdown_timer.py`) - A timer application that counts down from a specified time
7. **Password Generator** (`password_generator.py`) - A tool to generate secure random passwords

### Streamlit Web Applications
Located in the `streamlit_projects` directory:
1. **BMI Calculator** (`bmi_calculator.py`) - A web application to calculate Body Mass Index
2. **Data Dashboard** (`data_dashboard.py`) - A data visualization dashboard

## Setup Instructions

### Basic Projects
1. Clone this repository
2. Navigate to the project directory
3. Run the Python file:
   ```
   python <project_name>.py
   ```

### Streamlit Projects
1. Navigate to the `streamlit_projects` directory
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```
   streamlit run <project_name>.py
   ```

## Requirements

### Basic Projects
- Python 3.7 or higher
- No additional dependencies required

### Streamlit Projects
- Python 3.7 or higher
- Required packages:
  - streamlit==1.44.0
  - python-dotenv==1.0.0

## Project Structure
```
.
├── streamlit_projects/          # Streamlit web applications
│   ├── bmi_calculator.py
│   ├── data_dashboard.py
│   ├── requirements.txt
│   └── README.md
├── rock_paper_scissors.py
├── password_generator.py
├── countdown_timer.py
├── hangman.py
├── guess_number_user.py
├── guess_number_computer.py
├── mad_libs.py
└── README.md
```
