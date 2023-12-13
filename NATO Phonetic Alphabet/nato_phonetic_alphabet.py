import pandas

def load_phonetic_data(file_path):
    """
    Load the NATO phonetic alphabet data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file containing NATO phonetic alphabet data.

    Returns:
    - pandas.DataFrame: A DataFrame containing the loaded data.
    """
    data = pandas.read_csv(file_path)
    return data

def create_phonetic_dict(data_frame):
    """
    Create a dictionary mapping letters to their corresponding NATO phonetic codes.

    Parameters:
    - data_frame (pandas.DataFrame): DataFrame containing NATO phonetic alphabet data.

    Returns:
    - dict: A dictionary where keys are letters and values are corresponding phonetic codes.
    """
    return {row.letter: row.code for (index, row) in data_frame.iterrows()}

def phonetic_alphabet():
    """
    Get the NATO phonetic alphabet representation for a user-entered word.
    """
    # Load NATO phonetic alphabet data
    data = load_phonetic_data("nato_phonetic_alphabet.csv")

    # Create a dictionary mapping letters to their corresponding NATO phonetic codes
    phonetic_dict = create_phonetic_dict(data)

    # Get user input for a word
    word = input("Enter a word: ").upper()

    try:
        # Generate a list of NATO phonetic codes for each letter in the word
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        # Handle the case where a non-alphabetic character is entered
        print("Only alphabets allowed, Numeric characters are not allowed!")
        phonetic_alphabet()
    else:
        # Print the NATO phonetic representation of the entered word
        print(output_list)

# Execute the main function to get the NATO phonetic representation for a user-entered word
phonetic_alphabet()
