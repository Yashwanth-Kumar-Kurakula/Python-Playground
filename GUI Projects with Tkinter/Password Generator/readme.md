# Password Manager

This is a simple Password Manager application implemented in Python using the Tkinter library for the graphical user interface. The program allows users to generate secure passwords and store them along with website and email information.

## Getting Started

### Prerequisites
Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation
1. Clone or download this repository.
2. Install the required packages using the following command:
    ```bash
    pip install ttkbootstrap
    ```

### Running the Application
Run the Python script by executing the following command:
```bash
python password_manager.py
```

## Features

### Password Generation
Click the "Generate Password" button to create a strong and random password of length 12, combining uppercase letters, lowercase letters, digits, and punctuation.

### Adding Passwords
1. Enter the website name in the "Website" field.
2. Enter the email or username associated with the website in the "Email/Username" field.
3. Either enter a password manually or generate one using the "Generate Password" button.
4. Click the "Add" button to store the information in a file named "passwords".

## File Structure
- `password_manager.py`: Main Python script containing the password manager application.
- `logo.png`: Logo image used in the application.

## Contributing
Feel free to contribute to the development of this project. You can submit bug reports, feature requests, or even pull requests.

## Acknowledgments
- Special thanks to the developers of Tkinter and ttkbootstrap for making GUI development in Python easy and stylish.