import os
import pandas as pd


def find_word_from_end_string(file_name, suffix):
    # Creating proper dataframe from given txt file
    df = pd.read_csv(file_name, sep = ' ', header = None, on_bad_lines = 'skip')
    output_rows = []

    # Piping the count at the end of the row
    for i, row in df.iterrows():
        count = 0
        # Store all valid words for output row
        valid_words = []  
        for words in row:
            # Skip nan values
            if pd.notna(words):
                # Convert word to string to avoid float issues
                words = str(words)
                if words.endswith(suffix):    
                    count += 1
                # Add valid word to filtered row array
                valid_words.append(words)  
        if count > 0:
            output_row = ' '.join(valid_words) + f'|{count}'
            output_rows.append(output_row)
            

    with open("ans.txt", 'w') as f:
        f.write("\n".join(output_rows))


find_word_from_end_string("file4.txt", "e")





# without "on_bad_lines = 'skip'" param, it gives an error?
# pandas.errors.ParserError: Error tokenizing data. C error: Expected 3 fields in line 3, saw 4
# no idea how file1 passes with 1st row 6 fields, 2nd row 4 fields
# but file2 does not pass with 1st row 3 fields, 3rd row 4 fields??

# probably bc 1st row can have excess columns, but can't make extra columns after init???

# but on_bad_lines = 'skip' removes all rows with more columns than the first row
