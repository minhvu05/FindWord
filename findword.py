import os
import pandas as pd


def find_word_from_end_string(file_name, suffix):
    output_rows = []

    with open(file_name, "r") as f:
        for line in f:
            count = 0

            for word in line.split():
                if word.endswith(suffix):
                    count += 1
            if count > 0:
                output_row = line.strip() + f'|{count}'
                output_rows.append(output_row)

    with open("ans.txt", 'w') as f:
        f.write("\n".join(output_rows))
            
    

find_word_from_end_string("file1.txt", "y")





# without "on_bad_lines = 'skip'" param, it gives an error?
# pandas.errors.ParserError: Error tokenizing data. C error: Expected 3 fields in line 3, saw 4

# file1 passes with 1st row 6 fields, 2nd row 4 fields
# but file2 does not pass with 1st row 3 fields, 3rd row 4 fields
# probably bc 1st row can have excess columns, but can't make extra columns after init???

# on_bad_lines = 'skip' removes all rows with more columns than the first row
