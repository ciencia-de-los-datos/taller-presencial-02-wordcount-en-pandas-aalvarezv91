"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    filenames = glob.glob(f"{input_directory}/*.txt")

    dataframes = []
    for filename in filenames:
        dataframes.append(pd.read_csv(filename, sep="\t", header=None, names=["text"]))
    
    concatenated_df = pd.concat(dataframes, ignore_index=True)
    return concatenated_df

def clean_text(dataframe):
    """Text cleaning"""
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.lower()
    dataframe["text"] = dataframe["text"].str.replace(".", "")
    dataframe["text"] = dataframe["text"].str.replace(",", "")
    return dataframe

def count_words(dataframe):
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split()
    dataframe = dataframe.explode("text")
    dataframe["count"] = 1
    dataframe = dataframe.groupby("text").agg({"count": "sum"})

    return dataframe


def save_output(dataframe, output_filename):
    dataframe.to_csv(output_filename, sep="\t", index=True, header=False)

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    df = load_input("input")
    df = clean_text(df)
    df = count_words(df)
    save_output(df, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
