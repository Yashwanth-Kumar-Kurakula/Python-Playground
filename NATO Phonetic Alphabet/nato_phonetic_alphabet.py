import pandas

def read_phonetic_data(file_path):
    """
    Reads the NATO phonetic alphabet data from a CSV file and returns a dictionary.
    
    Parameters:
    - file_path (str): The path to the CSV file containing the NATO phonetic alphabet data.
    
    Returns:
    - dict: A dictionary mapping letters to their corresponding phonetic codes.
    """
    data = pandas.read_csv(file_path)
    phonetic_data = {row.letter: row.code for (index, row) in data.iterrows()}
    return phonetic_data

def main():
    """
    Main function to get user input, convert it to NATO phonetic alphabet codes, and print the result.
    """
    # Read NATO phonetic alphabet data from the CSV file
    file_path = "nato_phonetic_alphabet.csv"
    phonetic_data = read_phonetic_data(file_path)

    # Get user input and convert it to uppercase
    name = input("Enter something: ").upper()

    # Generate a list of NATO phonetic alphabet codes for each letter in the user input
    output_list = [phonetic_data[letter] for letter in name]

    # Print the resulting list of phonetic alphabet codes
    print(output_list)

# Call the main function if the script is executed
if __name__ == "__main__":
    main()
