# NATO Phonetic Alphabet Converter

## Overview

This Python script, `nato_phonetic_alphabet.py`, is a simple tool that converts text into its corresponding NATO Phonetic Alphabet representation. The NATO Phonetic Alphabet is a standardized set of words used to represent each letter of the alphabet in oral communication to avoid confusion, especially in noisy or critical situations.

For example, instead of saying "A," you might say "Alpha," and instead of "B," you would say "Bravo." This helps ensure clarity and precision when conveying information verbally.

## Usage

To use this script, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Yashwanth-Kumar-Kurakula/Python-Playground 
   ```
   or download the `nato_phonetic_alphabet.py` file.

2. Make sure you have Python installed on your system.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script with the following command:

   ```bash
   python nato_phonetic_alphabet.py
   ```

5. Enter the text you want to convert when prompted.

6. The script will output the corresponding NATO Phonetic Alphabet representation of the entered text.

## Implementation Details

The script uses Python and takes advantage of the `pandas` library for data manipulation, as well as list comprehension and dictionary comprehension for concise and readable code.

### Dependencies

- Python 3.x
- Pandas

You can install the required dependencies using the following command:

```bash
pip install pandas
```

### Code Structure

- `nato_phonetic_alphabet.py`: The main Python script.
- `nato_alphabet.csv`: A CSV file containing the mapping of letters to their NATO Phonetic Alphabet equivalents.

### How it Works

1. The script reads the NATO Alphabet mapping from the `nato_alphabet.csv` file into a Pandas DataFrame.
2. The user enters the text to be converted.
3. The script converts each letter in the input text to its NATO Phonetic Alphabet representation using a dictionary comprehension and list comprehension.
4. The final output is displayed to the user.

## Example

```plaintext
Input: Hello
Output: Hotel Echo Lima Lima Oscar
```

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to contribute, report issues, or suggest improvements!
