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