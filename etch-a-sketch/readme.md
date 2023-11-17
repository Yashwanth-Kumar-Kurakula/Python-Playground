# Etch-a-sketch

This is a basic Python script which utilizes the Turtle graphics library to create a simple program that allows you to control the movement of a turtle on the screen using keyboard inputs.

## Instructions

1. **Installation:**
   - Ensure that you have Python installed on your machine. If not, you can download it from [python.org](https://www.python.org/downloads/).
   - This script uses the built-in `turtle` module, which is included in the standard Python distribution.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/Yashwanth-Kumar-Kurakula/Python-Playground.git
   ```
3. **Navigate to etch-a-sketch folder**

4. **Run the Script:**
   - Execute the script by running the following command:
     ```bash
     python turtle_control.py
     ```

5. **Keyboard Controls:**
   - Press the following keys to control the turtle:
     - **'w'**: Move the turtle forward by 10 units.
     - **'s'**: Move the turtle backward by 10 units.
     - **'a'**: Turn the turtle to the right by 10 degrees and move forward when the 'w' key is pressed.
     - **'d'**: Turn the turtle to the left by 10 degrees.
     - **'c'**: Reset the turtle to its initial state.

6. **Exit the Program:**
   - Click anywhere on the turtle graphics window to exit the program.

## Code Overview

- `move_forward()`: Move the turtle forward by 10 units.
- `move_backward()`: Move the turtle backward by 10 units.
- `turn_clockwise()`: Turn the turtle to the right by 10 degrees and move forward when the 'w' key is pressed.
- `turn_anti_clockwise()`: Turn the turtle to the left by 10 degrees.
- `reset_turtle()`: Reset the turtle to its initial state.

- Keyboard event listeners are set up to map specific keys to their corresponding functions.
- The main event loop is started using `turtle.mainloop()`.

Feel free to experiment with the code and customize it according to your preferences!

**Note:** Ensure that the turtle graphics window is in focus for the keyboard inputs to be registered.

Enjoy controlling the turtle! 🐢
