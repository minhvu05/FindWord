import os
import pandas as pd

# Checks each word in the row to see if it matches
def check_suffix(row, suffix):
    words = row.split()
    return any(words.endswith(suffix) for words in words)


def find_word_from_end_string(file_name, suffix):
    # Creating & formatting proper dataframe from given txt file
    df = pd.read_csv(file_name, header = None)
    melted_df = df.melt()
    melted_df = melted_df.drop(columns=['variable'])

    melted_df.to_csv("ans.txt", header=False, index=False, sep='\t', mode='w')


find_word_from_end_string("file2.txt", "e")