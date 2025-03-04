# 🔒 Password Strength Meter

A Python application built with Streamlit that helps users evaluate password strength and generate secure passwords.

## Features

- ✅ Real-time password strength evaluation
- ✅ Detailed feedback and improvement suggestions
- ✅ Strong password generator
- ✅ Common password blacklist
- ✅ Beautiful and responsive UI
- ✅ Customizable scoring weights

## Requirements

- Python 3.8+
- uv package manager
- Streamlit

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd password-strength-meter
```

2. Create and activate virtual environment using uv:
```bash
uv venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Unix/MacOS
```

3. Install dependencies:
```bash
uv pip install streamlit
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Password Strength Criteria

The application evaluates passwords based on the following criteria:

- Minimum length of 8 characters
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Presence of special characters (!@#$%^&*)

## Scoring System

- **Weak (Score: 1-2)**: Password fails to meet multiple criteria
- **Moderate (Score: 3-4)**: Password meets most criteria but could be improved
- **Strong (Score: 5)**: Password meets all security criteria

## Contributing

Feel free to submit issues and enhancement requests!
