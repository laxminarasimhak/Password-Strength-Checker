# Password Strength Checker

A simple GUI application built with Python's Tkinter library to evaluate the strength of passwords. This application provides real-time feedback on password strength based on various criteria, helping users create stronger passwords.

## Features
- Checks password strength based on:
  - Length
  - Variety of characters (uppercase, lowercase, digits, special characters)
  - Avoidance of common passwords
- Provides visual feedback on password strength with color indicators.
- Toggle visibility of the password for ease of entry.

## Installation
To run this application, ensure you have Python installed on your machine. You can clone the repository and run the script as follows:

```bash
git clone https://github.com/laxminarasimhak/Password-Strength-Checker.git
cd Password-Strength-Checker
python MultipleFiles/password.py

## Usage
1. Launch the application.
2. Enter a password in the input field to check its strength.
3. The strength of the password will be displayed along with a color indicator:
  - Weak: Red
  - Moderate: Orange
  - Strong: Yellow
  - Very Strong: Green
4. Follow the password creation rules displayed in the application to create a secure password.

## Password Creation Rules
- At least 8 characters long
- Include both uppercase and lowercase letters
- Include at least one digit
- Include at least one special character (e.g., @, #, $, %)
- Avoid common passwords

## Contributing
Contributions are welcome! Please read the CONTRIBUTING.md for details on how to contribute to this project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- This application uses the Tkinter library for the GUI.
- Inspired by best practices for password security.
