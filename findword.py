import os
import pandas as pd

def find_word_from_end_string(file_name, suffix):
    # Creating & formatting proper dataframe from given txt file
    df = pd.read_csv(file_name, sep = ' ', header = None)
    output_rows = []

    # piping the count at the end of the row
    for i, row in df.iterrows():
        count = 0
        for words in row:
            if words.endswith(suffix):    
                count += 1
        if count > 0:
            output_row = ' '.join(row) + f'|{count}'
            output_rows.append(output_row)
            

    with open("ans.txt", 'w') as f:
        f.write("\n".join(output_rows))

# error when # of words on each row is different
find_word_from_end_string("file1.txt", "y")