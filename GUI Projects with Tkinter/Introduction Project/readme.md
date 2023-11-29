# Miles to Kilometers Converter using Tkinter

## Table of Contents
1. [Overview](#overview)
2. [Components](#components)
3. [How to Run](#how-to-run)
4. [Dependencies](#dependencies)
5. [License](#license)

## Overview

This is a simple Python program that utilizes the Tkinter library to create a graphical user interface (GUI) for converting miles to kilometers. The program features an entry widget for input, a conversion button, and an output label to display the converted result.

## Components

### 1. Tkinter Window
   - The main window of the GUI is created using the `ttkbootstrap` theme.
   - Window title is set to "Demo" with a size of 300x150 pixels.

### 2. Title Label
   - A large title label ("Miles to kilometers") is displayed at the top of the window, using the Calibri font with a size of 24 and in bold.

### 3. Input Frame
   - A frame to hold the input components (entry widget and conversion button).
   - Entry widget for the user to input the distance in miles.
   - Conversion button triggers the conversion function (`convert`) when clicked.

### 4. Conversion Function (`convert`)
   - Converts miles to kilometers using the formula: `kilometers = miles * 1.61`.
   - Rounds the result to two decimal places.
   - Updates the output label with the converted value.

### 5. Output Label
   - Displays the converted kilometers.
   - Font is set to Calibri with a size of 24 and in bold.

## How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Yashwanth-Kumar-Kurakula/Python-Playground 
   ```
2. **Navigate to the __GUI Projects with Tkinter / Introduction Project__ Folder**
   
3. **Install Dependencies:**
   Ensure you have Python and ttkbootstrap installed. You can install ttkbootstrap using:
   ```bash
   pip install ttkbootstrap
   ```

4. **Run the Code:**
   ```bash
   python miles_to_km_converter.py
   ```

## Dependencies

- [Tkinter](https://docs.python.org/3/library/tkinter.html): The standard GUI toolkit for Python.
- [ttkbootstrap](https://ttkbootstrap.readthedocs.io/): A library providing Bootstrap-inspired themes for Tkinter.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

