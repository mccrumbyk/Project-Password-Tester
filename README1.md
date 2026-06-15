Project Password Tester
Project Overview

This project is a simple Python password strength tester created for CYB 333 Security Automation. The script checks whether a password contains at least one uppercase letter, one lowercase letter, and one number. Based on how many of those requirements are met, the script assigns the password a strength label of Weak, Medium, or Strong.

The program runs in the terminal and continues asking the user for a password until all three requirements are met. This project was designed to demonstrate a basic security automation tool that can help users understand password requirements and improve password quality.

Features
Checks for at least one uppercase letter
Checks for at least one lowercase letter
Checks for at least one number
Assigns a password strength label:
Weak = one requirement met
Medium = two requirements met
Strong = all three requirements met
Displays missing requirements
Repeats until the password meets all requirements
Technologies Used
Python 3
VS Code
GitHub
Prerequisites

Before running this project, make sure you have:

Python 3 installed
VS Code or another code editor installed
Access to a terminal or command prompt

You can download Python here:
https://www.python.org/downloads/

How to Set Up and Run the Project
Clone the Repository

Open a terminal and run:

git clone https://github.com/mccrumbyk/Project-Password-Tester.git

Then move into the project folder:

cd Project-Password-Tester

Run on Windows

In Command Prompt or PowerShell, run:

python password_tester.py

If that does not work, try:

py password_tester.py

Run on Mac/Linux

Open the terminal and run:

python3 password_tester.py

Example Usage
Example input/output:
Password Strength Tester
-------------------------
Enter a password to test: password

Results
-------------------------
Requirements met: 1/3
Strength: Weak
Missing:
- an uppercase letter
- a number

Please try again.

Another example:

Enter a password to test: Password

Results
-------------------------
Requirements met: 2/3
Strength: Medium
Missing:
- a number

Final example:

Enter a password to test: Password1

Results
-------------------------
Requirements met: 3/3
Strength: Strong

Your password meets all requirements.

The objective of this project is to build a simple security automation tool that checks password strength based on basic security requirements. This project helps demonstrate Python scripting, input validation, conditional logic, looping, and user feedback in a cybersecurity-related context.

Repository Link

GitHub Repository:
https://github.com/mccrumbyk/Project-Password-Tester

Additional Notes
This project is terminal-based and does not use a graphical interface.
The script is designed to be simple and easy to run for beginner users.
No external Python packages are required for this project.
